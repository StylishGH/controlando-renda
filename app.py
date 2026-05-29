import streamlit as st

st.set_page_config(page_title="Gestão de Serviços", layout="centered")

st.title("🛠️ Controle de Serviços e Casa")

# Configurações de metas (Defina aqui ou deixe ele definir)
if 'total_recebido' not in st.session_state:
    st.session_state.total_recebido = 0.0

st.sidebar.header("Configurações")
meta_custos = st.sidebar.number_input("Meta Custo Fixo da Casa (R$)", value=3000.0)

# Entrada de novo serviço
st.header("Novo Serviço Realizado")
nome_servico = st.text_input("Nome do serviço (ex: Manutenção na Rua X)")
valor_servico = st.number_input("Valor recebido (R$)", min_value=0.0, step=50.0)

if st.button("Registrar Serviço"):
    st.session_state.total_recebido += valor_servico
    st.success(f"Serviço '{nome_servico}' registrado com sucesso!")

st.divider()

# Dashboard de Visualização
st.subheader("Status Financeiro do Mês")
col1, col2 = st.columns(2)
col1.metric("Total Acumulado", f"R$ {st.session_state.total_recebido:.2f}")
col2.metric("Meta da Casa", f"R$ {meta_custos:.2f}")

# Lógica de distribuição
if st.session_state.total_recebido >= meta_custos:
    sobra = st.session_state.total_recebido - meta_custos
    st.success(f"✅ Custos da casa cobertos! Sobra livre para uso/reserva: **R$ {sobra:.2f}**")
else:
    falta = meta_custos - st.session_state.total_recebido
    st.warning(f"⚠️ Ainda faltam R$ {falta:.2f} para quitar os custos da casa.")

if st.button("Limpar Mês (Novo Ciclo)"):
    st.session_state.total_recebido = 0.0
    st.rerun()
