from flask import Flask, request, jsonify
import json
import pymysql
app = Flask(__name__)


def db_connection():
    conn = None
    try:
        conn = pymysql.connect(host = 'sql6.freesqldatabase.com',
                               database = 'sql6408201',
                               user = 'sql6408201',
                               password = '6vv6Yp4QSD',
                               charset = 'utf8mb4',
                               cursorclass = pymysql.cursors.DictCursor)
    except pymysql.Error as e:
        print(e)
    return conn


@app.route('/blood', methods = ['GET', 'POST'])
def books():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("Select * from blood")
        books = [
            dict(Blood_Bank_Name = row['blood_bank_name'],
            Location = row['location'], Mobile_no = row['mobile_no'], Blood_Group = row['blood_group'])
            for row in cursor.fetchall()
        ]
        if books is not None:
            return jsonify(books) 

         
    if request.method == 'POST':
        new_name = request.form['blood_bank_name']
        new_loc = request.form['location']
        new_no = request.form['mobile_no']
        new_group = request.form['blood_group']
        sql = '''INSERT INTO blood (blood_bank_name, location, mobile_no, blood_group) 
                 VALUES (%s,%s,%s, %s)'''
        cursor = cursor.execute(sql,(new_name, new_loc, new_no, new_group))
        conn.commit()
        return "Entry Recorded successfully"


        #return jsonify(books_list), 201

if __name__ == '__main__':
    app.run()
