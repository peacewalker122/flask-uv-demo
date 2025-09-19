from flask import Flask

app = Flask(__name__)


@app.route('/v1/someone-to-talk', methods=['GET'])
def someone_to_talk():
    return "person you're talking now", 200, {'Content-Type': 'text/plain'}


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
