import psycopg2

DB_PARAMS = {
    "dbname": "messages",
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


def insert(content: str) -> None:
    try:
        with connexion.cursor() as cursor:
            cursor.execute("INSERT INTO messages (content) VALUES (%s)", (content,))
            connexion.commit()
    except Exception as error:
        print(f"Couldn't execute query: {error}")


def get(id: int = None) -> list[tuple]:
    try:
        with connexion.cursor() as cursor:
            cursor.execute(
                f"SELECT * FROM messages{f' WHERE id = {id}' if isinstance(id, int) else ''}"
            )
            return cursor.fetchall()
    except Exception as error:
        print(f"Couldn't execute query: {error}")


def update(id: int, content: str) -> None:
    try:
        with connexion.cursor() as cursor:
            cursor.execute(
                "UPDATE messages SET content = %s WHERE id = %s", (content, id)
            )
            connexion.commit()
    except Exception as error:
        print(f"Couldn't execute query: {error}")


def delete(id: int) -> None:
    try:
        with connexion.cursor() as cursor:
            cursor.execute(
                "DELETE FROM messages WHERE id = %s", (id,)
            )
            connexion.commit()
    except Exception as error:
        print(f"Couldn't execute query: {error}")


print(get())

connexion.close()
