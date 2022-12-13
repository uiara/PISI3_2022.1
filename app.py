import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.title("Análise de dados")

dados = pd.read_csv("dados/Portuguese.csv")

#st.dataframe(dados), comando q apareceria toda a tabela

genero_fem = dados.age.loc[dados.sex== 'F'].value_counts()
genero_mas = dados.age.loc[dados.sex== 'M'].value_counts()

x1 = genero_fem.index
y1 = genero_fem.values

x2 = genero_mas.index
y2 = genero_mas.values

plt.bar(x1, y1, label='Feminino', width = 0.4, align = 'edge')
plt.bar(x2, y2, label='Masculino', width = -0.4, align = 'edge')
plt.legend()
plt.title("Feminino vs Masculino")
plt.show()

st.pyplot(plt)