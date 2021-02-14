# Multiplos-Clientes-Em-Threading-TCP
Sistema simples de download de arquivos para a demonstração do uso do socketserver em python

## O que foi usado?

• Python 3.9.1

• Sublime Text 3

• Módulo socket e socketserver


# Como Funciona?

## O lado do servidor

Inicia obtendo os dados da pasta Testes, e elaborando uma mensagem de log que vai ser usada para 
mostrar as opções ao usuário.

```
mensagem = '-- OPÇÕES ENCONTRADAS -- \n\n'

arquivos = os.listdir('Teste')

for i_arq in range(len(arquivos)):
    arq = arquivos[i_arq]
    mensagem += f'[{i_arq}] ' + str(arq) + '\n'

mensagem += '\n' + 'Qual deles deseja baixar? '
```

Depois o server cria um TCPServer por base no socketserver, esse server funcionará em MultiThreading
e fazendo uso do clássico modelo TCP/IP utilizando do endrc e do objeto que irá ser executado para cada
vez que ocorrer a conexão de um cliente.

Após isso executa um looping com o serve_forever().

```
endrc = (host, port)

server = socketserver.ThreadingTCPServer(endrc, Requisicao)
server.serve_forever()
```

### Programação para lidar com o cliente

Quando um cliente conectar ele irá mandar um print mostrando de qual endereço é o cliente que acabou de conectar e mandar a mensagem que foi elaborada antes para o cliente.

```
print('requisição feita pelo endereço:', self.client_address)
self.request.send(mensagem.encode())
```

E aguardar até que o cliente dê algum input que indique qual opção ele deseja.

`opc = self.request.recv(128)`

Por último, quando receber a opção, trasnforma os dados obtidos em algo utilizável `opc = int(opc.decode())` e usa isso para procurar qual arquivo que o cliente deseja `temp = arquivos[opc]`.

Usa dessas informações para ler os dados do arquivo, e criar uma espécie de estrutura de criação para a recriação desse arquivo.

```
with open(f'Teste\\{temp}', 'r') as dados:
     arq = str([temp, dados.readlines()])
     print('prestes a mandar arquivo requisitado!')
```

Após isso, manda e termina a conexão.

## O lado do cliente

O lado do cliente cria um socket com o modo de funcionamento TCP/IP também, mas a diferença é que é 
feito pelo módulo socket e que busca se conectar com o servidor inicialmente criado.

```
sockobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockobj.connect((host, port))
```

Recebe a mensagem enviada pelo servidor (`data = sockobj.recv(1024)`) e retorna para que o usuário leia ao colocar 
ela dentro de uma mensagem de input (após destransformar ela do formato de bytes `msg = data.decode()`).

```
while True:
    user = input(msg)
    try:
        int(user)
	assert int(user) < 7
	break 

    except:
	print('Valor inválido, tente de novo')
	print()
```

Ele faz alguns testes para assegurar que os dados colocados sejam dados adequados, entretanto tentei fazer de um modo
que ao colocar coisas como Ctrl+Z ele quebrasse, para que caso você execute sem querer, não tenha que fechar o cmd.

Após mandar os dados que o usuário pôs no input `sockobj.send(user.encode())`, tenta receber os dados do arquivo requisitado
`data = sockobj.recv(2048)` e utiliza desses dados para a recriação desse arquivo, mas dentro da pasta Cliente:

```
os.chdir('Cliente')

with open(data[0], 'w') as arq:
    for elemento in data[1]:
    arq.write(elemento)
```

A maior sacada feita nessa parte é que o server manda a lista em formato de string, isso foi feito para facilitar a codificação
e decodificação do data, aí para fazer com que os dados do arquivo eu fiz isso:

```
data.decode()
data = eval(data)
```

logo abaixo ao que recebe o data, facilitando a sua utilização.

# Output e Funcionamento:


