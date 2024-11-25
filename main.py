from flask import Flask, request

app = Flask(__name__)

@app.route('/receive', methods=['POST'])
def receive_data():
    user_agent = request.headers.get('User-Agent')
    print(f"User-Agent: {user_agent}")
    return {'status': 'success', 'user_agent': user_agent}, 200

if __name__ == '__main__':
    app.run(debug=True)
