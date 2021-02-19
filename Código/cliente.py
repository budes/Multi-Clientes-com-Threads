import socket
import os

# Configuração do socket

port = 50000
host = 'localhost'

sockobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sockobj.connect((host, port))

# Progamação do cliente

data = sockobj.recv(1024)
msg = data.decode()

while True:
	user = input(msg)
	try:
		int(user)
		assert int(user) < 7
		break 

	except:
		print('Valor inválido, tente de novo')
		print()

sockobj.send(user.encode())

print()

data = sockobj.recv(2048)
data.decode()

data = eval(data)

try:
	os.chdir('Cliente')
except:
	os.mkdir('Cliente')
	os.chdir('Cliente')
	
	
with open(data[0], 'w') as arq:
	for elemento in data[1]:
		arq.write(elemento)





