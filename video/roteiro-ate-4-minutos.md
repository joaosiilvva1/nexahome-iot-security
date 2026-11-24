# Roteiro para vídeo de demonstração (até 4 minutos)

**Importante:** este roteiro prepara a apresentação, mas não é um vídeo gravado. Para cumprir o requisito de comprovação prática, grave sua própria captura com a placa e as evidências do laboratório.

- **0:00-0:25 | Escopo.** Apresentar o NexaSense/placa equivalente, autorização, rede de laboratório isolada e limites dos testes.
- **0:25-0:55 | Arquitetura.** Mostrar o diagrama: sensores -> MCU/flash -> firmware -> Wi-Fi -> serviço local. Dizer quais itens foram confirmados na placa.
- **0:55-1:25 | Firmware.** Exibir nome/tamanho/SHA-256 da imagem autorizada e uma evidência redigida de strings, partições ou configuração. Nunca exibir segredo.
- **1:25-1:55 | Hardware.** Mostrar placa e mapa físico; demonstrar apenas observação segura da interface realmente identificada. Não conectar sem confirmar tensão e pinagem.
- **1:55-2:30 | Comunicação.** Mostrar captura de laboratório e identificar origem, destino, protocolo, dados e proteção observada.
- **2:30-3:05 | Demonstração.** Reproduzir uma condição confirmada no dispositivo. O simulador demo/local_lab_simulation.py pode ilustrar o método; declarar em voz alta que é simulação local e não achado do NexaSense. O trecho prático do aparelho ainda depende da placa.
- **3:05-3:40 | Risco e mitigação.** Conectar evidência -> fragilidade -> impacto -> prioridade e recomendações correspondentes.
- **3:40-4:00 | Fechamento.** Explicar limites, estado dos testes e medidas prioritárias para uma versão comercial.

Inserir o link do vídeo final aqui: PENDENTE.
