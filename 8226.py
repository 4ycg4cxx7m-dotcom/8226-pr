from flask import Flask, render_template, request, url_for, jsonify
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')  # ✅ ПРОСТОЕ ИНТРО - БЕЗ regions!

@app.route('/love')
def love():
    return render_template('love.html')  # Страница любви

@app.route('/happiness')
def happiness():
    return render_template('happiness.html')  # Страница счастья

@app.route('/beauty')
def beauty():
    return render_template('beauty.html')  # Страница красоты

@app.route('/health')
def health():
    return render_template('health.html')  # Страница здоровья

@app.route('/success')
def success():
    return render_template('success.html')  # Страница Успеха

@app.route('/dreams')
def dreams():
    return render_template('dreams.html')  # Страница Улыбок

@app.route('/smiles')
def smiles():
    return render_template('smiles.html')  # Страница Тепла

@app.route('/warmth')
def warmth():
    return render_template('warmth.html')  # Страница вдохновения
    
@app.route('/inspiration')
def inspiration():
    return render_template('inspiration.html')  # Страница побед

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8800, ssl_context='adhoc', debug=True)
