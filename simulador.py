def simular_compra(renda, valor_produto):
    limite_parcela = renda * 0.3
    parcelas = valor_produto / limite_parcela
    parcelas_recomendadas = int(parcelas) + 1
    valor_parcela = valor_produto / parcelas_recomendadas

    if valor_parcela > renda * 0.3:
        status = "Parcela alta para sua renda"
    else:
        status = "Compra dentro de um limite seguro"

    return {
        "parcelas": parcelas_recomendadas,
        "valor_parcela": valor_parcela,
        "status": status
    }