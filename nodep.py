
from flask import Flask, render_template

#Homepage
@app.route('/')
def homepage():
	return render_template('#here we put the homepage.html')

#signup page

@app.route('/about')
def about():
	return render_template(#here we put about.html)

#signin page

@app.route('/signin')
def signin():
	return render_template(#here we put signin.html)

#submit page


#stories page


#comment page


#error page (404)


if __name__ = '__main__'
app.run(debug=True)
