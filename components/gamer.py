import flet as ft 


def gamer():
    return ft.Container(
        bgcolor=ft.colors.TRANSPARENT,
        content=ft.Column(
            controls=[
                ft.Image(
                    src="assets/imgs/forca_0.png",
                    width=400,
                    height=400
                )
            ]
        ),
    )