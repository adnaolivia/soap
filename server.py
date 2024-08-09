from spyne import Application, rpc, ServiceBase, Integer
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class CalculadoraService(ServiceBase):

    # O decorador @rpc é o mecanismo pelo qual você define as operações SOAP no Spyne. especifica os tipos de dados de entrada e saída
    @rpc(Integer, Integer, _returns=Integer) # @rps -> operacao soap; pode ser invocado por clientes
    def soma(contexto, a, b): # contexto: contém informações sobre a solicitação, como cabeçalhos HTTP, detalhes da mensagem SOAP
        return a + b

    @rpc(Integer, Integer, _returns=Integer)
    def subtracao(contexto, a, b):
        return a - b

# cria a aplicação
aplicacao = Application([CalculadoraService], tns='spyne.exemplo.calculadora', in_protocol=Soap11(), out_protocol=Soap11()) # tns= namespace de destindo

# servidor WSGI
aplicacao_wsgi = WsgiApplication(aplicacao)

if __name__ == '__main__':
    server = make_server('localhost', 8000, aplicacao_wsgi) # cria o servidor
    print("Servidor SOAP rodando na porta 8000 :)")
    server.serve_forever()
