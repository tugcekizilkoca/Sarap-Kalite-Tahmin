# 🍷 Wine Quality Classification

Bu proje, **kırmızı şarap kimyasal özelliklerini** kullanarak şarap kalitesini
**ikili sınıflandırma (iyi / kötü)** problemi olarak tahmin etmeyi amaçlamaktadır.

Veri seti üzerinde farklı **Makine Öğrenmesi** ve **Derin Öğrenme** modelleri
karşılaştırılmış, performansları detaylı metriklerle analiz edilmiştir.

---

## 📊 Veri Seti
- **Kaynak:** UCI Wine Quality Dataset (Red Wine)
- **Gözlem sayısı:** 1599
- **Özellik sayısı:** 11
- **Hedef değişken:** `quality_label`
  - `1` → İyi kalite (quality ≥ 7)
  - `0` → Düşük / Orta kalite

---

## ⚙️ Kullanılan Modeller
- Logistic Regression  
- Decision Tree  
- Random Forest  
- Gradient Boosting  
- K-Nearest Neighbors (KNN)  
- **MLPClassifier (Neural Network)** ⭐

---

## 🔀 Veri Bölme (Hold-Out)
Veri seti aşağıdaki şekilde ayrılmıştır:

- **%80 Eğitim**
- **%20 Test**
- Stratified split (sınıf dengesi korunmuştur)

---

## 📈 Değerlendirme Metrikleri
Her model için aşağıdaki metrikler hesaplanmıştır:

- Accuracy
- Precision
- Recall
- Specificity
- F1-Score
- ROC Curve & AUC
- Confusion Matrix
- 5-Fold Cross Validation
- McNemar Testi (model karşılaştırması)

---

## 🏆 Sonuçlar (Test Seti)

| Model | Accuracy |
|------|----------|
| Logistic Regression | 0.8938 |
| Decision Tree | 0.8938 |
| Random Forest | **0.9375** |
| Gradient Boosting | 0.9156 |
| KNN | 0.8938 |
| **MLPClassifier** | **0.9344** |

📌 **En iyi model:** `MLPClassifier`  
Model ve scaler dosyaları kaydedilmiştir.

---

## 💾 Kaydedilen Dosyalar
- `best_model.pkl` → Eğitilmiş en iyi model  
- `scaler.pkl` → StandardScaler (ön işleme için)

---

## ▶️ Projeyi Çalıştırma

```bash
pip install -r requirements.txt
