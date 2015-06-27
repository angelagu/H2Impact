Flask React
===========

Introduction
------------
Boilerplate to create a simple web app with Flask and React. Other fontend libraries included Twitter Bootstrap, jQuery, Lodash, Require.js & Font Awesome.

Demo
----
Deployed on Heroku: [flask-react.herokuapp.com](http://flask-react.herokuapp.com)

Installation
------------
* Install python dependencies
	
		pip install flask requests 

* Install required frontend libraries using [bower](http://bower.io/#install-bower).
		
		bower install 

* Transform JSX to JS using [React tool](http://facebook.github.io/react/docs/tooling-integration.html#productionizing-precompiled-jsx) for development purpose
		
		(FYI if this doesn't work just skip it...)

		jsx --watch app/static/jsx app/static/js
		
* Run Flask
		
		sh run.sh
		
* Start coding! :)

Author
------
Abhinay Omkar <abhiomkar@gmail.com>

License
-------
MIT