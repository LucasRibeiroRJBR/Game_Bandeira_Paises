import customtkinter as ctk
import requests
from PIL import Image, ImageTk
from io import BytesIO
import random

# Configuração inicial do CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class BandeiraQuizApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Duda Flags")
        self.geometry("750x550")
        self.iconbitmap("duda_flags.ico")

        # Inicialização de variáveis
        self.country_data = []
        self.correct_country = None
        self.score = 0

        # Layout da interface
        self.label_score = ctk.CTkLabel(self, text=f"Pontos: {self.score}", font=("Arial", 20))
        self.label_score.pack(pady=10)

        self.flag_label = ctk.CTkLabel(self, text="", font=('Arial',25), width=300, height=200)
        self.flag_label.pack(pady=20)

        self.acerto_erro = ctk.CTkLabel(self, text="", font=('Arial',25), width=300)
        self.acerto_erro.pack(pady=5)

        self.notification_label = ctk.CTkLabel(
            self, 
            text="", 
            font=("Arial", 24), 
            width=205, 
            fg_color="white",  # Fundo inicial branco
            text_color="black"  # Texto preto
        )
        self.notification_label.pack(pady=5)

        self.option_buttons = []
        for i in range(4):
            button = ctk.CTkButton(self, text="", font=('Arial',25), command=lambda b=i: self.check_answer(b))
            button.pack(pady=5, fill="x", padx=100)
            self.option_buttons.append(button)

        # Buscar dados dos países e iniciar o jogo
        self.load_country_data()
        self.next_question()

    def load_country_data(self):
        """Busca os dados da API REST Countries"""
        url = "https://restcountries.com/v3.1/all?fields=name,flags,translations"
        response = requests.get(url)
        if response.status_code == 200:
            self.country_data = response.json()
        else:
            ctk.CTkLabel(self, text="Erro ao carregar dados!", font=("Arial", 16)).pack()

    def get_country_name_in_portuguese(self, country):
        """Obtém o nome do país em português, se disponível"""
        return country["translations"].get("por", {}).get("common", country["name"]["common"])

    def next_question(self):
        """Carrega uma nova pergunta"""
        if not self.country_data:
            return

        # Escolher o país correto e três opções incorretas
        self.correct_country = random.choice(self.country_data)
        options = random.sample(self.country_data, 3)
        if self.correct_country not in options:
            options.append(self.correct_country)
        random.shuffle(options)

        # Baixar e exibir a bandeira
        flag_url = self.correct_country["flags"]["png"]
        response = requests.get(flag_url)
        img_data = BytesIO(response.content)
        img = Image.open(img_data).resize((300, 200))
        self.flag_image = ImageTk.PhotoImage(img)
        self.flag_label.configure(image=self.flag_image)

        # Configurar os botões de opção
        for i, button in enumerate(self.option_buttons):
            button.configure(text=self.get_country_name_in_portuguese(options[i]))

        # Limpar notificação anterior
        self.notification_label.configure(text="")

    def show_notification(self, message, color,t):
        """Exibe uma notificação temporária"""
        self.acerto_erro.configure(text=message,text_color=color)
        self.notification_label.configure(
            text=message, 
            fg_color=color,  # Cor de fundo
            text_color=t  # Cor do texto
        )
        #self.after(1000, lambda: self.notification_label.configure(text="", fg_color="transparent"))

    def check_answer(self, button_index):
        """Verifica a resposta do usuário"""
        selected_country = self.option_buttons[button_index].cget("text")
        correct_name = self.get_country_name_in_portuguese(self.correct_country)
        if selected_country == correct_name:
            self.score += 1
            self.label_score.configure(text=f"Pontos: {self.score}")
            self.show_notification("Correto!", "green","#000000")
        else:
            self.show_notification(f"Errado! Era {correct_name}.", "red","#000000")
        self.next_question()

# Executa o programa
if __name__ == "__main__":
    app = BandeiraQuizApp()
    app.mainloop()
