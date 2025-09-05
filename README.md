# Projeto de Criptografia de Pastas em Python

Este projeto permite criptografar e descriptografar arquivos de uma pasta usando senha, com a biblioteca `cryptography`.

## Como usar

### Instalação

```bash
pip install cryptography
```

### Criptografar

```bash
python criptu.py
```
Informe o caminho da pasta e a senha.

### Descriptografar

```bash
python descriptu.py
```
Informe o caminho da pasta e a senha usada na criptografia.

## Segurança

A chave é gerada a partir da senha usando SHA-256 e base64. Guarde sua senha, pois sem ela não é possível recuperar os arquivos.

## Licença

MIT