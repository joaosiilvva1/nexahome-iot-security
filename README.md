# NexaSense - Avaliação de Segurança IoT

Projeto acadêmico de Hardware Hacking apresentado em um site estático de página única. A organização visual usa navegação por seções, destaque inicial, cartões temáticos e rodapé, com conteúdo e implementação originais para o estudo de caso NexaHome.

**Site publicado:** https://joaosiilvva1.github.io/nexahome-iot-security/

## Como abrir

Abra index.html em um navegador. O site usa HTML e CSS, sem dependências ou JavaScript.

## Como reproduzir o laboratório de software

Com Python 3, execute `python demo/local_lab_simulation.py`. O script usa dados artificiais, abre um servidor HTTP temporário somente em 127.0.0.1, grava o log demonstrativo em network/evidence/ e registra o hash de uma fixture sintética. Não requer pacotes externos nem toca em hardware. Leia demo/README.md antes de interpretar os resultados.

## Estrutura

- index.html: conteúdo semântico, navegação e seções do projeto.
- css/style.css: identidade visual responsiva e acessibilidade.
- assets/imagens/hero-nexasense.svg: ilustração vetorial original.
- report/: relatório técnico curto em PDF.
- architecture/: diagrama de referência da arquitetura.
- firmware/, hardware/, network/: roteiros e registros de análise.
- findings/: hipóteses de risco separadas de resultados confirmados.
- remediation/: plano de hardening.
- demo/: demonstração didática offline e simulador local HTTP/OTA.
- case-study.md: estudo PurpleAir, achados publicados e lições aplicáveis.
- deliverables-checklist.md: conferência requisito a requisito do enunciado.
- video/: roteiro de apresentação.
- references.md: fontes primárias e referências.

## Escopo e limites

O enunciado descreve ESP32, sensores de temperatura e umidade, Wi-Fi, firmware, interfaces físicas e atualização. A placa real, o firmware original e a captura de rede não foram fornecidos. O site diferencia fatos do enunciado, hipóteses e recomendações. A ilustração não representa uma placa fotografada ou inspecionada.

As demonstrações em demo/ usam dados sintéticos; uma delas inicia um servidor HTTP temporário somente em 127.0.0.1. Elas não acessam a placa e não são evidências de falha no NexaSense. O registro de firmware real, análise das interfaces físicas, captura do tráfego do dispositivo e vídeo com a placa continuam pendentes. Consulte deliverables-checklist.md para o estado de cada requisito.

## Decisões de implementação

HTML semântico, links por âncora, link para pular ao conteúdo, foco visível, texto alternativo e suporte a prefers-reduced-motion. Grades e navegação adaptam-se a telas menores. A paleta marinho, azul, verde e creme é uma escolha visual do projeto, não uma identidade oficial da NexaHome.

## Fontes

OWASP IoT Security Testing Guide, NISTIR 8259A, ETSI EN 303 645 V3.1.3, MITRE EMB3D, documentação Espressif ESP-IDF e estudo acadêmico sobre PurpleAir. URLs e aplicação em references.md. O site público contém links para o relatório, estudo de caso e materiais do projeto.

