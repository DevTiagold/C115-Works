# 🧩 C115-Works - TRABALHO FINAL - QUESTÃO !

### 🧑‍🏫 Professor: Samuel Beraldi Mafra
### 📘 Autor: Tiago Augusto Carvalho
### 📆 Disciplina: C115 — Conceitos e tecnologias para dispositivos conectados
### 💻 Ferramenta: Mininet


Branch contendo o trabalho final da disciplina **C115**, desenvolvido em **Mininet**, utilizando linha de comando para criar e testar uma topologia linear com 6 switches.

---

## 🟣 Primeiro Ponto
### Criação da topologia de árvore de profundidade 3 e ramificação cinco

**Descrição:**  
Com uso de linha de comando padrão do Mininet, crie a topologia considerando o endereço MAC padronizado, larguras de banda bw de 30 Mbps e controlador do Mininet (não precisa especificar).

**Comando utilizado:**
```bash
sudo mn --topo tree,depth=3,fanout=5 --link tc,bw=30v --mac
````
![Primeiro Ponto](1(a)_Final.png)


## 🟣 Segundo Ponto
### Inspecione informações das interfaces, endereços
MAC, IP e portas através de linhas de comando;

**Descrição:**  
Listar e inspecionar as informações dos nós, conexões e interfaces da topologia criada, através das linhas de comando.

**Comandos utilizados:**
```bash
hl ifconfig
sh ovs-ofctl show s1
````
![Segundo_Ponto](1(B)_primeiroprint.png)
![Segundo_Ponto](1(B)_segundoprint.png)



## 🟣 Terceiro Ponto
### Testes de ping entre os diferentes nós

**Descrição:**  
Executar testes de conectividade entre todos os nós da topologia para garantir comunicação completa entre os hosts.

**Comando utilizado:**
```bash
pingall
````
![Terceiro_Ponto](Terceiro_Ponto.png)


## 🟣 Quarto Ponto
### Testes de desempenho com iperf

**Descrição:**  
Configuração do host 1 na porta 5555 como servidor TCP e o host 2 como cliente, executando testes de iperf durante 15 segundos, com relatórios por segundo.

**Comando utilizado:**
```bash
xterm h1 h2
h1 iperf -s -p 5555 &
h2 iperf -c h1 -p 5555 -t 15 -i 1
````
![Quato_Ponto](Quarto_Ponto.png)


🧠 Resumo dos Comandos
### Para referência rápida, seguem todos os comandos utilizados no trabalho:

**Comando utilizado:**
```bash
# Criação da topologia linear com 6 switches
sudo mn --topo linear,6 --link tc,bw=25

# Inspeção de nós, conexões e interfaces
nodes
net
dump

# Testes de conectividade entre os nós
pingall

# Testes de desempenho com iperf
h1 iperf -s -p 5555 &
h2 iperf -c h1 -p 5555 -t 15 -i 1

# Encerrando topologia e limpando cache
sudo mn -c
````

##✅ Conclusão
### Todas as etapas do trabalho foram executadas com sucesso, contemplando:

**Descrição:  
.Criação da topologia linear no Mininet;
.Inspeção das interfaces e conexões entre nós;
.Testes de conectividade e desempenho entre hosts;
.Limpeza final do ambiente para novas execuções.**








