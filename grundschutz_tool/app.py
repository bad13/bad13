from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

# Load a minimal set of example controls from BSI IT-Grundschutz
CONTROLS_FILE = os.path.join(os.path.dirname(__file__), 'controls.json')

try:
    with open(CONTROLS_FILE, 'r', encoding='utf-8') as f:
        CONTROLS = json.load(f)
except FileNotFoundError:
    CONTROLS = []

@app.route('/')
def index():
    return render_template('index.html', controls=CONTROLS)

@app.route('/api/controls')
def api_controls():
    return jsonify(CONTROLS)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
