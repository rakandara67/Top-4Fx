import streamlit as st

# Səhifə konfiqurasiyası
st.set_page_config(page_title="Forex Focus Pro", layout="wide")

# Başlıq və Reset düyməsi (Yuxarıda minimalist düzülüş)
col_t, col_r = st.columns([0.85, 0.15])
with col_t:
    st.title("🏛️ Market Analysis Terminal")
with col_r:
    if st.button("🔄 Reset"):
        st.rerun()

# --- 1. Rəngsiz və Minimalist Checklist ---
st.subheader("📝 Analiz Checklist")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.write("**Forecast**")
    st.radio("F", ["Gözlə", "Long", "Short"], label_visibility="collapsed", horizontal=True, key="r1")
with c2:
    st.write("**Technical**")
    st.radio("T", ["Gözlə", "Long", "Short"], label_visibility="collapsed", horizontal=True, key="r2")
with c3:
    st.write("**Weekly**")
    st.radio("W", ["Gözlə", "Long", "Short"], label_visibility="collapsed", horizontal=True, key="r3")
with c4:
    st.write("**Sentiment**")
    st.radio("S", ["Gözlə", "Long", "Short"], label_visibility="collapsed", horizontal=True, key="r4")

st.markdown("---")

# --- 2. Technical Summary (Tablar vasitəsilə) ---
st
