from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "replace-this-with-a-long-random-secret"
SECRET_CODE = "1416"

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form.get("code", "") == SECRET_CODE:
            session["unlocked"] = True
            return redirect(url_for("home"))
        error = "Almost... but that's not our secret 🤭"
    return render_template("login.html", error=error)

def protected():
    return not session.get("unlocked")

@app.route("/home")
def home():
    if protected(): return redirect(url_for("login"))
    return render_template("home.html")

@app.route("/story")
def story():
    if protected(): return redirect(url_for("login"))
    return render_template("story.html")

@app.route("/reasons")
def reasons():
    if protected(): return redirect(url_for("login"))
    return render_template("reasons.html")

@app.route("/letter")
def letter():
    if protected(): return redirect(url_for("login"))
    return render_template("letter.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
