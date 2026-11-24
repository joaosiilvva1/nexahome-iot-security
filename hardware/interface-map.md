# Mapa de interfaces físicas

## Estado

Pendente: nenhuma placa ou fotografia do NexaSense foi disponibilizada. UART, JTAG, SPI, I²C, pinos de programação, pontos de teste e acesso à flash são itens a verificar, não interfaces confirmadas.

| Interface/área | Onde procurar | Capacidade possível | Evidência a registrar | Estado |
|---|---|---|---|---|
| UART | Headers, pads, trilhas próximas ao MCU | Logs, console ou bootloader, conforme configuração | Fotos, tensão lógica, captura de boot autorizada | Pendente |
| JTAG | Pads do MCU | Depuração/leitura/controle se habilitada | Foto, identificação do MCU e estado de bloqueio | Pendente |
| SPI/I²C | Barramentos de sensores/flash | Comunicação com periféricos; risco depende de acesso | Mapa de conexões e componentes identificados | Pendente |
| Programação/USB | Conector e circuito associado | Gravação, recuperação ou alimentação | Foto, esquema e comportamento observado | Pendente |
| Flash externa | Encapsulamento e trilhas | Armazenamento de firmware/configuração | Identificação do componente e proteção | Pendente |

## Cuidados e avaliação

Não classificar a presença de uma interface como falha por si só. Verificar acessibilidade, autenticação, privilégios, conteúdo exposto, proteção da memória e necessidade operacional. Confirmar níveis de tensão antes de conectar equipamento. Não gravar eFuses nem executar operações irreversíveis.
