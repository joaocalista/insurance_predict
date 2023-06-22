
# Previsão de Custos Médicos
![Alt text](/images/logo.png)

## Objetivos

Nesse projeto nós iremos realizar uma análise minuciosa do banco de dados de uma empresa do setor de seguros de saúde e desenvolver um modelo que tem como objetivo prever os custos médicos anuais dos clientes, com o intuito de melhor precificar os valores dos planos de saúde.

O principais objetivos são:

- Verificar de que forma a idade, imc, número de dependentes, região de moradia e a condição de fumante impactam os valores pagos pelos clientes.

- Criar um modelo de Machine Learning cujo objetivo é prever os valores desembolsados pelos indivíduos, anualmente.

- Validação de algumas hipóteses:

    H1: Pessoas com 50 anos ou mais pagam, em média, mais que pessoas de idade inferior.

    H2: Pessoas do sexo masculino pagam, em média, 10% a mais que pessoas do sexo feminino.
    
    H3: Pessoas com IMC igual ou maior a 30 pagam, em média, 50% a mais que pessoas com imc abaixo de 30.
   
    H4: Indivíduos com idade abaixo de 25 anos pagam menos que aqueles que têm idade igual ou acima de 25.
   
    H5: Fumantes pagam, em média, 40% a mais que pessoas não fumantes
   
    H6: Indivíduos que moram na região 'southwest' gastam mais com seguro de saúde, em média.
   
    H7: Quanto maior o número de dependentes, maior o valor pago.


- Elaborar um aplicativo web que irá ajudar os funcionários a melhor precificar o valor pago anualmente pelos indivíduos.

### Links para o Dashboard e Notebook
Clique [**aqui**](https://huggingface.co/spaces/joaocalista/insurance-premium-prediction) para acessar o aplicativo web.

Clique [**aqui**](https://github.com/joaocalista/insurance_predict/blob/main/project.ipynb) para acessar o notebook do projeto

## Questão de Negócio

A HealthStar é uma empresa de médio porte que atua no mercado de seguros de saúde e sempre está comprometida em oferecer as melhores opções de planos possíveis. Entretanto, em uma reunião com a equipe de negócios, o CEO da empresa percebeu que a precificação dos planos era feita com base em intuição e em dados históricos limitados, o que poderia não ser suficiente para fornecer preços justos e competitivos. Para resolver tal problema, o diretor excecutivo da companhia decidiu nos contratar com a intenção de criarmos um sistema que irá realizar a automação da precificação dos planos de saúde, baseando-se em dados dos clientes,  como idade, sexo, IMC, quantidade de dependentes, local de residência e se é fumante ou não.

Desse modo, teremos a tarefa de criar um modelo de predição de custo anual de plano de saúde preciso e disponibilizá-lo de forma que todo o time de negócio possa ter acesso a ele.

## Principais Resultados
Conseguimos desenvolver um modelo utilizando o algorítmo Random Forest, que teve os seguintes resultados:

- MAE: 2664,78
- MAPE: 28,68%
- RMSE: 4600,52
- MPE: -18,18%
- R2: 85,97%

O MAE nos indica que os valores previstos estão variando, em média, 2664,78 para cima ou para baixo em relação ao valor real.

O MAPE informa que as nossas predições estão, em média, 28,68% distantes dos valores reais.

O RMSE tem o mesmo significado que o MAE, porém é mais impactado por erros maiores, uma vez que eleva os erros ao quadrado.

O valor do MPE indica que o nosso modelo está prevendo, em média, 18% a mais que o valor real. Nosso modelo está superestimado, em média.

Por fim, temos o R-quadrado (R2) de 85,97%, o que indica que 85,97% das variações da variável resposta são explicadas pelas variáveis explicativas disponíveis.

As métricas estão relativamente altas, e isso se deve principalmente ao fato de que nosso dataset é pequeno: temos apenas 1338 registros.


## Estratégia de solução
- Entendimento do modelo de negócio da empresa
- Entendimento do problema de negócio
- Coleta dos dados
- Análise Exploratória dos Dados
- Tratamento e limpeza dos dados
- Insights obtidos
- Desenvolvimento do modelo de machine learning
- Avaliação do modelo
- Publicação de aplicativo online

## Principais Insights
- Pessoas com 50 anos ou mais tendem a pagar 57% a mais, em média.
- Homens tendem a pagar 11% a mais que mulheres, em média.
- Pessoas com IMC igual ou superior a 30 tendem a pagar, em média, 45% a mais.
- Pessoas com menos de 25 anos tendem a pagar menos, em média.
- Fumantes pagam muito mais que não fumantes. 280% a mais em média.
- O número de dependentes não parece afetar tanto o valor pago pelo cliente.
- A região de moradia do cliente aparentemente não influencia nos valores pagos.

## Conclusão
Através dessa análise realizada foi possível atender aos objetivos da empresa:
Fornecer um aplicativo web para precificação dos planos de saúde.

## Próximos Passos
- Coletar mais dados históricos para que o modelo possa entender ainda mais como os valores variam.
- Testar as relações entre as variáveis, com o objetivo de fornecer mais informações ao modelo.
- Criar grupos relacionados às features, como 'jovem', 'adulto', 'idoso', 'obeso', 'peso normal' etc. Para também fornecer mais informações ao modelo.
