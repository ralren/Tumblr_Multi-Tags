import json
from flask import redirect, render_template, request, url_for, session
from app import app
from .forms import SearchForm
import pytumblr
import config


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	form = SearchForm()
	if form.validate_on_submit():
		input = form.tags.data #the tags the user is looking for
		return redirect(url_for('.results', input=input))
	return render_template('index.html', form=form)

@app.route('/results')
def results():
	search_tags = request.args['input'] #get search_tags from index page
	return render_template('results.html', matches=search_tumblr(search_tags))

def search_tumblr(search_tags):
	search_tags = search_tags.split("+")
	client = pytumblr.TumblrRestClient(config.TUMBLR_API)
	matches = []
	
	for i in range(len(search_tags)):
		posts = client.tagged(search_tags[i])

		#go through all the posts
		for j in range(20):
			#check if all the tags in search_tags is in 
			if all(tag in posts[j]['tags'] for tag in search_tags):
				#if so, put the url in matches
					matches.append(posts[j]['post_url'])

	matches = set(matches)			#make matches into a set to get rid of duplicates
	return matches