import subprocess
import os
import time

def obter_informacoes_sistema():
    informacoes = {}

    # Informações da memória RAM
    mem_info = subprocess.check_output('wmic MemoryChip get Capacity', shell=True).decode("utf-8").strip().split('\n')
    memoria_total = sum([int(x) for x in mem_info[1:]]) // (1024**3)  # Convertendo bytes para gigabytes
    informacoes['Memória RAM'] = f"{memoria_total} GB"

    # Frequência da memória RAM
    wmic_output = subprocess.check_output('wmic MemoryChip get Speed', shell=True).decode("utf-8").strip().split('\n')
    frequencia_ram = max([int(x) for x in wmic_output[1:]])  # Maior frequência entre as memórias
    informacoes['Frequência da memória RAM'] = f"{frequencia_ram} MHz"

    # Informações da GPU
    wmic_output = subprocess.check_output('wmic path win32_VideoController get Name', shell=True).decode("utf-8").strip().split('\n')
    gpu_info = [x.strip() for x in wmic_output[1:] if x.strip()]  # Remover linhas vazias
    informacoes['GPU'] = gpu_info[0] if gpu_info else "Não encontrada"

    subprocess.Popen('msinfo32')

    return informacoes

def salvar_em_arquivo(informacoes, arquivo):
    with open(arquivo, 'w') as f:
        for chave, valor in informacoes.items():
            f.write(f"{chave}: {valor}\n")

# Executar a função para obter as informações do sistema
informacoes_sistema = obter_informacoes_sistema()

# Salvar as informações em um arquivo de texto
arquivo_saida = 'informacoes_sistema.txt'
salvar_em_arquivo(informacoes_sistema, arquivo_saida)

# Abrir o arquivo de texto
subprocess.Popen(['notepad.exe', arquivo_saida])

# Aguardar um curto período de tempo (5 segundos) antes de excluir o arquivo
time.sleep(5)

# Excluir o arquivo
os.remove(arquivo_saida)
