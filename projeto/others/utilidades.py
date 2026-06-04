import os
from datetime import datetime
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

from datetime import datetime

def calcular_idade(data_nascimento):
    nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")

    hoje = datetime.today()

    idade = hoje.year - nascimento.year

    if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
        idade -= 1

    return idade