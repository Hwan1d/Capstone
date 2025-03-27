from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "백엔드 서버 실행 중"

if __name__ == '__main__':
    app.run(debug=True)