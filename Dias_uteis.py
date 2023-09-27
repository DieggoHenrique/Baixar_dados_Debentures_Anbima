import requests
from bs4 import BeautifulSoup
from datetime import datetime

def is_dia_util(data):
    # Verificar se a data é um sábado (5) ou domingo (6)
    if data.weekday() in [5, 6]:
        return False

    # Verificar se a data é um feriado no Brasil
    url_feriados = "https://www.calendario.com.br/feriados-federais.php"
    response = requests.get(url_feriados)
    soup = BeautifulSoup(response.text, 'html.parser')

    feriados = [dia.text for dia in soup.find_all("td", class_="tabela")]
    feriados = [feriado.strip() for feriado in feriados]

    data_str = data.strftime("%d/%m/%Y")

    if data_str in feriados:
        return False

    return True

if __name__ == "__main__":
    data = datetime(2023, 9, 7)  # Substitua pela data que você deseja verificar

    if is_dia_util(data):
        print("A data é um dia útil no Brasil.")
    else:
        print("A data não é um dia útil no Brasil (sábado, domingo ou feriado).")

