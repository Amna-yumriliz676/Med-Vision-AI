# 💊 MediScan AI

An AI-powered medicine safety app that reads prescriptions, verifies medicines, checks drug interactions, and finds verified pharmacies.

## ✨ Features

- 📸 **Prescription Reader** — Upload prescription photo, AI extracts medicine names using OCR
- 💊 **Medicine Verifier** — Verify medicines by barcode or name against our database
- ⚗️ **Drug Interaction Checker** — Check if two medicines are safe together
- 🏪 **Verified Pharmacy Finder** — Find DRAP-registered pharmacies near you
- 💾 **Medicine Database** — Browse 12+ verified medicines with full details

## 🚀 Deploy on Streamlit Cloud (Free)

1. **Push this project to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "MediScan AI"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/mediscan-ai.git
   git push -u origin main
   ```

2. **Go to [share.streamlit.io](https://share.streamlit.io)**

3. Click **"New app"** → Select your repo → `app.py` → **Deploy**

4. App live in 2-3 minutes! 🎉

## 🧑‍💻 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

**Note:** Tesseract OCR needs to be installed:
- **Windows:** [Download here](https://github.com/UB-Mannheim/tesseract/wiki)
- **Mac:** `brew install tesseract`
- **Linux:** `sudo apt install tesseract-ocr`

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Streamlit |
| OCR | Tesseract (pytesseract) |
| Image Processing | Pillow |
| Data | Pandas |
| Deployment | Streamlit Cloud |

## 📁 Project Structure

```
mediscan-ai/
├── app.py              # Main app
├── database.py         # Medicine + interaction data
├── ocr_utils.py        # Prescription OCR
├── verifier.py         # Medicine verification
├── requirements.txt
├── packages.txt        # System deps
└── README.md
```

## ⚠️ Disclaimer

**Educational purposes only.** Not a substitute for professional medical advice. Always consult a licensed doctor or pharmacist before taking any medicine.

## 📄 License

MIT
