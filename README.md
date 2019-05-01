# Trabalho 1 - Descrição
O objetivo do trabalho consiste em implementar codificadores e decodificadores para detecção e correção de erros usando as técnicas de redundância de bloco, CRC e código de Hamming. Os codificadores e decodificadores deverão ser executados em linha de comando recebendo parâmetros de entrada e apresentando o resultado na saída padrão do terminal (OBS. NÃO devem ser utilizados menus, entradas/saídas por arquivos, ou interface gráfica). Os detalhes sobre a entrada e saída para cada técnica estão apresentados abaixo:

## Versão do Python
Python 3.6.5 :: Anaconda, Inc.

## Algoritmos

## 1. Redundância de bloco (BCC)
  ### Codificador: 
    <string em ASCII> => <string codificada em hexadecimal>
  #### Exemplo:
  ```
  $ python bcc.py -e redes
  E4CAC9CAE7CA
  ```
  ```
  $ python bcc.py -e PUCRS@
  A0AA87A5A681F
  ```
  ### Decodificador: 
    <código em hexadecimal> => <string em ASCII> ou "ERRO"
  #### Exemplo:
  ```
  $ python bcc.py -d E4CAC9CAE7CA
  redes
  ```
  ```
  $ python bcc.py -d A0AA87A5A681F
  PUCRS@
  ```
  ```
  $ python bcc.py -d E4CAC9CAE7CB
  ERRO
  ```
## 2. CRC

  ### Codificador: 
    <string em ASCII> <polinômio gerador de ordem 5 expresso em binário> => <string codificada em hexadecimal>
  ### Decodificador: 
    <string em hexadecimal> <polinômio gerador de ordem 5 em binário> => <string em ASCII> e/ou "ERRO" 
  (OBS. os caracteres sem erro devem ser apresentados e indicados os caracteres que tiveram erro na transmissão)

## 3. Código de Hamming
 
  ### Codificador: 
    <string em ASCII> => <string codificada em hexadecimal>
O Codificador consiste em receber uma string em ASCII e para cada elemento desta string é realizado a codificação em binário com 8 bits. Logo após isso, para cada binário é executada a codificação onde: 
1. Aloca os espaços no binário para os indices de potência 2 (2^0, 2^1, 2^2...2^n), desta forma o o binário terá 11 bits.

2. Para cada indice que possue bit igual a 1 é a realizado a conversão em binário.
3. Executa a operação xor (paridade) entre cada bit dos binários.
4. Para cada bit gerado é colocado no binário de 11 bits seu devido valor e na sua posição de potência de 2.
5. retorna este binário (11 bits) gerado em hexadecimal.
  #### Exemplo:
  ```
  $ python hamming.py -e redes
  79962C62B62C79E 
  ```
   ```
  $ python hamming.py -e PUCRS@
  50252F49D51B51C483  
  ```
  ### Decodificador: 
    <código em hexadecimal> => <string em ASCII> 
  
  (OBS. os caracteres que apresentarem erro deverão ser corrigidos e sua correção indicada na saída)
  #### Exemplo:
  ```
  $ python hamming.py -d 79962C62B62C79E
  redes
  ```
  ```
  $ python hamming.py -d 50252F49D51B51C483
  PUCRS@
  ```
  ```
  $ python hamming.py -d 79961C62B62C69E
  rbdes
  ERRO no caractere 2-> Correção: b
  ERRO no caractere 5 -> Correção: s
  ```
