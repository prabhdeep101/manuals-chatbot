 Azure OpenAI Voice Chatbot

This project is a Streamlit-based chatbot that connects to Azure OpenAI
and uses Azure Speech Services for speech-to-text (STT) and
text-to-speech (TTS).
- Users can type OR speak questions.
- The bot always displays answers in text.
- The bot can also read answers aloud with a “Skip Talking” button to
stop speech anytime.



 Project Structure

    manuals-chatbot/
    │
    ├── app.py                  # Main Streamlit app
    ├── core/
    │   ├── openai_client.py    # Handles GPT requests via Azure OpenAI
    │   └── azure_speech.py     # Speech-to-Text & Text-to-Speech helpers
    │
    ├── .env                    # Environment variables (not committed)
    ├── requirements.txt        # Python dependencies
    └── README.md               # Project documentation

------------------------------------------------------------------------

 Setup

1. Clone repo & create venv

    git clone <repo-url>
    cd manuals-chatbot
    python -m venv .venv
    .venv\Scripts\activate   # On Windows
    source .venv/bin/activate # On Mac/Linux

2. Install dependencies

    pip install -r requirements.txt

3. Create Azure resources

-   Azure OpenAI → deploy a model (e.g., gpt-35-turbo or gpt-4o).
-   Azure Speech → create a Speech resource.

4. Configure .env

Create a .env file in project root:

    # Azure OpenAI
    AZURE_OPENAI_KEY=your-openai-key
    AZURE_OPENAI_ENDPOINT=https://your-openai-resource.openai.azure.com/
    AZURE_OPENAI_DEPLOYMENT=gpt-35-turbo  # or gpt-4o, etc.

    # Azure Speech
    AZURE_SPEECH_KEY=your-speech-key
    AZURE_SPEECH_REGION=eastus

------------------------------------------------------------------------

 Run the App

    streamlit run app.py

Open in your browser at http://localhost:8501.

------------------------------------------------------------------------

 Usage

1.  Type a question in the chat box.
    -   The bot replies in text (and can read it aloud).
2.  Click Speak to ask a question with your microphone.
    -   The bot transcribes your voice, answers, and reads it aloud.
3.  Click Skip Talking anytime to stop playback.
    -   The full text answer stays visible in the chat.

------------------------------------------------------------------------

 Customization


-   Disable auto-speaking:
    Comment out the text_to_speech(answer) call in app.py if you only
    want manual playback.

------------------------------------------------------------------------

 Requirements

-   Python 3.9+
-   Azure OpenAI resource (with deployed GPT model)
-   Azure Cognitive Services Speech resource

------------------------------------------------------------------------

 Notes

-   Microphone input requires running Streamlit locally (browser mic
    integration needs streamlit-webrtc if you want web recording).
-   The bot is kept simple — no document/manual parsing; it’s a pure
    generative assistant.

------------------------------------------------------------------------

 Now you have a voice-enabled Azure GPT chatbot that works with both
text and speech!
