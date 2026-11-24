# Caso pesquisado: PurpleAir

## Dispositivo

Gao, Luo, Zhang, Pearson e Fu estudaram sensores de qualidade do ar PurpleAir baseados em ESP8266.

## Superfícies envolvidas

O estudo examinou a interface física UART usada para acesso ao firmware e o mecanismo de atualização remota OTA.

## Problema relatado

No dispositivo pesquisado, os autores relataram que o acesso por UART possibilitava ler conteúdo da flash, incluindo credenciais Wi-Fi, e que a atualização OTA não autenticava adequadamente o servidor nem verificava criptograficamente o firmware antes de aceitá-lo. O artigo descreve riscos de alteração física do firmware e de entrega remota de imagem não autorizada.

## Mitigações discutidas para o cenário NexaHome

- Validar criptograficamente assinatura e integridade da imagem antes da instalação e no processo de boot.
- Autenticar o servidor de atualização e proteger a comunicação.
- Restringir/desabilitar interfaces de debug em produção, proteger a flash e evitar segredos reutilizados.
- Projetar recuperação segura e controle anti-rollback.

## O que o caso ensina para a NexaHome

O caso mostra por que as superfícies física, firmware e atualização precisam ser analisadas em conjunto: debug pode expor material usado pela conectividade, enquanto um OTA sem validação pode permitir código não autorizado. Essas são verificações prioritárias para o NexaSense, não conclusões sobre ele. Nenhuma vulnerabilidade foi confirmada no NexaSense nesta entrega.

## Fonte primária

Gao et al., “Microcontroller Based IoT System Firmware Security: Case Studies”, IEEE ICII, 2019. [Artigo completo](https://www.cs.uml.edu/~xinwenfu/paper/Conferences/19_ICII_MicrocontrollerBasedIoTSystemFirmwareSecurity-CaseStudies.pdf).

