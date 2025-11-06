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
### Inspecione informações das interfaces

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
### Crie um desenho ilustrativo da topologia com todas asinformações obtidas no item anterior.

![Terceiro_Ponto](1(C)_desenho.png)


## 🟣 Quarto Ponto
### Execute testes de ping entre os diferentes nós, mostre os pacotes chegando nos nós com uso do comando tcpdump.

**Comando utilizado:**
```bash
pingall
xterm h1
sudo topdump - h1-eth0
hl ping -c 5 h2
````
![Quato_Ponto](1(D)_primeiroprint.png)
![Quato_Ponto](1(D)_segundoprint.png)
![Quato_Ponto](1(D)_terceiroprint.png)

## 🟣 Quinto Ponto
**Descrição:**  
Especifique que o host 1 na porta 5555 vai ser umservidor TCP e o host 2 um cliente e execute testes deiperf, considere um relatório por segundo com teste de20 segundos. Faça os testes para larguras de banda bw
de 30 e 40 Mbps (Necessário reconstruir a topologiapara os outros valores).

**Comandos utilizados:**
```bash
xterm h1 h2
iperf -s -p 5555
iperf -c 10.0.0.1 -p 5555 -t 20 -i 1

//criando nova topologia depois de limpar o cache
sudo mn -- topo tree, depth=3, fanout=5 -- link=tc, bw=40 -- mac
xterm h1 h2
iperf -s -p 5555
iperf -c 10.0.0.1 -p 5555 -t 20 -i 1
````
![Quinto_Ponto](1(E)_primeiroprint.png)
![Quinto_Ponto](1(E)_cofignewTOPO40.png)
![Quinto_Ponto](1(E)_ultimo.png)



🧠 Resumo dos Comandos
### Para referência rápida, seguem todos os comandos utilizados no trabalho:

**Comando utilizado:**
```bash
# Criação da topologia linear com 6 switches
sudo mn -- topo tree, depth=3, fanout=5 -- link=tc, bw=30 -- mac
sudo mn -- topo tree, depth=3, fanout=5 -- link=tc, bw=40 -- mac

# Inspeção de nós, conexões e interfaces
nodes
net
dump
hl ifconfig
sh ovs-ofctl show s1

# Testes de conectividade entre os nós
pingall

# Testes de desempenho com iperf
iperf -s -p 5555
iperf -c 10.0.0.1 -p 5555 -t 20 -i 1

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








