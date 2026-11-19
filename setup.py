from setuptools import setup, find_packages

setup(
    name="asr-speech-recognition",
    version="1.0.0",
    author="Jotheeswaran Arunkumar",
    description="Automatic Speech Recognition system using OpenAI Whisper and Google STT",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "openai-whisper>=20231117",
        "SpeechRecognition>=3.10.0",
        "PyAudio>=0.2.13",
        "librosa>=0.10.0",
        "soundfile>=0.12.1",
        "noisereduce>=3.0.0",
        "pydub>=0.25.1",
        "torch>=2.0.0",
        "transformers>=4.35.0",
        "numpy>=1.24.0",
        "scipy>=1.11.0",
        "fastapi>=0.100.0",
        "uvicorn[standard]>=0.23.0",
        "python-multipart>=0.0.6",
        "pydantic>=2.0.0",
        "python-dotenv>=1.0.0",
        "tqdm>=4.65.0",
        "loguru>=0.7.0",
    ],
    entry_points={
        "console_scripts": [
            "asr-transcribe=src.transcriber:main",
            "asr-record=src.audio_recorder:main",
            "asr-api=api.main:app",
        ]
    },
)
