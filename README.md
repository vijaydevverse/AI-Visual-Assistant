# 🧠 AI Visual Assistant (YOLOv8 + Llama 3)

An AI-powered real-time computer vision application that detects objects from a webcam using **YOLOv8** and generates intelligent human-like explanations using **Llama 3 (via Ollama)** with voice output.

---

## 🚀 Features

* 📸 Capture image from webcam using key press
* 🎯 Real-time object detection using YOLOv8
* 🤖 AI-generated explanations using Llama 3 (Ollama)
* 🔊 Text-to-speech voice output
* 🖥️ Live webcam preview
* ⚡ Snapshot-based AI processing (no continuous detection spam)
* 🧠 Lightweight offline AI pipeline

---

## 🧱 Project Structure

```

AI-Visual-Assistant/
│
├── app.py              # Main application (camera + control flow)
├── detector.py         # YOLOv8 object detection logic
├── speaker.py          # Text-to-speech engine
├── config.py           # Configuration settings (optional)
├── yolov8n.pt          # Pretrained YOLO model
├── requirements.txt    # Dependencies
├── .gitignore          # Ignore system files
└── README.md           # Project documentation

````

---

## ⚙️ Installation Guide

### 1. Clone or Download the Project

```bash
git clone https:https://github.com/vijaydevverse/AI-Visual-Assistant
cd AI-Visual-Assistant
````

---

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it:

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Install YOLO Requirements

```bash
pip install ultralytics opencv-python pyttsx3 numpy
```

---

### 5. Install & Run Ollama (Llama 3)

Make sure Ollama is installed:

```bash
ollama run llama3
```

---

## ▶️ Run the Application

```bash
python app.py
```

---

## 🎮 Controls

* **S** → Capture image and analyze objects
* **Q** → Quit application

---

## 🧠 How It Works

1. Webcam captures real-time video
2. User presses **S** to capture frame
3. YOLOv8 detects objects in image
4. Detected objects sent to Llama 3
5. AI generates explanation
6. Voice output speaks the result

---

## 🛠️ Technologies Used

* Python 🐍
* OpenCV 👁️
* Ultralytics YOLOv8 🎯
* Ollama (Llama 3) 🧠
* pyttsx3 🔊
* NumPy 📊

---

## 📌 Future Improvements

* Object tracking across frames
* Click-based object explanation
* Real-time bounding box labels UI
* Streamlit web version (browser-based AI assistant)
* Save detection history
* Faster inference optimization

---

## 👨‍💻 Author

**Vijay Krishnan P.M**

---

## 📜 License

This project is for educational and portfolio purposes.

```
Just say: **next step 🚀**
```
