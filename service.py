from flask import Flask, jsonify, request

from tech_interview import TechnicalInterviewer

app = Flask(__name__)


@app.route('/', methods=['POST'])
def technical():
    args = request.args

    ti = TechnicalInterviewer()

    questions = ti.generate_questions(set(args.get('keywords')))

    return jsonify(
        {
            'technical_questions': questions
        }
    )


@app.route('/', methods=['GET'])
def hello():
    return '<h2>Technical Interviewer</h2>'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=65535)
