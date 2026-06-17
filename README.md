# 🧠 AI Visual Assistant (YOLOv8 + Llama 3)

A real-time AI-powered vision system that combines **computer vision** and **large language models** to detect objects from a webcam and generate intelligent human-like explanations with voice output.

It works like a lightweight **Google Lens + AI assistant**, running fully on your local system.

---

## 🚀 Demo

📸 Capture an image from webcam  
🧠 Detect objects using YOLOv8  
🤖 Generate explanation using Llama 3 (Ollama)  
🔊 Speak the result using text-to-speech  

---

## ✨ Features

- 🎯 Real-time object detection using YOLOv8
- 🤖 AI-generated natural language explanations (Llama 3 via Ollama)
- 🔊 Voice output using pyttsx3
- 📸 Snapshot-based processing (press key to analyze)
- 🖥️ Live webcam preview
- ⚡ Fully offline AI pipeline (after setup)

---

## 🛠️ Tech Stack

- Python 🐍
- OpenCV 👁️
- Ultralytics YOLOv8 🎯
- Ollama (Llama 3) 🧠
- pyttsx3 🔊
- NumPy

---

## 📁 Project Structure

```

AI-Visual-Assistant/
│── app.py              # Main application (camera + control flow)
│── detector.py         # YOLOv8 object detection logic
│── speaker.py          # Text-to-speech engine
│── config.py           # Configuration settings (optional)
│── requirements.txt    # Dependencies
│── yolov8n.pt          # Pretrained YOLO model
│── README.md           # Project documentation

````

---

## ⚙️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/AI-Visual-Assistant.git
cd AI-Visual-Assistant
pip install -r requirements.txt
````

---

## ▶️ Run the Project

```bash
python app.py
```

---

## 🎮 Controls

* **S** → Capture image and analyze objects
* **Q** → Quit application

---

## 🧠 AI Pipeline

```
Webcam Input → YOLOv8 Detection → Llama 3 Explanation → Voice Output
```

---

## 🔥 Example Output

```
Detected: bottle

AI Explanation:
A bottle is a container commonly used to store liquids such as water, juice, or beverages. It is designed for easy transport and everyday use.
```

---

## 🎯 Use Cases

* AI learning projects
* Computer vision portfolio project
* Smart assistant prototypes
* Edge AI applications
* Resume / internship showcase project

---

## 🚀 Future Improvements

* 🎯 Object tracking across frames
* 🖱️ Click-based object explanation
* 🌐 Streamlit web interface version
* 📦 Model optimization for faster inference
* 📱 Mobile-friendly AI assistant UI
* 🎥 Save detection history + logs

---

## 👨‍💻 Author

**Vijay Krishnan P.M**

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub and feel free to improve it!

---

## 📌 Inspiration

Built as a combination of:

* Google Lens style vision systems
* Local LLM-based AI assistants
* Real-time computer vision applications

```
