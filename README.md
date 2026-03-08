#Gemini Smart Chat

**Gemini Smart Chat** is an intelligent AI assistant built with **Google Gemini API** and **Streamlit**. It features a modern interface and dynamic model configuration, allowing users to customize AI parameters and interact with Google's latest generative models seamlessly.

#Key Features

* **Dynamic Model Selection:** Switch between different Gemini models (1.5 Flash, 2.0 Flash, etc.) instantly.
* **Advanced Configuration:** Real-time adjustment of parameters like `Temperature`, `Top-P`, and `Max Output Tokens`.
* **Session Memory:** Intelligent chat history tracking throughout the session.
* **Modern UI:** Clean, fast, and responsive user experience powered by Streamlit.
* **Secure Setup:** Easy API key management with `.env` file support.

#Installation & Setup

Follow these steps to get the project running on your local machine:

# 1. Clone the Repository
```bash
git clone [https://github.com/bngssntrk5/gemini-smart-chat.git](https://github.com/bngssntrk5/gemini-smart-chat.git)
cd gemini-smart-chat

#2. Install Dependencies
pip install -r requirements.txt

#3. Configure API Key
GOOGLE_API_KEY=your_api_key_here

#4. Run the Application
streamlit run app.py

Requirements
The project relies on the following core libraries:

streamlit
google-generativeai
python-dotenv

Roadmap (Future Plans)
[ ] Support for file uploads (PDF, CSV, Images) for multi-modal analysis.
[ ] Text-to-Speech (TTS) integration for AI responses.
[ ] Customizable System Instructions (System Prompts).
[ ] Exporting chat history to JSON or PDF format.

Contributing
Contributions are welcome! Feel free to open a Pull Request or report any bugs in the Issues section.
