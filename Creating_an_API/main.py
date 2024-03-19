from flask import Flask, request, jsonify

#Se necesita crear el Flask App
app = Flask(__name__)

#Se necesita crear el Root (kinda location on our api, we can go to get some data)
@app.route("/get-user/<user_id>")

#In flask we created a dict  and then we jsonified that dict, so we can return to the user
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Juan P",
        "email": "juan.fuentesh15@gmail.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    
    return jsonify(user_data), 200 # The 200 is the status code 

#El siguiente condicional hará que corra nuestro servidor Flask
if __name__ == "__main__":
    app.run(debug=True) 