# Leitor-de-Multiplos-Arquivos-de-Texto-em-Python

Propósito do projeto
- Este projeto tem como objetivo demonstrar a leitura automática de múltiplos arquivos de texto a partir de um diretório específico, utilizando Python puro.
- Ele representa a base de qualquer aplicação backend que trabalha com:
   * documentos
   * logs
   * relatórios
   * dados textuais
   * pré-processamento de informações
- Antes de usar IA, é essencial dominar arquivos, diretórios e fluxo de dados — e esse projeto foca exatamente nisso.


Como o programa funciona
- O script percorre uma pasta chamada documentos, identifica todos os arquivos .txt e:
  1.) Abre cada arquivo individualmente
  2.) Lê seu conteúdo utilizando codificação UTF-8
  3.) Exibe o nome do arquivo
  4.) Imprime o conteúdo no terminal de forma organizada
- Cada arquivo é tratado de forma independente, simulando um cenário real de processamento em lote.


Tecnologias e conceitos utilizados
- Python
- File I/O
- Leitura de diretórios
- Manipulação de caminhos com os
- Codificação UTF-8
- Processamento em lote
- Backend básico
- Organização de dados em pastas


Estrutura do projeto
projeto/
├── documentos/
│   ├── doc1.txt
│   ├── doc2.txt
│   └── doc3.txt
├── ler_varios_arquivos.py
└── README.md

Essa estrutura é comum em sistemas que processam grandes volumes de arquivos.


- Como executar o projeto
  1.) Clone o repositório:

  git clone https://github.com/seu-usuario/leitor-multiplos-arquivos-python

  2.) Crie a pasta documentos no mesmo diretório do script
  3.) Adicione arquivos .txt dentro da pasta
  4.) Execute o programa:

  python ler_varios_arquivos.py


Alterando os arquivos analisados
- Para adicionar novos arquivos, basta:
   * Criar ou copiar arquivos .txt para a pasta documentos
   * Executar novamente o script
- O código não precisa ser alterado.


Por que este projeto é relevante?
- Porque ele demonstra que você sabe:
   * Trabalhar com múltiplos arquivos
   * Organizar dados em diretórios
   * Criar scripts reutilizáveis
   * Preparar dados para processamento posterior
- Construir a base para:
    * análise de documentos
    * pipelines de dados
    * integração com IA
    * sistemas backend reais
- Muitos erros em projetos com IA começam aqui — e este projeto mostra que você domina essa etapa.


Resumo profissional
- Script desenvolvido em Python para leitura e processamento automático de múltiplos arquivos de texto a partir de um diretório específico.
- O projeto demonstra domínio de File I/O, organização de dados e lógica de processamento em lote, servindo como base para aplicações backend e futuras integrações com inteligência artificial.
