# Conferência com o enunciado do professor

Esta tabela separa os itens preparados dos itens que dependem de ensaio em equipamento e da gravação final. “Preparado” significa que o documento ou procedimento está no repositório; não significa que o produto real foi testado.

| Exigência | Material no repositório | Estado honesto |
|---|---|---|
| Descrição do dispositivo e arquitetura | Relatório, diagrama SVG e site | Preparado com base no enunciado; confirmar no equipamento |
| Mapa da superfície de ataque | Site, mapa físico e notas | Planejado; interfaces reais não observadas |
| Metodologia e preservação do firmware | Notas e checklist de hash | Procedimento preparado; firmware original não recebido |
| Hash SHA-256 do firmware do dispositivo | firmware/hashes.txt | Pendente; não existe imagem original fornecida |
| Análise de partições, strings, endpoints e configuração | firmware/analysis-notes.md | Pendente; exige imagem autorizada |
| Análise das interfaces físicas | hardware/interface-map.md | Pendente; exige inspeção da placa |
| Análise da comunicação do dispositivo | network/protocol-analysis.md | Pendente; sem PCAP ou captura do dispositivo |
| Demonstração controlada | demo/local_lab_simulation.py e registros | Simulação local reproduzível; não prova falha no produto |
| Achados com evidência, impacto, probabilidade e mitigação | findings/findings.md e relatório | Cenários do produto condicionais; observações simuladas separadas |
| Referência real pesquisada | case-study.md e references.md | Preparado com fonte primária e lição para NexaHome |
| Mitigações e hardening comercial | remediation/hardening-plan.md | Preparado conceitualmente |
| README, estrutura e reprodutibilidade | README.md | Preparado |
| Vídeo de até quatro minutos | video/roteiro-ate-4-minutos.md | Roteiro preparado; vídeo ainda não gravado |

## Para transformar em entrega prática completa

Obter a placa de laboratório ou equivalente físico, a imagem de firmware autorizada e uma rede isolada. Coletar fotos/saída serial, hashes, observações/capturas de rede e uma demonstração reproduzível no aparelho. Depois atualizar o estado dos achados e gravar o vídeo com essas evidências. Não substituir esses itens por dados simulados.

