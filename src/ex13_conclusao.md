# Exercício 13: conclusão (Parte C)

Resultados do `ex13_comparacao_buscas.py`, com N = 31:

| Lista | Alvo | Linear | Binária | Bubble Sort | Bubble + Binária |
|---|---|---|---|---|---|
| arr_sorted | primeiro (1) | 1 | 9 | - | - |
| arr_sorted | meio (16) | 16 | 1 | - | - |
| arr_sorted | ausente (-1) | 31 | 10 | - | - |
| arr_reverse | primeiro (31) | 1 | 9 | 465 | 474 |
| arr_reverse | meio (16) | 16 | 1 | 465 | 466 |
| arr_reverse | ausente (-1) | 31 | 10 | 465 | 475 |
| arr_random | primeiro (20) | 1 | 5 | 465 | 470 |
| arr_random | meio (29) | 16 | 9 | 465 | 474 |
| arr_random | ausente (-1) | 31 | 10 | 465 | 475 |

## 1. Pré-requisitos

A busca linear não tem pré-requisito: funciona em qualquer lista, porque olha um elemento de cada
vez. A binária exige a lista em ordem crescente, porque só assim dá para descartar uma metade
inteira olhando o meio. Testei aplicar a binária direto na `arr_random` e ela não encontrou o 20,
que está na lista.

## 2. Big O

A linear é O(N): com o alvo ausente fez as 31 comparações. A binária é O(log N): cada volta descarta
metade da lista, então com N = 31 são no máximo 5 voltas, ou 10 comparações na minha contagem (a de
igualdade e a de direção). O Bubble Sort clássico é O(N²) e sempre faz N(N−1)/2 = 465 comparações.

## 3. Quando vale ordenar com Bubble Sort

Para uma busca só, não vale: ordenar custa 465 comparações, e a pior busca linear custa 31. Ordenar
só compensa quando a mesma lista vai receber muitas buscas. No pior caso, k buscas custam 31k na
linear e 465 + 10k ordenando antes. A partir de **k = 23** a segunda opção fica mais barata (695
contra 713). De forma geral, com o Bubble Sort isso acontece depois de mais ou menos N/2 buscas.

## 4. Relação com os resultados

- Com o alvo na primeira posição a linear ganhou (1 comparação contra 9 da binária). A Big O fala do
  pior caso, não de toda execução.
- Com o alvo no meio foi o contrário: a binária achou o 16 na primeira comparação e a linear precisou
  de 16.
- Com o alvo ausente, que é o pior caso das duas, foram 31 contra 10. Essa diferença cresce com N:
  para 1.000.000 de elementos seriam 1.000.000 contra 40.
- Nas listas fora de ordem, as 465 comparações do Bubble Sort dominam o total (466 a 475), muito
  mais que qualquer busca linear isolada.

Minha conclusão: se a lista já está ordenada, uso a busca binária. Se não está e vou buscar poucas
vezes, a linear sai mais barata. Ordenar antes só vale quando a mesma lista recebe muitas buscas,
mais de 23 neste caso.
