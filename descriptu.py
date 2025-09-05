import os  # Importa para interagir com o sistema operacional
from cryptography.fernet import Fernet  # Importa a classe para criptografia simétrica
import base64  # Importa para codificação e decodificação em base64
import hashlib  # Importa para funções de hash

def gerar_chave(senha):
    # Gera uma chave a partir da senha fornecida
    return base64.urlsafe_b64encode(hashlib.sha256(senha.encode()).digest())

def descriptografar_arquivo(caminho_arquivo, chave):
    # Abre o arquivo criptografado em modo leitura binária
    with open(caminho_arquivo, 'rb') as f:
        dados_criptografados = f.read()  # Lê os dados criptografados
    fernet = Fernet(chave)  # Cria um objeto Fernet com a chave gerada
    dados = fernet.decrypt(dados_criptografados)  # Descriptografa os dados
    # Remove a extensão .enc para restaurar o nome original
    caminho_original = caminho_arquivo[:-4]
    # Escreve os dados descriptografados no arquivo original
    with open(caminho_original, 'wb') as f:
        f.write(dados)
    os.remove(caminho_arquivo)  # Remove o arquivo criptografado

def descriptografar_pasta(caminho_pasta, senha):
    chave = gerar_chave(senha)  # Gera a chave a partir da senha
    # Percorre todos os arquivos na pasta e subpastas
    for root, _, files in os.walk(caminho_pasta):
        for nome_arquivo in files:
            if nome_arquivo.endswith('.enc'):  # Apenas arquivos criptografados
                caminho_arquivo = os.path.join(root, nome_arquivo)
                descriptografar_arquivo(caminho_arquivo, chave)
    print("Descriptografia concluída.")

if __name__ == "__main__":
    pasta = input("Digite o caminho da pasta a ser descriptografada: ")
    senha = input("Digite a senha para descriptografia: ")
    descriptografar_pasta(pasta, senha) # Chama a função para descriptografar a pasta