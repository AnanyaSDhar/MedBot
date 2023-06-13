from flask import Flask ,render_template,request
from datetime import datetime
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from nltk.stem import WordNetLemmatizer
# Import the NLTK chat module
import nltk.chat.util

app = Flask(__name__)

# Load the model and the vectorizer
with open("model.pkl", "rb") as f:
    model = pickle.load(f)
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Define a function to preprocess the input symptoms
def preprocess(symptoms):
    # Convert the symptoms into a list of words
    words = symptoms.split()
    # Lemmatize the words using WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()
    lemmas = [lemmatizer.lemmatize(word) for word in words]
    # Join the lemmas back into a string
    return " ".join(lemmas)

# Define a function to postprocess the output disease
def postprocess(disease):
    # Capitalize the first letter of each word
    return disease.title()

# Define a list of pairs of patterns and responses for greetings
greetings = [
    (r"hi|hello|hey", ["Hello, I am a health care chatbot. How can I help you?", "Hey, I am a health care chatbot. How can I help you?"]),
    (r"how are you|how do you do", ["I am fine, thank you.", "I am doing well, thank you.", "I am good, thank you."]),
    (r"what is your name|who are you", ["I am a health care chatbot.", "My name is HealthBot.", "I am HealthBot, a health care chatbot."]),
    (r"you are amazing|you are awesome|you are great", ["Thank you for your kind words.", "You are too kind.", "You made my day."]),
    (r"thank you|thanks|thankyou", ["You are welcome.", "It's my pleasure.", "No problem."]),
    (r"bye|goodbye|see you", ["Bye for now.", "Goodbye, take care.", "See you soon."])
]

# Create a greetbot object with the greetings list
greetbot = nltk.chat.util.Chat(greetings)

# Define a function to check if the user input is a greeting
def is_greeting(input_symptoms):
    # Return True if the greetbot responds to the input, False otherwise
    return greetbot.respond(input_symptoms) is not None

# Define a function to generate a greeting response based on the user input
def get_greeting_response(input_symptoms):
    # Return the greetbot response to the input
    return greetbot.respond(input_symptoms)

##################################################

you = []
bot = ["Hello I am a bot Happy to see you , tell me your problem ."]
time = []


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/chatbot',methods=["GET","POST"])
def chatbot():
    if request.method == "POST":
        time_now = datetime.now().strftime("%H:%M")
        input_symptoms = request.form.get('names')
        if len(input_symptoms)!=0:
            you.append(input_symptoms)
            # Check if the input symptoms are a greeting
            if is_greeting(input_symptoms):
                # Generate a greeting response based on the input symptoms
                output_disease = get_greeting_response(input_symptoms)
            else:
                # Preprocess the input symptoms
                processed_symptoms = preprocess(input_symptoms)
                # Transform the input symptoms into a sparse matrix of TF-IDF features
                input_vector = vectorizer.transform([processed_symptoms])
                # Predict the output disease using the model
                output_disease = model.predict(input_vector)[0]
                # Postprocess the output disease
                output_disease = postprocess(output_disease)
            # Append the output disease to bot list
            bot.append(output_disease)
            time.append(time_now)
        return render_template('chatbot.html',results = zip(you,bot,time))
    else:
        you.clear()
        bot.clear()
        return render_template('chatbot.html')





##################################################


if __name__ == '__main__':
    app.run(debug=True)
