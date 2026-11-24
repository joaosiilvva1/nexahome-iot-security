# Notas de análise do firmware

## Estado

Pendente: a imagem original não foi incluída nos arquivos recebidos. Nenhuma afirmação sobre partições, bibliotecas, endpoints, credenciais ou mensagens de debug do NexaSense foi confirmada.

## Procedimento

1. Registrar origem, autorização, nome e tamanho do arquivo.
2. Calcular SHA-256 do original e registrar em `hashes.txt`; preservar uma cópia imutável.
3. Fazer a análise somente em cópia de trabalho. Identificar formato e mapa de partições com ferramentas adequadas à plataforma e registrar versões/comandos.
4. Extrair strings e conteúdo de arquivos de forma offline; procurar configuração, endpoints, protocolos, versão, logs e dados potencialmente sensíveis.
5. Redigir valores sensíveis antes de inserir evidência no repositório; manter originais protegidos.
6. Verificar o mecanismo de atualização e a validação criptográfica da imagem, sem instalar firmware fora do laboratório.

## Registro de observação

| ID | Arquivo/offset | Observação literal redigida | Relevância | Confirmado? |
|---|---|---|---|---|
| — | PENDENTE | Nenhum firmware recebido | — | Não |
