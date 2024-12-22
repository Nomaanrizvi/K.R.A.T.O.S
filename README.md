
# K.R.A.T.O.S - A voice based chatbot

K.R.A.T.O.S stands for `Knowledgeable Responsive Assistant with Thoughtful Organized Speech`. This project is a voice-enabled chatbot that integrates OpenAI's API and speech recognition technology. It allows users to interact with the chatbot through voice input and receive intelligent responses in the form of speech.

## Features

- **Voice Input**: Users can speak to the chatbot, and the chatbot will recognize the speech using speech recognition technology.
- **Intelligent Speech Responses**: The chatbot uses OpenAI's GPT-3.5-turbo to generate intelligent, accurate responses and communicates them via text-to-speech for a fully voice-based interaction.
- **Natural Conversation Flow**: The chatbot can carry on conversations, handle follow-up questions, and engage in meaningful dialogue.
- **File Management**: The chatbot can utilize the os module to control the file explorer, allowing users to open, browse, and manage files through voice commands.
- **Web Navigation**: By using the webbrowser module, the chatbot allows users to open websites and perform web searches, all through voice commands for seamless browsing.

## Requirements

To run the chatbot, ensure you have the following dependencies:

- Python 3.6 or higher
- `openai` library for accessing the OpenAI API
- `speech_recognition` library for converting speech to text
- `win32com.client` library for text-to-speech (voice output)
- `pyaudio` for microphone input support (only for mac users)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Nomaanrizvi/K.R.A.T.O.S.git
   cd K.R.A.T.O.S
   ```

2. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the chatbot**:

   ```bash
   python main.py
   ```

## Usage

Once everything is set up, the chatbot will listen for your voice input, convert it to text, generate a response using OpenAI's API, and then read the response aloud.

### Example Workflow:

1. **User speaks**: "Hello, how are you?"
2. **Chatbot processes**: The chatbot uses speech recognition to convert the audio to text and sends it to OpenAI's API for processing.
3. **Chatbot responds**: "I'm doing great, thanks for asking!"
4. **User hears the response**: The chatbot uses text-to-speech to say the response aloud.

You can continue the conversation naturally, and the chatbot will adapt to follow-up questions.

## Customization

- **Custom Responses**: You can modify the behavior of the chatbot by adjusting the `openai` API parameters or by adding specific prompt instructions for better customization.
- **Voice Settings**: Adjust the voice output (rate, volume, voice type) in the `win32com.client` settings to personalize the chatbot’s voice.

## Contributing

Feel free to fork this repository, contribute by adding new features, fixing bugs, or improving the overall functionality. You can open an issue if you encounter any problems or have suggestions for improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

With this setup, you're ready to engage with your intelligent voice-enabled chatbot!
