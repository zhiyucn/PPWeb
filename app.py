from flask import Flask, request, jsonify
from render import main
import os
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
async def index(path="/"):
    # 如果是/，返回index.pp
    if path == "/":
        return str(await main(open(os.path.join(os.path.dirname(__file__),"files", "index.pp"), "r").read()))
    else:
        file_path = os.path.join(os.path.dirname(__file__), "files", path)
        print(file_path)
        if not os.path.exists(file_path) or not path.endswith('.pp'):
            return "404 Not Found", 404
        return str(await main(open(file_path, "r").read()))

if __name__ == '__main__':
    app.run(debug=True)