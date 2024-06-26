from flask import Flask, render_template, request
import sqlite3
from sqlite3 import Error
app = Flask(__name__)
DATABASE = "webtags.db"

def create_connection(db_filename):
    try:
        connection = sqlite3.connect(db_filename)
        return connection
    except Error as e:
        print(e)
        return None

@app.route('/')
def render_index():  # put application's code here
    return render_template('index.html')

@app.route('/webpages')
def render_webpage():  # put application's code here

    query = "SELECT id, mileage, power, brand, dat, fuel, gear, condition FROM web_tags"
    connection = create_connection(DATABASE)
    cursor = connection.cursor()
    cursor.execute(query, )
    data_list = cursor.fetchall()
    print(data_list)

    return render_template('webpages.html', data=data_list)

@app.route('/styles')
def render_styles():  # put application's code here

    query = "SELECT id, mileage, power, brand, dat, fuel, gear, condition FROM web_tags WHERE gear = 'Manual'"
    connection = create_connection(DATABASE)
    cursor = connection.cursor()
    cursor.execute(query, )
    data_list = cursor.fetchall()
    print(data_list)

    return render_template('styles.html', data=data_list)


    return render_template('styles.html')

@app.route('/autos')
def render_autos():  # put application's code here

    query = "SELECT id, mileage, power, brand, dat, fuel, gear, condition FROM web_tags WHERE gear = 'Automatic'"
    connection = create_connection(DATABASE)
    cursor = connection.cursor()
    cursor.execute(query, )
    data_list = cursor.fetchall()
    print(data_list)

    return render_template('autos.html', data=data_list)


@app.route('/search', methods=['GET', 'POST'])
def render_search():  # put application's code here

    find = request.form['Search']
    title = "Look for: '" + find + "' "
    find = "%" + find + "%"

    query = "SELECT id, mileage, power, brand, dat, fuel, gear, condition FROM web_tags WHERE id LIKE ? OR mileage LIKE ? OR power LIKE ? OR brand LIKE ? OR dat LIKE ? OR fuel LIKE ? OR gear LIKE ? OR condition LIKE ?"
    connection = create_connection(DATABASE)
    cursor = connection.cursor()
    cursor.execute(query, (find, find, find, find, find, find, find, find))
    data_list = cursor.fetchall()
    print(data_list)

    return render_template('webpages.html', data=data_list)




if __name__ == '__main__':
    app.run()
