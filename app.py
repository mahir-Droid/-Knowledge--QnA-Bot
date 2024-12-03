from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    question = request.json.get('question')
    answer = answer_question(question, G, qa_model)
    return jsonify({'answer': answer})

if __name__ == "__main__":
    app.run(debug=True)
