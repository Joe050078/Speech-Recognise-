# System Architecture

## Overview

The ASR system is split into four distinct layers:

```
┌────────────────────────────────────────────────────────────┐
│                      Input Layer                           │
│   Microphone (PyAudio)  |  Audio File  |  HTTP Upload      │
└───────────────┬────────────────────────────────────────────┘
                │
                ▼
┌────────────────────────────────────────────────────────────┐
│                   Preprocessing Layer                       │
│  AudioProcessor                                            │
│  • Load (soundfile / pydub)                               │
│  • Mono conversion                                        │
│  • Resample → 16 kHz                                      │
│  • Amplitude normalisation                                │
│  • Noise reduction (noisereduce spectral gating)          │
└───────────────┬────────────────────────────────────────────┘
                │
                ▼
┌────────────────────────────────────────────────────────────┐
│                     ASR Engine Layer                       │
│  ASREngine                                                 │
│  ┌───────────────────┐   ┌────────────────────────────┐  │
│  │  OpenAI Whisper   │   │  Google Speech Recognition │  │
│  │  (offline, local) │   │  (online, API call)        │  │
│  └───────────────────┘   └────────────────────────────┘  │
└───────────────┬────────────────────────────────────────────┘
                │
                ▼
┌────────────────────────────────────────────────────────────┐
│                   Post-processing Layer                     │
│  text_utils                                                │
│  • Clean whitespace                                       │
│  • Remove filler words                                    │
│  • Capitalise sentences                                   │
│  • Add punctuation                                        │
└───────────────┬────────────────────────────────────────────┘
                │
                ▼
┌────────────────────────────────────────────────────────────┐
│                      Output Layer                          │
│   Console  |  JSON file  |  FastAPI JSON response         │
└────────────────────────────────────────────────────────────┘
```

## Key Design Decisions

| Decision | Rationale |
|---|---|
| Whisper as default engine | Offline, multilingual, no API key needed |
| 16 kHz target sample rate | Whisper's native input rate; best quality |
| Noise reduction before ASR | Significantly improves WER in noisy environments |
| FastAPI for REST API | Async support, auto Swagger docs, type safety |
| Pydantic models | Strict input/output validation for the API |
| Layered architecture | Each layer is independently testable |
