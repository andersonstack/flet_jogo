import flet as ft
import string
from random import choice
from components.gamer import gamer

lista_word = [
    "ABACATE",
    "ABACAXI",
]

choiced = choice(lista_word).upper()

def keyboard(page: ft.Page):
    global data

    def discover (letter):
        return ft.Container(
            height=40,
            width=40,
            padding=5,
            border_radius=20,
            bgcolor=ft.colors.WHITE,
            margin=ft.margin.only(bottom=50, top=50),
            content=ft.Text(
                value=letter,
                font_family="MADE_TOMMY_BOLD",
                color=ft.colors.BLACK,
                size=15,
                text_align=ft.TextAlign.CENTER,
                weight=ft.FontWeight.BOLD
                ),
            alignment=ft.alignment.center,
        )
    
    def valitade(e):
        right = False

        for pos, letter in enumerate(choiced):
            if e.control.content.value == letter:
                word.controls[pos] = discover(letter)
                right = True
        
        if not right:
            character.data += 1
            miss = character.data
            character.src = f"assets/imgs/forca_{miss}.png"
            character.update()

        word.update()

        e.control.disabled = True
        e.control.content.color = ft.colors.PRIMARY
        e.control.update()
        page.update()

    word = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            discover('_') for _ in choiced
        ]
    )

    character = ft.Image(
        data=0,
        src="assets/imgs/forca_0.png",
        width=400,
        height=400
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
        on_click=valitade,
        ) for letter in string.ascii_uppercase
    ]
    

    main_container_teclado = ft.Container(
        margin=ft.margin.only(bottom=50),
        opacity=0.8,
        padding=5,
        shadow=ft.BoxShadow(
            blur_radius=20,
            spread_radius=20,
            color=ft.colors.PRIMARY,
        ),
        border_radius=10,
        content= ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls = [
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

    return ft.Container(
        opacity=0.8,
        padding=10,
        content= ft.Column(
            expand=True,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls = [
                character,
                word,
                main_container_teclado,
            ]
        )
    )