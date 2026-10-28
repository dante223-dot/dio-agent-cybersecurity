# Análise: SQL Injection no login de laboratório

Registro técnico preparado a partir da leitura dos fontes e da execução dos testes Python. **Não é uma transcrição de conversa com o Hermes.** Consulte [validation.json](../evidence/validation.json) para a data, ambiente e hashes da execução.

## 1. Contexto e escopo

Laboratório local solicitado para o desafio DIO. Python com SQLite em memória, duas contas fictícias, sem servidor HTTP, portas abertas ou conexão a serviços externos. Objetivo: reproduzir desvio de autenticação e verificar a correção por parametrização.

Arquivos analisados: [login vulnerável](../examples/vulnerable_app.py), [login corrigido](../app.py) e [banco descartável](../examples/lab_database.py).

## 2. Achado e evidência

**Observado:** a função `login` da versão vulnerável insere `username` e `password` diretamente na string SQL com f-strings. Uma entrada consegue encerrar o literal e mudar a consulta.

No laboratório, o usuário `estudante' -- ` com senha incorreta produz uma consulta equivalente a:

```sql
SELECT id FROM users WHERE username = 'estudante' -- ' AND password = 'errada'
```

O trecho após `--` vira comentário; a verificação de senha deixa de participar do filtro. O resultado é `True` apesar da senha errada. Uma segunda reprodução altera a condição por meio do campo de senha. Ambas estão nos testes, limitadas ao banco fictício.

**Inferido:** em uma aplicação real que utilizasse esse booleano para conceder acesso, a falha poderia permitir autenticação indevida.

**Não verificado:** acesso a uma aplicação remota, leitura de dados de produção, execução de comandos do sistema operacional ou comprometimento de infraestrutura.

## 3. Impacto (C/I/D)

- **Confidencialidade:** nenhum dado real foi exposto no laboratório; acesso indevido a dados seria possível em uma aplicação que confiasse no login.
- **Integridade:** a decisão de autenticação foi contornada. Alterações em registros não foram demonstradas.
- **Disponibilidade:** não houve interrupção demonstrada; não atribuir indisponibilidade ao teste.

Impacto **baixo no ativo deste laboratório**, que contém somente dados fictícios e não protege um serviço real. O mesmo defeito deve ser reavaliado antes de qualquer implantação.

## 4. Probabilidade

**Baixa para um incidente no ambiente atual:** o programa só é executado localmente, não aceita tráfego remoto e não possui usuários reais. A **reprodução deliberada da falha é simples e foi confirmada**; isso é diferente de afirmar alta probabilidade de um incidente remoto neste ambiente.

## 5. Severidade

**Baixa no laboratório** pela matriz do projeto: impacto baixo × probabilidade baixa. Confiança alta quanto ao desvio de login reproduzido; a estimativa de risco só vale para o escopo descrito.

**Cenário hipotético separado:** se essa função fosse ligada a um login público que protegesse dados sensíveis, sem barreiras adicionais, impacto e probabilidade poderiam ser altos, resultando em severidade crítica nessa matriz. Esse cenário não foi implantado nem testado. Não foi calculado CVSS.

## 6. Referências

Classe da falha: [CWE-89](https://cwe.mitre.org/data/definitions/89.html). Relação condicional: [MITRE ATT&CK T1190 — Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/), tática Initial Access. T1190 exige o contexto de exploração de aplicação exposta; não caracteriza a execução local realizada aqui.

Correção orientada pela [OWASP](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) e pela [API sqlite3 do Python](https://docs.python.org/3/library/sqlite3.html).

## 7. Correção

Em `app.py`, o SQL é fixo e os valores são passados separadamente:

```python
row = connection.execute(
    "SELECT id FROM users WHERE username = ? AND password = ?",
    (username, password),
).fetchone()
```

O driver trata aspas e operadores na entrada como parte do valor. Não foi adicionada uma lista de palavras proibidas; nomes legítimos como `d'ávila` continuam funcionando.

## 8. Validação

Comando reproduzível na raiz:

```bash
python -m scripts.validate --record
```

Resultado: **12 testes aprovados**. As duas reproduções de desvio retornam `True` antes e `False` depois. O login correto retorna `True` nas duas versões. A conta legítima com aspas e acento funciona após a correção; as tentativas verificadas não alteram o conteúdo do banco.

Status: **SQL Injection mitigado no escopo testado**. Evidências: [tests.txt](../evidence/tests.txt), [demo.txt](../evidence/demo.txt) e [validation.json](../evidence/validation.json).

## 9. Risco residual e próximo passo

As senhas fictícias permanecem em texto puro para manter a comparação focada na parametrização. Um sistema real precisaria de hashing apropriado de senhas, gestão de sessão, autorização, limites de tentativas e outros controles. Esses itens não foram auditados nem implementados como parte deste exercício.

Pergunta de aprendizado: por que a mesma aspa muda a consulta na versão vulnerável, mas é apenas um caractere do nome na versão parametrizada?
