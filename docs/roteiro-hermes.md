# Roteiro de demonstração no Hermes

## Preparar

1. Instale o Hermes seguindo a [documentação oficial](https://hermes-agent.nousresearch.com/docs/getting-started/installation).
2. Reabra o terminal e execute `hermes setup` para escolher e autenticar seu provedor de modelo. Não compartilhe tokens ou chaves no chat nem no GitHub.
3. Abra a pasta deste projeto no VS Code. O terminal deve mostrar a raiz que contém `AGENTS.md`, `app.py` e `skills/`.
4. Execute `hermes`. Peça a leitura de `AGENTS.md`, `agent/persona.md` e `skills/vulnerability-analysis/SKILL.md`. Se o comportamento parecer genérico, confira o diretório e se existe um arquivo de contexto pessoal sobrescrevendo o projeto.

## Demonstrar a conversa de contexto

Use o caso 1 dos [cenários](cenarios-de-avaliacao.md). Capture a primeira resposta. Em seguida informe, apenas se corresponder ao seu laboratório, que você é responsável pelo ambiente e detalhe versão, serviços, finalidade e acesso de recuperação. Não invente um servidor real para executar o roteiro: a conversa também pode ser explicitamente hipotética.

O ponto da demonstração é o mentor adaptar a orientação ao contexto recebido, uma pergunta por vez.

## Demonstrar a análise e a correção

Prompt para o exemplo vulnerável:

```text
Atue como meu mentor de AppSec e use a skill vulnerability-analysis.
Este repositório é meu laboratório autorizado, local e descartável.
O banco contém somente contas fictícias e não há servidor na internet.
Leia examples/vulnerable_app.py e examples/lab_database.py.
Você pode executar os testes locais. Encontre a falha, explique sua
reprodução no laboratório, cite CWE e a técnica MITRE ATT&CK quando
o contexto justificar, e explique como reescrever a consulta.
```

Prompt de reteste:

```text
Leia a versão corrigida em app.py. Compare com a função anterior.
Execute python -m unittest discover -s tests -v e python -m scripts.demo.
Verifique se o desvio de autenticação foi mitigado sem quebrar entradas
legítimas com aspas. Apresente o relatório da skill com os limites da análise.
```

O repositório já preserva o antes/depois; não é necessário sobrescrever o exemplo vulnerável para fazer a comparação.

## Evidências para o portfólio

- Capture a análise apontando a concatenação SQL e explicando sua causa.
- Capture as perguntas de contexto do cenário Ubuntu.
- Capture o reteste mostrando recusa da injeção e aprovação do login legítimo.
- Registre harness, modelo e data. Remova da captura qualquer chave ou dado pessoal.

Guarde somente capturas reais. Os arquivos [tests.txt](../evidence/tests.txt) e [demo.txt](../evidence/demo.txt) já registram a execução local do código. Eles não são prints de uma conversa com o Hermes.
