import streamlit as st
import pandas as pd
 
# ---------------------------------------------
# Dashboard Cursos Escola Nova Geração
# ---------------------------------------------
 
st.title(" Dashboard Cursos - Escola Nova Geração")
 
# 1. Criando a base de dados
dados = {
    "curso": ["Reforço de Matemática", "Inglês Básico", "Robótica", "Teatro",
                     "Reforço de Potugues", "Espanhol", "Xadrex", "Pintura"],
    "categoria": ["Exatas", "Idiomas", "Tecnologia", "Arte",
                  "Humanas", "Idiomas", "Tecnologia", "Arte"],
    "mensalidade": [120.00, 150.00, 200.00, 100.00, 120.00, 140.00, 90.00, 110.00],
    "carga_horaria": [4, 3, 5, 2, 4, 3, 2, 3],
    "avaliacao": [4.7, 4.3, 4.9, 4.5, 4.2, 4.4, 4.6, 4.8]
}
df = pd.DataFrame(dados)

# 2. Filtros na barra lateral
st.sidebar.title("Filtros")
 
categoria_escolhida = st.sidebar.selectbox(
    "categoria:",
    ["Todas"] + list(df["categoria"].unique())
)
 
valor_maximo = st.sidebar.slider(
    "Valor máximo do mensalidade (R$):",
    min_value=float(df["mensalidade"].min()),
    max_value=float(df["mensalidade"].max()),
    value=float(df["mensalidade"].max())
)
 
# 3. Aplicando os filtros
df_filtrado = df[df["mensalidade"] <= valor_maximo]
 
if categoria_escolhida != "Todas":
    df_filtrado = df_filtrado[df_filtrado["categoria"] == categoria_escolhida]

# 4. Mostrando a tabela filtrada
st.subheader("Cursos filtrados")
st.dataframe(df_filtrado)
 
# 5. Métricas
col1, col2 = st.columns(2)
 
faturamento_total = df_filtrado["mensalidade"].sum()
avaliacao_media = df_filtrado["avaliacao"].mean() if len(df_filtrado) > 0 else 0
 
col1.metric("Faturamento total", f"R$ {faturamento_total:.2f}")
col2.metric("Avaliação média", f"{avaliacao_media:.1f} ")
 
# 6. Gráfico
st.subheader("Valor total por Curso")
 
if len(df_filtrado) > 0:
    valor_por_restaurante = df_filtrado.groupby("curso")["mensalidade"].sum()
    st.bar_chart(valor_por_restaurante)
else:
    st.write("Nenhum curso encontrado com esse filtro.")