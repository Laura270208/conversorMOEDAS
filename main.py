#janela => 500 x 500
#título
#campos para selecionar de origem e destino
# botão para converter
#lista de exibição com os nomes das moedas
import customtkinter

#importar a biblioteca que vai fazer a janela

# criar e configurar a jenela
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("600x600")
# criar os botões, textos e demias elementos
titulo = customtkinter.CTkLabel(janela, text="Conversor de Moedas", font=("Times New Roman", 30), text_color=("#DB3E39"))
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem", font=("Times New Roman", 16))
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino", font=("Times New Roman", 16))
campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values= [ "USD", "EUR", "BRL", "BTC"], font=("Times New Roman", 16 ), fg_color = ("#DB3E39", "821D1A"))
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values= [ "USD", "EUR", "BRL", "BTC"], font=("Times New Roman", 16), fg_color=("#DB3E39", "821D1A"))
def converter_moeda():
    print("converter_moeda")
botao_converter = customtkinter.CTkButton(janela, text=" converter", command=converter_moeda, font=("Times New Roman", 16), fg_color=("#DB3E39", "821D1A"))

lista_moedas = customtkinter.CTkScrollableFrame(janela )

moedas_disponiveis = ["USD: dolara americano", "EUR:euro", "BRL:real brasileiro", "BTC:bitcoin" ]

for moeda in moedas_disponiveis:
    texto_moeda = customtkinter.CTkLabel (lista_moedas, text=moeda, font=("Times New Roman", 16))
    texto_moeda.pack()

#moeda1 = customtkinter.CTkLabel(lista_moedas, text="USD:dólar americano")
#moeda2 = customtkinter.CTkLabel(lista_moedas, text="EUR:euro")
#moeda3 = customtkinter.CTkLabel(lista_moedas, text="BRL:real brasileiro")
#moeda4 = customtkinter.CTkLabel(lista_moedas, text="BTC:bitcoin")
#moeda1.pack()
#moeda2.pack()
#moeda3.pack()
#moeda4.pack()
#colocar os elementos criados na tela
titulo.pack(padx=10, pady=10)
texto_moeda_origem.pack(padx=10, pady=0)
campo_moeda_origem.pack(padx=10, pady=0)
texto_moeda_destino.pack(padx=10, pady=0)
campo_moeda_destino.pack(padx=10, pady=0)
botao_converter.pack(padx=10, pady=10)
lista_moedas.pack(padx=10, pady=10)


#rodar a janela
janela.mainloop()