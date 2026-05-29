import streamlit as st

st.set_page_config(page_title="Gestão Familiar Pro", layout="wide")

st.title("💰 Controle Financeiro Familiar 360º")

# Inicialização dos Estados
if 'servicos' not in st.session_state: st.session_state.servicos = []
if 'gastos' not in st.session_state: st.session_state.gastos = []
if 'metas' not in st.session_state: 
    st.session_state.metas = {"Casa": 3000.0, "Reserva": 1000.0, "Lazer": 500.0}

# --- CÁLCULOS ---
total_recebido = sum(s['recebido'] for s in st.session_state.servicos)
total_gasto = sum(g['valor'] for g in st.session_state.gastos)
saldo_livre = total_recebido - total_gasto

# --- LADO ESQUERDO: Entradas e Gastos ---
with st.sidebar:
    st.header("Fluxo de Caixa")
    
    st.subheader("Registrar Serviço")
    s_nome = st.text_input("Serviço (ex: Rua Vênus)")
    s_val = st.number_input("Valor Recebido (R$)", min_value=0.0)
    if st.button("Lançar Serviço"):
        st.session_state.servicos.append({"nome": s_nome, "recebido": s_val})
        st.rerun()

    st.subheader("Registrar Gasto")
    g_desc = st.text_input("Gasto (ex: Almoço, Peça)")
    g_val = st.number_input("Valor Gasto (R$)", min_value=0.0)
    if st.button("Lançar Gasto"):
        st.session_state.gastos.append({"desc": g_desc, "valor": g_val})
        st.rerun()

# --- LADO DIREITO: Dashboard e Metas ---
col1, col2 = st.columns(2)

with col1:
    st.metric("Total Entradas", f"R$ {total_recebido:.2f}")
    st.metric("Total Gastos", f"R$ {total_gasto:.2f}")
    st.info(f"### Saldo para Metas: R$ {saldo_livre:.2f}")

with col2:
    st.subheader("Progresso das Metas")
    saldo_para_distribuir = saldo_livre
    for nome, valor in st.session_state.metas.items():
        alocado = min(saldo_para_distribuir, valor)
        st.write(f"**{nome}**: R$ {alocado:.2f} / R$ {valor:.2f}")
        st.progress(min(alocado / valor, 1.0) if valor > 0 else 1.0)
        saldo_para_distribuir -= alocado

# --- RESUMO DE GASTOS ---
st.divider()
st.subheader("Lista de Gastos")
if st.session_state.gastos:
    st.table(st.session_state.gastos)

if st.button("Zerar Mês"):
    st.session_state.servicos = []
    st.session_state.gastos = []
    st.rerun()
