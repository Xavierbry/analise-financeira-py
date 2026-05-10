import customtkinter as ctk
from orcamento import calcular_orcamento
from cartao import analisar_cartao
from simulador import simular_compra

ctk.set_appearance_mode("dark") # ativa o tema dark
ctk.set_default_color_theme("dark-blue") # cor azul dos botões
app = ctk.CTk()
app.title("Análise Financeira")
app.geometry("400x630")


def limpar_tela():
    for widget in app.winfo_children():
        widget.destroy()

# MENU
def mostrar_menu():
    limpar_tela()

    titulo = ctk.CTkLabel(app, text="Análise Financeira", font=("Arial", 20))
    titulo.pack(pady=20)
    msg = ctk.CTkLabel(app, text="Cada realidade financeira é diferente. Use esta regra como referência e adapte conforme suas prioridades.", font=("Arial", 12, "italic"), wraplength=350, justify="center")
    msg.pack(pady=10)

    # botão dentro de um Frame

    #  botão orçamento
    frame = ctk.CTkFrame(app, fg_color="#63635f", corner_radius=12)
    frame.pack(pady=10, padx=20, fill="x")

    ctk.CTkButton(frame, text="Orçamento", font=("Arial", 14, "bold"), command=tela_orcamento).pack(anchor="w",pady=10, padx=10)
    ctk.CTkLabel(frame, text="Regra 50-30-20 aplicada à sua renda", font=("Arial", 12), text_color="gray").pack(anchor="w", padx=14)
    ctk.CTkButton(frame, text="Acessar →", command=tela_orcamento, width=100).pack(anchor="w", padx=14, pady=(8, 14))


    #botão cartão de crédito
    frame = ctk.CTkFrame(app, fg_color="#63635f", corner_radius=12)
    frame.pack(pady=10, padx=20, fill="x")
    
    ctk.CTkButton(frame, text="Cartão de Crédito",font=("Arial", 14, "bold"), command=tela_cartao).pack(anchor="w", pady=10, padx=10)
    ctk.CTkLabel(frame, text="Seu limite vs. sua renda", font=("Arial", 12), text_color="gray").pack(anchor="w", padx=14)
    ctk.CTkButton(frame, text="Acessar →", command=tela_cartao, width=100).pack(anchor="w", padx=14, pady=(8, 14))


    #botao simulador de compra
    frame = ctk.CTkFrame(app, fg_color="#63635f", corner_radius=12)
    frame.pack(pady=10, padx=20, fill="x")
    ctk.CTkButton(frame, text="Simular Compra", font=("Arial", 14, "bold"), command=tela_simulador).pack(anchor="w", pady=10, padx=10)
    ctk.CTkLabel(frame, text="Calcule o parcelamento ideal para não comprometer sua renda", font=("Arial", 12), text_color="gray").pack(anchor="w", padx=14)
    ctk.CTkButton(frame, text="Acessar →", command=tela_simulador, width=100).pack(anchor="w", padx=14, pady=(8, 14))

    #botões soltos na tela
    #ctk.CTkButton(app, text="Orçamento", command=tela_orcamento).pack(pady=10)
    #ctk.CTkButton(app, text="Cartão de Crédito", command=tela_cartao).pack(pady=10)
    #ctk.CTkButton(app, text="Simular Compra", command=tela_simulador).pack(pady=10)

    
# TELA ORÇAMENTO

def tela_orcamento():
    limpar_tela()

    ctk.CTkLabel(app, text="Digite sua renda", font=("Arial", 14)).pack(pady=10) #cria e posiciona o texto
    entry = ctk.CTkEntry(app) # CTkEntry seria o campo de entrada como um input 
    entry.pack(pady=10) #mostra o campo da tela

    ctk.CTkLabel(app, text="sem pontuação, apenas números", font=("Arial", 9, "italic")).pack(pady=5)

    resultado = ctk.CTkLabel(app, text="")
    resultado.pack(pady=10)

    rodape = ctk.CTkLabel(app, text="", wraplength=350, justify="left")
    rodape.pack(pady=10)

    def calcular():
        try:
            renda = float(entry.get())
            dados = calcular_orcamento(renda)

            resultado.configure(
                text=f"""
Essenciais: R$ {dados['essencial']:.2f}
Lazer: R$ {dados['lazer']:.2f}
Investimentos: R$ {dados['investimento']:.2f}

{dados['diagnostico']}
"""
            )

            rodape.configure(
                text="""
Regra 50-30-20:
50% Essenciais → moradia, contas, alimentação
30% Lazer → compras, Entretenimento, Desejo e Estilo de Vida.
20% Investimentos → Investimentos, Estudos e Metas

A regra 50/30/20 é uma estratégia simples e eficaz para organizar suas finanças pessoais. Criada pela senadora americana Elizabeth Warren."""
            )

        except:
            resultado.configure(text="Digite um valor válido")
            rodape.configure(text="")

    ctk.CTkButton(app, text="Calcular", command=calcular).pack(pady=10)
    ctk.CTkButton(app, text="Voltar", command=mostrar_menu).pack(pady=10)


# TELA CARTÃO (LIMITE X RENDA)

def tela_cartao():
    limpar_tela()

    ctk.CTkLabel(app, text="Digite sua renda", font=("Arial", 14)).pack(pady=5)
    entry_renda = ctk.CTkEntry(app)
    entry_renda.pack(pady=5)

    ctk.CTkLabel(app, text="Limite do cartão", font=("Arial", 14)).pack(pady=5)
    entry_limite = ctk.CTkEntry(app)
    entry_limite.pack(pady=5)

    ctk.CTkLabel(app, text="sem pontuação, apenas números", font=("Arial", 9, "italic")).pack(pady=5)


    resultado = ctk.CTkLabel(app, text="", wraplength=350, justify="left")
    resultado.pack(pady=15)

    def analisar():
        try:
            renda = float(entry_renda.get())
            limite = float(entry_limite.get())

            if renda <= 0:
                resultado.configure(text="A renda deve ser maior que zero.")
                return

            dados = analisar_cartao(renda, limite)

            resultado.configure(
                text=f"""
Limite representa {dados['porcentagem']:.1f}% da sua renda

Situação: {dados['status']}

Dica: {dados['dica']}
"""
            )

        except:
            resultado.configure(text="Digite valores válidos")

    ctk.CTkButton(app, text="Analisar", command=analisar).pack(pady=10)
    ctk.CTkButton(app, text="Voltar", command=mostrar_menu).pack(pady=10)


# TELA SIMULADOR DE COMPRA

def tela_simulador():
    limpar_tela()

    ctk.CTkLabel(app, text="Digite sua renda", font=("Arial", 14)).pack(pady=5)
    entry_renda = ctk.CTkEntry(app)
    entry_renda.pack(pady=5)

    ctk.CTkLabel(app, text="Valor do produto", font=("Arial", 14)).pack(pady=5)
    entry_valor = ctk.CTkEntry(app)
    entry_valor.pack(pady=5)

    ctk.CTkLabel(app, text="sem pontuação, apenas números", font=("Arial", 9, "italic")).pack(pady=5)

    resultado = ctk.CTkLabel(app, text="")
    resultado.pack(pady=10)

    explicacao = ctk.CTkLabel(app, text="", wraplength=350, justify="left")
    explicacao.pack(pady=10)

    def simular():
        try:
            renda = float(entry_renda.get())
            valor = float(entry_valor.get())

            if renda <= 0:
                resultado.configure(text="A renda deve ser maior que zero.")
                return

            dados = simular_compra(renda, valor)

            resultado.configure(
                text=f"""
Parcelar em: {dados['parcelas']}x
Valor da parcela: R$ {dados['valor_parcela']:.2f}

{dados['status']}
"""
            )

            explicacao.configure(
                text=f"""
Cálculo baseado em até 30% da renda mensal.

Renda informada: R$ {renda:.2f}
Valor máximo recomendado por parcela: R$ {renda * 0.3:.2f}

Isso evita comprometer demais sua renda.
"""
            )

        except:
            resultado.configure(text="Digite valores válidos")
            explicacao.configure(text="")

    ctk.CTkButton(app, text="Simular", command=simular).pack(pady=10)
    ctk.CTkButton(app, text="Voltar", command=mostrar_menu).pack(pady=10)

# iniciar
mostrar_menu()
app.mainloop()