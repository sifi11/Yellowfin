# STARTER BACKEND
# NO REAL FUNCTION OTHER THAN LISTENING FOR BUTTONS
# I WILL HOOK IT UP TO THE MODULES

from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder='.')
CORS(app)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/panels/<path:filename>')
def panels(filename):
    return send_from_directory('panels', filename)

@app.route('/api/module/<int:module_id>/start', methods=['POST'])
def module_start(module_id):
    # YOUR CODE HERE
    print(f"[MODULE {module_id}] Execute pressed")
    return jsonify(ok=True, message=f"Module {module_id} started")

@app.route('/api/module/<int:module_id>/pause', methods=['POST'])
def module_pause(module_id):
    # YOUR CODE HERE
    print(f"[MODULE {module_id}] PAUSE pressed")
    return jsonify(ok=True, message=f"Module {module_id} paused")

if __name__ == '__main__':
    app.run(port=8080, debug=True)
