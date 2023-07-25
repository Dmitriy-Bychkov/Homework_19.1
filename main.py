from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

hostName = "localhost"  # Адрес для доступа по локальной сети
serverPort = 8080  # Порт доступа


class MyServer(BaseHTTPRequestHandler):
    """
    Класс отвечает за обработку входящих запросов от клиентов
    """

    def __get_html_content(self):
        """
        Метод получения html разметки из файла index.html
        """

        html_file = "index.html"

        try:
            with open(html_file, "r", encoding="utf-8") as file:
                html_content = file.read()
                return html_content

        except FileNotFoundError:
            print(f"Файл '{html_file}' не найден.")
            return None

        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return None

    def do_GET(self):
        """
        Метод обработки GET-запросов
        """

        #query_components = parse_qs(urlparse(self.path).query)
        page_content = self.__get_html_content()
        self.send_response(200)  # Отправка кода ответа
        self.send_header("Content-type", "text/html")  # Отправка типа данных, который будет передаваться
        self.end_headers()  # Завершение формирования заголовков ответа
        self.wfile.write(bytes(page_content, "utf-8"))  # Тело ответа


if __name__ == "__main__":
    # Инициализация веб-сервера

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросовд
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")
