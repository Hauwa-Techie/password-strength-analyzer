from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 10:
        score += 1
    else:
        feedback.append("Password must be at least 10 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    if re.search(r"[!@#$%^&*()]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, feedback

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    feedback = []
    if request.method == "POST":
        password = request.form["password"]
        result, feedback = check_password_strength(password)
    return render_template("index.html", result=result, feedback=feedback)

if __name__ == "__main__":
    app.run(debug=True)
