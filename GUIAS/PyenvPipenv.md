## 💜 Comandos úteis do pyenv

O `pyenv` é usado para gerenciar múltiplas versões do Python.

### 🛠 Instalação e Configuração

```sh
pyenv install --list              # Lista todas as versões disponíveis para instalação
pyenv install 3.11.4              # Instala a versão 3.11.4 do Python
pyenv uninstall 3.11.4            # Remove a versão 3.11.4 do Python
pyenv rehash                      # Reconfigura os links simbólicos após instalar/remover versões
```

### 🔄 Gerenciamento de Versões

```sh
pyenv versions                    # Lista todas as versões instaladas
pyenv global 3.11.4               # Define a versão global do Python
pyenv local 3.11.4                # Define a versão do Python para um diretório específico
pyenv shell 3.11.4                # Define a versão do Python para a sessão atual do terminal
pyenv which python                # Mostra o caminho do executável Python ativo
pyenv version                      # Mostra a versão do Python atualmente ativa
```

### 🔍 Debug e Informações

```sh
pyenv doctor                      # Diagnostica possíveis problemas na configuração do pyenv
pyenv help                        # Mostra a ajuda geral do pyenv
pyenv commands                    # Lista todos os comandos disponíveis no pyenv
```

### 🔥 Removendo o pyenv

```sh
rm -rf ~/.pyenv                   # Remove o pyenv completamente (Linux/macOS)
```

---

## 💜 Comandos úteis do pipenv

O `pipenv` é usado para gerenciar dependências e ambientes virtuais do Python.

### 🛠 Instalação e Inicialização

```sh
pipenv install                     # Instala dependências do Pipfile
pipenv install requests             # Instala uma dependência no ambiente virtual
pipenv install --dev pytest         # Instala uma dependência apenas para desenvolvimento
pipenv uninstall requests           # Remove uma dependência
pipenv install --skip-lock          # Instala dependências sem travar o Pipfile.lock
pipenv lock                         # Gera ou atualiza o Pipfile.lock
```

### 🔄 Gerenciamento do Ambiente Virtual

```sh
pipenv --venv                       # Mostra o caminho do ambiente virtual
pipenv shell                        # Ativa o ambiente virtual
pipenv run python                    # Executa o Python dentro do ambiente virtual
pipenv run pytest                    # Executa um comando no ambiente virtual
pipenv uninstall --all               # Remove todas as dependências e o ambiente virtual
```

### 🔍 Debug e Informações

```sh
pipenv graph                         # Mostra a árvore de dependências
pipenv check                         # Verifica vulnerabilidades nas dependências
pipenv sync                          # Instala dependências baseadas no Pipfile.lock
```

### 🔥 Removendo o pipenv

```sh
pipenv --rm                          # Remove o ambiente virtual
```

---

## 📊 Comandos adicionais do pyenv

### Instalação de Versões do Python

```sh
pyenv install --list  # Lista todas as versões disponíveis para instalação
pyenv install <versão>  # Instalar uma versão específica do Python
pyenv uninstall <versão>  # Remover uma versão do Python
```

### Gerenciamento de Versões

```sh
pyenv global <versão>  # Define a versão padrão do Python para todo o sistema
pyenv local <versão>  # Define a versão do Python para um diretório específico
pyenv shell <versão>  # Define a versão do Python para a sessão atual do shell
pyenv versions  # Lista todas as versões instaladas do Python
pyenv version  # Exibir a versão do Python atualmente ativa
```

---

## 📊 Comandos adicionais do pipenv

### Instalação e Ambiente Virtual

```sh
pipenv install  # Instalar dependências definidas no Pipfile
pipenv install <pacote>  # Instalar uma nova dependência
pipenv install <pacote> --dev  # Instalar uma dependência apenas para desenvolvimento
pipenv uninstall <pacote>  # Desinstalar uma dependência
pipenv uninstall --all  # Remover todas as dependências e o ambiente virtual
```

### Gerenciamento do Ambiente Virtual

```sh
pipenv shell  # Ativar o ambiente virtual
pipenv run <comando>  # Executar um comando dentro do ambiente virtual sem ativá-lo
pipenv --venv  # Exibir o caminho do ambiente virtual
pipenv lock  # Gerar ou atualizar o Pipfile.lock
pipenv sync  # Instalar dependências diretamente do Pipfile.lock
```

### Utilitários

```sh
pipenv check  # Verificar vulnerabilidades de segurança nas dependências
pipenv graph  # Exibir a árvore de dependências do projeto
```

---
