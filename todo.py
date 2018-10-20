from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = {
	1 : {
		"id": 1,
		"name": "get coffee",
		"description": "none of that cheap stuff",
		"is_urgent": False,
		"done": False
	},
	2 : {
		"id": 2,
		"name": "get milk",
		"description": "in a carton",
		"is_urgent": True,
		"done": False
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
			"is_urgent": "is_urgent" in request.form,
			"done": "done" in request.form
			
			}

		tasks[next_id] = task_to_add
		
		next_id += 1
		return redirect("/")



# @app.route("/edit/<int:id>")	
# def show_edit(id):
# 	return render_template("edit_task_form.html", task = tasks[id])
	
@app.route("/edit/<int:id>", methods = ["GET","POST"])
def edit_task(id):
	if request.method =="POST":
		task_to_add = {
			"id" : id,
			"name": request.form["task"],
			"description": request.form["description"],
			"is_urgent": "is_urgent" in request.form, 
			"done" : "done" in request.form
			}
		tasks[id] = task_to_add
		return redirect("/")
	
	else:
		return render_template("edit_task_form.html", task = tasks[id])

@app.route("/done/<int:id>")
def show_done(id):
	task = tasks[id]
	print(task)
	if task["done"] == False:
		task["done"] = True
	else:
		task["done"] = False
	
	return redirect("/")
	



if __name__ == "__main__":
	app.run(host='0.0.0.0',port=8080, debug=True)