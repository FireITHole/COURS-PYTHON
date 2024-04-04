import psycopg2
from datetime import datetime

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


class Message:
    def __init__(self) -> None:
        self._id: int | None = None
        self._content: str | None = None
        self._datetime_creation: datetime | None = None

    @property
    def id(self) -> int | None:
        return self._id

    @property
    def content(self) -> str | None:
        return self._content

    @content.setter
    def content(self, new_content: str) -> None:
        if not isinstance(new_content, str):
            raise TypeError

        if not len(new_content) <= 250:
            raise ValueError

        self._content = new_content

    @property
    def datetime_creation(self) -> datetime | None:
        return self._datetime_creation

    def insert(self, content: str) -> None:
        with connexion.cursor() as cursor:
            cursor.execute(
                "INSERT INTO messages (content) VALUES (%s) RETURNING id",
                (content,),
            )
            id = cursor.fetchone()[0]
            connexion.commit()
        self.load(id)

    def load(self, id: int):
        with connexion.cursor() as cursor:
            cursor.execute("SELECT * FROM messages WHERE id = %s", (id,))
            data: list[tuple] = cursor.fetchall()

        if not len(data): raise ValueError("ID doesn't exists in DB")

        self._id = id
        self._content = data[0][1]
        self._datetime_creation = data[0][2]

    def update(self) -> None:
        if self._id == None:
            raise ValueError("ID is None")
        with connexion.cursor() as cursor:
            cursor.execute(
                "UPDATE messages SET content = %s WHERE id = %s",
                (self._content, self._id),
            )
            connexion.commit()

    def delete(self) -> None:
        if self._id == None:
            raise ValueError("ID is None")
        with connexion.cursor() as cursor:
            cursor.execute(
                "DELETE FROM messages WHERE id = %s",
                (self._id,),
            )
            connexion.commit()

message = Message()
message.load(1)
print(message.content)
new_message = Message()
new_message.insert("toto")
print(new_message.content)