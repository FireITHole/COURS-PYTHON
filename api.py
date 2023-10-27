from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DB_PATH = "./db/messages.txt"

def readFromDb() -> list[str]:
    with open(DB_PATH) as file:
        messages = [mes.replace('\n', '') for mes in file.readlines()]
        """ 
        # Équivalent à la ligne de code au-dessus
        messages = []
        for mes in file.readlines():
            messages.append(mes.replace('\n', '')) """
    
    return messages

def addToDb(message: str) -> None:
    messages = readFromDb()
    if message in messages:
        raise ValueError
    
    with open(DB_PATH, 'a') as file:
        file.write(message + '\n')

def deleteFromDb(message: str) -> None:
    messages = readFromDb()
    if message not in messages:
        raise ValueError
    
    with open(DB_PATH, 'w') as file:
        new_messages = [mes for mes in messages if mes != message and mes != ""]
        # Équivalent à la ligne du dessus
        """ new_messages = []
        for mes in messages:
            if mes != message and mes != "":
                new_messages.append(mes) """

        if len(new_messages) > 0:
            file.write('\n'.join(new_messages) + '\n')
        else:
            file.write("")

def updateDb(old_message: str, new_message: str) -> None:
    messages = readFromDb()
    if old_message not in messages or new_message in messages:
        raise ValueError
        
    new_messages = [mes if mes != old_message else new_message for mes in messages]

    with open(DB_PATH, 'w') as file:
        file.write('\n'.join(new_messages) + '\n')


@app.route("/api", methods=["GET", "POST", "PUT", "DELETE"])
def apiRoute():
    match request.method:
        case "GET":
            return {"messages": readFromDb()}, 200, {"ContentType": "application/json"}
        case "POST":
            data = request.json
            message = data["message"]

            if not message:
                return {"err": "Message manquant !"}, 400, {"Content-Type": "application/json"}

            try:
                addToDb(message)
            except ValueError:
                return {"err": "Ce message est déjà présent dans la base de données !"}, 400, {"Content-Type": "application/json"}

            return {"msg": f"Votre message '{message}' a été enregistré dans la base de donnée !"}, 201, {"Content-Type": "application/json"}
        case "PUT":
            data = request.json
            old_message = data["old_message"]
            new_message = data["new_message"]

            if not old_message or not new_message:
                return {"err": "Messages manquant !"}, 400, {"Content-Type": "application/json"}
            
            try:
                updateDb(old_message, new_message)
            except ValueError:
                return {"err": "L'ancien message n'éxiste pas ou le nouveau message est déjà présent dans la base de données !"}, 400, {"Content-Type": "application/json"}

            return {"msg": f"Votre message '{old_message}' a été modifié par '{new_message}'"}, 200, {"Content-Type": "application/json"}
        case "DELETE":
            data = request.json
            message = data["message"]

            if not message:
                return {"err": "Message manquant !"}, 400, {"Content-Type": "application/json"}
            
            try:
                deleteFromDb(message)
            except ValueError:
                return {"err": "Ce message n'est pas présent dans la base de données !"}, 400, {"Content-Type": "application/json"}

            return {"msg": f"Votre message '{message}' a été supprimé de la base de donnée !"}, 200, {"Content-Type": "application/json"}
        
if __name__ == "__main__":
    app.run(debug=True, port=3001)