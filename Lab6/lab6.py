import socket
import sys
import operator as op

operators={'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}
host = ''
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
stack = []

try:
	s.bind((host, port))
except socket.error as e:
	print(str(e))

s.listen(5)

while True:
	print('Oczekiwanie na połączenie')
	connection, client = s.accept()
	try:
		print('client connected: ' + client[0])
		connection.sendall(str.encode("Kalkulator RPN. Aby poznac wynik podaj znak ="))

		while True:
			data = connection.recv(16)
			if data:
				parsedData = str(data).replace('b', '').replace('\'', '')

				if parsedData != '=':
					if parsedData in operators:
						res = operators[parsedData](stack.pop(),stack.pop())
					else:
						res = float(parsedData)
					stack.append(res)
				else:
					connection.sendall(str.encode('wynik: ' + str(stack.pop())))
					stack = []
			else:
				break

	except NameError as err:
		e = sys.exc_info()[0]
		print(str(e))
		print(str(err))
	finally:
		connection.close()