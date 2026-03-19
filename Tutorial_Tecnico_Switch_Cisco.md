# Tutorial Técnico: Configuração Inicial de Switch Cisco

Este tutorial fornece um guia passo a passo para a configuração inicial de um switch Cisco, abrangendo desde o acesso básico até a configuração de rede e segurança.

## 1. Introdução

### Objetivo da Configuração
O objetivo principal é estabelecer uma base segura e funcional para o switch, permitindo que ele opere corretamente na rede e possa ser gerenciado de forma eficiente e protegida.

### Importância da Configuração Inicial
A configuração inicial é o primeiro passo para garantir a integridade da rede. Sem ela, o dispositivo permanece com configurações padrão que podem ser inseguras e dificultar a administração remota e o monitoramento do tráfego.

## 2. Acesso ao Dispositivo

### Acesso via Console
O acesso inicial é feito fisicamente através da porta **Console** do switch, utilizando um cabo console (RJ45 para Serial/USB) conectado a um computador com um emulador de terminal (ex: PuTTY, Tera Term).

### Entrada nos Modos de Operação

O IOS da Cisco utiliza uma estrutura hierárquica de modos:

*   **User EXEC Mode:** Modo de visualização limitada.
    *   *Prompt:* `Switch>`
*   **Privileged EXEC Mode:** Permite comandos de diagnóstico e visualização completa.
    *   *Comando:* `enable`
    *   *Prompt:* `Switch#`
*   **Global Configuration Mode:** Onde as alterações de configuração são realizadas.
    *   *Comando:* `configure terminal`
    *   *Prompt:* `Switch(config)#`

## 3. Configuração Básica

### Definição de Hostname
Identifica o dispositivo na rede.
```cisco
hostname SW_Lab01
```
*   **Explicação:** Altera o nome do switch de "Switch" para "SW_Lab01".

### Configuração de Senhas

#### Console
Protege o acesso físico.
```cisco
line console 0
 password console123
 login
 exit
```
*   **Explicação:** Define a senha `console123` para a porta console e exige login.

#### Enable Secret
Protege o acesso ao modo privilegiado com criptografia forte.
```cisco
enable secret cisco123
```
*   **Explicação:** Define `cisco123` como senha para o comando `enable`.

#### VTY (Acesso Remoto)
Permite acesso via Telnet ou SSH.
```cisco
line vty 0 4
 password vty123
 login
 exit
```
*   **Explicação:** Configura 5 linhas virtuais (0 a 4) com a senha `vty123`.

## 4. Segurança

### Ativação de Criptografia de Senhas
```cisco
service password-encryption
```
*   **Explicação:** Criptografa as senhas que aparecem em texto simples no arquivo de configuração.

### Banner MOTD
```cisco
banner motd "ACESSO RESTRITO: Somente usuários autorizados!"
```
*   **Explicação:** Exibe uma mensagem de aviso legal ao acessar o dispositivo.

## 5. Configuração de Rede

### Interface VLAN 1
Interface virtual para gerenciamento.
```cisco
interface vlan 1
 ip address 192.168.10.2 255.255.255.0
 no shutdown
 exit
```
*   **Explicação:** Define o IP `192.168.10.2` e ativa a interface com `no shutdown`.

### Gateway Padrão
```cisco
ip default-gateway 192.168.10.1
```
*   **Explicação:** Define o endereço do roteador para que o switch alcance outras redes.

## 6. Salvamento das Configurações

### Diferença entre Configurações
*   **running-config:** Configuração atual na memória RAM (volátil). Perdida ao reiniciar.
*   **startup-config:** Configuração salva na NVRAM (não volátil). Carregada ao iniciar.

### Comando de Salvamento
```cisco
copy running-config startup-config
```
*   **Explicação:** Salva as alterações atuais para que persistam após o reboot.

## 7. Explicação dos Comandos
Cada comando listado acima foi acompanhado de sua respectiva explicação funcional para garantir o entendimento completo do processo de configuração.

---
**Autor:** André R. Zavan / Manus AI
**Data:** 19 de Março de 2026
