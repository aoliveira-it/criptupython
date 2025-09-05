import os # Importa  interagir com o sistema operacional
from cryptography.fernet import Fernet # Impotar a classe para criptografia simétrica
import base64 # Importa para codificação e decodificação em base64
import hashlib # Importa para funções de hash

def gerar_chave(senha):
    # Gera uma chave a partir da senha fornecida
    # Usa SHA-256 para criar um hash da senha e depois codifica em base64
    return base64.urlsafe_b64encode(hashlib.sha256(senha.encode()).digest())

def criptografar_arquivo(caminho_arquivo, chave):
    # Abre o arquivo em modo leitura binária
    with open(caminho_arquivo, 'rb') as f:
        dados = f.read() # Lê os dados do arquivo   
    fernet = Fernet(chave) # Cria um objeto Fernet com a chave gerada
    dados_criptografados = fernet.encrypt(dados) # Criptografa os dados do arquivo

    # Escreve os dados criptografados em um novo arquivo com extensão .enc
    with open(caminho_arquivo + '.enc', 'wb') as f: # Abre o arquivo em modo escrita binária
        f.write(dados_criptografados) # Escreve os dados criptografados no novo arquivo
    os.remove(caminho_arquivo) # Remove o arquivo original

def criptografar_pasta(caminho_pasta, senha):
    chave = gerar_chave(senha) # Gera a chave a partir da senha
    # Percorre todos os arquivos na pasta e subpastas
    for root, _, files in os.walk(caminho_pasta): # Percorre a árvore de diretórios
        for  nome_arquivo in files: # Itera sobre os arquivos
            caminho_arquivo = os.path.join(root, nome_arquivo) # Cria o caminho completo do arquivo
            criptografar_arquivo(caminho_arquivo, chave) # Criptografa o arquivo
    print("Criptografia concluida.") # Mensagem de conclusão

if __name__ == "__main__":
     
    pasta = input("Digite o caminho da pasta a ser criptografada: ") #
    senha = input("Digite a senha para criptografia: ")
    criptografar_pasta(pasta, senha) # Chama a função para criptografar a pasta