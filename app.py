import streamlit as st

st.set_page_config(page_title="Forex Master Dashboard", layout="wide")

# --- Reset Funksiyası ---
if st.button("🔄 Bütün Analizi Sıfırla (Reset)"):
    st.rerun()

st.title("🏛️ Forex & Market Control Panel")

# --- 1. Checklist Paneli (Minimalist) ---
st.subheader("📝 My Analysis Checklist")
c1, c2, c3, c4 = st.columns(4)
with c1:
    f = st.radio("Forecast Poll:", ["Gözlənilir", "Long 🟢", "Short 🔴"], horizontal=True, key="r1")
with c2:
    t = st.radio("Technical:", ["Gözlənilir", "Long 🟢", "Short 🔴"], horizontal=True, key="r2")
with c3:
    w = st.radio("Weekly:", ["Gözlənilir", "Long 🟢", "Short 🔴"], horizontal=True, key="r3")
with c4:
    s = st.radio("Sentiment:", ["Gözlənilir", "Long 🟢", "Short 🔴"], horizontal=True, key="r4")

st.markdown("---")

# --- 2. Technical Summary (Kateqoriyalı Tab-lar) ---
st.subheader("📈 Technical Summary (Investing.com)")

# Tab-lar vasitəsilə cədvəli qruplaşdırırıq (Siyahı uzanmır)
tab1, tab2, tab3 = st.tabs(["💱 Forex (Majors)", "🌕 Emtia (Qızıl, Neft, Gümüş)", "📊 İndekslər (Nasdaq, S&P)"])

with tab1:
    # Major cütlüklər
    st.components.v1.html("""
        <iframe src="https://www.widgets.investing.com/live-currency-cross-rates?theme=darkTheme&pairs=1,2,3,4,5,7,8,9" 
        width="100%" height="350" frameborder="0" allowtransparency="true"></iframe>
    """, height=360)

with tab2:
    # Qızıl (1), Gümüş (2), WTI (8849), Brent (8833)
    st.components.v1.html("""
        <iframe src="https://www.widgets.investing.com/live-commodities?theme=darkTheme&pairs=8830,8836,8849,8833,8910" 
        width="100%" height="350" frameborder="0" allowtransparency="true"></iframe>
    """, height=360)

with tab3:
    # Nasdaq (14958), S&P 500 (166), DAX (172)
    st.components.v1.html("""
        <iframe src="https://www.widgets.investing.com/indices-summary?theme=darkTheme&pairs=166,14958,172,27" 
        width="100%" height="350" frameborder="0" allowtransparency="true"></iframe>
    """, height=360)

st.write("---")

# --- 3. Digər Analiz Mənbələri ---
col_l, col_r = st.columns(2)

with col_l:
    st.subheader("🎯 Fundamental & Weekly")
    st.markdown("[🔗 Mitrade Forecast Poll](https://www.mitrade.com/en/financial-tools/Forecast)")
    st.markdown("[🔗 DailyForex Weekly Forecast](https://www.dailyforex.com/forex-technical-analysis/weekly-forex-forecast/page-1)")

with col_r:
    st.subheader("👥 Sentiment & News")
    st.markdown("[🔗 FXSSI Sentiment Ratio](https://fxssi.com/tools/current-ratio?filter=EURUSD)")
    st.markdown("[🔗 FXStreet News](https://www.fxstreet.com/news)")

# --- 4. Yekun Qərar İndikatoru ---
st.write("---")
if "🔴" in f+t+w+s and "🟢" not in f+t+w+s:
    st.error("🚨 YEKUN QƏRAR: GÜCLÜ SATIŞ (STRONG SELL)")
elif "🟢" in f+t+w+s and "🔴" not in f+t+w+s:
    st.success("🚀 YEKUN QƏRAR: GÜCLÜ ALIŞ (STRONG BUY)")
elif "🟢" in f+t+w+s and "🔴" in f+t+w+s:
    st.warning("⚖️ YEKUN QƏRAR: QARIŞIQ SİQNALLAR (GÖZLƏ)")
else:
    st.info("💡 Analiz tamamlanmayıb...")
    
