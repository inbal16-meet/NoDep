from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def HomePage():
	return render_template("HomePage.html")


@app.route('/sign_up_page')
def sign_up_page():
	return render_template("sign_up_page.html")
	

@app.route('/AboutUs')
def AboutUs():
	return render_template("AboutUs.html")

<<<<<<< HEAD
@app.route('/base')
def base():
	return render_template("base.html")
=======
@app.route('/submit')
def submit():
	return render_template("submit.html")

@app.route('/log_in')
def log_in():
	return render_template("log_in.html")

@app.route('/stories')
def stories():
	return render_template("stories.html")

@app.route('/AddAComment')
def AddAComment():
	return render_template("AddAComment.html")

@app.route('/SeeComment')
def SeeComment():
	return render_template("SeeComment.html")

>>>>>>> 76f6cb9f3ded29998edf84cd7cc8589aacb17340

if __name__ == '__main__':
	app.run(debug=True)
