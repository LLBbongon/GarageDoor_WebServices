import psycopg2
import logging
con = None
results = None
testData = None


def Database_Version():
    try:
        conn = psycopg2.connect(host="127.0.0.1", database="familyaccess", user="postgres", password="password", port="5432")
        cur = conn.cursor()
        print('PostgreSQL database version:')
        cur.execute("Select version()")
        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
            
#Fetch and returns the username gathered from postgres database.           
def Database_FetchUser(username):
    familyName = None
    try:
        conn = psycopg2.connect(host="127.0.0.1", database="familyaccess", user="postgres", password="password", port="5432")
        cur = conn.cursor()
        print('PostgreSQL database version:')
        cur.execute("SELECT * FROM familymembers WHERE family_user = %s",(username,))
        # display the PostgreSQL database server version
        db_fetch_username = cur.fetchone()
        familyName = db_fetch_username[1]
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    return familyName
#Fetch and returns the username gathered from postgres database.
def Database_FetchPassword(password):
    familyPassword = None
    try:
        conn = psycopg2.connect(host="127.0.0.1", database="familyaccess", user="postgres", password="password", port="5432")
        cur = conn.cursor()
        print('PostgreSQL database version:')
        cur.execute("SELECT * FROM familymembers WHERE family_password = crypt(%s, family_password)",(password,))
        # display the PostgreSQL database server version
        db_fetch_password = cur.fetchone()
        if cur.rowcount == 1:
            familyPassword = True
        elif cur.rowcount == 0:
            familyPassword = False
        else:
            familyPassword = False
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    return familyPassword


