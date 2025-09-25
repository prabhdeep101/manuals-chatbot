import os
import azure.cognitiveservices.speech as speechsdk

# Keep a global synthesizer so we can stop it
_synthesizer = None

def _speech_config():
    return speechsdk.SpeechConfig(
        subscription=os.getenv("AZURE_SPEECH_KEY"),
        region=os.getenv("AZURE_SPEECH_REGION")
    )

def speech_to_text() -> str:
    cfg = _speech_config()
    recognizer = speechsdk.SpeechRecognizer(speech_config=cfg)
    print(" Speak now...")
    result = recognizer.recognize_once()
    return result.text

def text_to_speech(text: str):
    """Speak text out loud (save synthesizer so we can stop later)."""
    global _synthesizer
    cfg = _speech_config()
    cfg.speech_synthesis_voice_name = "en-US-AriaNeural"
    _synthesizer = speechsdk.SpeechSynthesizer(speech_config=cfg)
    _synthesizer.speak_text_async(text)  # non-blocking

def stop_speaking():
    """Stop ongoing speech playback."""
    global _synthesizer
    if _synthesizer:
        _synthesizer.stop_speaking_async()
