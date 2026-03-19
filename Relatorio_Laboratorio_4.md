# Relatório de Atividades: Laboratório 4 - Configuração Inicial de Switch Cisco

Este relatório detalha as ações realizadas para cumprir os requisitos do Laboratório 4, focando na configuração inicial de um switch Cisco conforme o enunciado fornecido.

## 1. Introdução
O objetivo deste laboratório foi realizar a configuração inicial completa de um switch Cisco, garantindo acesso seguro via console e remoto (SSH/Telnet), além de configurações básicas de rede e segurança.

## 2. Passo a Passo das Ações Realizadas

A tabela abaixo descreve cada ação executada e o comando correspondente utilizado no ambiente IOS da Cisco.

| Passo | Ação Realizada | Comando(s) Utilizado(s) |
| :--- | :--- | :--- |
| 1 | Acesso ao modo privilegiado | `enable` |
| 2 | Acesso ao modo de configuração global | `configure terminal` |
| 3 | Configuração do nome do switch | `hostname SW_Lab01` |
| 4 | Configuração de senha criptografada para modo EXEC | `enable secret [senha]` |
| 5 | Configuração de senha e login na linha de console | `line console 0`, `password [senha]`, `login` |
| 6 | Configuração de senha e login nas linhas VTY (0-4) | `line vty 0 4`, `password [senha]`, `login` |
| 7 | Configuração da interface VLAN 1 (IP e Máscara) | `interface vlan 1`, `ip address 192.168.10.2 255.255.255.0`, `no shutdown` |
| 8 | Configuração do Gateway Padrão | `ip default-gateway 192.168.10.1` |
| 9 | Ativação da criptografia de senhas de texto plano | `service password-encryption` |
| 10 | Configuração do Banner MOTD | `banner motd "ACESSO RESTRITO: Somente usuários autorizados!"` |
| 11 | Salvamento das configurações na NVRAM | `copy running-config startup-config` |

## 3. Detalhamento Técnico

### 3.1. Segurança de Acesso
Foi utilizada a criptografia forte para a senha do modo EXEC privilegiado através do comando `enable secret`, que utiliza algoritmos de hash (como MD5 ou SHA-256 dependendo da versão do IOS) em vez do comando `enable password`, que é menos seguro.

### 3.2. Acesso Remoto
As linhas VTY foram limitadas a 5 sessões simultâneas (0 a 4), garantindo que o switch suporte múltiplos acessos administrativos ao mesmo tempo, mantendo o controle de autenticação obrigatório.

### 3.3. Conectividade de Rede
A interface virtual de gerenciamento (VLAN 1) foi configurada com o endereço IP `192.168.10.2`. Para permitir o gerenciamento a partir de outras sub-redes, o gateway padrão foi definido como `192.168.10.1`.

## 4. Conclusão
Todas as tarefas solicitadas no enunciado foram concluídas com sucesso. O arquivo de configuração final foi gerado e está disponível no repositório como `configuracao_switch_lab04.txt`.

---
**Data:** 19 de Março de 2026
**Responsável:** Manus AI
