# Fundamentos para analisar vulnerabilidades

## Vulnerabilidade, ameaça e risco

- **Vulnerabilidade:** fraqueza que pode ser explorada. Exemplo: transformar dados do login em parte da sintaxe SQL.
- **Ameaça:** agente ou evento capaz de explorar uma fraqueza e causar dano. Exemplo: alguém tentar entrar sem credenciais válidas.
- **Risco:** possibilidade de dano no contexto do ativo, considerando a probabilidade e o impacto. Uma falha reproduzível não significa que um incidente real já aconteceu.
- **Superfície de ataque:** pontos pelos quais um sistema pode receber interações. Ter um serviço acessível aumenta a exposição, mas não confirma, isoladamente, uma falha.

## Tríade C/I/D

| Pilar | O que proteger | Exemplo de consequência |
|---|---|---|
| Confidencialidade | Acesso apenas por quem deve ter acesso | Leitura indevida de dados |
| Integridade | Correção dos dados e das operações | Alteração não autorizada de um cadastro |
| Disponibilidade | Acesso ao serviço quando necessário | Interrupção do login |

Descreva cada pilar separadamente. Não atribua perda de dados, execução remota ou indisponibilidade a um teste que apenas demonstrou um booleano de autenticação incorreto.

## Matriz qualitativa do projeto

Esta matriz é uma convenção didática para comparação, **não é CVSS** e não representa porcentagens.

**Impacto:** baixo = efeito restrito a dados fictícios ou função sem criticidade; médio = perda limitada de dados/operações de um ativo real, com recuperação viável; alto = dados sensíveis, privilégio elevado ou serviço essencial comprometido. Avalie os três pilares e use o maior efeito sustentado, explicando o motivo.

**Probabilidade:** baixa = acesso muito restrito e barreiras relevantes; média = caminho plausível, mas exige acesso ou condições adicionais; alta = entrada acessível, poucos pré-requisitos e falha reproduzível no cenário considerado. Falta de exposição ou de informação não equivale a probabilidade zero.

| Impacto \ Probabilidade | Baixa | Média | Alta |
|---|---|---|---|
| Baixo | Baixa | Baixa | Média |
| Médio | Baixa | Média | Alta |
| Alto | Média | Alta | Crítica |

Sem dados essenciais, use **indeterminada**. Indique confiança baixa/média/alta conforme a qualidade da evidência. Registre separadamente a facilidade de reprodução num teste deliberado e a probabilidade de incidente no ambiente de uso.

Não rebaixe a gravidade de uma futura implantação com dados reais só porque o exemplo atual usa dados fictícios. Reavalie o cenário antes de publicar um serviço.

## SQL Injection e classificação

SQL Injection ocorre quando entradas externas conseguem alterar a estrutura da consulta. No SQLite, use `execute(sql, parametros)` com marcadores `?`, passando os valores separadamente. Validar tamanho e formato pode complementar essa defesa, mas não a substitui. Parâmetros de valores não escolhem nomes de tabelas ou colunas.

**CWE-89** identifica a classe de fraqueza. **MITRE ATT&CK T1190**, na tática Initial Access, descreve explorar uma aplicação exposta para obter acesso inicial; sua relação com SQL Injection depende do cenário. O laboratório deste projeto é local e não demonstra acesso inicial remoto.

## Boas práticas

- Corrigir a causa e retestar fluxos legítimos e entradas adversas.
- Aplicar menor privilégio e separar ambientes de desenvolvimento e produção.
- Armazenar senhas com algoritmos de derivação apropriados, salt e biblioteca revisada; nunca usar texto puro em produção.
- Usar gestão de segredos, MFA quando aplicável e limites contra tentativas automatizadas.
- Atualizar dependências e serviços com planejamento de compatibilidade e recuperação.
- Manter logs úteis sem senhas, tokens ou dados sensíveis desnecessários.
- Testar backups e evitar mudanças de firewall/SSH sem caminho de recuperação.
- Registrar limitações: um teste que passa não comprova ausência de todas as vulnerabilidades.

## Fontes primárias

- [MITRE CWE-89](https://cwe.mitre.org/data/definitions/89.html)
- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/)
- [OWASP: prevenção de SQL Injection](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- [Python: sqlite3 e parâmetros](https://docs.python.org/3/library/sqlite3.html)
- [OWASP: armazenamento de senhas](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
