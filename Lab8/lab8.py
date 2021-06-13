import socket
import sys


def getResponse(status="0"):
    if status == "0":
        body = "<html><body>Obecny stan maszyny: <b>Wylaczona</b><br><a href=\"/wlacz\">Wlacz</a></body></html>\n"
    else:
        body = "<html><body>Obecny stan maszyny: <b>Wlaczona</b><br><a href=\"/wylacz\">Wylacz</a></body></html>\n"
    headers = "HTTP/1.1 200 OK\nContent-Type: text/html\nContent-Length: " + str(len(body)) + "\nConnection: close\n"

    return headers + "\n" + body


host = ''
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))

s.listen(1)

while True:
    print('Oczekiwanie na połączenie')
    connection, client = s.accept()
    try:
        print('client connected: ' + client[0])

        data = connection.recv(12)
        parsedData = str(data).replace('b', '').replace('\'', '')

        if '/wlacz' in parsedData:
            with open('machine.txt', 'w') as statusFile:
                statusFile.write("1")
            connection.send(str.encode(getResponse("1")));
        elif '/wylacz' in parsedData:
            with open('machine.txt', 'w') as statusFile:
                statusFile.write("0")
            connection.send(str.encode(getResponse("0")));
        else:
            with open('machine.txt', 'r') as statusFile:
                connection.send(str.encode(getResponse(statusFile.read())));

        connection.close()

    except NameError as err:
        e = sys.exc_info()[0]
        print(str(e))
        print(str(err))
    finally:
        connection.close()