# Leitura e Processamento de Múltiplos Arquivos com Python

Projeto desenvolvido em **Python**, utilizando exclusivamente recursos da biblioteca padrão para realizar a leitura automática de múltiplos arquivos de texto armazenados em um diretório.

O sistema percorre uma pasta, identifica arquivos com extensão `.txt`, lê seus conteúdos e apresenta as informações no terminal.

O objetivo é demonstrar conceitos fundamentais de **manipulação de arquivos (File I/O), navegação em diretórios e processamento sequencial de documentos**.

## Objetivo do projeto

Demonstrar como automatizar a leitura de múltiplos arquivos de texto utilizando Python, sem necessidade de bibliotecas externas.

Esse tipo de operação é uma etapa fundamental em aplicações que trabalham com:

- Documentos e arquivos textuais.
- Logs de sistemas.
- Relatórios.
- Extração e preparação de informações.
- Pipelines de processamento de dados.
- Aplicações backend e sistemas com Inteligência Artificial.

O projeto concentra-se na etapa inicial desse processo: localizar, abrir e ler arquivos de texto.

## Funcionalidades

- Leitura automática de múltiplos arquivos `.txt`.
- Identificação de arquivos dentro de um diretório.
- Construção de caminhos utilizando `os.path.join()`.
- Leitura de conteúdo com codificação UTF-8.
- Exibição do nome de cada arquivo.
- Exibição do conteúdo diretamente no terminal.
- Filtro de arquivos por extensão.
- Processamento sequencial dos documentos encontrados.

## Tecnologias utilizadas

- Python
- Biblioteca padrão `os`
- File I/O
- Manipulação de diretórios
- Codificação UTF-8
- Processamento sequencial de arquivos

**Não é necessário instalar bibliotecas externas.**

## Estrutura do projeto

```text
Leitura-e-Processamento-de-Multiplos-Arquivos-com-Python/
│
├── documentos/
│   ├── teste1.txt
│   ├── teste2.txt
│   └── teste3.csv
│
├── nivel5_ler_varios_arquivos_OK.py
└── README.md
```

Os arquivos apresentados na pasta `documentos` foram utilizados nos testes locais. Outros arquivos `.txt` podem ser adicionados ou utilizados em seu lugar.

## Como funciona

O programa utiliza a biblioteca `os` para percorrer os arquivos de um diretório chamado `documentos`.

### 1. Definição do diretório

```python
import os

PASTA = "documentos"
```

A variável `PASTA` indica o diretório que será utilizado na leitura.

### 2. Identificação dos arquivos

```python
for nome_arquivo in os.listdir(PASTA):
    caminho = os.path.join(PASTA, nome_arquivo)
```

O método `os.listdir()` retorna os nomes das entradas encontradas no diretório.

A função `os.path.join()` constrói o caminho utilizado para acessar cada arquivo.

### 3. Filtro de arquivos `.txt`

```python
if caminho.endswith(".txt"):
```

O programa seleciona apenas os caminhos que terminam com a extensão `.txt`.

Arquivos com outras extensões, como `.csv`, não são processados.

### 4. Leitura dos arquivos

```python
with open(caminho, "r", encoding="utf-8") as f:
    conteudo = f.read()
```

O comando `with open()` permite abrir o arquivo e fechá-lo automaticamente ao final da operação.

O método `read()` realiza a leitura completa do conteúdo.

### 5. Exibição das informações

```python
print("=" * 40)
print(f"Arquivo: {nome_arquivo}")
print(conteudo)
```

O programa exibe uma linha separadora, o nome do arquivo e seu conteúdo.

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/jrm0316/Leitura-e-Processamento-de-Multiplos-Arquivos-com-Python.git
```

Entre no diretório:

```bash
cd Leitura-e-Processamento-de-Multiplos-Arquivos-com-Python
```

### 2. Criar a pasta de documentos

Caso a pasta `documentos` ainda não exista, crie-a na raiz do projeto.

No PowerShell:

```powershell
mkdir documentos
```

### 3. Adicionar arquivos de texto

Coloque um ou mais arquivos `.txt` dentro da pasta `documentos`.

Exemplo:

```text
documentos/
├── exemplo1.txt
├── exemplo2.txt
└── exemplo3.txt
```

### 4. Executar o programa

```powershell
python .\nivel5_ler_varios_arquivos_OK.py
```

O programa deverá ser executado a partir do diretório raiz do projeto, onde está localizada a pasta `documentos`.

## Exemplo de execução

Considerando dois arquivos de teste:

**teste1.txt**

```text
Este é o primeiro arquivo de teste do projeto.
```

**teste2.txt**

```text
Este é o segundo arquivo. Estamos testando a leitura de múltiplos documentos com Python.
```

A execução apresenta:

```text
========================================
Arquivo: teste1.txt
Este é o primeiro arquivo de teste do projeto.

========================================
Arquivo: teste2.txt
Este é o segundo arquivo. Estamos testando a leitura de múltiplos documentos com Python.
```

A ordem de leitura pode variar conforme a listagem retornada pelo sistema operacional.

## Testes realizados

Foram realizados dois testes funcionais no ambiente Windows, utilizando o terminal PowerShell do Cursor.

### Teste 1 — Leitura de múltiplos arquivos

Foram criados dois arquivos:

- `teste1.txt`
- `teste2.txt`

Ambos foram armazenados no diretório `documentos`.

**Resultado:** o programa identificou e exibiu corretamente o nome e o conteúdo dos dois arquivos.

### Teste 2 — Filtro por extensão

Foi adicionado um terceiro arquivo:

`teste3.csv`

O objetivo era verificar se o programa continuaria processando somente os arquivos `.txt`.

**Resultado:** os arquivos `teste1.txt` e `teste2.txt` foram lidos normalmente, enquanto `teste3.csv` foi ignorado.

Os dois testes foram concluídos com sucesso.

## Alterando os arquivos analisados

Para utilizar outros documentos:

1. Adicione ou substitua arquivos `.txt` dentro da pasta `documentos`.
2. Execute novamente o programa.
3. Os arquivos encontrados serão lidos e exibidos no terminal.

Não é necessário modificar o código para adicionar novos arquivos ao diretório.

## Limitações atuais

- O programa realiza leitura e exibição, sem transformação ou análise do conteúdo.
- Não possui tratamento específico para arquivos inexistentes, inacessíveis ou com codificação inválida.
- A pasta `documentos` precisa existir.
- Os arquivos são lidos integralmente em memória.
- Não realiza leitura recursiva de subdiretórios.
- O filtro identifica a extensão `.txt` em letras minúsculas.
- Não possui interface gráfica ou web.
- Não armazena resultados em banco de dados.

## Possíveis melhorias futuras

- Adicionar tratamento de exceções.
- Verificar automaticamente a existência do diretório.
- Permitir informar a pasta por argumento de linha de comando.
- Implementar leitura recursiva de subdiretórios.
- Suportar outros formatos de arquivos.
- Adicionar processamento e limpeza de textos.
- Implementar logs de execução.
- Integrar a leitura de documentos com pipelines de IA e RAG.

Essas funcionalidades representam possibilidades de evolução e não fazem parte da versão atual.

## Relevância técnica

Este projeto demonstra a aplicação prática de conceitos fundamentais para o desenvolvimento de software com Python:

- Manipulação de arquivos e diretórios.
- Utilização da biblioteca padrão.
- Leitura de dados textuais.
- Organização de operações sequenciais.
- Automação de tarefas repetitivas.
- Preparação de uma base para processamento posterior de documentos.

Esses conhecimentos podem ser utilizados em aplicações backend, ferramentas de automação e sistemas de processamento de informações.

## Autor

**Juliano Rodrigues Madeira**

Projeto desenvolvido para estudo e aplicação prática de Python, manipulação de arquivos e automação de leitura de documentos.

GitHub: [jrm0316](https://github.com/jrm0316)
