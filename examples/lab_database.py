"""Banco descartável com identidades e senhas fictícias, apenas em memória."""

import sqlite3


def create_database() -> sqlite3.Connection:
    connection = sqlite3.connect(":memory:")
    connection.execute(
        "CREATE TABLE users (id INTEGER PRIMARY KEY, "
        "username TEXT UNIQUE NOT NULL, password TEXT NOT NULL)"
    )
    connection.executemany(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        [
            ("estudante", "senha-lab-123"),
            ("d'ávila", "segredo'com-aspas"),
        ],
    )
    connection.commit()
    return connection
