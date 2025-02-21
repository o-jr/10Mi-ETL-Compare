# 10Mi-ETL-Compare

## 1. Introdução
Esse projeto analisa a eficiência de ferramentas ETL para testar o processamento de
grandes volumes de dados, contendo medições de temperatura de estações
meteorológicas.
O objetivo é avaliar o desempenho em termos de tempo de execução para realizar
operações de agregação por cidade, ordenação e salvamento dos resultados em .parquet.


## 2. Metodologia
### 2.1. Dados de Entrada
- **Tamanho do arquivo**: 10 milhões de linhas.
- **Formato do arquivo**: `.txt`, delimitado por `;`, com duas colunas:
  - `cidade` (texto, VARCHAR).
  - `temperatura` (número decimal, DECIMAL(3,1)).
- **Exemplo de conteúdo**:
  ```
  São Paulo;-10.5
  Rio de Janeiro;25.3
  São Paulo;15.7
  Rio de Janeiro;30.2
  ```

### 2.2. Operações Realizadas
- **Leitura do arquivo**.
- **Agregação por cidade**:
  - Cálculo da temperatura mínima (`MIN`).
  - Cálculo da média das temperaturas (`AVG`), arredondada para 1 casa decimal.
  - Cálculo da temperatura máxima (`MAX`).
- **Ordenação** dos resultados por cidade.
- **Exibição dos resultados** no console.
- **Salvamento dos resultados** em um arquivo (Parquet para DuckDB, ou outro formato para Python/Pandas).

### 2.3. Ferramentas Comparadas
1. **Python puro**:
   - Leitura do arquivo linha por linha.
   - Processamento manual das agregações usando dicionários ou listas.
   - Ordenação manual dos resultados.
2. **Pandas**:
   - Leitura do arquivo com `pd.read_csv`.
   - Uso de `groupby` e `agg` para agregações.
   - Ordenação com `sort_values`.
3. **DuckDB**:
   - Leitura do arquivo com `read_csv`.
   - Consulta SQL para agregações e ordenação.
   - Salvamento em Parquet com `write_parquet`.

### 2.4. Métrica de Avaliação
- **Tempo de execução**: Tempo total (em segundos) para realizar todas as operações, medido com `time.time()`.

### 2.5. Fluxograma
![pipeline](https://github.com/user-attachments/assets/1f2b4f5d-ea04-4405-adae-0255e931381b)


## 3. Resultados

```
Tempo de Execução (segundos)
Python puro: ████████████████████████████████████████████████████ 54.78
Pandas:      ████████████████████████████ 27.10
DuckDB:      ███████████ 10.64
```

## 4. Análise de Eficiência do DuckDB
### 4.1. Por que o DuckDB é mais rápido?
1. **Processamento Colunar**:
   - DuckDB utiliza um modelo de armazenamento colunar, otimizado para operações analíticas como agregações e filtros.
   - Em contraste, Pandas usa um modelo baseado em linhas (DataFrame), e Python puro processa os dados linha por linha, o que é menos eficiente para grandes volumes.

2. **Execução Otimizada**:
   - DuckDB é implementado em C++ e utiliza técnicas de otimização como vetorização e paralelismo.
   - Pandas, embora otimizado, depende de bibliotecas como NumPy e ainda tem overheads de Python.
   - Python puro não possui otimizações específicas para grandes volumes de dados.

3. **Leitura Eficiente de Arquivos**:
   - A função `read_csv` do DuckDB é altamente otimizada para leitura de arquivos grandes, com suporte a paralelismo.
   - Pandas também é eficiente, mas tem maior overhead devido à conversão para DataFrame.
   - Python puro lê o arquivo linha por linha, o que é ineficiente para 10 milhões de linhas.

4. **Consultas SQL**:
   - DuckDB permite consultas SQL diretas, que são otimizadas internamente.
   - Pandas requer chamadas de métodos como `groupby` e `agg`, que podem ser menos eficientes.
   - Python puro exige implementações manuais, que são propensas a ineficiências.


### 4.2. Benefícios Adicionais do DuckDB
- **Baixo Consumo de Memória**:
  - DuckDB processa dados em blocos, permitindo trabalhar com arquivos maiores que a memória RAM.
  - Pandas carrega todo o DataFrame na memória, o que pode ser problemático para arquivos muito grandes.
- **Facilidade de Uso**:
  - A sintaxe SQL do DuckDB é familiar para analistas de dados e engenheiros.
  - Pandas requer conhecimento de suas APIs, e Python puro exige mais código.
- **Integração com Ecossistema Analítico**:
  - O formato Parquet gerado pelo DuckDB é compatível com ferramentas como Apache Spark, Dask e outras.
 

## 5 Limitações e Considerações
### 5.1. Quando Usar Cada Ferramenta
- **DuckDB**:
  - Ideal para grandes volumes de dados e operações analíticas.
  - Quando o desempenho é crítico.
- **Pandas**:
  - Útil para datasets menores ou médios (até alguns milhões de linhas).
  - Quando há necessidade de manipulação interativa de dados.
- **Python puro**:
  - Apenas para prototipagem ou datasets muito pequenos.
  - Não recomendado para grandes volumes devido ao desempenho.

## 6. Conclusão
O DuckDB demonstrou ser significativamente mais eficiente que Pandas e Python puro para o processamento de 10 milhões de linhas. Isso representa uma melhoria de **2,55 vezes** em relação ao Pandas e **5,15 vezes** em relação ao Python puro.

A eficiência do DuckDB é atribuída ao seu modelo colunar, otimizações internas, leitura eficiente de arquivos e uso de consultas SQL. Além disso, o DuckDB oferece benefícios adicionais, como baixo consumo de memória e integração com o ecossistema analítico.

Para cenários de big data e análise de alto desempenho, o DuckDB é a escolha recomendada. Para datasets menores ou manipulação interativa, Pandas ainda é uma opção viável. Python puro deve ser evitado para grandes volumes de dados devido ao seu desempenho inferior.
