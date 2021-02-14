import socketserver
import os

# os.chdir(os.getcwd()) # Se estiver com problemas de achar a pasta Teste


# A mensagem dos arquivos que o cliente vai baixar

mensagem = '-- OPÇÕES ENCONTRADAS -- \n\n'

arquivos = os.listdir('Teste')

for i_arq in range(len(arquivos)):
	arq = arquivos[i_arq]
	mensagem += f'[{i_arq}] ' + str(arq) + '\n'

mensagem += '\n' + 'Qual deles deseja baixar? '


# A programação do servidor

port = 50000
host = 'localhost'

class Requisicao(socketserver.BaseRequestHandler):
    def handle(self):
        print('requisição feita pelo endereço:', self.client_address)

        self.request.send(mensagem.encode())

        opc = self.request.recv(128)
        opc = int(opc.decode())

        temp = arquivos[opc]

        with open(f'Teste\\{temp}', 'r') as dados:
        	arq = str([temp, dados.readlines()])
        	print('prestes a mandar arquivo requisitado!')

        self.request.send(arq.encode())

        # Enviou o pedido termina a conexão
        self.request.close()

        print('rompendo conexão')
        print('\n')


print(' -- servidor iniciado -- ')

endrc = (host, port)

server = socketserver.ThreadingTCPServer(endrc, Requisicao)
server.serve_forever()
