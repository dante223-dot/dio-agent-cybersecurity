# DIO Agent — Mentor de Cibersegurança

Especialização do [DIO Agent](https://github.com/digitalinnovationone/dio-agent) para conduzir análises defensivas de vulnerabilidades em português. O mentor entende o contexto, investiga evidências, avalia impacto e probabilidade, orienta a correção e verifica o resultado.

**Nenhum modelo foi treinado.** A especialização está nos arquivos Markdown que o harness lê. A proposta é aprender a justificar decisões de segurança, em vez de apenas executar comandos ou aceitar uma nota de risco sem explicação.

## O que foi entregue

| Arquivo | Função |
|---|---|
| [SKILL.md](skills/vulnerability-analysis/SKILL.md) | Roteiro defensivo: contexto, evidência, risco, correção e validação |
| [README da skill](skills/vulnerability-analysis/README.md) | Explicação da habilidade para pessoas |
| [security-basics.md](agent/knowledge/security-basics.md) | Vulnerabilidade, ameaça, risco, tríade C/I/D e boas práticas |
| [persona.md](agent/persona.md) | Especialização do mentor em AppSec |
| [AGENTS.md](AGENTS.md) | Registro da nova skill e orientação de quando usá-la |
| [app.py](app.py) | Login corrigido com consulta parametrizada |
| [vulnerable_app.py](examples/vulnerable_app.py) | Versão anterior, intencionalmente vulnerável e isolada |
| [test_login.py](tests/test_login.py) | 12 testes de reprodução e regressão |
| [Análise SQL Injection](docs/analise-sql-injection.md) | Relatório com achado, risco, correção e limites |
| [Cenários de avaliação](docs/cenarios-de-avaliacao.md) | Como verificar se o mentor pede contexto antes de agir |
| [Evidências](evidence/README.md) | Saídas reais dos testes e manifesto da execução |

Os arquivos originais de conhecimento e as demais skills do DIO Agent foram preservados. A base usada foi o commit `3751c04fac4813482a3c54a067482759215a69cf`.

## Melhoria escolhida: análises comparáveis

Toda análise concluída usa nove campos: contexto, achado, impacto, probabilidade, severidade, referências, correção, validação e risco residual. Uma matriz qualitativa explícita relaciona impacto e probabilidade; ela **não é CVSS**.

O agente diferencia fatos observados de hipóteses e usa “indeterminado” quando faltam dados. Assim, um Ubuntu exposto na internet não recebe uma classificação arbitrária nem uma lista de comandos antes de o mentor entender o cenário.

## Rodar o laboratório

Requer Python 3.10 ou superior com `sqlite3`. O laboratório usa apenas a biblioteca padrão: não requer `pip install`, banco externo, servidor ou conta de IA.

No terminal aberto **na raiz deste projeto**:

```bash
python -m scripts.demo
python -m unittest discover -s tests -v
```

Em sistemas onde o executável é `python3`, substitua `python` por `python3`. Para o login interativo:

```bash
python app.py
```

Use a conta fictícia `estudante` com a senha de laboratório `senha-lab-123`. O banco é criado em memória e descartado ao final.

Resultado registrado da comparação:

| Caso | Antes: vulnerável | Depois: parametrizado |
|---|---|---|
| Credenciais legítimas | Aceita | Aceita |
| Senha incorreta | Recusa | Recusa |
| SQL Injection no usuário | Aceita indevidamente | Recusa |
| SQL Injection na senha | Aceita indevidamente | Recusa |

As saídas reais estão em [demo.txt](evidence/demo.txt) e [tests.txt](evidence/tests.txt). Os testes também cobrem usuário inexistente, entradas vazias, caracteres legítimos e preservação do banco. Para gerar uma nova evidência local:

```bash
python -m scripts.validate --record
```

Esse comando atualiza os arquivos em `evidence/`, incluindo a data, a versão do Python e os hashes dos fontes em [validation.json](evidence/validation.json). Os testes Python avaliam a correção do código; não comprovam o comportamento de um modelo.

## Rodar o mentor no Hermes

Siga a [instalação oficial do Hermes](https://hermes-agent.nousresearch.com/docs/getting-started/installation). A documentação consultada oferece instalação nativa para Windows e instalação em Linux/macOS/WSL2.

Após instalar, reabra o terminal, rode `hermes setup` e configure seu provedor/modelo. Autentique-se diretamente no harness; não coloque chaves no repositório. O uso do provedor pode exigir créditos próprios.

No terminal do VS Code, entre na pasta que contém este `README.md` e `AGENTS.md` e inicie:

```bash
hermes
```

O [mecanismo de contexto do Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files) carrega instruções do projeto a partir do diretório de trabalho. O `AGENTS.md` encaminha os pedidos de segurança para a skill; não é necessário copiar a skill para uma instalação global.

Primeiro prompt:

```text
Leia AGENTS.md, agent/persona.md, agent/knowledge/security-basics.md
e skills/vulnerability-analysis/SKILL.md. Atue como meu mentor de AppSec.
Tenho um servidor Ubuntu de laboratório exposto na internet.
Quero melhorar a segurança. Por onde começo?
```

A resposta deve começar pela informação de contexto que falta, sem comandos. Depois, use o [roteiro de demonstração](docs/roteiro-hermes.md) para analisar o login vulnerável e retestar o corrigido.

## Escopo e limitações

- Use somente código e servidores próprios ou explicitamente autorizados. Este laboratório não faz requisições de rede nem abre portas.
- O exemplo guarda **senhas fictícias em texto puro**, para isolar a mudança de concatenação para parâmetros. Isso precisa ser substituído por armazenamento apropriado de senhas antes de qualquer uso real.
- Não foram implementados sessões, MFA, proteção contra força bruta, autorização de recursos, transporte TLS ou controles de produção.
- O status é **SQL Injection mitigado no escopo testado**, não “aplicação totalmente segura”.
- `CWE-89` descreve a falha. `T1190` é um mapeamento condicional para exploração de aplicação exposta; não é um ataque remoto demonstrado por este script local.
- Conversas de avaliação e prints devem vir de uma execução real do harness. O [registro de evidências](evidence/README.md) identifica o que foi executado e o que permanece pendente.

## Entrega no GitHub

Repositório público: [dante223-dot/dio-agent-cybersecurity](https://github.com/dante223-dot/dio-agent-cybersecurity). Use o endereço da página principal do repositório na entrega à DIO.

```bash
git clone https://github.com/dante223-dot/dio-agent-cybersecurity.git
cd dio-agent-cybersecurity
```

Para a apresentação, mostre a comparação antes/depois, os testes e uma conversa real em que o mentor investiga o contexto. O roteiro inclui quais momentos capturar. Evite publicar chaves, dados reais ou endereços de infraestrutura pessoal nos prints.

## Referências e créditos

- [DIO Agent — projeto base da Digital Innovation One](https://github.com/digitalinnovationone/dio-agent)
- [MITRE CWE-89](https://cwe.mitre.org/data/definitions/89.html)
- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/)
- [OWASP: prevenção de SQL Injection](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- [Python: sqlite3](https://docs.python.org/3/library/sqlite3.html)

Projeto educacional inspirado no desafio de especialização do DIO Agent em cibersegurança. A adaptação foi preparada com assistência de IA e verificada por execução dos testes locais.
