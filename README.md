# FITTEXT

## Sobre o programa

Este programa lê um texto em um arquivo e o imprime no terminal com um limite máximo de caracteres por linha.
Os parágrafos devem ser separados no arquivo por uma linha em branco.
Os espaços no arquivo precedidos por uma barra invertida ("\") escapam as palavras entre ele de ocuparem linhas diferentes.

### Arquivos

* `fitText.py`: arquivo executável do programa.
* `examples/input.txt`: exemplo de arquivo de entrada para teste.
* `examples/output1.txt`: arquivo com a saída do exemplo.
* `examples/output2.txt`: arquivo com a saída do exemplo (linhas justificadas). 


### Requisitos de instalação

* Python 2.7.* (não testado no Python 3.*)
* [numpy](https://www.numpy.org/)


### Executando localmente

Para executar localmente -- isto é, diretamente de dentro deste diretório --, passar o comando com a seguinte sintaxe no terminal:

```
python fitText.py [-h] [-j] [-n <num_char>] <file>
```

ou

```
./fitText.py [-h] [-j] [-n <num_char>] <file>
```

* Parâmetro obrigatório:
    * `<file>`: caminho para o arquivo de entrada a ser editado.

* Parâmetros opcionais:
    * `-h`, `--help`: exibe mensagem de ajuda do programa
    * `-j`, `--justify`: habilita a justificação o texto
    * `-n <num_char>`, `--num_char <num_char>`: número máximo de caracteres em cada linha (padrão = 40)


### Instalando no Linux

Para instalar o programa no Linux, de modo que possa ser chamado em qualquer diretório pelo simples comando `fitText`, executar os seguintes comandos no terminal:

```
sudo mkdir /usr/local/share/fitText
sudo cp * /usr/local/share/fitText
sudo ln -s /usr/local/share/fitText/fitText.py /usr/local/bin/fitText
sudo chmod a+x /usr/local/share/fitText/fitText.py /usr/local/bin/fitText
sudo chmod a+r /usr/local/share/fitText/*
```

A sintaxe é a mesma da [execução local](#executando-localmente)


### Status

Ao finalizado, o programa retorna um código padrão de status para o sistema:

* 0: caso o processamento tenha sido efetuado com sucesso.
* 1: caso tenha ocorrido algum erro.



## Testes

Após a instalação, seja no sistema ou localmente, execute os dois testes a seguir.


### Teste 1

Para testar o código localmente, rode-o em um terminal dentro do diretório raiz deste programa com o seguinte código:

```
python ./fitText examples/input.txt
```

No caso do teste da instalação no sistema, rode o seguinte comando:

```
fitText examples/input.txt
```

O resultado deve ser igual ao arquivo `eamples/output1.txt`.


### Teste 2

Para testar o código localmente, rode-o em um terminal dentro do diretório raiz deste programa com o seguinte código:

```
python ./fitText -j examples/input.txt
```

No caso do teste da instalação no sistema, rode o seguinte comando:

```
fitText -j examples/input.txt
```

O resultado deve ser igual ao arquivo `examples/output2.txt`.


## Log

2019-02-10: implementação do escape no espaço entre palavras que devem ocupar a mesma linha ("\ ")


## Autor

Daniel Bednarski Ramos

[https://www.astro.iag.usp.br/~bednarski](https://www.astro.iag.usp.br/~bednarski)

daniel.bednarski.ramos@gmail.com


## Licença

GNU GPLv3
