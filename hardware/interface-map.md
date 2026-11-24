# Mapa conceitual de interfaces físicas

Este mapa deriva do cenário descrito no enunciado. A inspeção de placa não integra o escopo desta entrega; os itens abaixo são interfaces a considerar, não interfaces observadas ou confirmadas em um NexaSense específico.

| Interface/área | Possível capacidade | Questão de segurança no projeto |
|---|---|---|
| UART | Logs, console ou bootloader, conforme configuração | Há segredos nos logs? O acesso privilegiado é restrito em produção? |
| JTAG | Depuração ou controle, se habilitado | O bloqueio de debug é compatível com fabricação e suporte? |
| SPI/I²C | Comunicação com sensores e memória | Um acesso indevido exporia ou alteraria dados? |
| Programação/USB | Gravação, recuperação ou alimentação | O fluxo de gravação exige autorização? |
| Flash | Firmware e parâmetros de configuração | Dados sensíveis são protegidos e chaves são únicas? |

Uma interface acessível não é automaticamente uma vulnerabilidade. A avaliação deve relacionar acessibilidade, privilégios, conteúdo, proteções e impacto. Não há pinagem, tensão ou medição atribuída ao dispositivo nesta entrega.
