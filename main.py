import flet as ft
from components.theme import theme_game
from components.game import keyboard

def main(page: ft.Page):
    # Configurações de tamanho e posição da tela
    page.title = "Jogo da Forca"
    page.window_width = 412
    page.window_height = 915
    page.bgcolor = ft.colors.TRANSPARENT
    page.decoration = ft.BoxDecoration(
        image=ft.DecorationImage(
            src="images/frutas.png",
            fit=ft.ImageFit.COVER
        )
    )
    page.fonts = {
        "MADE_TOMMY": "fonts/MADE TOMMY Thin_PERSONAL USE.otf",
        "MADE_TOMMY_REGULAR": "fonts/MADE TOMMY Regular_PERSONAL USE.otf",
        "MADE_TOMMY_BOLD": "fonts/MADE TOMMY Bold_PERSONAL USE.otf",
    }
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary="#cc9d65",
        )
    )

    # Tema atual
    current_theme = "Frutas"

    def reset_game(new_theme):
        nonlocal current_theme
        current_theme = new_theme

        if current_theme == "Frutas":
            page.theme = ft.Theme(
                color_scheme=ft.ColorScheme(
                    primary="#cc9d65",
                )
            )
        else:
            page.theme = ft.Theme(
                color_scheme=ft.ColorScheme(
                    primary="#75c4d4",
                )
            )

        main_container.content.controls[1] = keyboard(page, theme=current_theme)
        page.update()

    main_container = ft.Container(
        alignment=ft.alignment.center,
        expand=True,
        padding=ft.padding.only(left=10, right=10),
        content=ft.Column(
            controls=[
                theme_game(page, reset_game),
                keyboard(page, theme=current_theme, reset_game=reset_game),
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    # Adiciona o container à página
    page.add(main_container)

ft.app(target=main, assets_dir="assets")
