import psycopg2

DB_PARAMS = {
    "dbname": "db-only",
    "user": "fireithole",
    "password": "charli",
    "host": "localhost",
    "port": 5432,
}

def connectToDb():
    try:
        connection = psycopg2.connect(**DB_PARAMS)
        return connection
    except Exception as error:
        print(f"Couldn't connect to DB : {error}")
        exit(1)

connexion = connectToDb()

try:
    with connexion.cursor() as cursor:
        cursor.execute("INSERT INTO logs (level, log) VALUES ('CRITICAL', 'A problem happened')")
        connexion.commit()
except Exception as error:
    print(f"Couldn't execute query: {error}")
finally:
    connexion.close()