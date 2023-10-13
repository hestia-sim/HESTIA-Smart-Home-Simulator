<div align="center">
	<img src="https://github.com/SSEDG/SSEDG/blob/main/doc/img/logo_ssedg2.png?raw=true" alt="logo" width=400px>
  	<h1>Shared Smart Environment Data Generator (SSEDG)</h1>
</div>
<div>
	<p align="center">
		<a href="#sobre">Sobre</a> •
    <a href="#instalacao">Instalação</a> •
		<a href="#requisitos">Requisitos</a> •
		<a href="#cenarios">Cenários</a>
	</p>
</div>

<h2 id="sobre"> :eyes: Sobre</h2>

A aplicação SSEDG é um sistema projetado para fornecer dados precisos e consistentes de utilização de dispositivos em ambientes compartilhados, como casas com vários moradores. O sistema combina diferenes funcionalidaes para criar um ambiente virtual que replica fielmente as atividades dos moradores em uma casa compartilhada. Isso é alcançado por meio da modelagem espacial, consideração das preferências dos usuários, coleta de dados de sensores e uma rotina personalizável, garantindo que os dados gerados sejam precisos e relevantes para uma ampla variedade de aplicações, desde automação residencial até análises de consumo de energia.

* **Fornecimento de Dados Consistentes:** O objetivo central da aplicação é oferecer dados consistentes que espelham fielmente as atividades dos moradores na casa. Isso é conseguido ao considerar suas rotinas diárias e preferências individuais. Os dados resultantes refletem um modelo confiável do comportamento dos usuários na residência.

* **Modelo de Grafo para Representação:** A aplicação utiliza um modelo de grafo para representar a estrutura da casa. Nesse modelo, cada nó representa um cômodo, como quartos, banheiros e cozinhas, e as arestas indicam a distância e a conexão entre os cômodos. Isso permite à aplicação criar uma representação espacial realista e simular o movimento dos moradores na casa. O modelo de grafo é fundamental para gerar dados que levem em conta a proximidade dos cômodos e a dinâmica das atividades diárias.

* **Geração de Dados Baseada em Rotinas:** A aplicação baseia-se em uma rotina semanal predefinida para criar dados. Essa rotina engloba uma ampla gama de atividades, como dormir, acordar, tomar banho, cozinhar, trabalhar, ouvir música, entre outras. No entanto, os horários e a frequência de cada atividade podem ser personalizados de acordo com as necessidades do pesquisador, resultando em uma variação leve e realista nas rotinas diárias.

* **Consideração de Preferências dos Usuários:** A aplicação SSEDG pode utilizar as preferências individuais dos moradores. Isso significa que as configurações específicas, como temperatura desejada de um cômodo, iluminação ou preferências relacionadas a dispositivos inteligentes, são levadas em conta ao gerar dados. O sistema ajusta as rotinas e os parâmetros para atender às preferências exclusivas de cada usuário.

* **Variações nos Períodos de Atividade:** O sistema é flexível o suficiente para acomodar variações naturais nos horários das atividades dos moradores. Por exemplo, a hora de acordar ou dormir, ou os momentos de realizar atividades diárias, podem variar de um dia para o outro. A aplicação é capaz de acomodar essas variações para produzir dados que representem fielmente o comportamento real dos moradores.

<h2 id="requisitos"> :toolbox: Requisitos</h2>

* Python 3.10


<h2 id="instalacao"> :books: Gerando os Dados</h2>

Antes de tudo realize clone do repositório do projeto SSEDG para a sua máquina. Para isso execute os seguintes comando no terminal.

```
git clone git@github.com:SSEDG/SSEDG.git
git fetch
git checkout main
git pull
```
Para gerar um conjunto de dados simulados para ambientes inteligentes basta instalar as dependencias do projeto:

```
pip instal -r requirements.txt
```
E excutando o comando abaixo no diretório raiz do projeto o sistema será inicializado.
````
python3 main.py
````

Ao executa-lo será solicitado:
- O tipo de saída dos dados (Completo ou Simples).
- Quantidade de dias a serem simulados.
- A rotina a ser utilizada.

A partir disso teremos, uma saída de dados **Simples** ou uma saída de dados **Completa**. Os dados gerados são armazenados na pasta */dados*

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

![planta_1](https://github.com/SSEDG/SSEDG/blob/main/doc/img/planta_1.png?raw=true)

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

![planta_2](https://github.com/SSEDG/SSEDG/blob/main/doc/img/lanta_2.png?raw=true)





