```python
import streamlit as st

st.set_page_config(page_title="Gestão da Casa", page_icon="💰")

# Configurações iniciais
SALARIO_FIXO = 4000.00
CUSTOS_FIXOS = 3000.00

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
