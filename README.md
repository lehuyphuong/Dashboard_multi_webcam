# A Simple Multi-cam Dashboard

A Simple Multi-cam Dashboard is a lightweight desktop application built with **PySide6** (Qt for Python) and **OpenCV** that allows users to monitor multiple video sources in a single, tiled dashboard interface.

The application is designed for rapid prototyping and small-scale surveillance setups, supporting common camera input types such as:
- Local webcams
- HTTP video streams (e.g. DroidCam)
- RTSP video streams

-> It provides a grid-based overview for all cameras and a dedicated detail view for individual streams.

## Supported Video Sources
### 1. Webcam
Uses OpenCV VideoCapture with OS-specific backends. Automatically selects suitable backend 
- Windows: DirectShow / Media Foundation 
- Linux/macOS: default OpenCV backend 

Example: 0

### 2. HTTP Stream (DroidCam)
The application automatically normalizes common DroidCam URLs.  
Input:  

```
http://192.168.XX.XX:4747  
```

Normalized internally do:  
```
http://192.168.XX.XX:4747/video  
```
This allows plug-and-play usage without manual URL adjustments.

### 3. RTSP Stream
Standard RTSP streams are supported via FFmpeg backend.  
Example:
```
rtsp://admin:VERIFICATIONCODE@192.168.XX.XX:554/h264/ch0/main/av_stream?tcp
```
Remember: the ip, verification code and channel could be differrent.