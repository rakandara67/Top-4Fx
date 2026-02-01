import streamlit as st

# Səhifə konfiqurasiyası
st.set_page_config(page_title="Forex Focus Terminal", layout="wide")

# Reset düyməsi (Yuxarı sağda)
col_title, col_reset = st.columns([0.85, 0.15])
with col_title:
    st.title("🏛️ Forex Analysis Terminal")
with col_reset:
    if st.button("🔄 Reset"):
        st.rerun()

# --- 1. Checklist Paneli ---
st.subheader("📝 Analiz Checklist")
c1, c2, c3 = st.columns(3)
with c1:
    st.radio("Forecast Poll:", ["Gözlənilir", "Long 🟢", "Short 🔴"], horizontal=True, key="r1")
with c2:
    st.radio("Technical Summary:", ["Gözlənilir", "Long 🟢", "Short 🔴"], horizontal=True, key="r2")
with c3:
    st.radio("Sentiment/Weekly:", ["Gözlənilir", "Long 🟢", "Short 🔴"], horizontal=True, key="r3")

st.markdown("---")

# --- 2. Technical Summary (Sizin istədiyiniz geniş siyahı ilə) ---
st.subheader("📈 Bazarın Texniki Vəziyyəti")

tab1, tab2, tab3 = st.tabs(["💱 Valyutalar", "🌕 Metallar & Enerji", "📊 İndekslər"])

with tab1:
    # Forex Majors
    st.components.v1.html("""
        <iframe src="https://www.widgets.investing.com/live-currency-cross-rates?theme=darkTheme&pairs=1,2,3,5,7,8,4,6,9,10" 
        width="100%" height="450" frameborder="0" allowtransparency="true"></iframe>
    """, height=460)

with tab2:
    # Qızıl, Gümüş, Neft (WTI/Brent), Qaz
    st.components.v1.html("""
        <iframe src="https://www.widgets.investing.com/live-commodities?theme=darkTheme&pairs=8830,8836,8849,8833,8862" 
        width="100%" height="450" frameborder="0" allowtransparency="true"></iframe>
    """, height=460)

with tab3:
    # Nasdaq, S&P 500, DAX, Dow Jones
    st.components.v1.html("""
        <iframe src="https://www.widgets.investing.com/indices-summary?theme=darkTheme&pairs=14958,166,172,169" 
        width="100%" height="450" frameborder="
                          
