```python
import streamlit as st

st.title("💰 Controle Financeiro")

# O usuário define as metas ao abrir o site, nada fica salvo no código
meta_salario = st.sidebar.number_input("Definir Salário Fixo", value=0.0)
meta_custos = st.sidebar.number_input("Definir Custos Fixos", value=0.0)

renda = st.number_input("Renda do mês", value=0.0)

# O restante da lógica continua igual...

st.title("💰 Controle Financeiro")

renda_mes = st.number_input("Quanto entrou no total este mês?", min_value=0.0, step=100.0)

meta_total = SALARIO_FIXO + CUSTOS_FIXOS
sobra = renda_mes - meta_total

if renda_mes > 0:
    if renda_mes < meta_total:
        st.error(f"⚠️ Atenção! Renda insuficiente. Faltam R$ {abs(sobra):.2f} para as metas.")
    else:
        st.success(f"✅ Mês positivo! Reserva de Emergência: R$ {sobra:.2f}")
        st.info(f"Saldo para gastos pessoais: **R$ {SALARIO_FIXO:.2f}**")
    
    st.progress(min(renda_mes / meta_total, 1.0))
