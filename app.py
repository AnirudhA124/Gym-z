from flask import Flask, request, render_template, jsonify, redirect, url_for

app = Flask(__name__)

# Store responses
responses = {}



# Define a route to serve the HTML form
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/questions')
def questions():
    return render_template('index.html')

# Define a route to handle form submissions
@app.route('/submit', methods=['POST'])
def submit():
    response = request.json
    print("Received response:", response)
    
    # Assuming each question has a unique identifier
    question_id = response.get('question')
    print("Question:", question_id)
    answer = response.get('answers')
    
    # Store response
    responses[question_id] = answer
    
    # Check if all questions are answered
    if len(responses) == len(responses)+1:
        # Redirect to the responses page when all questions are answered
        print(responses)
        return redirect(url_for('show_responses'))
    else:
        print(responses)
        return jsonify({'message': 'Response received successfully'})


# Define a route to display the responses
@app.route('/responses', methods=['POST','GET'])
def show_responses():
    print("Show Responses:", responses)
    return render_template('responses.html', responses=responses)

if __name__ == '__main__':
    app.run(debug=True, port=5500)
