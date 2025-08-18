import streamlit as st
import pandas as pd
import io

# Başlangıç verileri (default)
default_data = {
    "Ortam": [
        "ata", "enpara", "akbank", "midas", "akbnk", 
        "ykb", "dvz", "ozlem_ykb", "ozlemata", "obaba_hisse", "bes"
    ],
    "Tutar": [
        2750000, 500000, 4200000, 280000, 1000,
        280000, 200000, 30000, 580000, 300000, 1100000
    ]
}

st.title("💰 Param Nerede?")

# CSV upload
uploaded_file = st.file_uploader("📂 CSV yükle (Ortam, Tutar)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.DataFrame(default_data)

# Düzenlenebilir tablo
edited_df = st.data_editor(df, num_rows="dynamic")

# Toplam hesapla
total = edited_df["Tutar"].sum()
st.subheader("📊 Toplam Para")
st.metric(label="Toplam", value=f"{total:,.0f} ₺")

# CSV export (download)
csv_buffer = io.StringIO()
edited_df.to_csv(csv_buffer, index=False)
st.download_button(
    label="💾 CSV olarak indir",
    data=csv_buffer.getvalue(),
    file_name="paralar.csv",
    mime="text/csv",
)
