import streamlit as st

st.set_page_config(page_title="Gestão Financeira Pro", layout="wide")

st.title("💰 Controle Financeiro Familiar 360º")

# Inicialização dos estados (memória do app)
if 'servicos' not in st.session_state: st.session_state.servicos = []
if 'gastos' not in st.session_state: st.session_state.gastos = []

# --- CONFIGURAÇÃO DE METAS (Editável na tela) ---
st.sidebar.header("⚙️ Configurar Metas do Mês")
meta_casa = st.sidebar.number_input("Meta: Casa (R$)", value=3000.0)
meta_reserva = st.sidebar.number_input("Meta: Reserva (R$)", value=1000.0)
meta_lazer = st.sidebar.number_input("Meta: Lazer (R$)", value=500.0)
meta_invest = st.sidebar.number_input("Meta: Carro/Investimento (R$)", value=500.0)

# Dicionário de metas dinâmico
metas = {"Casa": meta_casa, "Reserva": meta_reserva, "Lazer": meta_lazer, "Investimento": meta_invest}

# --- ENTRADAS E GASTOS ---
st.sidebar.divider()
st.sidebar.header("Fluxo de Caixa")

# Registrar Serviço
s_nome = st.sidebar.text_input("Serviço (ex: Rua Vênus)")
s_val = st.sidebar.number_input("Valor Recebido (R$)", min_value=0.0)
if st.sidebar.button("Lançar Entrada"):
    st.session_state.servicos.append({"nome": s_nome, "recebido": s_val})

# Registrar Gasto
g_desc = st.sidebar.text_input("Gasto (ex: Material, Gasolina)")
g_val = st.sidebar.number_input("Valor Gasto (R$)", min_value=0.0)
if st.sidebar.button("Lançar Gasto"):
    st.session_state.gastos.append({"desc": g_desc, "valor": g_val})

# --- CÁLCULOS ---
total_recebido = sum(s['recebido'] for s in st.session_state.servicos)
total_gasto = sum(g['valor'] for g in st.session_state.gastos)
saldo_livre = total_recebido - total_gasto

# --- DASHBOARD ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Resumo do Mês")
    st.metric("Total Entradas", f"R$ {total_recebido:.2f}")
    st.metric("Total Gastos", f"R$ {total_gasto:.2f}")
    st.metric("Saldo Líquido", f"R$ {saldo_livre:.2f}")
    
    st.subheader("Lista de Gastos")
    st.write(st.session_state.gastos)

with col2:
    st.subheader("Distribuição do Saldo")
    saldo_para_distribuir = saldo_livre
    for nome, valor in metas.items():
        alocado = min(max(saldo_para_distribuir, 0), valor)
        st.write(f"**{nome}**: R$ {alocado:.2f} / R$ {valor:.2f}")
        progresso = min(alocado / valor, 1.0) if valor > 0 else 0
        st.progress(progresso)
        saldo_para_distribuir -= alocado

if st.button("Zerar Mês"):
    st.session_state.servicos = []
    st.session_state.gastos = []
    st.rerun()
