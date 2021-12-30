
import socket
import sys

import psycopg2
# connect to postgresql and give it host ip
conn = psycopg2.connect(
host="127.0.0.1",
database="MHN_DATABASE",
user="postgres",
password="user" )

conn.autocommit = True

cursorr = conn.cursor()

print("connected >>>>")
honeybot_name = "system"

#sql = f"""INSERT INTO MHN_REAL_hacker_data(hacker_ip,attack_port,honeybot_name) VALUES({data} , {port},{honeybot_name});"""

cursorr.execute(f"""INSERT INTO MHN_REAL_hacker_data(hacker_ip,attack_port,honeybot_name) VALUES('120.0.0.1' , 233 , 'mr_robot');""")
# vendor_id = cur.fetchone()[0]
conn.commit()
cursorr.close()