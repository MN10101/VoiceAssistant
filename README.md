
# Voice Assistant Project 💻🌐

Welcome to the **Voice Assistant Project**! This project leverages speech recognition and text-to-speech technologies to create an interactive and engaging voice assistant.

# Author
-  Mahmoud Najmeh


<img src="https://avatars.githubusercontent.com/u/78208459?u=c3f9c7d6b49fc9726c5ea8bce260656bcb9654b3&v=4" width="200px" style="border-radius: 50%;">

---

## 📊 Project Overview
This voice assistant can:
- Recognize voice commands using **speech recognition**.
- Speak responses with **pyttsx3**.
- Provide weather updates using **OpenWeather API**.
- Process common commands such as:
  - **Time Inquiry**
  - **Date Inquiry**
  - **Weather Information**
  - **Exit Command**

## 🤖 Features
- Hands-free operation with voice commands.
- Multi-threaded design for smoother interactions.
- Wake-word detection ("Hello") to activate the assistant.
- WebSocket communication for seamless browser integration.

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/MN10101/VoiceAssistant.git
cd voice_assistant
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Keys
Edit the `BASE_URL` and `API_KEY` values in the code to include your OpenWeather API key.

## 🔧 Usage

### Run the Assistant
```bash
python manage.py runserver
```

### Open the Browser
Navigate to `http://127.0.0.1:8000/` to interact with the assistant.

### Voice Commands
- Say "Hello" to activate the assistant.
- Ask "What's the time?" or "What's the date?".
- Get weather updates with "What's the weather in [City]?".
- Say "Exit" or "Quit" to stop the assistant.

## 📊 Tech Stack
- **Django** for backend operations.
- **Django Channels** for WebSocket support.
- **SpeechRecognition** for capturing and processing user commands.
- **pyttsx3** for text-to-speech conversion.
- **OpenWeather API** for weather data.

## 🛠 Known Issues
- Limited support for accents and languages.
- Microphone access may require browser permissions.

## 💪 Contributing
We welcome contributions! Please fork the repository and create a pull request.

---

### ⏳ Future Enhancements
- Add NLP for more intelligent command processing.
- Support for multiple wake words.
- GUI enhancements.
- Improve weather handling for multiple word city names.

## 🌟 Let's Build the Future Together!
Feel free to reach out with suggestions or improvements.

---
https://github.com/user-attachments/assets/2c34290e-5c44-47f0-9bba-ca5361fb8a49

