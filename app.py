from flask import Flask, request, render_template
from spelling_bee import get_possible_words

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        letters = [request.form.get(f"letter{i}") for i in range(1, 7)]  # Get 6 letters
        center_letter = request.form.get("center_letter")  # Get the center letter
        if not all(letters) or not center_letter:
            return "Please enter all letters", 400
        possible_words = get_possible_words(letters, center_letter)
        return render_template("result.html", words=possible_words)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)