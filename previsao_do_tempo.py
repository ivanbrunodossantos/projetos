# Importa a biblioteca 'requests' para fazer solicitações HTTP.
import requests


def obter_previsao_tempo(api_key, cidade):
    # Monta a URL da API do OpenWeatherMap com a chave de API e o nome da cidade.
    url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric'

    # Faz uma solicitação GET à API do OpenWeatherMap usando a URL.
    resposta = requests.get(url)

    # Verifica se a resposta da solicitação HTTP foi bem-sucedida (código de status 200).
    if resposta.status_code == 200:
        # Converte os dados JSON da resposta em um dicionário.
        dados = resposta.json()

        # Extrai informações relevantes do dicionário.
        nome_cidade = dados['name']
        temperatura = dados['main']['temp']
        descricao_clima = dados['weather'][0]['description']

        # Exibe a previsão do tempo na saída padrão.
        print(f'Previsão do tempo em {nome_cidade}:')
        print(f'Temperatura: {temperatura}°C')
        print(f'Descrição do clima: {descricao_clima}')
    else:
        # Se a resposta da API não for bem-sucedida, exibe uma mensagem de erro.
        print('Não foi possível obter a previsão do tempo.')


if __name__ == "__main__":
    # Chave de API do OpenWeatherMap. Substitua 'SUA_CHAVE_DE_API_AQUI' pela sua chave.
    api_key = 'coloque sua chave de API aqui'

    # Solicita ao usuário que insira o nome da cidade.
    cidade = input('Digite o nome da cidade: ')

    # Chama a função 'obter_previsao_tempo' com a chave de API e o nome da cidade como argumentos.
    obter_previsao_tempo(api_key, cidade)
