"""Execute da raiz: python -m scripts.demo. Não faz requisições de rede."""

from contextlib import closing

from app import login
from examples.lab_database import create_database
from examples.vulnerable_app import login as vulnerable_login


def demonstrate() -> str:
    cases = [
        ("Credenciais legítimas", "estudante", "senha-lab-123"),
        ("Senha incorreta", "estudante", "errada"),
        ("Injeção no usuário", "estudante' -- ", "errada"),
        ("Injeção na senha", "inexistente", "' OR '1'='1"),
    ]
    lines = ["LABORATÓRIO LOCAL — SQLite em memória", "Caso | Antes (vulnerável) | Depois (parametrizado)"]
    with closing(create_database()) as database:
        for label, username, password in cases:
            before = vulnerable_login(database, username, password)
            after = login(database, username, password)
            lines.append(f"{label} | {before} | {after}")
        quoted = login(database, "d'ávila", "segredo'com-aspas")
        lines.append(f"Conta legítima com aspas e acento, após correção: {quoted}")
    lines.append("True = login aceito; False = login recusado.")
    lines.append("Escopo: SQL Injection no login. Senhas fictícias em texto puro; não usar em produção.")
    return "\n".join(lines)


if __name__ == "__main__":
    print(demonstrate())
