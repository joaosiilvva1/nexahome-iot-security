# Demonstração local

Execute com Python 3, sem pacotes adicionais:

    python demo/local_lab_simulation.py

A demonstração inicia um serviço HTTP temporário preso a 127.0.0.1, envia telemetria sintética e grava o corpo observado em network/evidence/loopback-http-simulation.jsonl. Em seguida compara uma atualização fictícia aceita por um verificador propositalmente incompleto com uma checagem HMAC de exemplo que rejeita bytes alterados.

Nenhum pacote é instalado, nenhuma placa é acessada, nenhuma conexão sai do loopback e a chave usada no exemplo é pública e insegura por projeto. Os registros demonstram apenas o comportamento do modelo didático. Não os apresente como PCAP, firmware, tráfego ou achados do NexaSense real.

