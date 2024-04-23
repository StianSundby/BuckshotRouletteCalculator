from flask import Flask, render_template, request, redirect, url_for
from Calc.Main import main

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/submit_configuration', methods=['POST'])
def submit_configuration():
    simulations = request.form.get('simulations', type=int)
    mode = request.form.get('mode', type=int)
    rounds = []
    for i in range(1, 7):
        round_value = request.form.get(f'round{i}')
        if round_value is not None:
            rounds.append(int(round_value))
        else:
            rounds.append(0)  # Default to blank if neither box is checked
    print("Simulation Count:", simulations)
    print("Mode:", mode)
    print("Rounds Submitted:", rounds)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)