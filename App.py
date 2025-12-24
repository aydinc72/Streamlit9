import streamlit as st
import pandas as pd
import io

st.set_page_config(
    page_title="Para Takip",       # Ana ekrana eklendiğinde görünen isim
    page_icon="💵"                 # İkon olarak kullanılacak emoji veya resim
)

# Başlangıç verileri (default)
default_data = {
    "Ortam": [
        "ata", "enpara", "akbank", "midas",  
        "ykb", "dvz", "ozlem_ykb", "ozlemata", "aylin_hisse", "bes"
    ],
    "Tutar": [
        4100000, 700000, 2200000, 2360000, 
        320000, 20000, 120000, 1500000, 480000, 1380000
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
