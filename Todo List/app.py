from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

todo = []

@app.route("/Todo")
def home():
    return render_template("home.html", todos = todo)

@app.route("/add", methods = ['POST', 'GET'])
def add():
    tasks = request.form['tasking']
    todo.append({"task":tasks})
    return redirect(url_for("home"))

@app.route('/edit/<int:index>', methods=['post','get'])
def edit(index):
    todos = todo[index]
    if request.method == 'POST':
        todos['task'] = request.form['edittask']
        return redirect(url_for("home"))
    else:
        return render_template("edit.html", todo=todo, index=index)


@app.route("/delete/<int:index>")
def delete(index):
    del todo[index]
    return redirect(url_for("home"))    

if __name__ == "__main__":
    app.run(debug=True)
