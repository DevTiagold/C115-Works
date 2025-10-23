# 🧩 C115-Works

Repositório contendo o trabalho da disciplina **C115**, desenvolvido em **Mininet**, utilizando linha de comando para criar e testar uma topologia linear com 6 switches.

---

## 🟣 Primeiro Ponto
### Criação da topologia linear com 6 switches

**Descrição:**  
Criação da topologia considerando o endereço MAC padronizado, largura de banda de 25 Mbps e o controlador padrão do Mininet (sem necessidade de especificar o tipo de controlador).

**Comando utilizado:**
```bash
sudo mn --topo linear,6 --link tc,bw=25
````
![Primeiro Ponto](Primeiro_Ponto.png)
