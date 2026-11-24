# Achados e cenários de risco

## Resultado atual

Não há achados confirmados sobre o NexaSense: não foi fornecido hardware, firmware ou captura de rede para inspeção. A matriz abaixo registra cenários que devem ser verificados. Os níveis são prioridade preliminar condicionada à confirmação, não uma classificação de vulnerabilidade observada.

| ID | Evidência | Fragilidade/ameaça | Impacto | Probabilidade | Prioridade condicional | Recomendação | Estado |
|---|---|---|---|---|---|---|---|
| C01 | Nenhuma evidência do NexaSense; cenário descrito no estudo PurpleAir | Se atualização aceitasse imagem sem autenticação/assinatura, um atacante no caminho poderia tentar firmware não autorizado | Controle do dispositivo, dados falsos ou indisponibilidade | Média se atualização alcançável e sem validação | Alta se confirmado | Assinatura de firmware, verificação no bootloader, TLS autenticado, anti-rollback e recuperação segura | Hipótese |
| C02 | Nenhuma evidência do NexaSense; UART/JTAG ainda não inspecionados | Se debug acessível sem proteção expuser firmware, segredos ou bootloader privilegiado, atacante com acesso físico poderia extrair/alterar dados ou código | Comprometimento do dispositivo e exposição de credenciais | Média, condicionada à acessibilidade/proteções | Média/alta se confirmado, conforme acesso e privilégio | Remover pads quando possível, proteger/desabilitar debug em produção, Secure Boot/Flash Encryption conforme MCU | Hipótese |
| C03 | Nenhuma captura recebida | Se dados/credenciais trafegarem sem proteção adequada, observador na rede local poderia lê-los ou alterá-los | Exposição de dados e comandos | Média se tráfego local e sem proteção | Alta se segredos/comandos confirmados | TLS com validação de certificado, autenticação individual, integridade e segmentação | Hipótese |
| F00 | Escopo e materiais recebidos: somente enunciado/template | Não é um achado técnico; nenhum teste do produto foi executado | Indeterminado | Indeterminada | Não classificar | Executar a avaliação em laboratório e substituir hipóteses por evidência | Limitação atual |

## Regra de promoção a achado

Promover C01-C03 a achado somente com evidência reproduzível do equipamento autorizado: identificação da placa/firmware, passos, captura ou arquivo redigido, condição necessária e avaliação de impacto. Se o mecanismo for seguro ou a interface não estiver acessível, registrar teste e resultado negativo em vez de manter hipótese como vulnerabilidade.

## Observações do simulador didático

Estas observações foram reproduzidas no modelo de software local e não devem ser promovidas a achados do NexaSense.

| ID | Evidência no modelo | Resultado | Impacto no modelo | Probabilidade no modelo | Risco para o produto |
|---|---|---|---|---|---|
| SIM01 | network/evidence/loopback-http-simulation.jsonl | Corpo JSON sintético observável no servidor HTTP local, sem TLS/autenticação | Exposição apenas de dados artificiais do exercício | Reproduzido nesta execução | Não atribuível ao NexaSense; requer captura do dispositivo real |
| SIM02 | demo/local-lab-output.txt | O atualizador fictício aceitou bytes alterados; a verificação HMAC de comparação rejeitou a alteração | O modelo inseguro não verifica autenticidade/integridade | Reproduzido nesta execução | Não atribuível ao NexaSense; exige verificação no firmware real |

Mitigação conceitual para C01/C03: validar assinatura da imagem, proteger o transporte com autenticação adequada e verificar integridade no dispositivo.
