import streamlit as st
import numpy as np
import joblib

# Sayfa ayarı
st.set_page_config(page_title="Şarap Kalitesi Tahmini", page_icon="🍷")

st.title("🍷 Şarap Kalitesi Tahmini")
st.write("Kimyasal özelliklere göre şarabın kalitesini tahmin eden makine öğrenmesi uygulaması.")

# Model ve scaler yükleme
try:
    model = joblib.load("best_model.pkl")
    scaler = joblib.load("scaler.pkl")
    st.success("Model başarıyla yüklendi!")
except:
    st.error("❌ Model yüklenemedi! best_model.pkl ve scaler.pkl dosyalarının aynı klasörde olduğundan emin olun.")
    st.stop()

st.subheader("🔎 Şarap Özelliklerini Giriniz")

# Kullanıcı giriş alanları (Türkçe)
fixed_acidity = st.number_input("Sabit Asitlik (Fixed Acidity)", value=7.4)
volatile_acidity = st.number_input("Uçucu Asitlik (Volatile Acidity)", value=0.7)
citric_acid = st.number_input("Sitrik Asit (Citric Acid)", value=0.0)
residual_sugar = st.number_input("Kalıntı Şeker (Residual Sugar)", value=1.9)
chlorides = st.number_input("Klorürler (Chlorides)", value=0.076)
free_sulfur_dioxide = st.number_input("Serbest Kükürt Dioksit (Free SO₂)", value=11)
total_sulfur_dioxide = st.number_input("Toplam Kükürt Dioksit (Total SO₂)", value=34)
density = st.number_input("Yoğunluk (Density)", value=0.9978)
pH = st.number_input("pH Değeri", value=3.51)
sulphates = st.number_input("Sülfatlar (Sulphates)", value=0.56)
alcohol = st.number_input("Alkol Oranı (Alcohol)", value=9.4)

# Tahmin butonu
if st.button("Tahmin Et"):
    user_input = np.array([[fixed_acidity, volatile_acidity, citric_acid,
                            residual_sugar, chlorides, free_sulfur_dioxide,
                            total_sulfur_dioxide, density, pH, sulphates, alcohol]])

    # Scaling
    user_input_scaled = scaler.transform(user_input)

    # Tahmin al
    prediction = model.predict(user_input_scaled)[0]
    probability = model.predict_proba(user_input_scaled)[0][1]  # iyi kalite olasılığı

    st.subheader("🔍 Tahmin Sonucu")

    if prediction == 1:
        st.success(f"🍷 Bu şarap **%{probability*100:.2f} olasılıkla İYİ KALİTE**.")
    else:
        st.error(f"🍷 Bu şarap **%{(1-probability)*100:.2f} olasılıkla KÖTÜ KALİTE**.")
