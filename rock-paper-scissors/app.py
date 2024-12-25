from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Define choices
choices = ["Rock", "Paper", "Scissors"]

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    user_choice = ""
    computer_choice = ""

    if request.method == "POST":
        user_choice = request.form.get("choice")
        computer_choice = random.choice(choices)
        
        # Determine the winner
        if user_choice == computer_choice:
            result = "It's a Tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
            (user_choice == "Paper" and computer_choice == "Rock") or \
            (user_choice == "Scissors" and computer_choice == "Paper"):
            result = "You Win!"
        else:
            result = "Computer Wins!"
    
    return render_template("index.html", result=result, user_choice=user_choice, computer_choice=computer_choice)

if __name__ == "__main__":
    app.run(debug=True)
