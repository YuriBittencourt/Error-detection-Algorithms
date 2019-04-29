# Trabalho 1 - Descrição
O objetivo do trabalho consiste em implementar codificadores e decodificadores para detecção e correção de erros usando as técnicas de redundância de bloco, CRC e código de Hamming. Os codificadores e decodificadores deverão ser executados em linha de comando recebendo parâmetros de entrada e apresentando o resultado na saída padrão do terminal (OBS. NÃO devem ser utilizados menus, entradas/saídas por arquivos, ou interface gráfica). Os detalhes sobre a entrada e saída para cada técnica estão apresentados abaixo:
## 1. Redundância de bloco
  ### Codificador: 
    <string em ASCII> => <string codificada em hexadecimal>
  #### Exemplo:
  ```shell
  $ python bcc.py -e redes
  E4CAC9CAE7CA
  ```
  ```shell
  $ python bcc.py -e PUCRS@
  A0AA87A5A681F
  ```
  ### Decodificador: 
    <código em hexadecimal> => <string em ASCII> ou "ERRO"
  #### Exemplo:
  ```shell
  $ python bcc.py -d E4CAC9CAE7CA
  redes
  ```
  ```shell
  $ python bcc.py -d A0AA87A5A681F
  PUCRS@
  ```
  ```shell
  $ python bcc.py -d E4CAC9CAE7CB
  ERRO
  ```
## 2. CRC

  #### Codificador: 
    <string em ASCII> <polinômio gerador de ordem 5 expresso em binário> => <string codificada em hexadecimal>
  #### Decodificador: 
    <string em hexadecimal> <polinômio gerador de ordem 5 em binário> => <string em ASCII> e/ou "ERRO" 
  (OBS. os caracteres sem erro devem ser apresentados e indicados os caracteres que tiveram erro na transmissão)

## 3. Código de Hamming
 
  #### Codificador: 
    <string em ASCII> => <string codificada em hexadecimal>
  #### Decodificador: 
    <código em hexadecimal> => <string em ASCII> 
  (OBS. os caracteres que apresentarem erro deverão ser corrigidos e sua correção indicada na saída)

### [Exemplos aqui](exemplos.md)
