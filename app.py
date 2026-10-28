"""Login parametrizado de laboratório. Não é um sistema de autenticação de produção.

O banco temporário usa dados fictícios e senhas em texto puro para isolar a
diferença entre concatenação e parâmetros. Veja os limites no README.
"""

import sqlite3
from contextlib import closing
from getpass import getpass

from examples.lab_database import create_database


def login(connection: sqlite3.Connection, username: str, password: str) -> bool:
    """Valores são dados, nunca parte da sintaxe da consulta."""
    row = connection.execute(
        "SELECT id FROM users WHERE username = ? AND password = ?",
        (username, password),
    ).fetchone()
    return row is not None


if __name__ == "__main__":
    print("Laboratório local: conta fictícia estudante / senha-lab-123")
    with closing(create_database()) as database:
        accepted = login(database, input("Usuário: "), getpass("Senha: "))
    print("Login autorizado" if accepted else "Credenciais inválidas")
