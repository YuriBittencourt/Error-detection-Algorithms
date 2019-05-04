# Trabalho 1 - Descrição
O objetivo do trabalho consiste em implementar codificadores e decodificadores para detecção e correção de erros usando as técnicas de redundância de bloco, CRC e código de Hamming. Os codificadores e decodificadores deverão ser executados em linha de comando recebendo parâmetros de entrada e apresentando o resultado na saída padrão do terminal.
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
  O Codificador consiste em receber uma string em ASCII e para cada elemento desta string é realizado a codificação em binário com 12 bits. Logo após isso, para cada binário é executada a codificação onde, realiza-se divisões sucessivas do binário em que se o primeiro bit do binário for igual a 1  então a divisão deve ser realizada através do polinomio caso contrário através do binário 0 sucessivamente, no final é adicionado este resultado no lugar dos ultimos 4 bits do binário inicial e logo após isso este binário é convertido para hexadecimal.
  
  ![codificacao_crc](https://user-images.githubusercontent.com/21231029/57184960-fb7f8200-6e99-11e9-9ff4-2f8f7ecb3ee2.png)
  
  ### Decodificador: 
    <string em hexadecimal> <polinômio gerador de ordem 5 em binário> => <string em ASCII> e/ou "ERRO"
  O decodificador consite em receber uma string em HEXADECIMAL e para cada 3 caracteres desta String é realizado a conversão para binário. Logo após isso, para cada binário é executada a decodificação onde, realiza-se divisões sucessivas do binário em que se o primeiro bit do binário for igual a 1  então a divisão deve ser realizada através do polinomio caso contrário através do binário 0 sucessivamente, no final se o resultado da divisão for igual a zero então não houve erro, caso contrário houve.
  ![decodificacao_crc](https://user-images.githubusercontent.com/21231029/57185105-d12ec400-6e9b-11e9-9943-002b07062d98.png)

  (OBS. os caracteres sem erro devem ser apresentados e indicados os caracteres que tiveram erro na transmissão)

## 3. Código de Hamming
 
  ### Codificador: 
    <string em ASCII> => <string codificada em hexadecimal>
O Codificador consiste em receber uma string em ASCII e para cada elemento desta string é realizado a codificação em binário com 8 bits. Logo após isso, para cada binário é executada a codificação onde: 
1. Aloca os espaços no binário para os indices de potência 2 ![potencia_de_dois](https://latex.codecogs.com/gif.latex?(2^{0},&space;2^{1},&space;2^{2}...2^{n})), desta forma o o binário terá 11 bits.
![binario_11_bits](https://user-images.githubusercontent.com/21231029/57020440-a3c5ea00-6bff-11e9-80f1-ced109437164.png)
2. Para cada indice que possue bit igual a 1 é a realizado a conversão em binário.
3. Executa a operação xor (paridade) entre cada bit dos binários.<br>
![tabela_xor](https://user-images.githubusercontent.com/21231029/57020462-afb1ac00-6bff-11e9-89e5-fd8dbecbd419.png)
4. Para cada bit gerado é colocado no binário de 11 bits seu devido valor e na sua posição de potência de 2.
![mensagem_final](https://user-images.githubusercontent.com/21231029/57020464-b3453300-6bff-11e9-96dd-dd829f4a57ee.png)
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
  O decodificador consite em receber uma string em HEXADECIMAL e para cada 3 caracteres desta String é realizado a conversão para binário. Logo após isso, para cada binário é executada a decodificação onde:
  1. Para cada indice que possue bit igual a 1 é a realizado a conversão em binário.
  2. Executa a operação xor (paridade) entre cada bit dos binários.
  3. converte o valor do xor para inteiro e verifica se é igual a zero. Se for então a string não tem erro, caso contrário arruma-se o erro (trocando o valor do bit naquele indice) no binário inicial.
  ![tabela_xor_com_problemas](https://user-images.githubusercontent.com/21231029/57110310-80d62b80-6d0e-11e9-9dc9-951f623473b5.png)
  4. Remove os bits dos indices de potência 2 ![potencia_de_dois](https://latex.codecogs.com/gif.latex?(2^{0},&space;2^{1},&space;2^{2}...2^{n})) do binário inicial.
  5. Converte este binário para ASCII.
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
