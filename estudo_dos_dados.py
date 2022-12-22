import pandas as pd

dados_por = pd.read_csv("dados/Portuguese.csv")
dados_mat = pd.read_csv("dados/Maths.csv")

shape_por = dados_por.shape
shape_mat = dados_mat.shape

#print(shape_por, shape_mat)

#print(dados_por.head(), dados_mat.head())


#transformando os dados de YES E NO para 1 e 0 para a dados_por

traducao_dic = {'yes': 1, 'no': 0}
dadosmodificados = dados_por[['schoolsup','famsup','paid','activities','nursery','higher','internet','romantic']].replace(traducao_dic)
dadosmodificados.head()