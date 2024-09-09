# Health Care Chatbot
![image](https://github.com/AnanyaSDhar/Healthcare-Chatbot/assets/90474789/40d4ada8-4e4a-48a3-99f3-f5d600cd23ed)
This is a Flask web app that uses a decision tree classifier to diagnose diseases based on user input symptoms. The app also uses the NLTK library to detect and respond to greetings from the user and make the chatbot more conversational and friendly.

Functionalities of the bot:
- Predict diseases from user-given symptoms
- Responds properly to greetings

## Installation

To run this app, you need to have Python 3 and the following libraries installed:

- Flask
- pickle
- sklearn
- nltk

You can install them using pip:

```bash
pip install Flask
pip install pickle
pip install sklearn
pip install nltk
```

You also need to download the model.pkl and vectorizer.pkl files from this repository and place them in the same folder as the app.py file.

## Usage

To run the app, navigate to the folder where the app.py file is located and run the following command:

```bash
python app.py
```

This will start a local server on your machine. You can then open your browser and go to http://localhost:5000/ to see the home page of the app.

To chat with the health care chatbot, click on the "Chat with me" button on the home page. This will take you to the chatbot page where you can type your symptoms or greetings in the input box and press enter. The chatbot will respond with a diagnosis or a greeting based on your input.

You can end the chat by typing "bye", "goodbye" or "see you" in the input box.
