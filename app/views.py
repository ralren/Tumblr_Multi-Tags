
from flask import redirect, render_template, request, url_for, session
from app import app
from .forms import SearchForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	form = SearchForm()
	if form.validate_on_submit():
		search_tags = form.tags.data #the tags the user is looking for
		return redirect(url_for('.results', search_tags=search_tags))
	return render_template('index.html', form=form)

@app.route('/results')
def results():
	search_tags = request.args['search_tags'] #get search_tags from index page
	return render_template('results.html',tags=search_tags)