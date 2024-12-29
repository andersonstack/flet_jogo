import flet as ft
from components.theme import theme_game
from components.gamer import gamer
from components.word import word
from components.keyboard import keyboard

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
    page.fonts = {
        "MADE_TOMMY": "assets/fonts/MADE TOMMY Thin_PERSONAL USE.otf",
        "MADE_TOMMY_REGULAR": "assets/fonts/MADE TOMMY Regular_PERSONAL USE.otf",
        "MADE_TOMMY_BOLD": "assets/fonts/MADE TOMMY Bold_PERSONAL USE.otf",
    }


    main_container = ft.Container(
        alignment=ft.alignment.center,
        expand=True,
        padding=ft.padding.only(left=10, right=10),
        content=ft.Column(
            controls=[
                theme_game(page),
                gamer(),
                word(),
                keyboard()
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            
        ),
    )

    page.add(main_container)

ft.app(target=main)