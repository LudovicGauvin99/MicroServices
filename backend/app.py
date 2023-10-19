import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name)

# Configurez SQLite comme base de données
conn = sqlite3.connect('tasks.db')
c = conn.cursor()

# Créez la table des tâches
c.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT)''')

@app.route('/api/tasks', methods=['GET', 'POST'])
def manage_tasks():
    if request.method == 'GET':
        # Récupérez la liste des tâches depuis la base de données
        c.execute('SELECT * FROM tasks')
        tasks = c.fetchall()
        return jsonify(tasks)
    elif request.method == 'POST':
        data = request.json
        # Ajoutez une nouvelle tâche à la base de données
        c.execute('INSERT INTO tasks (title, description) VALUES (?, ?)', (data['title'], data['description']))
        conn.commit()
        return 'Tâche ajoutée avec succès', 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
