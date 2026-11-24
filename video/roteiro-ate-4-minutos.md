# Roteiro para vídeo de demonstração de até quatro minutos

Este roteiro apresenta o escopo documental e a demonstração local. A simulação deve ser identificada como modelo didático, sem atribuir seus resultados ao equipamento NexaSense.

- **0:00–0:25 | Objetivo e escopo.** Apresentar o cenário NexaHome/NexaSense e dizer que esta versão cobre análise documental e demonstração de software local.
- **0:25–0:55 | Arquitetura.** Mostrar `architecture/architecture-diagram.svg` e explicar sensores, MCU/flash, firmware, Wi-Fi e serviço como arquitetura descrita pelo enunciado.
- **0:55–1:25 | Superfícies.** Exibir o mapa conceitual e explicar os riscos de UART/JTAG, armazenamento, atualização e comunicação, sem dizer que foram observados em uma placa.
- **1:25–2:10 | Firmware e integridade.** Mostrar o manifesto da fixture sintética e explicar que SHA-256 serve para rastreabilidade; esse hash não identifica firmware do produto.
- **2:10–3:00 | Demonstração local.** Executar `python demo/local_lab_simulation.py`; mostrar o log HTTP de loopback e a comparação de atualização. Destacar que os dados e bytes são artificiais.
- **3:00–3:35 | Riscos e referências.** Apresentar C01–C03 como hipóteses condicionais, SIM01–SIM02 como resultados do modelo e relacionar o caso PurpleAir às recomendações.
- **3:35–4:00 | Hardening e fechamento.** Resumir assinatura/anti-rollback, Secure Boot, Flash Encryption, TLS e redução de debug; apontar o PDF e as fontes.

## Publicação

Grave a apresentação, publique na plataforma aceita pelo professor e insira o link no README. Não apresente a demonstração simulada como teste do produto.
