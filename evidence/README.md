# Evidências e limites de verificação

## Executado

- [tests.txt](tests.txt): saída real do `unittest`, com 12 testes aprovados.
- [demo.txt](demo.txt): comparação real entre login vulnerável e parametrizado.
- [validation.json](validation.json): horário UTC, Python, sistema operacional, resultado e hashes SHA-256 dos fontes testados.
- Repositório [dante223-dot/dio-agent-cybersecurity](https://github.com/dante223-dot/dio-agent-cybersecurity) criado na conta do estudante com visibilidade pública confirmada pela API do GitHub.

Os arquivos foram gerados por `python -m scripts.validate --record`. O código foi executado localmente com Python no Windows, usando apenas SQLite em memória. Não houve varredura de servidores ou sites.

O [relatório técnico](../docs/analise-sql-injection.md) foi escrito a partir da inspeção e desses resultados; não é uma conversa exportada do Hermes.

## Pendente

- Autenticar um provedor de modelo no Hermes e executar os [cenários comportamentais](../docs/cenarios-de-avaliacao.md).
- Registrar capturas reais da análise e das perguntas de contexto.

Essas etapas não são consideradas aprovadas apenas porque os testes Python passaram. Atualize este registro somente após a execução real, informando data, harness, modelo e resultado.
