from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-user/<user_id>")
def getUser(user_id):
    user_data = {
        "user_id" : user_id,
        "name" : "mahi",
        "email" : "mahendran148200@gmail.com"
    }
    
    extra = request.args.get("extra")
    if user_data:
        user_data["extra"] = extra
    
    return jsonify(user_data), 200

@app.route("/create-user", methods=["POST"])
def createUser():
    data = request.get_json()
    return jsonify(data), 201

if __name__ == "__main__":
     app.run(debug=True)