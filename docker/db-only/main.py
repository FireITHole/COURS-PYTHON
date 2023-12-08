import psycopg2

DB_PARAMS = {
    "dbname": "db-only",
    "user": "fireithole",
    "password": "charli",
    "host": "localhost",
    "port": 5432,
}

try:
    connexion = psycopg2.connect(**DB_PARAMS)
except Exception as error:
    print(f"Couldn't connect to DB : {error}")
    exit(1)

try:
    with connexion.cursor() as cursor:
        level = "ERROR"
        log = "L'application s'est plantée"
        cursor.execute("INSERT INTO logs (level, log) VALUES (%s, %s)", (level, log))
        connexion.commit()
except Exception as error:
    print(f"Couldn't execute query: {error}")
finally:
    connexion.close()