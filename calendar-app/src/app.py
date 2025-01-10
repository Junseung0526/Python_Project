from flask import Flask, request, jsonify
from calendar_manager import CalendarManager

app = Flask(__name__)
calendar_manager = CalendarManager()

@app.route('/events', methods=['GET'])
def get_events():
    events = calendar_manager.list_events()
    return jsonify(events)

@app.route('/events', methods=['POST'])
def add_event():
    event_data = request.json
    calendar_manager.add_event(event_data)
    return jsonify({"message": "Event added successfully!"}), 201

@app.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    calendar_manager.remove_event(event_id)
    return jsonify({"message": "Event removed successfully!"}), 200

if __name__ == '__main__':
    app.run(debug=True)