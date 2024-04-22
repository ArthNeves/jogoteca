# Meu Primeiro Projeto Flask

Este é um projeto Flask simples para gerenciar uma lista de jogos e permitir que os usuários criem novos jogos após fazer login.

## Funcionalidades

- Visualizar uma lista de jogos existentes.
- Adicionar novos jogos após fazer login.
- Autenticar usuários com login e senha.
- Proteger rotas que requerem autenticação.

## Pré-requisitos

- Python 3.x instalado
- Poetry instalado (você pode instalar executando `poetry install`)


## Executando o Projeto

1. Clone este repositório:
   ```
   git clone https://github.com/seu_usuario/seu_projeto.git
   ```

2. Navegue até o diretório do projeto:
   ```
   cd jogoteca
   ```

2. Navegue até o diretório do projeto:
   ```
   poetry shell
   ```

3. Execute o script Python para iniciar o servidor Flask:
   ```
   python jogoteca.py
   ```

4. Abra um navegador da web e acesse `http://localhost:5000` para ver o aplicativo em funcionamento.

## Estrutura do Projeto

```
├── jogoteca.py                   # Script principal do Flask
├── README.md                     # Este arquivo de documentação
└── static/
    ├── bootstrap.css             # Arquivo CSS para estilos personalizados
└── templates/
    ├── lista.html                # Template HTML para exibir a lista de jogos
    ├── login.html                # Template HTML para a página de login
    ├── novo.html                 # Template HTML para adicionar novos jogos
    ├── template.html                # Template base que outros templates estendem
```

## Contribuindo

Contribuições são bem-vindas! Se você tiver alguma sugestão, correção de bugs ou novos recursos, sinta-se à vontade para abrir uma issue ou enviar um pull request.
