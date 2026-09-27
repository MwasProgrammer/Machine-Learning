from flask import Flask, jsonify
import random

app = Flask(__name__)

# 1. A mockup database of jokes (List of Dictionaries)
JOKE_DATABASE = [
    {
        "id": 1,
        "setup": "Do you know where you can get chicken broth in bulk?",
        "punchline": "The stock market."
    },
    {
        "id": 2,
        "setup": "How many seconds are in a year?",
        "punchline": "12. January 2nd, February 2nd, March 2nd..."
    },
    {
        "id": 3,
        "setup": "Why don't scientists trust atoms?",
        "punchline": "Because they make up everything!"
    }
]

# 2. Define the dynamic endpoint route
@app.route('/random_joke', methods=['GET'])
def get_random_joke():
    # Pick a random joke from our "database"
    selected_joke = random.choice(JOKE_DATABASE)
    
    # jsonify converts the Python dictionary into a JSON response for the web
    return jsonify(selected_joke)

if __name__ == '__main__':
    # Start the local server
    app.run(debug=True, port=5000)
