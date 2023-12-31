import flet as ft
import json

def main(page:ft.Page):
    page.window_width = 600
    page.window_height = 500

    letreiro = ft.Text(value='Adivinhe a Bandeira',
                       font_family='Arial',
                       size=20)
    
    lb_bandeira = ft.Text(value='🇮🇩')
    

    page.add(
        ft.Row([letreiro],ft.MainAxisAlignment.CENTER),
        ft.Row([lb_bandeira])
    )

ft.app(target=main)

