def analisar_cartao(renda, limite):
    if renda == 0:
        return {
            "porcentagem": 0,
            "status": "Renda inválida",
            "dica": "Informe uma renda maior que zero"
        }

    porcentagem = (limite / renda) * 100

    if limite > renda:
        status = "Risco alto: limite maior que a renda"
    elif limite > renda * 0.5:
        status = "Atenção: limite elevado"
    else:
        status = "Limite saudável"

    return {
        "porcentagem": porcentagem,
        "status": status,
        "dica": "Evite usar mais de 30% do limite"
    }