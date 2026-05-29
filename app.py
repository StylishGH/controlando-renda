import streamlit as st

# Configuração da página
st.set_page_config(page_title="Gestão Financeira", layout="centered")

st.title("💰 Controle Financeiro Familiar")

# Configurações de metas (input do usuário para não deixar valores expostos no código)
st.sidebar.header("Configurações")
meta_salario = st.sidebar.number_input("Definir Salário Fixo (R$)", min_value=0.0, value=0.0, step=100.0)
meta_custos = st.sidebar.number_input("Definir Custos Fixos (R$)", min_value=0.0, value=0.0, step=100.0)

# Input de entrada do mês
st.header("Entrada de Valores")
renda_mes = st.number_input("Quanto entrou de dinheiro no total este mês? (R$)", min_value=0.0, step=100.0)

# Lógica de cálculo
meta_total = meta_salario + meta_custos
sobra = renda_mes - meta_total

st.divider()

if renda_mes > 0:
    if renda_mes < meta_total:
        st.error(f"⚠️ Atenção! Renda insuficiente. Faltam R$ {abs(sobra):.2f} para cobrir as metas.")
    else:
        st.success(f"✅ Mês positivo! Reserva de Emergência garantida: R$ {sobra:.2f}")
        st.info(f"Saldo disponível para gastos pessoais: **R$ {meta_salario:.2f}**")
    
    # Barra de progresso visual
    if meta_total > 0:
        progresso = min(renda_mes / meta_total, 1.0)
        st.progress(progresso)
        st.write(f"Progresso da meta: {(progresso * 100):.1f}%")
else:
    st.write("Aguardando entrada de valores...")
