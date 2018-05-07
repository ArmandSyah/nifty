# How to set-up Nifty REST API
1. Clone the repo
2. Make sure you have Python 3.6 and Pip3 installed
3. Install Virtaulenv (pip3 install virtualenv)
4. Move into the server folder (cd server)
5. Install the virutal enviroment (virtualenv -p python3.6 venv)
6. Activate virtual environment (source venv/bin/activate)
7. Install requirements (pip3 install -r requirements.txt)
8. Set a secret Key (export SECRET_KEY='<secret key>')
9. Set the flask app (export FLASK_APP=app.py)
10. Set up db (flask db upgrade)
11. Run flask initdb command to set up table (flask initdb)
12. Run flask application to start server (flask run)