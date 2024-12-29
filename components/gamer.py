import flet as ft 


def gamer(new_data):
    print("NEW_DATA", new_data)

    if new_data == 1:
        return ft.Container(
            bgcolor=ft.colors.TRANSPARENT,
            content=ft.Column(
                controls=[
                    ft.Image(
                        data=1,
                        src="assets/imgs/forca_1.png",
                        width=400,
                        height=400
                    )
                ]
            ),
        )

    return ft.Container(
        bgcolor=ft.colors.TRANSPARENT,
        content=ft.Column(
            controls=[
                ft.Image(
                    data=0,
                    src="assets/imgs/forca_0.png",
                    width=400,
                    height=400
                )
            ]
        ),
    )