import streamlit as st
import pandas as pd

# Başlangıç verileri (ortam ve tutar)
data = {
    "Ortam": [
        "ata", "enpara", "akbank", "midas", "akbnk", 
        "ykb", "dvz", "ozlem_ykb", "ozlemata", "obaba_hisse", "bes"
    ],
    "Tutar": [
        2750000, 500000, 4200000, 280000, 1000,
        280000, 200000, 30000, 580000, 300000, 1100000
    ]
}

# DataFrame oluştur
df = pd.DataFrame(data)

st.title("💰 Param Nerede?")

# Düzenlenebilir tablo
edited_df = st.data_editor(df, num_rows="dynamic")

# Toplam hesapla
total = edited_df["Tutar"].sum()

st.subheader("📊 Toplam Para")
st.metric(label="Toplam", value=f"{total:,.0f} ₺")
