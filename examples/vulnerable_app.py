"""ANTES: exemplo intencionalmente vulnerável, exclusivo para laboratório.

Nunca use esta função em produção. A versão corrigida está em app.py.
"""

import sqlite3


def login(connection: sqlite3.Connection, username: str, password: str) -> bool:
    query = (
        "SELECT id FROM users "
        f"WHERE username = '{username}' AND password = '{password}'"
    )
    return connection.execute(query).fetchone() is not None
