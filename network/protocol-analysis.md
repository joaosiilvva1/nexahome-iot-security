# Análise de comunicação

## Escopo do resultado

A demonstração executada usa HTTP entre um cliente e um servidor temporário no endereço `127.0.0.1`, com telemetria sintética e sem TLS/autenticação. O registro JSONL é um log da aplicação simulada, não PCAP nem captura do NexaSense. A comunicação do produto não é caracterizada por esta simulação.

## Evidência local reproduzível

- Script: `demo/local_lab_simulation.py`
- Saída: `demo/local-lab-output.txt`
- Log: `network/evidence/loopback-http-simulation.jsonl`
- Protocolo no modelo: HTTP
- Origem/destino: cliente local para servidor em loopback e porta efêmera
- Conteúdo: telemetria artificial
- Transporte/autenticação no modelo: sem TLS e sem autenticação

Identificar HTTP ou MQTT não basta para concluir se a comunicação de um dispositivo é segura. Seriam necessários configuração, conteúdo, autenticação, proteção de transporte, integridade e modelo de ameaça do sistema avaliado.
