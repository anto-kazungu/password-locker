from flask import Flask, request, render_template, redirect, url_for
from interaction import Menu

app = Flask(__name__)
menu = Menu()  # Create an instance of Menu to manage interactions

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_account():
    account = request.form["account"]
    username = request.form["username"]
    password = request.form["password"]
    menu.accountdata.new_account(account, username, password)
    return f"Account for {username} added successfully! <a href='/'>Back to menu</a>"

@app.route("/search", methods=["GET"])
def search_account():
    filter_term = request.args.get("filter")
    search_results = menu.accountdata.search_account(filter_term)
    result_html = "<h3>Search Results</h3><ul>"
    for account in search_results:
        result_html += f"<li>{account.account}: {account.username}</li>"
    result_html += "</ul><a href='/'>Back to menu</a>"
    return result_html if search_results else "No accounts found. <a href='/'>Back to menu</a>"

@app.route("/generate-password", methods=["POST"])
def generate_password():
    length = int(request.form["length"])
    password = menu.password_generator(length)
    return f"Generated password: <strong>{password}</strong> <a href='/'>Back to menu</a>"

if __name__ == "__main__":
    app.run(debug=True)
