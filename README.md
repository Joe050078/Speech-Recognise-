# 🎙️ ASR – Automatic Speech Recognition System

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![OpenAI Whisper](https://img.shields.io/badge/Whisper-OpenAI-brightgreen)](https://github.com/openai/whisper)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?logo=fastapi)](https://fastapi.tiangolo.com/)

A production-ready **Automatic Speech Recognition (ASR)** system that converts spoken audio into text. It supports multiple engines (OpenAI Whisper, SpeechRecognition + Google), real-time microphone recording, batch audio file transcription, and a REST API for easy integration.

---

## 📸 Features

| Feature | Description |
|---|---|
| 🎤 **Live Microphone Input** | Record audio from mic and transcribe in real time |
| 📁 **Batch File Transcription** | Transcribe WAV / MP3 / M4A audio files |
| 🌐 **REST API** | FastAPI server exposing `/transcribe` endpoint |
| 🧠 **Multiple ASR Engines** | Whisper (offline) + Google Speech API (online) |
| 📊 **Noise Reduction** | Pre-processing pipeline with `noisereduce` |
| 📓 **Jupyter Notebook** | Exploratory analysis & demo notebook |
| ✅ **Unit Tests** | Full test suite with `pytest` |
| 🐳 **Docker Ready** | `Dockerfile` + `docker-compose.yml` included |

---

## 🛠️ Tools & Technologies

### Core ASR Engines
| Tool | Version | Purpose |
|---|---|---|
| [OpenAI Whisper](https://github.com/openai/whisper) | `>=20231117` | Offline multilingual ASR model |
| [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) | `>=3.10` | Wrapper for Google / CMU Sphinx engines |

### Audio Processing
| Tool | Purpose |
|---|---|
| [PyAudio](https://pypi.org/project/PyAudio/) | Real-time microphone capture |
| [librosa](https://librosa.org/) | Audio feature extraction & MFCC |
| [soundfile](https://pypi.org/project/SoundFile/) | Audio file I/O |
| [noisereduce](https://pypi.org/project/noisereduce/) | Spectral noise-gating |
| [pydub](https://github.com/jiaaro/pydub) | Audio format conversion |

### Machine Learning
| Tool | Purpose |
|---|---|
| [PyTorch](https://pytorch.org/) | Deep learning backbone for Whisper |
| [transformers (HuggingFace)](https://huggingface.co/docs/transformers) | Pre-trained ASR model loading |
| [numpy](https://numpy.org/) | Numerical computation |
| [scipy](https://scipy.org/) | Signal processing |

### API & Web
| Tool | Purpose |
|---|---|
| [FastAPI](https://fastapi.tiangolo.com/) | REST API framework |
| [uvicorn](https://www.uvicorn.org/) | ASGI web server |
| [python-multipart](https://pypi.org/project/python-multipart/) | File upload handling |

### Dev & Testing
| Tool | Purpose |
|---|---|
| [pytest](https://pytest.org/) | Unit testing |
| [Jupyter Notebook](https://jupyter.org/) | Interactive demo |
| [Docker](https://www.docker.com/) | Containerisation |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Environment variable management |

---

## 📂 Project Structure

```
asr-speech-recognition/
├── src/
│   ├── __init__.py
│   ├── asr_engine.py          # Core ASR engine (Whisper + Google)
│   ├── audio_recorder.py      # Microphone recording module
│   ├── audio_processor.py     # Preprocessing & noise reduction
│   ├── transcriber.py         # Batch file transcription
│   └── config.py              # Configuration & constants
├── api/
│   ├── __init__.py
│   ├── main.py                # FastAPI application
│   └── schemas.py             # Pydantic request/response models
├── utils/
│   ├── __init__.py
│   ├── audio_utils.py         # Format conversion helpers
│   └── text_utils.py          # Post-processing utilities
├── models/
│   └── .gitkeep               # Downloaded models are stored here
├── data/
│   └── samples/               # Sample audio files for testing
├── notebooks/
│   └── asr_demo.ipynb         # Jupyter demo notebook
├── tests/
│   ├── __init__.py
│   ├── test_asr_engine.py     # ASR engine tests
│   ├── test_audio_processor.py
│   └── test_api.py            # API endpoint tests
├── docs/
│   └── architecture.md        # System architecture notes
├── .env.example               # Environment variable template
├── .gitignore
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── setup.py
└── README.md
```

---

## ⚙️ Installation & Setup

### Prerequisites
- Python **3.8+**
- `ffmpeg` (required by Whisper and pydub)
- (Optional) CUDA-capable GPU for faster inference

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/asr-speech-recognition.git
cd asr-speech-recognition
```

### 2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate      # macOS / Linux
# venv\Scripts\activate       # Windows
```

### 3. Install system dependencies

**macOS (Homebrew)**
```bash
brew install ffmpeg portaudio
```

**Ubuntu / Debian**
```bash
sudo apt update && sudo apt install -y ffmpeg portaudio19-dev
```

**Windows**
Download and install [FFmpeg](https://ffmpeg.org/download.html) and add it to your `PATH`.

### 4. Install Python dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Configure environment variables
```bash
cp .env.example .env
# Edit .env to set your preferred Whisper model size, API keys, etc.
```

---

## 🚀 How to Run

### Option A – Command-Line Interface

#### Transcribe an audio file
```bash
python -m src.transcriber --file data/samples/sample.wav --engine whisper --model base
```

#### Real-time microphone transcription
```bash
python -m src.audio_recorder --engine whisper --duration 10
```

#### Batch transcription of a folder
```bash
python -m src.transcriber --folder data/samples/ --output results.txt
```

### Option B – REST API Server
```bash
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

Then open: [http://localhost:8000/docs](http://localhost:8000/docs) (Swagger UI)

**Upload an audio file:**
```bash
curl -X POST "http://localhost:8000/transcribe" \
  -H "accept: application/json" \
  -F "file=@data/samples/sample.wav"
```

### Option C – Docker
```bash
# Build and start
docker compose up --build

# API will be available at http://localhost:8000
```

### Option D – Jupyter Notebook
```bash
pip install jupyter
jupyter notebook notebooks/asr_demo.ipynb
```

---

## 🧪 Running Tests
```bash
pytest tests/ -v
```

---

## 🔧 Configuration

Edit `.env` to control runtime behaviour:

| Variable | Default | Description |
|---|---|---|
| `WHISPER_MODEL` | `base` | Whisper model size: `tiny`, `base`, `small`, `medium`, `large` |
| `ASR_ENGINE` | `whisper` | Engine to use: `whisper` or `google` |
| `GOOGLE_API_KEY` | _(empty)_ | Google Cloud Speech API key (optional) |
| `SAMPLE_RATE` | `16000` | Audio sample rate in Hz |
| `LANGUAGE` | `en` | Target language code |
| `MAX_DURATION` | `60` | Max recording duration in seconds |

---

## 📊 Supported Whisper Models

| Model | Parameters | VRAM | Speed | Accuracy |
|---|---|---|---|---|
| `tiny` | 39 M | ~1 GB | Fastest | ⭐⭐ |
| `base` | 74 M | ~1 GB | Fast | ⭐⭐⭐ |
| `small` | 244 M | ~2 GB | Moderate | ⭐⭐⭐⭐ |
| `medium` | 769 M | ~5 GB | Slow | ⭐⭐⭐⭐⭐ |
| `large` | 1550 M | ~10 GB | Slowest | ⭐⭐⭐⭐⭐ |

---

## 🗺️ Architecture

```
Audio Input (mic / file)
        │
        ▼
┌───────────────────┐
│  Audio Processor  │  ← Resampling, Noise Reduction, VAD
└───────────┬───────┘
            │
            ▼
┌────────────────────────────────────┐
│          ASR Engine                │
│  ┌─────────────┐  ┌─────────────┐ │
│  │   Whisper   │  │  Google STT │ │
│  └─────────────┘  └─────────────┘ │
└────────────────────┬───────────────┘
                     │
                     ▼
            ┌─────────────────┐
            │  Text Output    │  ← Console / File / API Response
            └─────────────────┘
```

---

## 📄 License

This project is licensed under the **MIT License** – see [LICENSE](LICENSE) for details.

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📬 Contact

**Author:** Jotheeswaran Arunkumar  
**GitHub:** [@jotheeswaran-arunkumar](https://github.com/jotheeswaran-arunkumar)
