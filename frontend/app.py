from flask import Flask, render_template

app = Flask(__name)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tasks')
def tasks():
    # Implémentez la logique pour afficher la liste des tâches depuis la base de données ici.
    # Vous pouvez utiliser SQLite pour simplifier.
    return "Liste des tâches"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
