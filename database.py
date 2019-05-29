import psycopg2

def Database_Query():
    conn = psycopg2.connect('dbname=familyaccess')
    pointer = conn.cursor()
    pointer.execute('select * from family')
    results = cur.fetchall()

for result in results:
    print(result)
