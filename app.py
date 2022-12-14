import streamlit as st
import pandas as pd
import seaborn as seaborn
import numpy as np
import matplotlib.pyplot as plt
#from sklearn import datasets 


#informacoes no head da pagina
st.set_page_config(page_title='Analise de dados', page_icon=':bar_chart')
st.title("Análise de dados")
st.write("Esta página tem como objetivo mostrar a analise dos dados de arquivos csv")

dados = pd.read_csv("dados/Portuguese.csv")


st.dataframe(dados)  # comando q aparece toda a tabela

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


#outros testes de como utilizar o streamlit no fim da pagina
dataset_name = st.sidebar.selectbox("Selected dataset", ("Maths", "Portuguese"))

classifier_name = st.sidebar.selectbox("Selected classifier", ("KNN", "SVM","Random forest"))

def get_dataset(dataset_name):
    if dataset_name == "Maths":
        data = dataset.load_maths()
    else:
        data = dataset.load_portuguese()
    X = data.data
    y = data.target
    return X, y

X, y = get_dataset(dataset_name)
st.write("shape of dataset", X.shape)
st.write("number of classes", len(np.unique(y)))