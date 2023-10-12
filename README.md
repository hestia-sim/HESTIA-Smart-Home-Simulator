<div align="center">
	<img src="https://github.com/MaykiSantos/SIAC/assets/58126683/3b1e27d1-31c4-40ba-b418-c35f664c6a07" alt="logo" width=300px>
  	<h1>Simulador de Ambientes Inteligentes Compartilhados</h1>
</div>
<div>
	<p align="center">
		<a href="#sobre">Sobre</a> •
    <a href="#instalacao">Instalação</a> •
		<a href="#requisitos">Requisitos</a> •
		<a href="#funcionamento">Funcionamento</a>
	</p>
</div>

<h2 id="sobre"> :eyes: Sobre</h2>

Descreva aqui sobre o projeto

<h2 id="instalacao"> :books: Instalação</h2>

Antes de tudo realize clone do repositório do projeto gita-middleware-sensors para a sua máquina. Para isso execute os seguintes comando no terminal.

```
git clone git@github.com:MaykiSantos/SAIC.git
git fetch
git checkout main
git pull
```

<h2 id="requisitos"> :toolbox: Requisitos</h2>

Para execusão deste módulo é necessário que a máquina possua pelo menos 3.5Gb de ram.

<h2 id="funcionamento"> :gear: Funcionamento</h2>

Explique o funcionamento da aplicação

<h2 id="cenarios">:gear: Cenários</h2>

### Grafo_casa-ROTINA_SIMPLES(2usuarios)

*MORADORES:* 
Gustavo, Amanda

*ROTINA SIMPLIFICADA:*
* Gustavo: Trabalho Remoto (8:00-12:00, 14:00 17:00)
* Amanda: Trabalho presencial (sai 7:00, chega 18:00)
* Fins de semana: Rotina variada(passear, lavar roupa)
* Dormem: às 23 horas
* Acordam: às 6 horas

*ATIVIDADES:*

Dormir, Caga, Mijar, Tomar banho, Escovar dentes, Café da manhã, Almoçar, Jantar, Cozinhar, Beber agua, Trabalhar home office, Trabalhar fora, Assistir TV, Ouvir música, Passear, Estudar, Lavar roupa, Limpar casa

*PLANTA BASE:*

![Integração -Arquiteturas_do_Sistema-Página-6 drawio (5)](https://github.com/MaykiSantos/SIAC/assets/58126683/b2ad202c-b455-4264-86f8-0f52f6f5b935)

### Grafo_casa-ROTINA_SIMPLES(Dividindo_ap)

*MORADORES:*
Andre, Vinicius

*ROTINA SIMPLIFICADA:*
* Andre: Trabalho presencial (sai 8:00, chega 13:00)
* Andre: Trabalho presencial (sai 14:00, chega 17:00)
* Andre: nas terças e quintas chega as 19:00
* Andre: dorme as 00:00 acorda as 07:00
* Vinicius: Na quarta aula presencial (sai 18:30, chega 20:30)
* Vinicius: dorme as 00:00 acorda as 07:00
* Vinicius: estuda em casa durante a semana e sai ocasionalmente
* Fins de semana: Rotina variada(passear, lavar roupa, limpar casa)


*ATIVIDADES:*

Dormir, Caga, Mijar, Tomar banho, Escovar dentes, Café da manhã, Almoçar, Jantar, Cozinhar, Beber agua, Trabalhar fora, Ouvir música, Passear, Estudar, Limpar casa

*PLANTA BASE:*

![Integração -Arquiteturas_do_Sistema-Página-6 drawio (4)](https://github.com/MaykiSantos/SIAC/assets/58126683/e03ac2d6-6063-409d-a2a7-6b9d2a58d1d5)

<h2 id="uso"> :eyes: Uso</h2>
<h3 id="gerador"> :eyes: Gerando os Dados</h3>
Para gerar um conjunto de dados simulados para ambientes inteligentes basta rodar o comando abaixo:

```
python3 main.py
```

Ao rodá-lo será solicitado:
- O tipo de saída dos dados (Completo ou Simples).
- Quantidade de dias a serem simulados.
- A rotina a ser utilizada.

A partir disso teremos, ou uma saída de dados **Simples**:

Ou uma saída de dados **Completa**:



