# Enunciado: DR1 TP1 (Teste de Performance)

- **Disciplina:** Velocidade e Qualidade com Estruturas de Dados e Algoritmos
- **Trimestre:** 26E4
- **Professor:** Ian Monteiro Nunes
- **Bloco:** Ciência da Computação
- **Turma:** GRLENGR2C2-N2-L1
- **Instituição:** Instituto Infnet

Texto do enunciado, na íntegra, como foi entregue pela disciplina.

> Observação do aluno: o Exercício 2 menciona "as restrições apresentadas", mas o texto recebido não as
> traz; as restrições adotadas estão declaradas no relatório. A seção "Entrega" pede o nome
> `nome_sobrenome_DR2_TP1.PDF`, mas a disciplina é o DR1; o arquivo segue o código da disciplina
> (`andre_becker_DR1_TP1.pdf`).

---

## Exercício 1: Busca linear instrumentada

**Introdução**

Em sistemas computacionais que manipulam grandes volumes de dados em memória, a busca por elementos é uma operação recorrente e potencialmente custosa. A busca linear costuma ser adotada como solução inicial por sua simplicidade, porém seu custo cresce proporcionalmente ao tamanho da entrada. Um desenvolvedor avançado deve ser capaz de implementar esse algoritmo de forma correta, mas também de mensurar seu comportamento operacional, identificando gargalos e compreendendo seus limites de escalabilidade. Neste exercício, você irá instrumentar explicitamente a busca linear, conectando organização dos dados, etapas da operação e eficiência computacional.

**Tarefa**

1. Gere um array não ordenado com 10.000 números inteiros distintos.
2. Implemente uma função de busca linear em Python.
3. Instrumente o código para contar o número de comparações realizadas.
4. Execute a busca para um elemento presente na primeira posição do array.
5. Registre o número total de comparações.

## Exercício 2: Ordenação com Cartas (Algoritmo Conceitual)

**Introdução**

Antes de codificar algoritmos, é fundamental saber abstrair e modelar soluções independentemente da linguagem. Muitos algoritmos clássicos de ordenação surgem de processos manuais intuitivos. Este exercício propõe a construção de um algoritmo conceitual sob fortes restrições operacionais, simulando limitações reais de acesso e movimentação de dados. O objetivo é avaliar sua capacidade de decompor o problema, definir passos claros e reconhecer o padrão algorítmico subjacente à solução.

**Tarefa**

1. Elabore um algoritmo passo a passo para ordenar as 13 cartas de espadas conforme as restrições apresentadas.
2. Descreva claramente o estado inicial, as operações permitidas e o estado final.
3. Identifique qual algoritmo de ordenação clássico o procedimento mais se aproxima.
4. Justifique sua resposta com base nas operações realizadas.
5. Descreva qualitativamente o custo do algoritmo em termos de Big O.

## Exercício 3: Busca Linear vs. Busca Binária (Análise Manual)

**Introdução**

A análise de algoritmos não depende exclusivamente de execução em máquina. Em muitos contextos, é necessário estimar custos manualmente para compreender comportamento e eficiência. Neste exercício, você analisará passo a passo a execução da busca linear em um conjunto pequeno de dados, reforçando o entendimento das etapas da operação e do custo associado.

**Tarefa**

1. Considere o array ordenado [2, 4, 6, 8, 10, 12, 13].
2. Simule manualmente a execução da busca linear pelo valor 8.
3. Conte o número de comparações realizadas.
4. Justifique o resultado obtido.
5. Relacione o número de passos ao tamanho do array.

## Exercício 4: Busca Linear vs. Busca Binária (Análise Manual)

**Introdução**

A busca binária explora a organização dos dados para reduzir significativamente o espaço de busca. A análise manual desse algoritmo é fundamental para compreender por que ele é mais eficiente do que a busca linear em arrays ordenados. Neste exercício, você realizará essa análise de forma detalhada.

**Tarefa**

1. Utilize o mesmo array do Exercício 3.
2. Simule manualmente a execução da busca binária pelo valor 8.
3. Conte o número de comparações realizadas.
4. Compare o resultado com a busca linear.
5. Relacione a diferença observada à notação Big O.

## Exercício 5: Otimização de Algoritmo (O(N²) → O(N))

**Introdução**

Identificar e eliminar ineficiências algorítmicas é uma competência central no desenvolvimento de software de qualidade. Algoritmos com complexidade quadrática rapidamente se tornam inviáveis em grandes volumes de dados. Neste exercício, você analisará um código real, identificará seu gargalo e o reescreverá de forma mais eficiente, preservando a funcionalidade.

```python
def maior_unico(arr):
    """
    Retorna o maior número que aparece exatamente uma vez no array.
    """

    maior = None  # Guardará o maior número único encontrado

    # Percorre cada elemento do array
    for i in range(len(arr)):
        atual = arr[i]
        contador = 0  # Contará quantas vezes 'atual' aparece

        # Compara o elemento atual com todos os outros
        for j in range(len(arr)):
            if arr[j] == atual:
                contador += 1

        # Se apareceu exatamente uma vez, é um candidato
        if contador == 1:
            # Atualiza o maior único encontrado
            if (maior is None) or (atual > maior):
                maior = atual

    return maior
```

**Tarefa**

1. Analise a função fornecida para encontrar o maior número único.
2. Identifique o motivo de sua complexidade O(N²).
3. Reescreva a função para que opere em O(N).
4. Explique a estratégia utilizada para reduzir a complexidade.
5. Justifique a nova complexidade usando Big O.

## Exercício 6: Tabuleiro de Xadrez e Grãos de Arroz

**Introdução**

Este exercício explora crescimento exponencial e sua relação direta com análise de complexidade algorítmica. O clássico problema do tabuleiro de xadrez e grãos de arroz é utilizado para demonstrar como funções aparentemente simples podem crescer rapidamente, tornando soluções ingênuas inviáveis. O objetivo é exercitar a modelagem correta do problema, a implementação em Python e a análise do custo computacional da abordagem adotada.

**Tarefa**

Considere as seguintes premissas obrigatórias:

1. O tabuleiro possui 64 quadrados, numerados de 1 a 64.
2. No quadrado 1, há 1 grão de arroz.
3. Em cada quadrado seguinte, a quantidade de grãos dobra em relação ao quadrado anterior.
4. A quantidade de grãos em um quadrado é dada por: grãos = 2^(n-1), onde n é o índice do quadrado.
5. A entrada da função representa uma quantidade alvo de grãos, e não o número do quadrado.

Com base nessas premissas:

1. Implemente uma função em Python que receba como parâmetro um número inteiro positivo qtd_graos.
2. Calcule qual é o menor índice de quadrado do tabuleiro em que a quantidade de grãos acumulada no próprio quadrado é maior ou igual a qtd_graos.
3. Caso a quantidade informada ultrapasse o total de grãos do tabuleiro (64 quadrados), a função deve retornar uma mensagem indicando que o valor excede o limite do tabuleiro.
4. Teste a função com, no mínimo:
   1. valores pequenos (ex: 1, 2, 4, 8);
   2. valores intermediários (ex: 1.000, 1.000.000);
   3. um valor maior que o total de grãos possíveis no tabuleiro.
5. Descreva a complexidade temporal da solução implementada utilizando Notação Big O, justificando sua resposta com base no número de iterações realizadas.

**Observações**

1. Não utilize fórmulas matemáticas prontas para calcular diretamente o índice do quadrado.
2. A solução deve ser baseada em iteração ou recursão, permitindo a análise explícita do custo computacional.
3. A clareza da implementação e da análise de complexidade faz parte da avaliação.

## Exercício 7: Notação Big O (Análise de Código)

A análise de complexidade raramente ocorre apenas sobre algoritmos escritos pelo próprio desenvolvedor. Na prática profissional, é comum avaliar código existente para estimar seu custo computacional, identificar gargalos e orientar decisões de otimização. Este exercício desenvolve a habilidade de ler código de forma analítica, explicitando hipóteses sobre o modelo de custo adotado e relacionando estrutura de controle, tamanho da entrada e crescimento assintótico.

Considere a seguinte função em Python:

```python
def only_a_strings(strings):
    result = []
    for s in strings:
        if len(s) > 0 and s[0] == "a":
            result.append(s)
    return result
```

**Tarefa**

Considere as seguintes premissas obrigatórias para a análise:

1. O array de entrada strings possui N elementos.
2. Cada elemento do array é uma string de tamanho médio constante (ou seja, o tamanho das strings não cresce com N).
3. As operações len(s), s[0] == "a" e append possuem custo constante O(1).
4. Não considere o custo de alocação de memória interna do Python além dessas operações.

Com base nessas premissas:

1. Identifique quantas vezes o laço for é executado em função de N.
2. Descreva as operações realizadas a cada iteração do laço.
3. Determine o custo total da função em função do tamanho do array de entrada.
4. Expresse a complexidade temporal do algoritmo utilizando Notação Big O.
5. Justifique tecnicamente sua resposta, relacionando a estrutura do código ao crescimento assintótico.

**Observações**

1. Não é necessário reescrever ou otimizar o código.
2. A resposta deve ser baseada exclusivamente na análise estrutural do algoritmo.
3. A clareza da justificativa é parte essencial da avaliação.

## Exercício 8: Bubble Sort Bidirecional (Cocktail Sort)

**Introdução**

Algoritmos clássicos podem ser aprimorados para reduzir trabalho desnecessário. O Bubble Sort bidirecional é uma variação que melhora o desempenho em certos cenários.

**Tarefa**

1. Modifique o Bubble Sort para torná-lo bidirecional.
2. Utilize dois índices externos, esquerdo e direito.
3. Garanta que o maior elemento vá para a direita e o menor para a esquerda.
4. Teste o algoritmo com diferentes arrays.
5. Compare conceitualmente com o Bubble Sort tradicional.

## Exercício 9: Bubble Sort Numérico

**Introdução**

A implementação correta de algoritmos clássicos é uma exigência básica para desenvolvedores avançados. Este exercício consolida a implementação prática do Bubble Sort, garantindo domínio do algoritmo.

**Tarefa**

1. Implemente o Bubble Sort em Python.
2. Ordene uma lista de números em ordem crescente.
3. Teste com listas já ordenadas e desordenadas.
4. Verifique a corretude da saída.
5. Registre evidências de execução.

## Exercício 10: Bubble Sort para Strings

**Introdução**

Algoritmos de ordenação devem ser adaptáveis a diferentes tipos de dados. Neste exercício, você aplicará o Bubble Sort para ordenar strings, reforçando o entendimento de comparações lexicográficas.

**Tarefa**

1. Modifique o Bubble Sort para ordenar strings.
2. Ordene listas de palavras em ordem alfabética.
3. Teste com diferentes conjuntos de strings.
4. Valide os resultados.
5. Documente o comportamento observado.

## Exercício 11: Instrumentação do Bubble Sort

**Introdução**

Mensurar custo computacional exige instrumentação explícita. Neste exercício, você aprofundará a análise do Bubble Sort contando operações reais.

**Tarefa**

1. Instrumente o Bubble Sort para contar comparações.
2. Conte também o número de trocas.
3. Execute o algoritmo para diferentes tamanhos de entrada.
4. Registre os resultados.
5. Analise o crescimento observado.

## Exercício 12: Bubble Sort Otimizado

**Introdução**

Pequenas otimizações podem gerar ganhos relevantes. Neste exercício, você aplicará uma otimização clássica ao Bubble Sort e avaliará seu impacto.

**Tarefa**

1. Modifique o Bubble Sort para interromper quando não houver trocas.
2. Execute o algoritmo com os mesmos dados do Exercício 11.
3. Compare os resultados.
4. Analise o ganho obtido.
5. Relacione com Big O.

## Exercício 13: Comparação de Estratégias de Busca (com Código e Testes)

Na prática, a escolha entre busca linear e busca binária depende de pré-requisitos, custo de preparação dos dados e perfil de uso (quantidade de buscas realizadas). Neste exercício, você vai implementar, instrumentar e testar as duas estratégias, comparando o custo por meio de contagem de operações (comparações e iterações), e não por tempo de execução em segundos. O objetivo é tornar a comparação objetiva e reproduzível, usando Notação Big O para interpretar os resultados.

**Premissas obrigatórias**

1. Você receberá listas de números inteiros com tamanho N.
2. A busca binária só pode ser aplicada corretamente em lista ordenada.
3. Quando a lista não estiver ordenada e você quiser usar busca binária, você deve ordená-la antes usando Bubble Sort (já visto nas subcompetências avaliadas).
4. Você deve comparar os algoritmos pelo número de comparações realizadas.
5. Faça a análise considerando o pior caso e também observe empiricamente os casos testados.

**Tarefa**

*Parte A — Implementação instrumentada*

1. Implemente a função `linear_search_count(arr, target)` que:
   1. retorna uma tupla `(index, comparisons)`
   2. `index` é a posição do elemento encontrado ou -1 se não encontrado
   3. `comparisons` é o número de comparações `arr[i] == target` executadas
2. Implemente a função `binary_search_count(sorted_arr, target)` que:
   1. retorna uma tupla `(index, comparisons)`
   2. assume que o array já está ordenado
   3. conta comparações de chave (comparações entre target e o valor do meio)
3. Implemente a função `bubble_sort_count(arr)` que:
   1. ordena uma cópia da lista (não altere a original)
   2. retorna `(sorted_arr, comparisons)` onde comparisons conta comparações entre pares adjacentes

*Parte B — Casos de teste controlados*

1. Crie 3 listas com N = 31:
   1. `arr_sorted`: lista ordenada crescente
   2. `arr_reverse`: lista ordenada decrescente
   3. `arr_random`: lista com os mesmos elementos, mas embaralhada (use `random.seed(42)`)
2. Para cada uma das 3 listas, execute as buscas para três alvos:
   1. `target_first` = primeiro elemento da lista
   2. `target_middle` = elemento do meio (posição N//2)
   3. `target_absent` = um valor que você garanta que não existe na lista (ex: -1)
3. Em cada execução, registre:
   1. Comparações da busca linear
   2. Comparações da busca binária (quando aplicável)
   3. Se a lista não estiver ordenada, registre também:
      1. Comparações do Bubble Sort
      2. Comparações totais "Bubble Sort + Busca Binária"

*Parte C — Interpretação e Big O*

1. Escreva uma conclusão técnica em Markdown respondendo:
   1. Quais são os pré-requisitos de cada busca?
   2. Qual é o Big O da busca linear e da busca binária?
   3. Em listas não ordenadas, quando faz sentido pagar o custo do Bubble Sort para usar busca binária?
   4. Relacione suas conclusões com os resultados (comparações) observados.

## Exercício 14: Organização de Código e Qualidade (Refatoração)

**Introdução**

Código eficiente não é apenas código rápido, mas também código legível, organizado e sustentável. Em ambientes profissionais, algoritmos corretos frequentemente precisam ser mantidos, revisados e evoluídos por outras pessoas. Este exercício avalia a capacidade de melhorar a qualidade estrutural do código sem alterar seu comportamento ou sua complexidade assintótica.

**Código fornecido para refatoração**

Utilize o código abaixo como ponto de partida. Não altere a lógica do algoritmo nem os resultados produzidos.

```python
def f(a, t):
    c = 0
    i = 0
    j = len(a) - 1
    r = -1
    while i <= j:
        m = (i + j) // 2
        c = c + 1
        if a[m] == t:
            r = m
            break
        c = c + 1
        if t < a[m]:
            j = m - 1
        else:
            i = m + 1
    return r, c

def h(arr):
    b = arr[:]
    n = len(b)
    k = 0
    for last in range(n - 1, 0, -1):
        for p in range(last):
            k += 1
            if b[p] > b[p + 1]:
                tmp = b[p]
                b[p] = b[p + 1]
                b[p + 1] = tmp
    return b, k
```

**Tarefa**

1. Refatore o código fornecido, preservando exatamente o comportamento.
2. Melhore nomes de funções, variáveis e parâmetros.
3. Organize o código para tornar a leitura e manutenção mais claras.
4. Adicione comentários técnicos objetivos.
5. Mantenha a complexidade assintótica dos algoritmos (busca binária e Bubble Sort).
6. Crie um pequeno teste que demonstre que a versão refatorada produz o mesmo resultado da original.

**Observações**

* Não utilize funções prontas como sorted, .sort() ou bibliotecas externas.
* Não altere contadores ou critérios de parada.
* O foco é qualidade de código, não otimização algorítmica.

## Vídeo Explicativo Obrigatório

Além da implementação e da documentação escrita, você deverá gravar um vídeo com duração entre 4 e 6 minutos, no qual deverá:

* Explicar, com suas próprias palavras, o que foi feito em cada conjunto de exercícios
* Demonstrar no terminal os principais comandos e execuções realizadas
* Comentar brevemente cada execução, explicando a estratégia adotada e as decisões técnicas
* Relacionar suas implementações com conceitos de eficiência e Big O, sempre que aplicável

O vídeo deve ser objetivo, técnico e demonstrar domínio do conteúdo desenvolvido no TP.

**Orientações para Defesa do Trabalho em Vídeo**

1. Utilize uma ferramenta adequada: É preciso que apareça a tela com seu trabalho e a imagem da sua webcam. Uma sugestão de ferramenta gratuita online para estudantes é o [Loom](https://www.loom.com/). Caso prefira, existe também a opção de baixar a ferramenta [OBS](https://obsproject.com/pt-br/download), dentre outras.
2. Escolha um local adequado: Grave em um ambiente calmo, sem ruídos ou distrações, para garantir boa qualidade de áudio e foco durante a defesa.
3. Webcam ligada: Certifique-se de que a webcam esteja ativada, com boa iluminação e enquadrando você de forma clara e centralizada.
4. Revise o vídeo: Assista a gravação para verificar se o vídeo e o áudio estão bons.
5. Salve o vídeo no Google Drive: Após a gravação, faça o upload do arquivo para o seu Google Drive de aluno Infnet.
6. Altere as permissões de acesso: Configure o compartilhamento do vídeo para "qualquer pessoa com o link" poder visualizar. Copie o link gerado e envie conforme as instruções da atividade.

## Entrega

Ao finalizar todos os exercícios:

1. Reúna todos os screenshots gerados durante a execução das tarefas em um único arquivo PDF
2. Grave um vídeo entre 4 e 6 minutos, explicando e demonstrando no terminal as atividades realizadas
   1. O vídeo deve ser armazenado no seu Google Drive institucional
   2. Insira o link do vídeo ao final do PDF
3. Nomeie o arquivo conforme o padrão: nome_sobrenome_DR2_TP1.PDF
4. Poste o PDF como resposta a este Teste de Performance no ambiente da disciplina

Os screenshots devem evidenciar claramente os comandos executados e suas respectivas saídas, funcionando como complemento às evidências textuais e à explicação apresentada no vídeo.

Boa sorte e bons estudos!
