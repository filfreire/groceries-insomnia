from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

groceries = []
valid_token = None

def generate_token():
    return str(uuid.uuid4())

@app.route('/get_token', methods=['GET'])
def get_token():
    global valid_token
    valid_token = generate_token()
    return jsonify({'token': valid_token})

def require_token(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token or token != valid_token:
            return jsonify({'error': 'Unauthorized'}), 401
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper

@app.route('/add_grocery', methods=['POST'])
@require_token
def add_grocery():
    data = request.json
    grocery = data.get('grocery')
    if not grocery:
        return jsonify({'error': 'Grocery not provided'}), 400
    # FIX: uncomment this block to prevent duplicate groceries
    if grocery in groceries:
        return jsonify({'error': 'Grocery already exists'}), 400
    else:
        groceries.append(grocery)
        return jsonify({'message': 'Grocery added successfully'})

@app.route('/get_groceries', methods=['GET'])
@require_token
def get_groceries():
    return jsonify({'groceries': groceries})

@app.route('/delete_grocery', methods=['DELETE'])
@require_token
def delete_grocery():
    data = request.json
    grocery = data.get('grocery')
    if grocery in groceries:
        groceries.remove(grocery)
        return jsonify({'message': 'Grocery deleted successfully'})
    else:
        return jsonify({'error': 'Grocery not found'}), 404

@app.route('/clear_all', methods=['GET'])
@require_token
def debug_clear_all():
    groceries.clear()
    return jsonify({'message': 'Debug all groceries deleted successfully'})

@app.route('/health', methods=['GET'])
def debug_health():
    return jsonify({'message': 'server is running'})

if __name__ == '__main__':
    app.run(debug=False)