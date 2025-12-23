from PySide6 import QtWidgets, QtCore, QtGui
from ui_surveillance_camera import Ui_MainWindow
from ui_cam_tile import Ui_CamTile
import sys
import cv2
import platform

# Establish camera
class VideoWorker(QtCore.QThread):
    frame_ready = QtCore.Signal(int, QtGui.QImage)   # (cam_idx, image)
    error = QtCore.Signal(int, str)                  # (cam_idx, message)

    def __init__(self, cam_idx, src=0, parent=None):
        super().__init__(parent)
        self.src = src
        self.cam_idx = cam_idx
        self._running = False

    def stop(self):
        self._running = False
        self.wait()

    def _normalize_url(self, s: str) -> str:
        # Friendly fix for DroidCam inputs like "http://IP:4747" (add /video)
        u = s.strip()
        if u.startswith("http://") and ":4747" in u and "/video" not in u:
            if not u.endswith("/"):
                u += "/video"
            else:
                u += "video"
        return u

    def _candidate_backends(self):
        # Choose backends per source type & OS (Windows is picky)
        if isinstance(self.src, str):
            return [cv2.CAP_FFMPEG, cv2.CAP_ANY]  # URLs: prefer FFmpeg
        if platform.system() == "Windows":
            return [cv2.CAP_DSHOW, cv2.CAP_MSMF, cv2.CAP_ANY]  # webcams
        return [cv2.CAP_ANY]

    def run(self):
        source = self.src
        if isinstance(source, str):
            source = self._normalize_url(source)

        cap = None
        opened = False
        for be in self._candidate_backends():
            try:
                # In case of cash, try again
                cap = cv2.VideoCapture(source, be)
            except Exception:
                cap = None

            if cap is not None and cap.isOpened():
                opened = True
                break
            if cap is not None:
                cap.release()
                cap = None

        if not opened or cap is None:
            self.error.emit(self.cam_idx, f"Open failed: {self.src}")
            return

        self._running = True
        consecutive_fail = 0
        while self._running:
            ret, frame = cap.read()
            if not ret:
                consecutive_fail += 1
                if consecutive_fail >= 5:   # give the stream a few chances
                    self.error.emit(self.cam_idx, "Read failed")
                    break
                self.msleep(50)
                continue
            consecutive_fail = 0

            # Convert to QImage
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb.shape
            qimg = QtGui.QImage(rgb.data, w, h, ch * w, QtGui.QImage.Format_RGB888)
            self.frame_ready.emit(self.cam_idx, qimg)
            self.msleep(1)  # let UI breathe; tuner for FPS

        try:
            cap.release()
        except Exception:
            pass

# ADJUST SIZE OF SUB-WINDOW HERE
TILE_W, TILE_H = 380, 260  # visual size for CamTile and AddTile 

class CamTile(QtWidgets.QWidget):
    clicked = QtCore.Signal(int)
    def __init__(self, title: str, idx: int, parent=None):
        super().__init__(parent)
        self.ui = Ui_CamTile(); self.ui.setupUi(self)
        self.idx = idx
        self.ui.barHeader.setText(title)
        # keep tiles a consistent size in the grid
        self.setMinimumSize(TILE_W, TILE_H)
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.installEventFilter(self)
    def eventFilter(self, obj, ev):
        if ev.type() == QtCore.QEvent.MouseButtonRelease:
            self.clicked.emit(self.idx); return True
        return super().eventFilter(obj, ev)

class AddTile(QtWidgets.QFrame):
    clicked = QtCore.Signal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(TILE_W, TILE_H)
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setStyleSheet("""
            QFrame{border:2px dashed #999;border-radius:10px;background:#fafafa;}
            QLabel{font-size:32px;color:#666;}
        """)
        lay = QtWidgets.QVBoxLayout(self); lay.setContentsMargins(12,12,12,12)
        lay.addStretch(1); lab = QtWidgets.QLabel("+"); lab.setAlignment(QtCore.Qt.AlignCenter)
        lay.addWidget(lab); lay.addStretch(1)
    def mouseReleaseEvent(self, e: QtGui.QMouseEvent):
        if e.button() == QtCore.Qt.LeftButton: self.clicked.emit()
        super().mouseReleaseEvent(e)

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow(); self.ui.setupUi(self)
        self.ui.scrollArea.setWidgetResizable(True)

        self.grid_layout: QtWidgets.QGridLayout = self.findChild(QtWidgets.QGridLayout, "layoutGridCams")
        # make the grid neat
        self.grid_layout.setHorizontalSpacing(12)
        self.grid_layout.setVerticalSpacing(12)
        # align items to top-left so they don't float in the middle
        # (apply per-widget in addWidget below)

        self.cams = [{"title":"CAM_1 / Zone A","url":""}]
        self.current_idx = -1

        self.rebuild_grid()

        self.ui.btnBack.clicked.connect(lambda: self.ui.stack.setCurrentIndex(0))
        self.ui.btnPrev.clicked.connect(self.prev_cam)
        self.ui.btnNext.clicked.connect(self.next_cam)
        self.ui.stack.setCurrentIndex(0)

    def clear_grid(self):
        for i in reversed(range(self.grid_layout.count())):
            w = self.grid_layout.itemAt(i).widget()
            self.grid_layout.takeAt(i)
            self.grid_layout.setContentsMargins(8, 8, 8, 8)
            self.grid_layout.setHorizontalSpacing(16)
            self.grid_layout.setVerticalSpacing(16)
            if w:
                w.setParent(None); w.deleteLater()

    def rebuild_grid(self):
        # stop and clear any existing workers first
        for w in getattr(self, "workers", []):
            try:
                if w.isRunning():
                    w.stop()
            except Exception:
                pass
        self.workers = []

        self.clear_grid()
        cols = 2
        for idx, cam in enumerate(self.cams):
            tile = CamTile(cam["title"], idx, parent=self.ui.gridContainer)
            tile.clicked.connect(self.show_detail)
            r, c = divmod(idx, cols)
            self.grid_layout.addWidget(tile, r, c, QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)

            worker = VideoWorker(idx, cam["url"] if cam["url"] else 0)
            worker.frame_ready.connect(self.update_frame)
            worker.error.connect(self.on_cam_error)
            worker.start()
            self.workers.append(worker)

        add_tile = AddTile(parent=self.ui.gridContainer)
        add_tile.clicked.connect(self.add_camera_dialog)
        r, c = divmod(len(self.cams), cols)
        self.grid_layout.addWidget(add_tile, r, c, QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.update_nav_buttons()


    @QtCore.Slot(int)
    def show_detail(self, idx):
        self.current_idx = idx
        self.ui.labelDetailTitle.setText(self.cams[idx]["title"])
        self.ui.stack.setCurrentIndex(1)
        self.update_nav_buttons()

    def update_nav_buttons(self):
        multi = len(self.cams) > 1 and self.current_idx != -1
        self.ui.btnPrev.setEnabled(multi)
        self.ui.btnNext.setEnabled(multi)

    def prev_cam(self):
        if len(self.cams) <= 1 or self.current_idx == -1: return
        self.show_detail((self.current_idx - 1) % len(self.cams))

    def next_cam(self):
        if len(self.cams) <= 1 or self.current_idx == -1: return
        self.show_detail((self.current_idx + 1) % len(self.cams))

    def add_camera_dialog(self):
        title, ok = QtWidgets.QInputDialog.getText(self, "Add Camera", "Camera title:")
        if not ok or not title.strip():
            return

        url, ok2 = QtWidgets.QInputDialog.getText(self, "Add Camera", "RTSP/URL:")
        if not ok2:
            return

        u = url.strip()
        # Friendly DroidCam normalization
        if u.startswith("http://") and ":4747" in u and "/video" not in u:
            u = u.rstrip("/") + "/video"

        # Append exactly once
        self.cams.append({"title": title.strip(), "url": u})
        self.rebuild_grid()

    def closeEvent(self, event):
        for w in getattr(self, "workers", []):
            if w.isRunning():
                w.stop()
        event.accept()

    @QtCore.Slot(int, QtGui.QImage)
    def update_frame(self, cam_idx, qimg):
        pix = QtGui.QPixmap.fromImage(qimg).scaled(
            320, 180, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation
        )
        tile_item = self.grid_layout.itemAt(cam_idx)
        if tile_item:
            tile = tile_item.widget()
            tile.ui.labelVideo.setPixmap(pix)
            tile.ui.iconReason.setText(f"Cam {cam_idx}")

        if self.current_idx == cam_idx:
            self.ui.labelDetailVideo.setPixmap(QtGui.QPixmap.fromImage(qimg))
            self.ui.labelDetailTitle.setText(f"Cam {cam_idx}")

    @QtCore.Slot(int, str)
    def on_cam_error(self, cam_idx, msg):
        item = self.grid_layout.itemAt(cam_idx)
        if item:    
            tile = item.widget()
            # use your two labels:
            if hasattr(tile.ui, "iconWarn"):
                tile.ui.iconWarn.setText("⚠")
            if hasattr(tile.ui, "iconReason"):
                tile.ui.iconReason.setText(msg)
        # ensure the worker will exit & cannot keep the device busy
        if 0 <= cam_idx < len(self.workers):
            self.workers[cam_idx].stop()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Main(); w.resize(1280, 800); w.show()
    sys.exit(app.exec())


