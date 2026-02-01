import streamlit as st

# Səhifə konfiqurasiyası
st.set_page_config(page_title="Forex Focus Pro", layout="wide")

# Başlıq və Reset düyməsi
col_title, col_reset = st.columns([0.85, 0.15])
with col_title:
    st.title("🏛️ Market Analysis Terminal")
with col_reset:
    if st.button("🔄 Reset"):
        st.rerun()

# --- 1. Sadə və Rəngsiz Checklist ---
st.subheader("📝 Analiz Checklist")
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.write("**Forecast Poll**")
    st.radio("F", ["Wait", "Long", "Short"], label_visibility="collapsed", horizontal=True, key="r1")
with c2:
    st.write("**Technical**")
    st.radio("T", ["Wait", "Long", "Short"], label_visibility="collapsed", horizontal=True, key="r2")
with c3:
    st.write("**Weekly**")
    st.radio("W", ["Wait", "Long", "Short"], label_visibility="collapsed", horizontal=True, key="r3")
with c4:
    st.write("**Sentiment**")
    st.radio("S", ["Wait", "Long", "Short"], label_visibility="collapsed", horizontal=True, key="r4")

st.markdown("---")

# --- 2. Bazarın Texniki Vəziyyəti ---
st.subheader("📈 Market Technical View")
tabs = st.tabs(["💱 Forex", "🌕 Metallar & Enerji", "📊 İndekslər"])

with tabs[0]:
    st.components.v1.html("""<iframe src="https://www.widgets.investing.com/live-currency-cross-rates?theme=darkTheme&pairs=1,2,3,5,7,8,4,6" width="100%" height="400" frameborder="0"></iframe>""", height=410)

with tabs[1]:
    st.components.v1.html("""<iframe src="https://www.widgets.investing.com/live-commodities?theme=darkTheme&pairs=8830,8836,8849,8833,8862" width="100%" height="400" frameborder="0"></iframe>""", height=410)

with tabs[2]:
    st.components.v1.html("""<iframe src="https://www.widgets.investing.com/indices-summary?theme=darkTheme&pairs=14958,166,172,169" width="100%" height="400" frameborder="0"></iframe>""", height=410)

st.markdown("---")

# --- 3. Checklist Ardıcıllığına Uyğun Linklər ---
st.subheader("🔗 Essential Links")

# Linklər checklist-dəki 1, 2, 3, 4 sırasına uyğun düzüldü
st.markdown("**1. Forecast Poll:** [Mitrade Analysis](https://www.mitrade.com/en/financial-tools/Forecast)")
st.markdown("**2. Technical:** (Yuxarıdakı cədvəllərə baxın)")
st.markdown("**3. Weekly:** [DailyForex Forecast](https://www.dailyforex.com/forex-technical-analysis/weekly-forex-forecast/page-1)")
st.markdown("**4. Sentiment:** [FXSSI Current Ratio](https://fxssi.com/tools/current-ratio?filter=EURUSD)")
