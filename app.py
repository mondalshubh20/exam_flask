from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
#app.secret_key = 'your_secret_key'

questions = [
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 7 * 6?", "answer": "42"}
]
@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for i, question in enumerate(questions):
        user_answer = request.form.get(f'q{i}')
        if user_answer.lower() == question["answer"].lower():
            score += 1
    flash(f'Your score: {score}/{len(questions)}', 'info')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

