import streamlit as st

# Səhifə konfiqurasiyası
st.set_page_config(page_title="Forex Focus Pro", layout="wide")

# Reset düyməsini yuxarıda daha kiçik edirik
col_t, col_r = st.columns([0.8, 0.2])
with col_t:
    st.title("🏛️ Market Analysis Terminal")
with col_r:
    if st.button("🔄 Reset"):
        st.rerun()

# --- 1. Səliqəli Analiz Paneli ---
st.subheader("📝 Analiz Checklist")

# Daha az yer tutan yan-yana radio düymələr
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.write("**Forecast**")
    st.radio("F", ["Wait", "L 🟢", "S 🔴"], label_visibility="collapsed", horizontal=True, key="r1")
with c2:
    st.write("**Technical**")
    st.radio("T", ["Wait", "L 🟢", "S 🔴"], label_visibility="collapsed", horizontal=True, key="r2")
with c3:
    st.write("**Weekly**")
    st.radio("W", ["Wait", "L 🟢", "S 🔴"], label_visibility="collapsed", horizontal=True, key="r3")
with c4:
    st.write("**Sentiment**")
    st.radio("S", ["Wait", "L 🟢", "S 🔴"], label_visibility="collapsed", horizontal=True, key="r4")

st.markdown("---")

# --- 2. Technical Summary (Tablar vasitəsilə minimalist görünüş) ---
st.subheader("📈 Market Technical View")

tabs = st.tabs(["💱 Forex", "🌕 Commodities", "📊 Indices"])

with tabs[0]:
    # Forex Majors
    st.components.v1.html("""
        <iframe src="https://www.widgets.investing.com/live-currency-cross-rates?theme=darkTheme&pairs=1,2,3,5,7,8,4,6" 
        width="100%" height="400" frameborder="0"></iframe>
    """, height=410)

with tabs[1]:
    # Metals & Oil
    st.components.v1.html("""
        <iframe src="https://www.widgets.investing.com/live-commodities?theme=darkTheme&pairs=8830,8836,8849,8833,8862" 
        width="100%" height="400" frameborder="0"></iframe>
    """, height=410)

with tabs[2]:
    # Indices
    st.components.v1.html("""
        <iframe src="https://www.widgets.investing.com/indices-summary?theme=darkTheme&pairs=14958,166,172,169" 
        width="100%" height="400" frameborder="0"></iframe>
    """, height=410)

st.write("---")

# --- 3. Analiz Linkləri (Minimalist Linklər) ---
st.subheader("🔗 Essential Links")
l1, l2 = st.columns(2)

with l1:
    st.markdown("[🎯 Mitrade Forecast Poll](https://www.mitrade.com/en/financial-tools/Forecast)")
    st.markdown("[📅 DailyForex Weekly Forecast](https://www.dailyforex.com/forex-technical-analysis/weekly-forex-forecast/page-1)")

with l2:
    st.markdown("[👥 FXSSI Sentiment Ratio](https://fxssi.com/tools/current-ratio?filter=EURUSD)")
    st.markdown("[📊 TradingView Chart](https://www.tradingview.com/chart/)")
    
