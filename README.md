# Avaliação de Segurança IoT do NexaSense

Projeto acadêmico para avaliação autorizada do protótipo IoT descrito no enunciado: microcontrolador da família ESP32, sensores de temperatura e umidade, Wi-Fi, firmware, interfaces físicas e atualização de software.

## Objetivo

Organizar uma avaliação rastreável da arquitetura e das superfícies física, de firmware e de comunicação; relacionar evidências a riscos; e propor controles para uma futura versão comercial.

## Estado e limites desta entrega

O material entregue contém a metodologia, o modelo de arquitetura baseado no enunciado, uma demonstração offline de conceito sobre atualização sem verificação, a análise de um caso público e o plano de hardening. **Nenhuma placa NexaSense, firmware original, captura de rede ou evidência física foi fornecida para esta elaboração. Portanto, os resultados do produto real estão pendentes e nenhuma vulnerabilidade foi atribuída ao NexaSense.** A demonstração no diretório `demo/` é um modelo de software didático, isolado e sem conexão de rede; não é uma exploração do hardware nem prova de falha no protótipo.

Preencha os campos marcados como pendentes somente após executar os procedimentos na placa de laboratório fornecida ou em equipamento próprio expressamente autorizado. Não publique credenciais, chaves ou dados pessoais.

## Arquitetura de referência

Veja [`architecture/architecture-diagram.svg`](architecture/architecture-diagram.svg). Os componentes são os descritos no enunciado e devem ser confirmados por inspeção do equipamento.

## Estrutura

- `architecture/`: diagrama lógico de referência.
- `firmware/`: preservação, hash e notas de análise; aguarda imagem original.
- `hardware/`: mapa de interfaces e roteiro de verificação; aguarda placa e evidências.
- `network/`: roteiro de análise em rede isolada; aguarda captura autorizada.
- `findings/`: separa cenário demonstrativo de achados confirmados.
- `remediation/`: plano de hardening priorizado.
- `demo/`: modelo offline reproduzível e saída capturada.
- `video/`: roteiro de até quatro minutos para gravação pelo estudante.
- `report/`: versão PDF do relatório técnico.

## Como reproduzir a demonstração didática

Use Python 3.10 ou superior. A demonstração só processa bytes locais criados pelo próprio script:

```powershell
python demo/unsigned_update_demo.py
```

Ela mostra que um verificador fictício que não valida assinatura aceita um pacote de teste arbitrário. Isso ilustra uma classe de erro; não testa o NexaSense e não deve ser apresentado como achado do produto.

## Etapas para completar a avaliação real

1. Receber o modelo de placa e firmware autorizados; fotografar a placa e registrar modelo/revisão.
2. Preservar a imagem original sem modificá-la e calcular SHA-256 antes da análise.
3. Inspecionar interfaces sem aplicar tensão desconhecida; identificar níveis lógicos antes de conectar adaptadores.
4. Analisar boot/logs, firmware e atualização em cópia de trabalho.
5. Observar tráfego somente em rede de laboratório isolada, documentando protocolo, destinos e proteção.
6. Reproduzir uma condição observada no próprio laboratório e guardar captura, data, ferramenta e passos.
7. Atualizar `findings/findings.md` com fatos observados e remover ou reclassificar hipóteses que não se confirmarem.
8. Gravar o vídeo com o dispositivo e evidências reais; inserir o link no relatório ou neste README.

## Fontes

As fontes primárias e sua aplicação estão em [`references.md`](references.md). O caso PurpleAir citado é de terceiros e serve como referência de metodologia, não como evidência contra a NexaHome.
