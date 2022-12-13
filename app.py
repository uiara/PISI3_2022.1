import streamlit as st
import pandas as pd
import seaborn as seaborn
import numpy as np
import matplotlib.pyplot as plt


st.title("Análise de dados")
st.write("Esta página tem como intuito mostrar a analise dos dados de arquivos csv")

dados = pd.read_csv("dados/Portuguese.csv")



st.dataframe(dados) #comando q aparece toda a tabela

# grafico fem X masculino
genero_fem = dados.age.loc[dados.sex == 'F'].value_counts()
genero_mas = dados.age.loc[dados.sex == 'M'].value_counts()

x1 = genero_fem.index
y1 = genero_fem.values

x2 = genero_mas.index
y2 = genero_mas.values

plt.bar(x1, y1, label='Feminino', width=0.4, align='edge')
plt.bar(x2, y2, label='Masculino', width=-0.4, align='edge')
plt.legend()
plt.title("Feminino vs Masculino")
plt.show()

st.pyplot(plt)
