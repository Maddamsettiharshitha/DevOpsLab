from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

# Route for the registration page
@app.route("/", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        # Collect form data
        full_name = request.form.get("full_name")
        username = request.form.get("username")
        email = request.form.get("email")
        phone = request.form.get("phone")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        gender = request.form.get("gender")
        
        # For now, just print the data (or save to database, etc.)
        print(f"Full Name: {full_name}")
        print(f"Username: {username}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print(f"Gender: {gender}")
        return redirect(url_for("registration"))  # Reload the page

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
