from flask import Flask, request, jsonify

app = Flask(__name__)

groceries = []

@app.route('/add_grocery', methods=['POST'])
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
def get_groceries():
    return jsonify({'groceries': groceries})

@app.route('/delete_grocery', methods=['DELETE'])
def delete_grocery():
    data = request.json
    grocery = data.get('grocery')
    if grocery in groceries:
        groceries.remove(grocery)
        return jsonify({'message': 'Grocery deleted successfully'})
    else:
        return jsonify({'error': 'Grocery not found'}), 404

@app.route('/clear_all', methods=['GET'])
def debug_clear_all():
    groceries.clear()
    return jsonify({'message': 'Debug all groceries deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)