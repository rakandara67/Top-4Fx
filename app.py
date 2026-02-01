import streamlit as st

# Səhifə konfiqurasiyası
st.set_page_config(page_title="Forex Forecast Hub", layout="wide")

# Başlıq
st.title("📊 Forex Strategy Dashboard")
st.markdown("Fundamental, Texniki və Sentiment analizlər bir yerdə.")

# Aktiv seçimi (Linkləri dinamik etmək üçün)
symbol = st.sidebar.selectbox("Aktiv seçin:", ["EURUSD", "GBPUSD", "XAUUSD", "BTCUSD", "USDJPY"])

# --- 1. Forecast Poll (Mitrade) ---
st.subheader("🎯 1. Forecast Poll (Fundamental Orta Rəy)")
st.info("Böyük qurumların və analitiklerin qiymət gözləntiləri:")
st.markdown(f"[Mitrade Forecast Poll - {symbol} üçün keçid et](https://www.mitrade.com/en/financial-tools/Forecast)")
# Mitrade birbaşa daxilə yerləşdirməyə (iframe) icazə vermədiyi üçün düymə ən sürətli yoldur.

st.write("---")

# --- 2. Technical Summary (Investing.com) ---
st.subheader("📈 2. Technical Summary (İndikatorlar)")
# Investing.com-un hazır widget-i (Bütün indikatorların səsverməsi)
st.components.v1.html(f"""
    <iframe src="https://www.widgets.investing.com/live-currency-cross-rates?theme=darkTheme&pairs=1,2,3,4,5,7,8,9,10" 
    width="100%" height="400" frameborder="0" allowtransparency="true" marginwidth="0" marginheight="0"></iframe>
""", height=420)

st.write("---")

# --- 3. Weekly Forecast & Sentiment (Yan-yana) ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("📅 3. Weekly Forecast")
    st.write("Həftəlik bazar proqnozları:")
    st.markdown("[DailyForex Weekly Analysis](https://www.dailyforex.com/forex-technical-analysis/weekly-forex-forecast/page-1)")
    st.caption("DailyForex həftəlik strategiyaları bura mütəmadi yüklənir.")

with col2:
    st.subheader("👥 4. Market Sentiment")
    st.write("Real treyderlərin AL/SAT nisbəti:")
    # FXSSI və ya alternativ sentiment linki
    st.markdown(f"[FXSSI Sentiment Ratio - {symbol}](https://fxssi.com/tools/current-ratio?filter={symbol})")
    st.progress(65) # Nümunəvi vizual göstərici
    st.caption("Pərakəndə treyderlərin çoxu hansı tərəfdədir?")

st.write("---")

# Alt Qeyd
st.warning("⚠️ Bu tətbiq yalnız məlumat xarakterlidir. Ticarət qərarlarınızı öz riskinizlə verin.")
