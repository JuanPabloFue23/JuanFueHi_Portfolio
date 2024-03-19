from flask import Flask, request, jsonify

#Se necesita crear el Flask App
app = Flask(__name__)

#El siguiente condicional hará que corra nuestro servidor Flask
if __name__ == "__main__":
    app.run(debug=True)