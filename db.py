import pymysql

conn = pymysql.connect(
    host = 'sql6.freesqldatabase.com',
    database = 'sql6408201',
    user = 'sql6408201',
    password = '6vv6Yp4QSD',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

cursor = conn.cursor()
sql_query = ''' CREATE TABLE blood (
    blood_bank_name text NOT NULL,
    location text NOT NULL,
    mobile_no text NOT NULL,
    blood_group text NOT NULL 
)'''

cursor.execute(sql_query)
conn.close()