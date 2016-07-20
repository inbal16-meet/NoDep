
from flask import Flask, render_template
app = Flask(__name__)


#Homepage
@app.route('/')
def homepage():
	return render_template(#here we put the homepage.html)

#signup page

@app.route('/about')
def about():
	return render_template(#here we put about.html)

#signin page

@app.route('/signin')
def signin():
	return render_template(#here we put signin.html)

#submit page

@app.route('/submit')
def submit():
	return render_template(#here we put submit.html)

#stories page

@app.route('/stories')
def stories():
	return render_template(#here we put stories)


#a single story page
@app.route('story/<id>')
def storyid(id):
	return render_template(#singlestory.html, id=id)

#comment page (sending a comment)


@app.route('/comment')
def stories():
	return render_template(#comment.html)

#error page (404)
@app.errorhandler(404)
def page_not_found(e):
	return render_template(#'404.html')

if __name__ = '__main__':
	app.run(debug=True)
