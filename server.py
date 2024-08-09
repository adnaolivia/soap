from spyne import Application, rpc, ServiceBase, Unicode, Integer
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
import random

class HotelService(ServiceBase):
    @rpc(Unicode, Unicode, _returns=Unicode)
    def fazer_reserva(contexto, nomeCliente, tipoQuarto): # 2 entradas Unicode e 1 saida Unicode
        numero_confirmacao = f"CONF-{random.randint(1000, 9999)}"
        print(f"reserva criada para {nomeCliente} no quarto {tipoQuarto}. número de confirmação: {numero_confirmacao}")
        return numero_confirmacao

# cria a aplicacao
aplicacao = Application([HotelService], tns='spyne.reserva_hotel', in_protocol=Soap11(), out_protocol=Soap11()) # tns - namespace do destino

# servidor WSGI
aplicacao_wsgi = WsgiApplication(aplicacao)

if __name__ == '__main__':
    server = make_server('localhost', 8000, aplicacao_wsgi) # cria o servidor
    print("Servidor SABAO rodando :)")
    server.serve_forever()


'''
rpc -> decorador; indica que o método a seguir é uma operacao SOPA; pode ser chamado remotramente por um cliente
Unicode -> tipo de dado do spyne usado para representar str
    -> parametros dos tipos de dados que o metodo aceita; neste caso, o metodo espera 2 argumentos de entrada do tipo Unicode e o retorno deste metodo tambem é do tipo Unicode
tns -> namespace de destino
contexto -> contém informações sobre a solicitação, como cabeçalhos HTTP, detalhes da mensagem SOAP
'''