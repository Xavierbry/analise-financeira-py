def calcular_orcamento(renda):
    essencial = renda * 0.5
    lazer = renda * 0.3
    investimento = renda * 0.2

    ## calculo da em 50%, 30% e 20% da renda.
    
    if renda < 1500:
        diagnostico = "Renda baixa — pode ser difícil seguir essa regra."
    else:
        diagnostico = "Boa base para organização financeira."

    return {
        "essencial": essencial,
        "lazer": lazer,
        "investimento": investimento,
        "descricao": {
            "essencial": "Aluguel, contas, mercado",
            "lazer": "Compras, entretenimento",
            "investimento": "Poupança, estudos"
        },
        "diagnostico": diagnostico
    }