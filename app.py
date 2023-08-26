from flask import Flask, request, render_template
import nltk
import language_tool_python as lt

app = Flask(__name__)
tool = lt.LanguageTool('en-US')
nltk.download('punkt')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/correct', methods=['POST'])
def correct_text():
    user_text = request.form['user_text']
    sentences = nltk.sent_tokenize(user_text)
    corrected_text = ""
    for sentence in sentences:
        matches = tool.check(sentence)
        corrected_sentence = tool.correct(sentence)
        corrected_text += corrected_sentence + " "
    return render_template('index.html', corrected_text=corrected_text.strip())

if __name__ == '__main__':
    app.run(debug=True)
