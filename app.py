import streamlit as st

# Səhifə konfiqurasiyası
st.set_page_config(page_title="Forex Focus Terminal", layout="wide")

# Reset düyməsi (Yuxarı sağda)
col_title, col_reset = st.columns([0.85, 0.15])
with col_title:
    st.title("🏛️ Forex Analysis Terminal")
with col_reset:
    if st.button("🔄 Reset All"):
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

# --- 2. Technical Summary (Kateqoriyalı) ---
st.subheader("📈 Technical Summary (Investing.com)")

tab1, tab2, tab3 = st.tabs(["💱 Forex Majors", "🌕 Commodities", "📊 Indices"])

with tab1:
    # Major Forex Pairs
    st.components.v1.html("""
        <iframe src="https://www.widgets.investing.com/live-currency-cross-rates?theme=darkTheme&pairs=1,2,3,5,7,8,4,6,9,10" 
        width="100%" height="450" frameborder="0" allowtransparency="true" marginwidth="0" marginheight="0"></iframe>
    """, height=460)

with tab2:
    # Gold, Silver, WTI, Brent, Natural Gas, Copper
    st.components.v1.html("""
        <iframe src="https://www.widgets.investing.com/live-commodities?theme=darkTheme&pairs=8830,8836,8849,8833,8862,8831" 
        width="100%" height="450" frameborder="0" allowtransparency="true" marginwidth="0" marginheight="0"></iframe>
    """, height=460)

with tab3:
    # Nasdaq, S&P 500, DAX, Dow 30, US Dollar Index
    st.components.v1.html("""
        <iframe src="https://www.widgets.investing.com/indices-summary?theme=darkTheme&pairs=14958,166,172,169,942611" 
        width="100%" height="450" frameborder="0" allowtransparency="true" marginwidth="0" marginheight="0"></iframe>
    """, height=460)

st.write("---")

# --- 3. Linklər Bölməsi ---
st.subheader("🔗 Analiz Mənbələri")
l1, l2, l3 = st.columns(3)

with l1:
    st.markdown("🎯 **Forecasts**")
    st.markdown("[Mitrade Forecast Poll](https://www.mitrade.com/en/financial-tools/Forecast)")
    st.markdown("[DailyForex Weekly](https://www.dailyforex.com/forex-technical-analysis/weekly-forex-forecast/page-1)")

with l2:
    st.markdown("👥 **Sentiment**")
    st.markdown("[FXSSI Sentiment Ratio](https://fxssi.com/tools/current-ratio?filter=EURUSD)")
    st.markdown("[Myfxbook Outlook](https://www.myfxbook.com/community/outlook)")

with l3:
    st.markdown("📅 **Utility**")
    st.markdown("[Investing Economic Calendar](https://www.investing.com/economic-calendar/)")
    st.markdown("[Market Hours](https://www.forexfactory.com/market)")
    
