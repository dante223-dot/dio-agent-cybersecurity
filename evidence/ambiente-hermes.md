# Estado do ambiente Hermes

Verificação em 28/10/2026, no Windows.

- O instalador oficial `install.ps1` foi obtido do domínio da Nous Research.
- Foi solicitada instalação CLI não interativa, sem Chromium e sem driver de controle do computador.
- A versão estável selecionada pelo instalador foi `v0.22.5`.
- O código do Hermes foi baixado; o instalador também baixou Git, uv e Python 3.14.9.
- A instalação **não foi concluída**. O bootstrap do Python terminou com `Missing expected target directory for Python minor version link` e `bootstrap Python installation failed`.
- Uma nova tentativa e uma tentativa com outra pasta de instalação do Python encontraram a mesma falha. O executável Python baixado respondeu à consulta de versão, mas isso não fez o instalador do Hermes concluir.
- Nenhum provedor de modelo foi autenticado; não houve conversa ou avaliação comportamental executada no Hermes.

O laboratório Python do projeto foi executado separadamente com sucesso: 12 testes aprovados, também na cópia obtida do repositório publicado. Os 34 arquivos publicados na primeira versão foram comparados com a origem local; não houve divergência de conteúdo, links locais quebrados ou diferenças nos hashes dos fontes testados.

Próximo passo: concluir a instalação por uma opção suportada da [documentação oficial](https://hermes-agent.nousresearch.com/docs/getting-started/installation), configurar o provedor com `hermes setup` e executar o [roteiro de avaliação](../docs/roteiro-hermes.md). Não interpretar a presença do código baixado como confirmação de que o comando `hermes` está instalado e funcional.
