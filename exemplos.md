# Trabalho 1 - Exemplos
## Redundância de bloco (BCC)

$ bcc_encoder redes
E4CAC9CAE7CA

$ bcc_decoder E4CAC9CAE7CA
redes

$ bcc_decoder E4CAC9CAE7CB
ERRO

## CRC

$ crc_encoder redes 10101
72365964C659736

$ crc_decoder 72365964C659736 10101
redes

$ crc_decoder 72365A64C659737 10101
r_de_
ERRO nos caracteres: 2, 5

## Código de Hamming

$ ham_encoder redes
79962C62B62C79E

$ ham_decoder 79962C62B62C79E
redes

$ ham_decoder 79961C62B62C69E
r>des
ERRO no caractere 2 -> Correção: >
ERRO no caractere 5 -> Correção: s
