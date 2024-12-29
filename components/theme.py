import flet as ft


def theme_game(page: ft.Page):
    def change_theme(e):
        text = e.control.parent.controls[0].value
        text = "Países" if text == "Frutas" else "Frutas"
        e.control.parent.controls[0].value = text
        page.update()

    return ft.Row(
        controls=[
            ft.Text(
                value="Frutas",
                color=ft.colors.WHITE,
                size=30,
                weight=ft.FontWeight.BOLD,
                font_family='Poppins',
            ),
            ft.IconButton(
                icon=ft.icons.CHANGE_CIRCLE,
                icon_color=ft.colors.WHITE,
                icon_size=30,
                on_click=change_theme,
            )
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )