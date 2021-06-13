import socket


with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
	s.connect(("youtube.com",80))
	s.sendall(b"GET / HTTP/1.1\r\nHost:youtube.com\r\n\r\n")
	getted = str(s.recv(4096),'utf-8')

	with open("data.txt","w") as f:
		f.write(getted)