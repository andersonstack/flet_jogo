import flet as ft 


def word():
    return ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Text(
                value="",
                color=ft.colors.WHITE,
                size=25,
                weight=ft.FontWeight.BOLD
            )
        ]
    )