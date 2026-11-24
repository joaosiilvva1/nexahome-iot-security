# Análise de firmware e modelo de atualização

## Escopo e resultado

Não foi analisada uma imagem original do NexaSense. Portanto, não há conclusão sobre formato, partições, bibliotecas, strings, endpoints, credenciais ou logs do produto. O script local modela apenas a validação de um pacote de atualização e usa bytes sintéticos.

## Procedimento de preservação para uma imagem autorizada

1. Registrar origem, autorização, nome e tamanho do arquivo.
2. Calcular SHA-256 do original e preservar uma cópia íntegra.
3. Analisar somente uma cópia de trabalho e registrar ferramentas, versões e comandos.
4. Identificar formato, partições, strings, bibliotecas, configuração, protocolos e mecanismo de atualização.
5. Redigir valores sensíveis antes de publicar evidências.

## Observação do modelo didático

`demo/local_lab_simulation.py` demonstra que um verificador fictício incompleto aceita bytes alterados, enquanto a checagem HMAC de comparação rejeita a alteração. Isso ilustra por que autenticidade e integridade devem ser verificadas; não é análise nem achado do firmware NexaSense.

O hash de `firmware/simulated-fixture-hash.txt` identifica somente bytes sintéticos gerados para o exercício. Não representa firmware do produto.
