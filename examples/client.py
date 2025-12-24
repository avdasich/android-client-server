import socket
import sys


def send_message(message, host='127.0.0.1', port=5555):

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        print(f"[CLIENT] Подключение к {host}:{port}...")
        client_socket.connect((host, port))
        print("[CLIENT] Подключено!")

        print(f"[CLIENT] Отправка: {message}")
        client_socket.send(message.encode('utf-8'))

        response = client_socket.recv(1024).decode('utf-8')
        print(f"[CLIENT] Получен ответ: {response}")

    except ConnectionRefusedError:
        print("[CLIENT] Ошибка: Сервер не запущен или недоступен")
    except Exception as e:
        print(f"[CLIENT] Ошибка: {e}")
    finally:
        client_socket.close()
        print("[CLIENT] Соединение закрыто")


if __name__ == "__main__":
    message = sys.argv[1] if len(sys.argv) > 1 else "Hello World!"
    host = sys.argv[2] if len(sys.argv) > 2 else '127.0.0.1'
    port = int(sys.argv[3]) if len(sys.argv) > 3 else 5555

    send_message(message, host, port)