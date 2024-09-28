from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['github_webhooks']
collection = db['actions']

# Webhook endpoint for receiving GitHub events
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    action = data.get('action')
    
    if action == 'push':
        author = data['pusher']['name']
        to_branch = data['ref'].split('/')[-1]
        timestamp = datetime.utcnow().isoformat()
        document = {
            "request_id": data['after'],
            "author": author,
            "action": "PUSH",
            "from_branch": "",
            "to_branch": to_branch,
            "timestamp": timestamp
        }
        collection.insert_one(document)
    
    # Handle other actions (Pull Request, Merge) similarly
    return 'Webhook received', 200

# Fetch the latest GitHub actions from MongoDB
@app.route('/latest-actions', methods=['GET'])
def latest_actions():
    actions = list(collection.find().sort('_id', -1).limit(10))  # Retrieve the latest 10 actions
    for action in actions:
        action['_id'] = str(action['_id'])  # Convert ObjectID to string
    return jsonify(actions)

# Serve the frontend (index.html)
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
