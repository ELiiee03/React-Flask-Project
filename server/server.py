from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, origins='*')

@app.route("/members", methods=(['GET']))
def members():
    return jsonify(
        {
            "members": [
                'arpan',
                'lieca',
                'jessie'
            ]
        }
    )
    # return {"members": ("Member1", "Member2", "Member3", "Member4")}

if __name__ == "__main__":
    app.run(debug=True, port=8080)