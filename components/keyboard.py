import flet as ft
import string


def keyboard():
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
        content= ft.Row (
            expand=True,
            wrap=True,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=main_container_teclas
        )
    )