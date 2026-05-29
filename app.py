import streamlit as st

st.set_page_config(page_title="Gestão Financeira Pro", layout="centered")

st.title("💰 Controle de Metas & Caixinhas")

# Inicialização do estado
if 'total_acumulado' not in st.session_state:
    st.session_state.total_acumulado = 0.0
if 'metas' not in st.session_state:
    # Metas iniciais (prioridades)
    st.session_state.metas = {"Casa": 3000.0, "Reserva": 1000.0, "Lazer": 500.0}

# 1. Entrada de Serviço
st.sidebar.header("Novo Serviço")
valor_servico = st.sidebar.number_input("Quanto ganhou neste serviço?", min_value=0.0, step=50.0)
if st.sidebar.button("Adicionar ao Total"):
    st.session_state.total_acumulado += valor_servico

# 2. Gerenciador de Metas (+)
st.sidebar.divider()
st.sidebar.header("Adicionar Meta (+)")
nova_meta = st.sidebar.text_input("Nome da nova meta (ex: Carro, IPCA+)")
valor_meta = st.sidebar.number_input("Valor total da meta", min_value=0.0)
if st.sidebar.button("Criar Meta"):
    st.session_state.metas[nova_meta] = valor_meta

# 3. Dashboard Principal
st.subheader(f"Total Disponível: R$ {st.session_state.total_acumulado:.2f}")

st.write("### Progresso das suas Caixinhas")

# Lógica de distribuição (Prioridade de cima para baixo)
saldo_restante = st.session_state.total_acumulado

for nome, valor in st.session_state.metas.items():
    # Cálculo de quanto falta para essa meta
    progresso = min(saldo_restante / valor, 1.0) if valor > 0 else 1.0
    
    col1, col2 = st.columns([3, 1])
    col1.write(f"**{nome}**")
    col2.write(f"R$ {min(saldo_restante, valor):.2f} / R$ {valor:.2f}")
    st.progress(progresso)
    
    saldo_restante -= valor
    if saldo_restante < 0: saldo_restante = 0

if st.button("Resetar Mês"):
    st.session_state.total_acumulado = 0.0
    st.rerun()
