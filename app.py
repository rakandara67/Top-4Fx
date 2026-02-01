import streamlit as st

st.set_page_config(page_title="Forex Focus Terminal", layout="wide")

# Reset düyməsi yuxarı sağ küncdə minimalist şəkildə
col_head, col_res = st.columns([0.9, 0.1])
with col_res:
    if st.button("🔄 Reset"):
        st.rerun()

st.title("🏛️ Forex Analysis Terminal")

# --- 1. Checklist Paneli (Radio düymələri ilə daha səliqəli) ---
st.subheader("📝 Analiz Checklist")
c1, c2, c3 = st.columns(3)
with c1:
    f = st.radio("Forecast Poll:", ["Gözlənilir", "Long 🟢", "Short 🔴"], horizontal=True, key="r1")
with c2:
    t = st.radio("Technical:", ["Gözlənilir", "Long 🟢", "Short 🔴"], horizontal=True, key="r2")
with c3:
    s = st.radio("Sentiment/Weekly:", ["Gözlənilir", "Long 🟢", "Short 🔴"], horizontal=True, key="r4")

st.markdown("---")

# --- 2. Təkmilləşdirilmiş Technical Summary (Investing.com) ---
st.subheader("📈 Bazarın Texniki Vəziyyəti")

# Kateqoriyalar üzrə ayrılmış minimalist cədvəllər
tab1, tab2, tab3 = st.tabs(["💱 Əsas Valyutalar", "🌕 Metallar & Enerji", "📊 İndekslər & CFD"])

with tab1:
    # EURUSD, GBPUSD, USDJPY, AUDUSD, USDCAD, NZDUSD, USDCHF
    st.components.v1.html("""
        <iframe src="https://www.widgets.investing.com/live-currency-cross-rates?theme=darkTheme&pairs=1,2,3,5,7,8,4" 
        width="100%" height="400" frameborder="0" allowtransparency="true"></iframe>
    """, height=410)

with tab2:
    # Qızıl (8830), Gümüş (8836), WTI Neft (8849), Brent (8833), Təbii Qaz (8862)
    st.components.v1.html("""
        <iframe src="https://www.widgets.investing.com/live-commodities?theme=darkTheme&pairs=8830,8836,8849,8833,8862" 
        width="100%" height="400" frameborder="0" allowtransparency="true"></iframe>
    """, height=410)

with tab3:
    # US Tech 100 (Nasdaq), US 500 (S&P), DAX (Germany 40), US 30 (Dow)
    st.components.v1.html("""
        <iframe src="https://www.widgets.investing.com/indices-summary?theme=darkTheme&pairs=14958,166,172,169" 
        width="100%" height="400" frameborder="0" allowtransparency="true"></iframe>
    """, height=410)

st.write("---")

# --- 3. Analiz Mənbələri (Yalnız Linklər) ---
st.subheader("🔗 Faydalı Linklər")
l1, l2, l3 = st.columns(3)

with l1:
    st.markdown("🎯 **Forecasts**")
    st.markdown("[Mitrade Forecast Poll](https://www.mitrade.com/en/financial-tools/Forecast)")
    st.markdown("[DailyForex Weekly](https://www.dailyforex.com/forex-technical-analysis/weekly-forex-forecast/page-1)")

with l2:
    st.markdown("👥 **Psychology**")
    st.markdown("[FXSSI Sentiment Ratio](https://fxssi.com/tools/current-ratio?filter=EURUSD)")
    st.markdown("[Myfxbook Outlook](
    
