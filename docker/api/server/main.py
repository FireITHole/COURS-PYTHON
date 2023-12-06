from flask import Flask, request
from flask_cors import CORS
import os
import psycopg2

app = Flask(__name__)
CORS(app)

DB_PARAMS = {
    "dbname": "python-db",
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PWD"),
    "host": os.getenv("DB_IP"),
    "port": 5432,
}

def connectToDb():
    try:
        connection = psycopg2.connect(**DB_PARAMS)
        return connection
    except Exception as error:
        print(f"Couldn't connect to DB : {error}")
        exit(1)

def readFromDb() -> list:
    connexion = connectToDb()

    try:
        with connexion.cursor() as cursor:
            cursor.execute('SELECT * FROM messages')
            messages = cursor.fetchall()
    except Exception as error:
        print(f"Couldn't execute query: {error}")
    finally:
        connexion.close()

    return messages if messages else []


def addToDb(message: str) -> None:
    connexion = connectToDb()

    try:
        with connexion.cursor() as cursor:
            cursor.execute('INSERT INTO messages (message) VALUES (%s)', (message,))
            connexion.commit()
    except Exception as error:
        print(f"Couldn't execute query: {error}")
    finally:
        connexion.close()


def deleteFromDb(message: str) -> None:
    connexion = connectToDb()

    try:
        with connexion.cursor() as cursor:
            cursor.execute('DELETE FROM messages WHERE message = %s', (message,))
            connexion.commit()
    except Exception as error:
        print(f"Couldn't execute query: {error}")
    finally:
        connexion.close()


def updateDb(old_message: str, new_message: str) -> None:
    connexion = connectToDb()

    try:
        with connexion.cursor() as cursor:
            cursor.execute('UPDATE messages SET message = %s WHERE message = %s', (new_message, old_message))
            connexion.commit()
    except Exception as error:
        print(f"Couldn't execute query: {error}")
    finally:
        connexion.close()


@app.route("/api", methods=["GET", "POST", "PUT", "DELETE"])
def apiRoute():
    match request.method:
        case "GET":
            return {"messages": readFromDb()}, 200, {"ContentType": "application/json"}
        case "POST":
            data = request.json
            message = data["message"]

            if not message:
                return (
                    {"err": "Message manquant !"},
                    400,
                    {"Content-Type": "application/json"},
                )

            try:
                addToDb(message)
            except ValueError:
                return (
                    {"err": "Ce message est déjà présent dans la base de données !"},
                    400,
                    {"Content-Type": "application/json"},
                )

            return (
                {
                    "msg": f"Votre message '{message}' a été enregistré dans la base de donnée !"
                },
                201,
                {"Content-Type": "application/json"},
            )
        case "PUT":
            data = request.json
            old_message = data["old_message"]
            new_message = data["new_message"]

            if not old_message or not new_message:
                return (
                    {"err": "Messages manquant !"},
                    400,
                    {"Content-Type": "application/json"},
                )

            try:
                updateDb(old_message, new_message)
            except ValueError:
                return (
                    {
                        "err": "L'ancien message n'éxiste pas ou le nouveau message est déjà présent dans la base de données !"
                    },
                    400,
                    {"Content-Type": "application/json"},
                )

            return (
                {
                    "msg": f"Votre message '{old_message}' a été modifié par '{new_message}'"
                },
                200,
                {"Content-Type": "application/json"},
            )
        case "DELETE":
            data = request.json
            message = data["message"]

            if not message:
                return (
                    {"err": "Message manquant !"},
                    400,
                    {"Content-Type": "application/json"},
                )

            try:
                deleteFromDb(message)
            except ValueError:
                return (
                    {"err": "Ce message n'est pas présent dans la base de données !"},
                    400,
                    {"Content-Type": "application/json"},
                )

            return (
                {
                    "msg": f"Votre message '{message}' a été supprimé de la base de donnée !"
                },
                200,
                {"Content-Type": "application/json"},
            )


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("port"))
