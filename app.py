import streamlit as st

st.set_page_config(page_title="Forex Strategy Dashboard", layout="wide")

# Səhifəni yeniləyəndə işarələrin silinməsi üçün "Session State" yaradırıq
if 'check_reset' not in st.session_state:
    st.session_state.check_reset = False

def reset_checks():
    st.session_state.check_reset = True

st.title("📊 Forex Strategy Dashboard & Checklist")
st.write("Mənbələri analiz edin və öz qeydlərinizi götürün.")

# --- Checklist Bölməsi (Yuxarıda Sabit) ---
st.subheader("📝 Şəxsi Analiz Qeydlərim")
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("**1. Forecast Poll**")
    f_l = st.checkbox("Long", key="f1")
    f_s = st.checkbox("Short", key="f2")

with c2:
    st.markdown("**2. Technical Summary**")
    t_l = st.checkbox("Long", key="t1")
    t_s = st.checkbox("Short", key="t2")

with c3:
    st.markdown("**3. Weekly Forecast**")
    w_l = st.checkbox("Long", key="w1")
    w_s = st.checkbox("Short", key="w2")

with c4:
    st.markdown("**4. Sentiment**")
    s_l = st.checkbox("Long", key="s1")
    s_s = st.checkbox("Short", key="s2")

# Silmə düyməsi
if st.button("Seçimləri Təmizlə (Reset)"):
    st.rerun() # Səhifəni yeniləyərək bütün checkbox-ları sıfırlayır

st.markdown("---")

# --- Mənbələr Bölməsi ---

# 1. Forecast Poll (Mitrade)
st.subheader("🎯 1. Forecast Poll")
st.markdown("[👉 Mitrade Forecast Poll-a Get](https://www.mitrade.com/en/financial-tools/Forecast)")

# 2. Technical Summary (Investing.com Widget)
st.subheader("📈 2. Technical Summary")
st.components.v1.html("""
    <iframe src="https://www.widgets.investing.com/live-currency-cross-rates?theme=darkTheme&pairs=1,2,3,4,5,7,8,9,10" 
    width="100%" height="400" frameborder="0" allowtransparency="true" marginwidth="0" marginheight="0"></iframe>
""", height=420)

# 3 & 4 Yan-yana
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📅 3. Weekly Forecast")
    st.markdown("[👉 DailyForex Weekly Forecast](https://www.dailyforex.com/forex-technical-analysis/weekly-forex-forecast/page-1)")

with col_right:
    st.subheader("👥 4. Sentiment")
    st.markdown("[👉 FXSSI Sentiment Ratio](https://fxssi.com/tools/current-ratio?filter=EURUSD)")

st.write("---")
st.caption("Qeyd: Checkbox-lar yalnız sizin vizual yaddaşınız üçündür, səhifəni yeniləsəniz sıfırlanacaq.")
