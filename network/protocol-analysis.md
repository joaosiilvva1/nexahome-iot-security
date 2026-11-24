# Análise de comunicação

## Estado

Pendente: não foi fornecida captura de rede nem ambiente NexaHome. MQTT, HTTP, HTTPS e os destinos do tráfego são exemplos do enunciado, não resultados confirmados.

## Plano de captura autorizado

- Usar apenas a placa fornecida e uma rede de laboratório isolada, sem acesso a serviços externos ou rede de produção.
- Registrar topologia, endereços, horário, ferramenta/versão e condição do dispositivo.
- Capturar tráfego passivo e identificar DNS, TCP/UDP, protocolos de aplicação, origem/destino e frequência.
- Inspecionar tipo de dados e identificadores com valores sensíveis redigidos.
- Avaliar autenticação, confidencialidade, integridade, validação de certificados e proteção contra replay no contexto observado.
- Observar atualização somente se houver endpoint de laboratório autorizado; não interceptar serviços de terceiros.

## Registro

| Campo | Resultado |
|---|---|
| Protocolo(s) | Pendente |
| Origem/destino | Pendente |
| Dados observados | Pendente |
| Autenticação | Pendente |
| Criptografia/integridade | Pendente |
| Evidência | Pendente |

Identificar MQTT ou HTTP, por exemplo, não basta para concluir que a comunicação é segura. A conclusão depende de configuração, autenticação, proteção de transporte, conteúdo e modelo de ameaça.

## Observação reproduzida no simulador local (não é tráfego NexaSense)

A execução de demo/local_lab_simulation.py enviou um objeto JSON sintético por HTTP a um servidor temporário em 127.0.0.1. O servidor registrou o corpo em network/evidence/loopback-http-simulation.jsonl. Na simulação, não há TLS nem autenticação. O registro é log de aplicação gerado pelo simulador, não PCAP nem captura de rede do dispositivo. A origem/destino são somente loopback; nenhum dado real foi usado.

| Campo | Resultado do modelo local |
|---|---|
| Protocolo | HTTP sobre loopback |
| Origem/destino | cliente local para 127.0.0.1, porta efêmera |
| Conteúdo | telemetria inteiramente sintética |
| TLS/autenticação | ausentes no modelo didático |
| Estado do NexaSense real | não testado |
