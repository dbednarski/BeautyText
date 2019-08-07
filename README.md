# BeautyText

Este é um pacote usado para a formatação de textos - em especial, limitação de caracteres por linhas. É composto pelo módulo Python `BeautyText` e por um script executável que o implementa.

### Estrutura de diretórios

* `beautytext`: diretório do módulo BeautyText
* `scripts` : diretório do script de implementação
* `examples`: arquivos exemplos para testes.



## Instalação


Primeiramente, escolha se deseja instalar localmente (apenas para seu usuário) ou em todo o sistema. Abra um terminal e, a partir do diretório raiz deste pacote:

* Para instalar localmente, execute o comando:
```
$ python setup.py install --user
```

* Para instalar em todo o sistema, execute o comando:
```
$ sudo python setup.py install
```

### Requisitos de instalação

* Python > 2.7
* [setuptools](https://pypi.org/project/setuptools)
* [numpy](https://www.numpy.org/)



# O pacote

## Módulo beautytext

O módulo beautytext é composto apenas por uma classe homônima. A descrição dos atributos e métodos podem ser encontrada no próprio arquivo `beautytext/BeautyText.py`. A classe possibilita a implementação das funcionalidades por terceiros, sendo recomendado importá-la como

```
from beautytext.BeautyText import BeautyText
```


## Script fitText.py

O script `fitText.py` é uma implementação do módulo que lê um arquivo de texto e o imprime formatado no terminal com um limite máximo de caracteres por linha. Ele pode ser chamado de qualquer local através com a sintaxe:

```
fitText.py [-h] [-j] [-n <num_char>] <file>
```

* Parâmetro obrigatório:
    * `<file>`: caminho para o arquivo de entrada com o texto a ser editado.

* Parâmetros opcionais:
    * `-h`, `--help`: exibe mensagem de ajuda do programa
    * `-j`, `--justify`: habilita o texto justificado
    * `-n <num_char>`, `--num_char <num_char>`: número máximo de caracteres em cada linha (padrão: 40)

### Status de saída

Ao finalizado o script, é retornado um código padrão de status para o sistema:

* 0: caso o processamento tenha sido efetuado com sucesso.
* 1: caso tenha ocorrido algum erro.



## Usabilidade

Tanto os métodos `getBeautyText()` e `saveBeautyText()` da classe `BeautyText`, quanto para o script `fitText.py` só funcionarão corretamente se as seguintes observações forem levadas em conta:

* Os parágrafos devem ser separados no arquivo por uma linha em branco. Uma quebra de linha simples é tratada como continuação do mesmo parágrafo.
* A barra invertida procedida por um espaço ("\ ") pode ser usada para explicitar conteúdos que não devem ser separados de linha. Exemplo:
    > O Teorema de Pitágoras diz que a soma dos quadrados dos catetos é igual ao quadrado da hipotenusa, ou seja, c²\ =\ a²\ +\ b².

  previne que a fórmula matemática se separe em duas linhas. O resultado após rodar o script fica:

    > O Teorema de Pitágoras diz que a soma
    >
    > dos quadrados dos catetos é igual ao
    >
    > quadrado da hipotenusa, ou  seja,
    >
    > c² = a² + b².
    
  Sem as barras invertidas no texto de entrada, a saída ficaria

    > O Teorema de Pitágoras diz que a soma
    >
    > dos quadrados dos catetos é igual ao
    >
    > quadrado da hipotenusa, ou seja, c² = a²
    >
    > \+ b².


# Testes

Após a instalação, execute os dois testes a seguir.


### Teste 1

Rode dentro do diretório raiz o seguinte código:

```
fitText.py examples/input.txt
```

O resultado deve ser igual ao arquivo `examples/output1.txt`.


### Teste 2

Rode dentro do diretório raiz o seguinte código:

```
fitText.py -j examples/input.txt
```

O resultado deve ser igual ao arquivo `examples/output2.txt`.



## Autor

Daniel Bednarski Ramos

[https://www.astro.iag.usp.br/~bednarski](https://www.astro.iag.usp.br/~bednarski)

daniel.bednarski.ramos@gmail.com


## Licença

GNU GPLv3
