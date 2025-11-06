# 🧩 C115-Works - Trabalho Final - Questão 2

### 🧑‍🏫 Professor: Samuel Beraldi Mafra
### 📘 Autor: Tiago Augusto Carvalho
### 📆 Disciplina: C115 — Conceitos e tecnologias para dispositivos conectados
### 💻 Ferramenta: Mininet


Branch contendo o trabalho final da disciplina C115(questão 2), desenvolvido em Mininet e python, utilizando linha de comando para criar e testar uma topologia linear com 6 switches.

---

## 🟣 Primeiro Ponto
### Criação da topologia customizada

**Descrição:**  
Com uso de linha de comando padrão do Mininet, crie atopologia customizada considerando o endereço MAC padronizado e controlador manual;
 
**Comando utilizado:**
```bash
cd ~/mininet-topos \\previamente criada
nano topologia_customizada.py \\abre o terminal onde escrevo o código de topologia
sudo mn --custom topologia_customizada.py --topo topologiacustomizada --controller=default

````
![Primeiro Ponto](2(A)_print1acessandopasta.png)
![Primeiro Ponto](2(A)_print2criandocódigopython.png)
![Primeiro Ponto](2(A)_print3criandoatopologia.png)


## 🟣 Segundo Ponto
### Inspeção de informações das interfaces, endereços MAC, IP e portas

**Descrição:**  
Listar e inspecionar as informações dos nós, conexões e interfaces da topologia criada, através das linhas de comando.

**Comando utilizado:**
```bash
dump
````
![Segundo_Ponto](2(B)_print1inspecionando.png)

## 🟣 Terceiro Ponto
### Crie um desenho ilustrativo da topologia com todas as
informações obtidas no item anterior

![Terceiro_Ponto](2(C)_print1Desenho.png)

## 🟣 Quarto Ponto
### Testes de ping entre os diferentes nós

**Descrição:**  
Executar testes de conectividade entre todos os nós da topologia para garantir comunicação completa entre os hosts.

**Comando utilizado:**
```bash
pingall
xterm h1
ping -c 3  10.0.0.5
````
![Quarto_Ponto](2(D)_testePINGALL.png)
![Quarto_Ponto](2(D)_testepingh1parah5.png)


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







