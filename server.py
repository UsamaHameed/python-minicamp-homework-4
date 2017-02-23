from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/addmovie')
def addmovie():
    return render_template('addmovie.html')

@app.route('/movie', methods = ['POST'])
def movie():

    connection = sqlite3.connect('movies.db')
    cursor = connection.cursor()
    try:
        name = request.form['name']
        description = request.form['description']

        cursor.execute('INSERT INTO movies (name, description) VALUES (?, ?)', (name, description))
        connection.commit()
    except:
        connection.rollback()
        return ('unable to submit data')
    finally:
        connection.close()
        print('added')
        return "data added"


@app.route('/movie-list', methods = ['GET'])
def movieList():

    connection = sqlite3.connect('movies.db')
    cursor = connection.cursor()
    try:
        cursor.execute('SELECT * FROM movies')
        message = jsonify(cursor.fetchall())
    except:
        connection.rollback()
        return ('unable to get data')
    finally:
        connection.close()
        print('found it :P')
        return render_template('movies.html', message = message)
