# Tutorial Técnico: Configuração Inicial de Switch Cisco

## 1. Introdução

### Objetivo da Configuração
Este tutorial tem como objetivo guiar o usuário através dos passos essenciais para realizar a configuração inicial de um switch Cisco. Ao final, o switch estará configurado com um nome de host, senhas de acesso seguras para console e acesso remoto (Telnet/SSH), uma interface de gerenciamento (VLAN 1) com endereço IP e gateway padrão, além de medidas básicas de segurança como criptografia de senhas e um banner de aviso.

### Importância da Configuração Inicial
A configuração inicial de um switch é crucial para garantir a segurança, a gerenciabilidade e a funcionalidade básica do dispositivo em uma rede. Sem uma configuração adequada, o switch pode ser vulnerável a acessos não autorizados e não será capaz de se comunicar corretamente com outros dispositivos na rede para fins de gerenciamento.

## 2. Acesso ao Dispositivo

O acesso a um switch Cisco para configuração inicial é tipicamente realizado via porta console, utilizando um cabo console e um emulador de terminal (como PuTTY ou Tera Term) em um computador. Após o acesso, o usuário navegará por diferentes modos de operação do IOS (Sistema Operacional Interconectado) da Cisco.

### Modos de Operação do IOS

*   **User EXEC Mode (Modo Usuário):** É o primeiro modo que o usuário acessa após fazer login. Possui funcionalidades limitadas, principalmente para visualização de informações básicas. É indicado pelo prompt `Switch>`. Para entrar neste modo, basta acessar o switch.

*   **Privileged EXEC Mode (Modo Privilegiado):** Permite acesso a comandos de visualização mais avançados e a capacidade de entrar no modo de configuração global. É indicado pelo prompt `Switch#`. Para entrar neste modo, utiliza-se o comando `enable`.

*   **Global Configuration Mode (Modo de Configuração Global):** A partir deste modo, o usuário pode fazer alterações na configuração do switch que afetam o dispositivo como um todo. É indicado pelo prompt `Switch(config)#`. Para entrar neste modo, utiliza-se o comando `configure terminal`.

## 3. Configuração Básica

### Definição de Hostname
O hostname é o nome de identificação do switch na rede, facilitando a sua identificação e gerenciamento.

```cisco
hostname SW_Lab01
```
*   **`hostname SW_Lab01`**: Define o nome do switch para `SW_Lab01`.

### Configuração de Senhas
É fundamental configurar senhas para proteger o acesso ao switch, tanto via console quanto remotamente.

#### Senha de Console
Protege o acesso físico ao switch através da porta console.

```cisco
line console 0
 password console123
 login
 exit
```
*   **`line console 0`**: Entra no modo de configuração da linha de console (porta física).
*   **`password console123`**: Define `console123` como a senha para acesso via console.
*   **`login`**: Ativa a exigência de autenticação por senha ao tentar acessar o switch via console.
*   **`exit`**: Sai do modo de configuração da linha de console e retorna ao modo de configuração global.

#### Senha `enable secret`
Define uma senha criptografada para o modo EXEC privilegiado, sendo mais segura que `enable password`.

```cisco
enable secret cisco123
```
*   **`enable secret cisco123`**: Configura `cisco123` como a senha para entrar no modo privilegiado. Esta senha é armazenada de forma criptografada.

#### Senha VTY (Acesso Remoto)
Protege o acesso remoto ao switch via Telnet ou SSH.

```cisco
line vty 0 4
 password vty123
 login
 transport input all
 exit
```
*   **`line vty 0 4`**: Entra no modo de configuração das linhas VTY (Virtual Teletype), que são as portas lógicas para acesso remoto. `0 4` indica que serão configuradas 5 sessões simultâneas (da 0 à 4).
*   **`password vty123`**: Define `vty123` como a senha para acesso remoto.
*   **`login`**: Ativa a exigência de autenticação por senha para acesso remoto.
*   **`transport input all`**: Permite que todos os protocolos de transporte (Telnet e SSH) sejam usados para acessar as linhas VTY. Pode ser configurado para `ssh` ou `telnet` especificamente.
*   **`exit`**: Sai do modo de configuração da linha VTY e retorna ao modo de configuração global.

## 4. Segurança

### Ativação de Criptografia de Senhas
Este comando criptografa todas as senhas de texto simples que foram configuradas no switch, tornando-as mais seguras ao serem visualizadas no arquivo de configuração.

```cisco
service password-encryption
```
*   **`service password-encryption`**: Criptografa todas as senhas não criptografadas no arquivo de configuração (running-config e startup-config).

### Banner MOTD (Message of the Day)
Um banner MOTD exibe uma mensagem de aviso para qualquer usuário que tente acessar o switch, geralmente informando sobre restrições de acesso.

```cisco
banner motd "ACESSO RESTRITO: Somente usuários autorizados!"
```
*   **`banner motd "ACESSO RESTRITO: Somente usuários autorizados!"`**: Configura a mensagem "ACESSO RESTRITO: Somente usuários autorizados!" para ser exibida antes do prompt de login.

## 5. Configuração de Rede

### Configuração da Interface VLAN 1
A VLAN 1 é a VLAN de gerenciamento padrão em switches Cisco. Configurar um endereço IP nesta interface permite que o switch seja gerenciado remotamente via rede.

```cisco
interface vlan 1
 ip address 192.168.10.2 255.255.255.0
 no shutdown
 exit
```
*   **`interface vlan 1`**: Entra no modo de configuração da interface virtual VLAN 1.
*   **`ip address 192.168.10.2 255.255.255.0`**: Atribui o endereço IP `192.168.10.2` com a máscara de sub-rede `255.255.255.0` à interface VLAN 1.
*   **`no shutdown`**: Ativa a interface VLAN 1. Por padrão, as interfaces VLAN vêm desativadas.
*   **`exit`**: Sai do modo de configuração da interface e retorna ao modo de configuração global.

### Gateway Padrão
O gateway padrão é o endereço IP do roteador que o switch usará para enviar tráfego para redes fora de sua própria sub-rede.

```cisco
ip default-gateway 192.168.10.1
```
*   **`ip default-gateway 192.168.10.1`**: Define `192.168.10.1` como o gateway padrão para o switch.

## 6. Salvamento das Configurações

É vital salvar as configurações para que elas não sejam perdidas em caso de reinicialização do switch.

### Diferença entre `running-config` e `startup-config`

*   **`running-config`**: É o arquivo de configuração que está atualmente em uso pelo switch (na RAM). Quaisquer alterações feitas no modo de configuração global são aplicadas imediatamente ao `running-config`.

*   **`startup-config`**: É o arquivo de configuração que é carregado quando o switch é inicializado (armazenado na NVRAM - Non-Volatile RAM). Se as alterações no `running-config` não forem salvas no `startup-config`, elas serão perdidas após uma reinicialização do switch.

Para salvar as configurações, utiliza-se o seguinte comando:

```cisco
end
copy running-config startup-config
```
*   **`end`**: Sai de qualquer modo de configuração e retorna diretamente ao modo EXEC privilegiado.
*   **`copy running-config startup-config`**: Copia a configuração ativa (running-config) para a configuração de inicialização (startup-config), garantindo que as alterações sejam mantidas após uma reinicialização.

## 7. Explicação dos Comandos

Todos os comandos foram explicados detalhadamente nas seções anteriores, contextualizando sua função e importância dentro da configuração do switch Cisco.

---
**Autor:** Manus AI
**Data:** 19 de Março de 2026
