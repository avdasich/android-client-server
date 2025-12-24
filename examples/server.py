import socket
import sys
from datetime import datetime


def start_server(host='127.0.0.1', port=5555):

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server_socket.bind((host, port))
        print(f"[SERVER] Сервер запущен на {host}:{port}")

        server_socket.listen(5)
        print("[SERVER] Ожидание подключений...")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"\n[SERVER] Подключился клиент: {client_address}")

            try:
                data = client_socket.recv(1024)

                if data:
                    message = data.decode('utf-8')
                    print(f"[SERVER] Получено: {message}")

                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    response = f"Server received: '{message}' at {timestamp}"

                    client_socket.send(response.encode('utf-8'))
                    print(f"[SERVER] Отправлено: {response}")

            except Exception as e:
                print(f"[SERVER] Ошибка обработки клиента: {e}")

            finally:
                client_socket.close()
                print(f"[SERVER] Соединение с {client_address} закрыто")

    except KeyboardInterrupt:
        print("\n[SERVER] Остановка сервера...")
    except Exception as e:
        print(f"[SERVER] Ошибка: {e}")
    finally:
        server_socket.close()
        print("[SERVER] Сервер остановлен")


if __name__ == "__main__":
    host = sys.argv[1] if len(sys.argv) > 1 else '127.0.0.1'
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 5555

    start_server(host, port)