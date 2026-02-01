import streamlit as st

# Səhifə konfiqurasiyası
st.set_page_config(page_title="Forex Focus Terminal", layout="wide")

# Başlıq və Reset düyməsi
col_t, col_r = st.columns([0.85, 0.15])
with col_t:
    st.title("🏛️ Forex Analysis Terminal")
with col_reset if 'col_reset' in locals() else col_r:
    if st.button("🔄 Reset"):
        st.rerun()

# --- 1. Checklist Paneli (4 ayrı bölmə) ---
st.subheader("📝 Analiz Checklist")
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.radio("1. Forecast Poll:", ["Gözlənilir", "Long 🟢", "Short 🔴"], horizontal=True, key="r1")
with c2:
    st.radio("2. Technical:", ["Gözlənilir", "Long 🟢", "Short 🔴"], horizontal=True, key="r2")
with c3:
    st.radio("3. Weekly:", ["Gözlənilir", "Long 🟢", "Short 🔴"], horizontal=True, key="r3")
with c4:
    st.radio("4. Sentiment:", ["Gözlənilir", "Long 🟢", "Short 🔴"], horizontal=True, key="r4")

st.markdown("---")

# --- 2. Technical Summary (Kateqoriyalı) ---
st.subheader("📈 Bazarın Texniki Vəziyyəti")

t1, t2, t3 = st.tabs(["💱 Valyutalar", "🌕 Metallar & Enerji", "📊 İndekslər"])

with t1:
    st.components.v1.html("""
        <iframe src="https://www.widgets.investing.com/live-currency-cross-rates?theme=darkTheme&pairs=1,2,3,5,7,8,4,6,9,10" 
        width="100%" height="450" frameborder="0" allowtransparency="true"></iframe>
    """, height=460)

with t2:
    st.components.v1.html("""
        <iframe src="https://www.widgets.investing.com/live-commodities?theme=darkTheme&pairs=8830,8836,8849,8833,8862" 
        width="100%" height="450" frameborder="0" allowtransparency="true"></iframe>
    """, height=460)

with t3:
    st.components.v1.html("""
        <iframe src="https://www.widgets.investing.com/indices-summary?theme=darkTheme&pairs=14958,166,172,169" 
        width="100%" height="450" frameborder="0" allowtransparency="true"></iframe>
    """, height=460)

st.write("---")

# --- 3. Analiz Linkləri ---
st.subheader("🔗 Əsas Analiz Mənbələri")
l1, l2 = st.columns(2)

with l1:
    st.markdown("🎯 **Forecasts (1 & 3)**")
    st.markdown("[Mitrade Forecast Poll](https://www.mitrade.com/en/financial-tools/Forecast)")
    st.markdown("[DailyForex Weekly](https://www.dailyforex.com/forex-technical-analysis/weekly-forex-forecast/page-1)")

with l2:
    st.markdown("👥 **Sentiment (4)**")
    st.markdown("[FXSSI Sentiment Ratio](https://fxssi.com/tools/current-ratio?filter=EURUSD)")
    
