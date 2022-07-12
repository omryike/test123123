from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if(request.method == 'POST'):
        return jsonify({'about': request.get_json()}), 201
    else:
        return jsonify({'about': 'hello world!'})


if __name__ == '__main__':
    app.run(debug=True)
