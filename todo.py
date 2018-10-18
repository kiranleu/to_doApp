from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = {
	1 : {
		"id": 1,
		"name": "get coffee",
		"description": "none of that cheap stuff",
		"is_urgent": False
	},
	2 : {
		"id": 2,
		"name": "get milk",
		"description": "in a carton",
		"is_urgent": True
	},
}

next_id = 3


@app.route("/")
def show_hi():
	return render_template("index.html", todo_items=tasks.values())
    
@app.route("/add", methods = ["GET", "POST"])
def add_task():
	global next_id
	if request.method == "GET":
		return render_template("todo_form.html")
	else:
		task_to_add = {
			"id": next_id ,
			"name": request.form["task"],
			"description": request.form["description"],
			"is_urgent": "is_urgent" in request.form
			}

		tasks[next_id] = task_to_add
		
		next_id += 1
		return redirect("/")


if __name__ == "__main__":
	app.run(host='0.0.0.0',port=8080, debug=True)