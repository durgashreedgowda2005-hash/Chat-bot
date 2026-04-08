from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']

    # Extract numbers (attended and total)
    numbers = list(map(int, re.findall(r'\d+', user_input)))

    if len(numbers) >= 2:
        attended, total = numbers[0], numbers[1]

        if total == 0:
            return jsonify({"reply": "Total classes cannot be zero 😅"})

        percentage = (attended / total) * 100

        if percentage >= 85:
            reply = f"Your attendance is {percentage:.2f}% ✅ You are Eligible!"
        else:
            reply = f"Your attendance is {percentage:.2f}% ❌ Not Eligible"

    else:
        reply = "Please enter like: 'I attended 40 out of 50 classes' 😊"

    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)