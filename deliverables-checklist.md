# Conferência da entrega

O escopo desta versão é análise documental do cenário NexaSense e demonstração em software local. A inspeção física foi excluída do escopo informado para esta entrega; nenhum resultado simulado é atribuído ao produto.

| Requisito | Material | Estado nesta versão |
|---|---|---|
| Relatório curto em PDF | `report/Relatorio-Tecnico-NexaHome.pdf` | Incluído; arquitetura, método, limites, matriz de risco, estudo e hardening |
| Arquitetura e componentes | `architecture/architecture-diagram.svg` | Incluídos como modelo de referência baseado no enunciado |
| Mapa da superfície de ataque | Site e `hardware/interface-map.md` | Incluído conceitualmente; sem inspeção ou medições de placa |
| Preservação e hash do firmware | `firmware/hashes.txt`, `firmware/simulated-fixture-hash.txt` | Procedimento e exemplo sintético separados; não há hash do firmware NexaSense |
| Análise básica de firmware | `firmware/analysis-notes.md` e demonstração | O comportamento de atualização é simulado; imagem do produto não analisada |
| Interfaces físicas | `hardware/interface-map.md` | Discussão conceitual; ensaio físico fora do escopo adotado |
| Comunicação e protocolo | `network/protocol-analysis.md` e log JSONL | Demonstração HTTP reproduzida em loopback; não representa tráfego do produto |
| Demonstração controlada | `demo/local_lab_simulation.py` e saída registrada | Reproduzível em software local, com dados sintéticos |
| Riscos, impacto e mitigação | `findings/findings.md` e relatório | Cenários condicionais separados das observações do simulador |
| Referência real e lição para NexaHome | `case-study.md`, `references.md` | Incluídos com estudo PurpleAir e referências técnicas |
| Plano de hardening | `remediation/hardening-plan.md` | Incluído para versão comercial |
| README e reprodução | `README.md` | Incluídos com escopo, ferramentas, resumos, evidências e comando |
| Vídeo de até quatro minutos | `video/roteiro-ate-4-minutos.md` | Roteiro incluído; falta gravar e adicionar o link do vídeo |

## Única ação restante para fechar o pacote de entrega

Gravar a apresentação de até quatro minutos conforme o roteiro, publicar em plataforma aceita pelo professor e inserir o link neste README. Se o professor exigir evidências de equipamento apesar do escopo adotado, o vídeo e o relatório deverão ser atualizados para refletir essas evidências reais; a simulação não as substitui.
