import streamlit as st
import duckdb
import pandas as pd

def create_duckdb(): # errado ao trazer a query calculado dentro do dashboard, deixar os dados pre processados
    result = duckdb.sql(""" 
        SELECT cidade,
            MIN(temperatura) AS min_temperature,
            CAST(AVG(temperatura) AS DECIMAL(3,1)) AS mean_temperature,
            MAX(temperatura) AS max_temperature
        FROM read_csv("data/measurements.txt", AUTO_DETECT=FALSE, sep=';', columns={'cidade':VARCHAR, 'temperatura': 'DECIMAL(3,1)'})
        GROUP BY cidade
        ORDER BY cidade
    """)
    
    df = result.df()
    return df

def main():
    st.title("Weather Station SUmmary")
    st.write("This dash SHows the summary of")
    data = create_duckdb()
    
    st.dataframe(data)

if __name__ == "__main__":
    main()