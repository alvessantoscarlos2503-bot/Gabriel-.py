# Exercício 03 — Condições com `if` e `else`

## Objetivo

Revisar a tomada de decisão em Python por meio de uma condição simples com dois caminhos possíveis.

## Arquivos

- `main.py`

## Conteúdos trabalhados

- comparação com `>=`;
- estrutura `if`;
- estrutura `else`;
- dois-pontos ao final da condição;
- indentação dos blocos;
- variável de referência;
- cálculo dentro do bloco `else`;
- mensagens com f-strings.

## Como executar

No terminal do VS Code, dentro da pasta do exercício:

```bash
py main.py
```

ou:

```bash
python main.py
```

## Dados sugeridos para teste

### Teste 1 — acesso liberado

```text
Nome: Ana
Idade: 15
```

### Teste 2 — acesso ainda não liberado

```text
Nome: Lucas
Idade: 12
```

## Resultados esperados

- para uma idade igual ou superior a 14, o programa deve liberar o acesso;
- para uma idade inferior a 14, o programa deve informar quantos anos faltam;
- apenas um dos blocos deve ser executado em cada teste.

## Erros para observar

1. Remova os dois-pontos depois do `if` e leia o `SyntaxError`.
2. Retire a indentação de uma linha e leia o `IndentationError`.
3. Digite texto no lugar da idade e leia o `ValueError`.
4. Corrija o código e execute novamente.
