import psycopg2
from datetime import date

conn = psycopg2.connect(
    host="127.0.0.1",
    database="testdata",
    user="postgres",
    password="user")
    
    
conn.autocommit = True
    
cursor = conn.cursor()

print("connected >>>>")

sql = """INSERT INTO chat_board(name,description)
             VALUES ("hello" , date.today());"""
    


cursor.execute('''INSERT INTO chat_board(name,description) VALUES ('mobile devolopment' , 'this is mobile>>>> welcome')''')
#vendor_id = cur.fetchone()[0]
conn.commit()
cursor.close()