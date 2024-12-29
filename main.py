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

    main_container_theme = ft.Text(
        value="Jogo da Forca",
        color=ft.colors.WHITE,
        size=25,
        weight=ft.FontWeight.BOLD,
    )

    main_container_game = ft.Container(
        bgcolor=ft.colors.OUTLINE_VARIANT,
        content=ft.Column(
            [
                ft.Text(
                    value="Container da forca",
                    color=ft.colors.WHITE,
                    size=25,
                    weight=ft.FontWeight.BOLD,),
            ]
        ),
    )

    main_container_teclado = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    value="Container do teclado",
                    color=ft.colors.WHITE,
                    size=25,
                    weight=ft.FontWeight.BOLD,),
            ]
        ),
    )

    main_container = ft.Container(
        alignment=ft.alignment.center,
        expand=True,
        padding=ft.padding.only(left=10, right=10),
        content=ft.Column(
            controls=[
                main_container_theme,
                main_container_game,
                main_container_teclado
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            
        ),
    )

    page.add(main_container)

ft.app(target=main)