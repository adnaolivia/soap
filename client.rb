require 'savon'

# URL do WSDL do serviço SOAP
wsdl_url = 'http://localhost:8000/soap?wsdl'

# Cria o cliente SOAP
client = Savon.client(wsdl: wsdl_url)

# Chama o método 'fazer_reserva' do serviço SOAP
response = client.call(:fazer_reserva, message: { nomeCliente: 'João SOPA', tipoQuarto: 'Solteiro' }) # rpc -> Unicode
response_body = response.body
# Exibe a resposta
confirmation_number = response.body[:fazer_reserva_response][:fazer_reserva_result]
puts "numero de confirmacao: #{confirmation_number}"
