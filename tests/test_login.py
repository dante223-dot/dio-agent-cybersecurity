"""Regressões de segurança: provar o defeito e a propriedade da correção."""

import unittest

from app import login
from examples.lab_database import create_database
from examples.vulnerable_app import login as vulnerable_login


class LoginSecurityTests(unittest.TestCase):
    def setUp(self):
        self.database = create_database()
        self.addCleanup(self.database.close)

    def test_legitimate_login_works_before_and_after(self):
        for authenticate in (vulnerable_login, login):
            with self.subTest(version=authenticate.__module__):
                self.assertTrue(authenticate(self.database, "estudante", "senha-lab-123"))

    def test_wrong_password_is_rejected_before_and_after(self):
        for authenticate in (vulnerable_login, login):
            with self.subTest(version=authenticate.__module__):
                self.assertFalse(authenticate(self.database, "estudante", "errada"))

    def test_vulnerable_login_allows_username_bypass(self):
        self.assertTrue(vulnerable_login(self.database, "estudante' -- ", "errada"))

    def test_fixed_login_blocks_same_username_bypass(self):
        self.assertFalse(login(self.database, "estudante' -- ", "errada"))

    def test_vulnerable_login_allows_password_bypass(self):
        self.assertTrue(vulnerable_login(self.database, "inexistente", "' OR '1'='1"))

    def test_fixed_login_blocks_same_password_bypass(self):
        self.assertFalse(login(self.database, "inexistente", "' OR '1'='1"))

    def test_legitimate_quotes_and_unicode_are_supported(self):
        self.assertTrue(login(self.database, "d'ávila", "segredo'com-aspas"))

    def test_valid_username_cannot_use_another_users_password(self):
        self.assertFalse(login(self.database, "estudante", "segredo'com-aspas"))

    def test_nonexistent_user_is_rejected(self):
        self.assertFalse(login(self.database, "inexistente", "senha-lab-123"))

    def test_empty_credentials_are_rejected(self):
        for username, password in [("", ""), ("estudante", ""), ("", "senha-lab-123")]:
            with self.subTest(username=username):
                self.assertFalse(login(self.database, username, password))

    def test_sql_like_inputs_preserve_database_contents(self):
        before = self.database.execute("SELECT * FROM users ORDER BY id").fetchall()
        for payload in ["'", "' OR 1=1 -- ", "'; DROP TABLE users; -- ", "/* */"]:
            with self.subTest(payload=payload):
                self.assertFalse(login(self.database, payload, payload))
        after = self.database.execute("SELECT * FROM users ORDER BY id").fetchall()
        self.assertEqual(before, after)

    def test_sql_shaped_username_can_be_a_literal_account(self):
        # A blacklist could pass the bypass tests while breaking valid data.
        username = "literal' OR 1=1 -- "
        self.database.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, "outra-senha-ficticia"),
        )
        self.assertTrue(login(self.database, username, "outra-senha-ficticia"))
        self.assertFalse(login(self.database, username, "errada"))


if __name__ == "__main__":
    unittest.main()
