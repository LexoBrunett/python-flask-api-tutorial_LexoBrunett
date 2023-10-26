from flask import Flask
from flask import Flask, jsonify
from flask import request

app = Flask(__name__)


todos = [
    { "label": "My first task", "done": False }
]

#@app.route('/todos', methods=['GET'])
#def hello_world():
#    return "<h1>Hello!</h1>"

@app.route('/todos', methods=['GET'])
def hello_world():
    # you can convert that variable into a json string like this
    json_text = jsonify(todos)

    # and then you can return it to the front end in the response body like this
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    return jsonify(todos), 200


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    new_todos = list(filter(lambda item: item.get('position') == position, todos))
    return jsonify(new_todos)

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)