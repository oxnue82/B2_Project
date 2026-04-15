# 🌿 Agricare - AI-Powered Crop Disease Detection System

# Authors
  -  K. RaviTeja (Y22ACS479)
  -  A. Suresh (Y22ACS414)
  -  J. Meena (Y22ACS466)
  -  G. RamTeja (L22ACS599)

Agricare is a full-stack web application that uses deep learning to detect diseases in crop leaves and recommend suitable treatments. Users can upload images of crop leaves and receive real-time predictions along with product recommendations.

---

## 🚀 Features

* 🌱 Multi-crop disease detection (Chilli, Cotton, Maize, Rice)
* 📷 Upload leaf images for instant analysis
* 🤖 AI-powered predictions using CNN models
* 📊 Real-time disease detection results
* 🛍️ Product recommendations based on detected disease
* 🖼️ Live preview of uploaded images
* 💻 Responsive UI built with Tailwind CSS

---

## 🧠 Machine Learning

* Separate CNN models trained for each crop
* Image preprocessing (224x224 resizing, normalization)
* Built using TensorFlow/Keras
* Models saved as `.h5` and integrated into Flask backend
* Training implemented using Jupyter Notebooks

---

## 🛠️ Tech Stack

* **Frontend:** HTML, Tailwind CSS, JavaScript
* **Backend:** Flask (Python)
* **Machine Learning:** TensorFlow / Keras
* **Tools:** Jupyter Notebook

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/agricare.git
cd agricare
```

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
python app.py
```

### 5️⃣ Open in Browser

```
http://127.0.0.1:7103/
```

---

## 📌 Usage

1. Select a crop (Chilli, Cotton, Maize, Rice)
2. Upload a leaf image
3. Click **Predict Disease**
4. View prediction results
5. Check recommended products

---

## 🧪 Future Improvements

* Add more crop support
* Improve model accuracy with larger datasets
* Deploy using cloud platforms (AWS/Heroku)
* Add user authentication system
* Mobile app integration

---

## 📄 License

This project is for Academic Purpose.

---

## 🙌 Acknowledgements

* TensorFlow & Keras for ML framework
* Tailwind CSS for UI design
* Open-source agricultural datasets
