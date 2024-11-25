# VoiceKit Assistant

A real-time voice interaction system powered by LiveKit and OpenAI, enabling natural conversations with AI. You've probably seen OpenAI's new voice mode for ChatGPT and I will be breaking down the process of how to make your version of this voice mode throughout this code...

## Overview
VoiceKit Assistant integrates LiveKit's real-time communication capabilities with OpenAI's language models to create a responsive voice assistant. It handles speech-to-text, natural language processing, and text-to-speech in real-time.

## Technical Stack
- **Python 3.11+**
- **LiveKit**: For real-time audio streaming
- **OpenAI**: For STT, TTS, and language processing
- **Silero**: For voice activity detection

## Setup Guide

### Prerequisites
- Python 3.11 or higher
- OpenAI API account with billing enabled
- LiveKit account and credentials

### Installation

1. Clone the repository:
```bash
git clone [https://github.com/MagellaX/VoiceKit-Assistant.git]
cd VoiceKit-Assistant
```

2. Create and activate virtual environment:
```bash
python -m venv ai
.\ai\Scripts\activate  # Windows
source ai/Scripts/activate  # Unix/MacOS
```

3. Install required packages:
```bash
pip install python-dotenv livekit-server-sdk-python openai livekit-plugins-openai livekit-plugins-silero
```

4. Configure environment variables in `.env`:
```env
LIVEKIT_URL=wss://your-livekit-url
LIVEKIT_API_SECRET=your-secret
LIVEKIT_API_KEY=your-key
OPENAI_API_KEY=your-openai-key
```

### Running the Assistant
```bash
python main.py start
```

## Common Issues & Solutions

### OpenAI API Quota
- Error 429 indicates exceeded API quota
- Solution: Enable billing in OpenAI account
- Check quota limits in OpenAI dashboard

### Environment Variables
- Ensure `.env` file is in the root directory
- No spaces around '=' in `.env` file
- No quotes around values

### Python Environment
- Clear `__pycache__` if code changes aren't reflecting
- Use the correct Python interpreter from virtual environment
- Check PATH variables if Python commands fail

## Features
- Real-time speech-to-text conversion
- Natural language processing
- Text-to-speech response generation
- Voice activity detection
- Interrupt-capable conversation flow
- Environment-aware configurations

## Development Notes
- Uses async/await for non-blocking operations
- Implements error handling for API failures
- Supports dynamic conversation context

## Troubleshooting
1. **Voice Not Detected**: Check microphone settings
2. **API Errors**: Verify API keys and quotas
3. **Connection Issues**: Check LiveKit URL and credentials

## Future Enhancements
- Multi-language support
- Custom wake word detection
- Voice modulation options
- Extended conversation context

## Contributing
Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License
MIT License - Feel free to use and modify for your projects.

## Acknowledgments
- LiveKit team for real-time communication framework
- OpenAI for AI capabilities
- Silero for voice activity detection

---


