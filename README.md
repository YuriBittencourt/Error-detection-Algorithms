# Trabalho 1 - Descrição
O objetivo do trabalho consiste em implementar codificadores e decodificadores para detecção e correção de erros usando as técnicas de redundância de bloco, CRC e código de Hamming. Os codificadores e decodificadores deverão ser executados em linha de comando recebendo parâmetros de entrada e apresentando o resultado na saída padrão do terminal (OBS. NÃO devem ser utilizados menus, entradas/saídas por arquivos, ou interface gráfica). Os detalhes sobre a entrada e saída para cada técnica estão apresentados abaixo:
## 1. Redundância de bloco
  #### Codificador: 
    <string em ASCII> => <string codificada em hexadecimal>

  #### Decodificador: 
    <código em hexadecimal> => <string em ASCII> ou "ERRO"

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

### Outros detalhes de implementação:

- os códigos implementados devem ser executados a partir de um terminal por linha de comando - não deve ser necessário utilizar uma IDE para executar o simulador!!!
- pode ser utilizada qualquer linguagem para implementação
- a entrada e saída devem respeitar EXATAMENTE os formatos apresentados

### Avaliação:
* Implementação dos codificadores/decodificadores para as 3 técnicas (redundância de bloco, CRC e código de Hamming)
* Código bem comentado e estruturado
* Documentação apresentando: como as técnicas foram implementadas, 1 exemplo usando cada técnica, detalhes para compilação e execução dos códigos.

O trabalho deve ser realizado individualmente ou em duplas. O código fonte (empacotado em um arquivo zip) deve ser submetido pelo Moodle até o dia 6/5 às 11:30 (impreterivelmente). Não serão aceitos trabalhos atrasados e/ou enviados por e-mail. Trabalhos que não compilam ou que não executam não serão avaliados. Todos os trabalhos serão analisados e comparados. Caso seja identificada cópia de trabalhos, todos os trabalhos envolvidos receberão nota ZERO!

### [Exemplos aqui](exemplos.md)
