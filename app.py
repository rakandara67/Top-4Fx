import streamlit as st

# Səhifə ayarları
st.set_page_config(page_title="Forex Focus Pro", layout="wide")

# Reset düyməsi və Başlıq
col_title, col_reset = st.columns([0.85, 0.15])
with col_title:
    st.title("🏛️ Market Analysis Terminal")
with col_reset:
    if st.button("🔄 Reset"):
        st.rerun()

# --- 1. Rəngsiz və 4 Sütunlu Checklist ---
st.subheader("📝 Analiz Checklist")
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.write("**1. Forecast**")
    st.radio("F", ["Wait", "Long", "Short"], label_visibility="collapsed", horizontal=True, key="r1")
with c2:
    st.write("**2. Technical**")
    st.radio("T", ["Wait", "Long", "Short"], label_visibility="collapsed", horizontal=True, key="r2")
with c3:
    st.write("**3. Weekly**")
    st.radio("W", ["Wait", "Long", "Short"], label_visibility="collapsed", horizontal=True, key="r3")
with c4:
    st.write("**4. Sentiment**")
    st.radio("S", ["Wait", "Long", "Short"], label_visibility="collapsed", horizontal=True, key="r4")

st.markdown("---")

# --- 2. Technical Summary (Kateqoriyalı Tablar) ---
st.subheader("📈 Market Technical View")
tabs = st.tabs(["💱 Forex", "🌕 Commodities", "📊 Indices"])

with tabs[0]:
    st.components.v1.html("""
        <iframe src="https://www.widgets.investing.com/live-currency-cross-rates?theme=darkTheme&pairs=1,2,3,5,7,8,4,6" 
        width="100%" height="400" frameborder="0"></iframe>
    """, height=410)

with tabs[1]:
    st.components.v1.html("""
        <iframe src="https://www.widgets.investing.com/live-commodities?theme=darkTheme&pairs=8830,8836,8849,8833,8862" 
        width="100%" height="400" frameborder="0"></iframe>
    """, height=410)

with tabs[2]:
    st.components.v1.html("""
        <iframe src="https://www.widgets.investing.com/indices-summary?theme=darkTheme&pairs=14958,166,172,169" 
        width="100%" height="400" frameborder="0"></iframe>
    """, height=410)

st.markdown("---")

# --- 3. Qalan Əsas Analiz Linkləri ---
st.subheader("🔗 Essential Links")
l1, l2 = st.columns(2)

with l1:
    st.markdown("🎯 **Forecasts (1 & 3)**")
    st.markdown("[Mitrade Forecast Poll](https://www.mitrade.com/en/financial-tools/Forecast)")
    st.markdown("[DailyForex Weekly Forecast](https://www.dailyforex.com/forex-technical-analysis/weekly-forex-forecast/page-1)")

with l2:
    st.markdown("👥 **Sentiment (4)**")
    st.markdown("[FXSSI Sentiment Ratio](https://fxssi.com/tools/current-ratio?filter=EURUSD)")
    
