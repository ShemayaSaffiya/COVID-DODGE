from flask import Flask, render_template, request, jsonify
from replit import db
import leaderboard
import json
app = Flask('app')

# db["number1"] = "Player 1"
# db["score1"] = 0
# db["number2"] = "Player 2"
# db["score2"] = 0
# db["number3"] = "Player 3"
# db["score3"] = 0
# db["number4"] = "Player 4"
# db["score4"] = 0
# db["number5"] = "Player 5"
# db["score5"] = 0

@app.route('/')
def home():
  return render_template('homepage.html')
  
@app.route('/username', methods=["POST", "GET"])
def send_username():
  username = request.form["name_input"]
  return jsonify({"username":username})
  
@app.route('/instructions')
def instructions():
  return render_template("instructions.html")

@app.route("/leaderboard")
def display_leaderboard():
  return render_template("getLeaderboard.html")

    
  
app.run(host='0.0.0.0', port=81)