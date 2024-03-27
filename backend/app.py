from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)


#client = MongoClient('mongodb+srv://user15:12345678user@cluster0.jmc7smb.mongodb.net/')
client=MongoClient('mongodb://mongodb:27017/')
db = client['mydatabase']
collection = db['users']

@app.route('/api/store', methods=['POST'])
def store_data():
    data = request.get_json()
    name = data['name']
    email = data['email']
    collection.insert_one({'name': name, 'email': email})
    return jsonify({'message': 'Data stored successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
