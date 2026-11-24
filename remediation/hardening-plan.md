# Plano de hardening para versão comercial

## Prioridade 1 - atualização e integridade

- Assinar cada imagem com chave privada mantida fora do dispositivo; verificar assinatura e versão antes de instalar.
- Habilitar Secure Boot compatível com o modelo ESP32 exato, protegendo a cadeia de inicialização.
- Implementar anti-rollback para bloquear versões vulneráveis, com processo documentado para recuperação segura.
- Atualização autenticada e criptografada em transporte, validando certificados; definir comportamento seguro em falha de conexão ou energia.

## Prioridade 2 - dados e interfaces

- Usar Flash Encryption em modo de produção e chave única por unidade, após análise do ciclo de provisionamento e recuperação.
- Não embutir credenciais compartilhadas; provisionar identidade e segredo únicos por dispositivo.
- Remover logs detalhados, chaves, senhas e configuração sensível da saída serial.
- Desabilitar ou restringir UART/JTAG/ROM download conforme requisitos de manutenção. Aplicar eFuses somente em produção e após validar o plano de provisionamento; nunca na atividade acadêmica.

## Prioridade 3 - comunicações e ciclo de vida

- Usar TLS com validação de identidade do servidor, autenticação do dispositivo e proteção contra replay para dados e comandos.
- Restringir serviços e portas ao mínimo; documentar destinos e requisitos de rede.
- Publicar política de atualização e período de suporte, inventário de componentes, canal de reporte de vulnerabilidades e procedimento de resposta.
- Testar configuração de fábrica, recuperação de atualização e restauração segura antes do piloto.

Secure Boot e Flash Encryption têm papéis complementares: autenticidade/integridade de código executável e confidencialidade de conteúdo da flash. A configuração exata depende da variante do ESP32 e deve seguir documentação oficial da Espressif; os efeitos de eFuses são potencialmente irreversíveis.
