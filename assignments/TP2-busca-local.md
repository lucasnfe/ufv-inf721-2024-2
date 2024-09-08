---
layout: page
title: TP 2 - Busca local
permalink: /assignments/tp2-busca-local
nav_exclude: true
---

# TP2 - Busca local

## Introdução

No [projeto anterior](/assignments/tp1-busca), você implementou diferentes algoritmos de busca para resolver o problema do caminho mais curto em mapas com estrutura de grade. Como parte desse processo, você teve que criar mapas manualmente para comparar o desempenho dos diferentes algoritmos. Neste projeto, você irá implementar um algoritmo genético para gerar mapas automaticamente, em particular, mapas que maximizem o tamanho do caminho entre um dado estado inicial e um final. O objetivo deste projeto é praticar a modelagem e a implementação de algoritmos genéticos, bem como analisar os resultados desse tipo de algoritmo, em particular o impacto dos parâmetros do algoritmo na curva de adaptação das soluções.

## Código-base

### Executar servidor

Clique [aqui](/assets/code/tp2-busca-local.zip) para baixar o código-base, que inclui um cliente em JavaScript para configurar os parâmetros do algoritmo, definir estados iniciais e finais, iniciar a busca e salvar os mapas gerados. Além disso, o código também contém um servidor em Python para implementar e executar o algoritmo genético. Para executar o servidor, você precisará instalar as dependências do projeto e iniciar o servidor com os seguintes comandos:

```
pip install -r requirements.txt # Instalar dependencias
python3 server.py -port 5001 # Executar o servidor
```

Assim que o servidor iniciar, você pode abrir o seguinte endereço em qualquer navegador: [http://localhost:5001](http://localhost:5001).

## Tarefas

Antes de iniciar as tarefas, estude as classes `Individual` e `GeneticAlgorithm`, as quais você irá utilizar como base para implementar o seu algoritmo genético.

### 1. Representação dos indivíduos

Sua primeira tarefa é definir uma codificação em forma de genótipo para representar um mapa e implementar os métodos `gen_genotype` e `Individual.get_phenotype` para gerar um indivíduo aleatório e mapear seu genótipo para um fenótipo, respectivamente.

### 2. Função de adaptação

A segunda tarefa é definir uma função de adaptação que retorne valores de adaptação altos para mapas com altos caminhos entre a origem e o destino. Uma ideia simples é utilizar o A* que você implementou no projeto anterior para encontrar o caminho entre a origem e o destino, e retornar o tamanho do caminho encontrado como valor de adaptação. Note que quanto maior o mapa, mais difícil será encontrar um caminho entre a origem e o destino, portanto é importante decidir como calcular a adaptação de indivíduos infactíveis, de tal forma que mapas que precisem de pouca alteração para se tornarem factíveis tenham adaptação maior do que mapas que precisem de mais modificações. Implemente a sua função de adaptação no método `Individual.fitness`.

### 3. Inicialização da população

Agora que você terminou a implementação da classe `Individual`, você pode inicializar a população do algoritmo genético no método `GeneticAlgorithm.initialize_population`. Para isso, basta criar um número `self.population_size` de indivíduos e adicioná-los à lista `self.population`.

### 3. Seleção 

Escolha um método de seleção visto em aula (se escolher outro, adicionar referência) e o implemente no método `GeneticAlgorithm.selection`. Esse método deve retornar dois individuos de `self.population` com base em seus valores de adaptação `fitness_scores`, dando mais chance para aqueles com maior valor de fitness. 

### 4. Cruzamento

Defina um método de cruzamento adequado à sua representação de indivíduos e o implemente no método `GeneticAlgorithm.crossover`. Esse método deve retornar dois novos indivíduos filhos como resultado do cruzamento genético de dois indivíduos pais `parent1` e `parent2`. 

### 5. Mutação

Defina um método de mutação adequado à sua representação de indivíduos e o implemente no método `GeneticAlgorithm.mutate`. Esse método deve alterar aleatoriamente os genes de um indivíduo de acordo com a taxa de mutação defiida `self.mutation_rate`. 

### 6. Evolução 

Implemente o método `GeneticAlgoritm.evolve` para executar uma única geração do algoritmo genético. Esse método deve seguir a seguinte estrutura:

1. Avaliação da população atual `self.population` com o método `Individual.fitness`
2. Inicializar a nova geração `new_pop` com uma lista vazia
3. Repetir até que o tamanho de `new_pop` seja igual a `self.population_size`:
    1. Selecionar dois pais `p1` e `p2` para cruzamento com o método `GeneticAlgorithm.select`. 
    2. Gerar dois filhos `c1` e `c2` por meio do cruzamento entre `p1` e `p2` com `GeneticAlgorithm.crossover`
    3. Mutar os filhos `c1` e `c2` aleatoriamente com o método `GeneticAlgorithm.mutate`
    4. Adicionar `c1` e `c2` a `new_pop`
4. Atualizar a população atual `self.population` com a nova geração

Note que essa é a estrutura mínima que a sua implementação deve conter. Fique à vontade para acrescentar melhorias, como elitismo, por exemplo. A função `GeneticAlgoritm.evolve` deve retonar uma tupla `(best, path)`, onde `best` é o fenótipo (mapa em formato de grade) do melhor indivíduo da população ao final da geração e `path` é o caminho mais curto em o estado incial e o final nesse indivíduo. 

Ao final dessa etapa, você deveria conseguir executar seu algoritmo genético no cliente Javascript para diferentes tamahos de população e números de gerações. O cliente deveria mostar o melhor individuo ao final de cada geração.

### 7. Estética dos mapas

As fases anteriores delineiam um algoritmo genético voltado para a maximização do percurso entre os estados de origem e destino. Neste estágio final de implementação, você será encarregado de ampliar a funcionalidade da sua função de adaptação `Individual.fitness` para também influenciar a estética dos mapas produzidos. *A alteração deve manter a avaliação com base no percurso*, ou seja, você irá integrar novos termos à sua função original para orientar as características estéticas do mapa. Para realizar isso, será necessário definir a estética desejada para seus mapas e codificá-la matematicamente de modo que possa ser incorporada à função de adaptação. Algumas ideias simples:

- Simetria vertical, horizontal, diagonal ou completa
- ...  

### 8. Relatório

Após concluir a implementação do algoritmo genético, você irá analisar o seu desempenho com relação ao tamanho da população (P), número de gerações (G) e taxa de mutação (T). Execute o seu algoritmo 30 vezes e reporte a curva de adaptação média do melhor indivíduo para cada configuração de parâmetros abaixo:

1. Variação de tamanho da população:
    - P = 100, G = 100, T = 1
    - P = 400, G = 100, T = 1
    - P = 800, G = 100, T = 1
    - P = 1600, G = 100, T = 1
2. Variação do número de gerações:
    - P = 400, G = 100, T = 1
    - P = 400, G = 250, T = 1
    - P = 400, G = 500, T = 1
    - P = 400, G = 1000, T = 1
3. Variação da taxa de mutação:
    - P = 200, G = 250, T = 1
    - P = 200, G = 250, T = 5
    - P = 200, G = 250, T = 15
    - P = 200, G = 250, T = 20

O seu relatório deve conter no máximo 2 páginas no formato da [Association for the Advancement of Artificial Intelligence (AAAI)](https://aaai.org/authorkit24-2/) (disponível também no [Overleaf](https://www.overleaf.com/latex/templates/aaai-2023-author-kit/wxnmhzcrjbpc)). Cada variação de parâmetros gerará uma curva, ou seja, serão 12 gráficos no total. Agrupe essas gráficos em 3 imagens por tipo de parâmetro, onde cada imagem conterá 4 gráficos. Inclua também 3 mapas no seu relatório, uma para cada grupo de experimentos, ilustrando o melhor indivíduo encontrado dentre todas as variações daquele grupo. Discuta as características desse mapa. 

## Submissão

Para submeter o seu trabalho, submeta o seu arquivo `genetic.py` e o seu relatório `relatorio.pdf` (em formato pdf) na tarefa **TP2 - Busca local** no PVANet.

## Referências

- [Evolutionary Computing, The Nature of Code](https://natureofcode.com/genetic-algorithms/)