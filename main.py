import flet as ft
from math import pi

def main(page: ft.Page):
    # Configurações de tamanho e posição da tela
    page.title = "Jogo da Forca"
    page.window_width = 412
    page.window_height = 915
    page.bgcolor = ft.colors.TRANSPARENT
    page.decoration = ft.BoxDecoration(
        image = ft.DecorationImage(
            src="assets/imgs/gradient.png",
            fit=ft.ImageFit.COVER
        )
    )

    page.add()

ft.app(target=main)