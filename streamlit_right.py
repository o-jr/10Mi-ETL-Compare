import streamlit as st
import duckdb
import pandas as pd

def load_data():
    con = duckdb.connect()
    df = con.execute("SELECT * FROM 'data/measurements.parquet'").df()
    con.close()
    return df

def main():
    st.title("Weather Station SUmmary")
    st.write("This dash SHows the summary of")
    data = load_data()

    #shows the data in table format
    st.dataframe(data)

if __name__ == "__main__":
    main()