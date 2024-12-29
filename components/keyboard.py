import flet as ft
import string
from random import choice

lista_word = [
    "ABACATE",
    "ABACAXI",
]

choice = choice(lista_word).upper()


def keyboard():

    def discover (letter):
        return ft.Container(
            height=40,
            width=40,
            padding=5,
            border_radius=20,
            bgcolor=ft.colors.PRIMARY,
            content=ft.Text(
                value=letter,
                font_family="MADE_TOMMY_BOLD",
                color=ft.colors.WHITE,
                size=15,
                text_align=ft.TextAlign.CENTER,
                weight=ft.FontWeight.BOLD
                ),
            alignment=ft.alignment.center,
        )

    word = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Text(
                value="_",
                color=ft.colors.WHITE,
                size=25,
                weight=ft.FontWeight.BOLD
            )
        ]
    )

    main_container_teclas = [ ft.Container(
        height=40,
        width=40,
        padding=5,
        border_radius=20,
        bgcolor=ft.colors.PRIMARY,
        content=ft.Text(
            value=letter,
            color=ft.colors.WHITE,
            size=15,
            text_align=ft.TextAlign.CENTER,
            weight=ft.FontWeight.BOLD
            ),
        alignment=ft.alignment.center,
        ) for letter in string.ascii_uppercase
    ]

    return ft.Container(
        margin=ft.margin.only(bottom=50),
        opacity=0.8,
        shadow=ft.BoxShadow(
            blur_radius=20,
            spread_radius=20,
            color=ft.colors.PRIMARY,
        ),
        border_radius=10,
        padding=10,
        content= ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            controls = [
                word,
                ft.Row (
                expand=True,
                wrap=True,
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=main_container_teclas
                )
            ]
        )
    )