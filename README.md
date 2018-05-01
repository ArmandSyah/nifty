Sentiment Analysis over Rotten Tomatoes review set. Based off of http://nifty.stanford.edu/2016/manley-urness-movie-review-sentiment/

# How to set-up Flask-RESTful API
1. Clone the repo
2. Make sure you have Python 3.6 and Pip3 installed
3. Install Virtaulenv (pip3 install virtualenv)
4. Move into the server folder (cd server)
4. Install the virutal enviroment (virtualenv -p python3.6 venv)
5. Activate virtual environment (source venv/bin/activate)
6. Install requirements (pip3 install -r requirements.txt)
7. Set a secret Key (export SECRET_KEY='<secret key>')
8. Set the flask app (export FLASK_APP=app.py)
9. Set up db (flask db init && flask db upgrade)
10. Run flask shell and then run setup_words command (flask shell, once in shell, type setup_words())
11. Close shell (quit() or CTRL-Z)
12. Run flask (flask run)