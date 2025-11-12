from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/message', methods=['POST'])
def handle_message():
    data = request.get_json()
    client_msg = data.get("message", "")
    

    print(f"Client says: {client_msg}")
    

    if client_msg == "I am client":
        reply = "I am server"
    elif client_msg == "Nice to meet you!":
        reply = "Nice to meet you too!"
    else:
        reply = "Server received: " + client_msg
    
    print(f"Server says: {reply}")
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
