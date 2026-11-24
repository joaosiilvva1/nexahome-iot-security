# NexaSense — avaliação de segurança IoT

## Objetivo e dispositivo

Este trabalho estrutura uma avaliação de segurança do NexaSense, dispositivo conceitual da NexaHome descrito no enunciado. O cenário informa um microcontrolador da família ESP32, sensores de temperatura e umidade, firmware, Wi-Fi, armazenamento e atualização. O diagrama representa essa arquitetura de referência; modelos de componentes, interfaces e protocolos não são tratados como observações de uma placa específica.

## Escopo desta entrega

O escopo adotado é documental e inclui uma demonstração reproduzível de software local. A inspeção de uma placa física e a análise de uma imagem original de firmware não integram esta versão. Por isso, não são atribuídas vulnerabilidades ao NexaSense real. O teste de rede é HTTP em loopback com dados artificiais, não tráfego do produto nem PCAP.

## Arquitetura e materiais

- [Site do projeto](https://joaosiilvva1.github.io/nexahome-iot-security/)
- [Diagrama de arquitetura](architecture/architecture-diagram.svg)
- [Relatório técnico em PDF](report/Relatorio-Tecnico-NexaHome.pdf)
- [Achados e cenários](findings/findings.md)
- [Plano de hardening](remediation/hardening-plan.md)
- [Caso pesquisado: PurpleAir](case-study.md)
- [Checklist da entrega](deliverables-checklist.md)
- [Roteiro do vídeo](video/roteiro-ate-4-minutos.md)

## Ferramentas

A demonstração utiliza Python 3 e somente módulos da biblioteca padrão. O script inicia um servidor temporário em `127.0.0.1`, registra a requisição sintética em JSONL, calcula SHA-256 de bytes artificiais e compara um verificador de atualização fictício com uma checagem HMAC didática. Não requer placa, privilégios, pacotes adicionais ou conexão externa.

## Resumo das análises

### Firmware

Não há imagem original do NexaSense analisada nesta entrega. Assim, não se reportam formato, partições, bibliotecas, endpoints, credenciais ou strings do produto, e nenhum hash sintético é apresentado como hash do dispositivo. O simulador ilustra preservação por hash e validação de pacote; consulte `firmware/analysis-notes.md` e `firmware/simulated-fixture-hash.txt`.

### Hardware

O mapa conceitual descreve UART, JTAG, SPI/I²C, programação e armazenamento como interfaces a considerar conforme o cenário do enunciado. Não contém pinagem, fotografia nem resultado de medição de uma placa. A presença de uma interface não é classificada como vulnerabilidade sem contexto e evidência.

### Comunicação

Na simulação, o cliente envia telemetria artificial por HTTP a um servidor local, sem TLS ou autenticação. O log reproduzível está em `network/evidence/loopback-http-simulation.jsonl`. Esse resultado descreve somente o modelo de software. Protocolo, destinos, conteúdo e proteções do equipamento não foram inferidos a partir dele.

### Achados e recomendações

C01–C03 são hipóteses condicionais sobre atualização, depuração e comunicação. SIM01–SIM02 são observações do simulador, não achados do NexaSense. O caso PurpleAir é referência externa e serve para relacionar acesso físico, firmware e atualização. O plano de hardening recomenda validação de assinatura, Secure Boot, Flash Encryption, credenciais individuais, TLS validado, redução de debug e recuperação segura, considerando a variante exata do MCU.

## Reproduzir a demonstração

Na raiz do repositório, execute:

```bash
python demo/local_lab_simulation.py
```

A saída esperada está em `demo/local-lab-output.txt`. O script usa apenas loopback e dados sintéticos; não teste nem conecte dispositivos sem autorização.

## Vídeo

O roteiro de até quatro minutos está em `video/roteiro-ate-4-minutos.md`. A gravação e o link ainda precisam ser inseridos neste README para completar o item de vídeo do enunciado.
