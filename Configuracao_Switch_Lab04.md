# Configuração Inicial de Switch Cisco

Abaixo está o detalhamento dos comandos utilizados para a configuração inicial do switch Cisco, acompanhados de suas respectivas descrições.

| Comando | Descrição |
| :--- | :--- |
| `enable` | Entra no modo EXEC privilegiado. |
| `configure terminal` | Entra no modo de configuração global. |
| `hostname SW_Lab01` | Define o nome do dispositivo como SW_Lab01. |
| `enable secret cisco123` | Define uma senha criptografada para o modo privilegiado. |
| `line console 0` | Entra na configuração da porta de console física. |
| `password console123` | Define a senha para acesso via console. |
| `login` | Exige autenticação por senha ao conectar. |
| `exit` | Sai do modo de configuração de linha. |
| `line vty 0 4` | Configura as linhas virtuais para acesso remoto (5 sessões). |
| `password vty123` | Define a senha para conexões remotas (Telnet/SSH). |
| `login` | Exige autenticação por senha para acesso remoto. |
| `transport input all` | Permite todos os protocolos de transporte (Telnet e SSH). |
| `exit` | Retorna ao modo de configuração global. |
| `interface vlan 1` | Entra na configuração da interface virtual de gerenciamento. |
| `ip address 192.168.10.2 255.255.255.0` | Atribui o endereço IP e a máscara de sub-rede. |
| `no shutdown` | Ativa a interface (por padrão, interfaces VLAN vêm desativadas). |
| `exit` | Retorna ao modo de configuração global. |
| `ip default-gateway 192.168.10.1` | Define o endereço do roteador para saída da rede local. |
| `service password-encryption` | Criptografa todas as senhas de texto simples no arquivo de configuração. |
| `banner motd "ACESSO RESTRITO: Somente usuários autorizados!"` | Define a mensagem de aviso exibida no login. |
| `end` | Sai do modo de configuração e volta ao modo privilegiado. |
| `copy running-config startup-config` | Salva as configurações da RAM para a memória não volátil (NVRAM). |
