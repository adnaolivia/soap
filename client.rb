require 'savon'

# URL do WSDL do serviço SOAP
wsdl_url = 'http://localhost:8000/soap?wsdl'

# Cria o cliente SOAP
client = Savon.client(wsdl: wsdl_url)

# Chama o método 'reserve' do serviço SOAP
response = client.call(:reserve, message: { nomeCliente: 'João SOPA', tipoQuarto: 'Single Room' })

# Exibe a resposta
puts "numero de confirmacao: #{response.body[:reserve_response][:return]}"