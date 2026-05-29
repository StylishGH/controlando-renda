import streamlit as st

st.set_page_config(page_title="Gestão Financeira Pro", layout="wide")

st.title("📊 Controle de Serviços & Gastos")

# Inicialização
if 'servicos' not in st.session_state: st.session_state.servicos = []
if 'gastos' not in st.session_state: st.session_state.gastos = [] # Lista de despesas

# --- SIDEBAR: Lançamento de Entradas (Serviços) ---
with st.sidebar:
    st.header("1. Entradas (Serviços)")
    nome = st.text_input("Serviço")
    valor_total = st.number_input("Valor Total (R$)", min_value=0.0)
    recebido = st.number_input("Quanto entrou agora (R$)", min_value=0.0)
    if st.button("Lançar Entrada"):
        st.session_state.servicos.append({"nome": nome, "recebido": recebido})
        st.rerun()

# --- CÁLCULO DE SALDO ---
total_recebido = sum(s['recebido'] for s in st.session_state.servicos)
total_gasto = sum(g['valor'] for g in st.session_state.gastos)
saldo_atual = total_recebido - total_gasto

# --- LADO DIREITO: Gastos & Dashboard ---
col_dash, col_gastos = st.columns([1, 1])

with col_dash:
    st.subheader(f"Saldo Disponível: R$ {saldo_atual:.2f}")
    st.metric("Total Entradas", f"R$ {total_recebido:.2f}")
    st.metric("Total Saídas", f"R$ {total_gasto:.2f}")

with col_gastos:
    st.subheader("2. Lançar Gastos")
    desc_gasto = st.text_input("O que foi gasto? (ex: Peças, Gasolina)")
    valor_gasto = st.number_input("Valor do gasto (R$)", min_value=0.0)
    if st.button("Lançar Gasto"):
        st.session_state.gastos.append({"desc": desc_gasto, "valor": valor_gasto})
        st.rerun()

# --- RESUMO DE GASTOS ---
st.divider()
st.subheader("Para onde o dinheiro está indo?")
for g in st.session_state.gastos:
    st.write(f"- {g['desc']}: **R$ {g['valor']:.2f}**")

# --- VISUALIZAÇÃO DE FLUXO ---
