import cv2
import requests
from detector import detect_objects
from speaker import speak

OLLAMA_URL = "http://localhost:11434/api/generate"

def ask_llama(prompt):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )
        return response.json()["response"]
    except:
        return "AI not responding."

cam = cv2.VideoCapture(0)

print("===================================")
print("   AI VISUAL ASSISTANT READY       ")
print("===================================")
print("Press S = Capture & Analyze")
print("Press Q = Quit")

while True:

    ret, frame = cam.read()
    if not ret:
        continue

    cv2.imshow("AI Visual Assistant", frame)

    key = cv2.waitKey(1) & 0xFF

    # 🚀 QUIT
    if key == ord('q'):
        print("Exiting...")
        break

    # 📸 SNAPSHOT MODE
    if key == ord('s'):

        print("\n📸 Image Captured. Analyzing...")

        detections = detect_objects(frame)

        if not detections:
            print("No objects detected.")
            continue

        names = list(set([d["name"] for d in detections]))

        print("Detected:", names)

        for obj in names:

            prompt = f"""
You are a Google Lens AI assistant.

Explain this object simply:
- What it is
- What it is used for
- One real-world fact

Object: {obj}
"""

            explanation = ask_llama(prompt)

            print(f"\n{obj.upper()}:\n{explanation}\n")

            speak(explanation)

cam.release()
cv2.destroyAllWindows()