
# Baixando as bibliotecas necessárias para o projeto
import requests
import os
from datetime import datetime, date, timedelta


def baixa_base_ambima(data):

    def converter_data_formato(data_str):
        """_summary_
        The aimed of this function is update the type of date for the url patern of Anbima site.

        Args:
            data_str (_type_): Take the date in format dd/mm/yyyy and convert to pattern yymmdd.

        Returns:
            _type_: The Function return the date in format yymmdd.
        """
        try:
            # Converter a data de entrada para um objeto datetime
            data = datetime.strptime(data_str, "%d/%m/%Y")

            # Formatando a data no formato "yymmdd"
            data_formatada = data.strftime("%y%m%d")

            return data_formatada
        except ValueError:
            return "Data de entrada inválida. Use o formato 'dd/mm/yyyy'."
        
    try:
        # Converter a data dd/mm/yyyy para yymmdd, formato da url da anbima
        data_format = converter_data_formato(data)
        # incluindo a data formatada na url da anbima
        url = f"https://www.anbima.com.br/informacoes/merc-sec-debentures/arqs/db{data_format}.txt"
        # O nome em que o arquivo será salvo no diretório
        nome_arquivo = f"db{data_format}.txt"
        # Diretório
        diretorio = "C:/Users/dieggo.araujo/Downloads/06 - MAX/06 - MAX/Arquivos_diários/"
        
        # Fazendo a requisição ao site por meio da url
        response = requests.get(url)
        # Verificar se houve algum erro na requisição HTTP 
        response.raise_for_status()  

        # Montar o caminho completo do arquivo no diretório especificado
        caminho_arquivo = os.path.join(diretorio, nome_arquivo)

        # Salva o arquivo no diretório
        with open(caminho_arquivo, 'wb') as arquivo:
            arquivo.write(response.content)

        # Abre (r) o conteúdo do arquivo e substituir "@" por ";"
        with open(caminho_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            conteudo = conteudo.replace('@', ';')

        # Salvar o conteúdo modificado no arquivo
        with open(caminho_arquivo, 'w') as arquivo:
            arquivo.write(conteudo)
    
        print(f"Arquivo {nome_arquivo} baixado e delimitador '@' substituído por ';' no diretório {diretorio} com sucesso!")
    except Exception as e:

        # Se ocorrer um erro, salvar os detalhes do erro em um arquivo de erro.
        erro = f"Ocorreu um erro ao baixar e modificar o arquivo: {str(e)}"
        with open("erro.txt", 'w') as arquivo_erro:
            arquivo_erro.write(erro)

# Executa a aplicação
if __name__ == "__main__":
    hoje = date.today()                     # Date de hoje
    ontem = timedelta(-1)                   # Menos um dia
    ontem = hoje + timedelta(-1)            # Pegando o dia de ontem
    data = ontem.strftime('%d/%m/%Y')       # Formatando para dd/mm/yyyy
    baixa_base_ambima(data)                 # Executando a Função

