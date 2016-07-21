from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def HomePage():
	return render_template("HomePage.html")


@app.route('/signup')
def signup():
	return render_template("sign_up_page.html")
	

@app.route('/aboutus')
def aboutus():
	return render_template("AboutUs.html")



if __name__ == '__main__':
	app.run(debug=True)
