from flask import Flask, request, jsonify

#Se necesita crear el Flask App
app = Flask(__name__)

#Se necesita crear el Root (kinda location on our api, we can go to get some data)
@app.route("/")

def home():
    return "JuanAPI"

#El siguiente condicional hará que corra nuestro servidor Flask
if __name__ == "__main__":
    app.run(debug=True)