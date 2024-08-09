from spyne import Application, rpc, ServiceBase, Unicode, Integer
from spyne.protocol.soap import soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
import random

class HotelService(ServiceBase):
    @rpc(Unicode, Unicode, _returns=Unicode)
    def fazer_reserva(contexto, nomeCliente, tipoQuarto):
        numero_confirmacao = f"CONF-{random.randint(1000, 9999)}"
        print(f"reserva criada para {nomeCliente} no quarto {tipoQuarto}. número de confirmação: {numero_confirmacao}")
        return numero_confirmacao

aplicacao = Application([HotelService], tns='spyne.reserva_hotel', in_protocol=soap11(), out_protocol=soap11()) # tns - namespace do destino

aplicacao_wsgi = WsgiApplication(aplicacao)

if __name__ == '__main__':
    server = make_server('localhost', 8000, aplicacao_wsgi)
    print("Servidor SABAO rodando :)")
    server.serve_forever()