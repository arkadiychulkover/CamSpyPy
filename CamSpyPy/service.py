import socket
import cv2
import time

def stream_video():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(('178.95.15.120', 12345))
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

stream_video()
