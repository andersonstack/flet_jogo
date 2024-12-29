import flet as ft
import string
from random import choice

list_fruits = [
    "ABACATE",
    "ABACAXI",
    "ACEROLA",
    "AMEIXA",
    "AMORA",
    "BANANA",
    "CAQUI",
    "CARAMBOLA",
    "CEREJA",
    "DAMASCO",
    "FIGO",
    "FRAMBOESA",
    "GOIABA",
    "GRAVIOLA",
    "GUARANÁ",
    "JABUTICABA",
    "JACA",
    "KIWI",
    "LARANJA",
    "LICHIA",
    "MANGA",
    "MELANCIA",
    "MIRTIILO",
    "MORANGO",
    "NECTARINA",
    "PERA",
    "PITANGA",
    "PITAYA",
    "SAPOTI",
    "SERIGUELA",
    "TAMARINDO",
    "TANGERINA",
    "TORANJA",
    "UMBU",
    "UVA",
    "COCO",
    "ABRICO",
    "BACABA",
    "BURITI",
    "PISTACHE",
    "MEXERICA",
    "GUABIROBA",
    "MUNGUBA",
    "PAINEIRA",
    "GRUMIXAMA",
    "CAMU",
    "JENIPAPO",
    "ARATICUM",
    "JAMBO",
    "QUINCE",
    "MARAJOARA",
    "SAPUCAIA",
    "GUAVIRA",
    "ACARI",
    "MANJERICÃO",
    "BERGAMOTA",
    "BUCHA",
    "CACAU",
    "CITRON",
    "MANGABA",
    "ADELFA",
    "BERIBA",
    "OLIVEIRA",
    "BIMBIM",
    "CAJUEIRO",
    "CASCUDO",
    "CACAUEIRO",
    "CAMUCAMU",
    "ANONA",
    "CAJUEIRO",
    "CORINDA",
    "CAMBUCI",
    "COROCO",
    "BACUPARI",
]


list_countrys = [
    "AFEGANISTÃO",
    "ALEMANHA",
    "ANDORRA",
    "ANGOLA",
    "ARGÉLIA",
    "ARGENTINA",
    "AZERBAIJÃO",
    "BAHAMAS",
    "BANGLADESH",
    "BARBADOS",
    "BAREIN",
    "BELIZE",
    "BENIM",
    "BIELORRÚSSIA",
    "BOTSUANA",
    "BRASIL",
    "BRUNEI",
    "BURKINA FASO",
    "BURUNDI",
    "CAMBOJA",
    "CATAR",
    "CHILE",
    "CHINA",
    "CHIPRE",
    "COMORES",
    "CUBA",
    "DINAMARCA",
    "DOMÍNICA",
    "EGITO",
    "EQUADOR",
    "ERITREIA",
    "ESPANHA",
    "ESTADOS UNIDOS",
    "FILIPINAS",
    "FINLÂNDIA",
    "GANA",
    "GRANADA",
    "GUATEMALA",
    "GUIANA",
    "HAITI",
    "HOLANDA",
    "HONDURAS",
    "HUNGRIA",
    "INDONÉSIA",
    "IRAQUE",
    "IRLANDA",
    "ISRAEL",
    "JAMAICA",
    "KIRIBATI",
    "KUWAIT",
    "LAOS",
    "LESOTO",
    "LIECHTENSTEIN",
    "LUXEMBURGO",
]


def keyboard(page: ft.Page, theme="Frutas", reset_game=None):
    choiced = choice(list_fruits) if theme == "Frutas" else choice(list_countrys)
    global dicas
    dicas = 3 if len(choiced) >= 7 else 2 if len(choiced) >= 5 else 1

    def restart_game(e):
        print("BOTÃO CLICADO")
        if reset_game:
            # Resetando os componentes
            word.controls = [discover('_') for _ in choiced]  # Resetando a palavra
            character.src = "assets/imgs/forca_0.png"  # Resetando a imagem da forca
            character.data = 0  # Resetando o número de tentativas erradas
            main_container_gamer.controls[0].visible = False  # Ocultando a mensagem de vitória/derrota
            main_container_gamer.controls[1].visible = True  # Mantendo o botão de reiniciar
            dicas = 3 if len(choiced) >= 7 else 2 if len(choiced) >= 5 else 1  # Resetando as dicas
            word.update()  # Atualizando a exibição da palavra
            character.update()  # Atualizando a imagem da forca
            # Resetar as teclas e seus estados
            for button in main_container_teclas:
                button.content.color = ft.colors.WHITE
                button.disabled = False
                button.update()
            page.update()  # Atualizando a página

    

    def discover(letter):
        return ft.Container(
            height=40,
            width=40,
            border_radius=20,
            bgcolor=ft.colors.WHITE,
            content=ft.Text(
                value=letter,
                font_family="MADE_TOMMY_BOLD",
                color=ft.colors.BLACK,
                size=15,
                text_align=ft.TextAlign.CENTER,
                weight=ft.FontWeight.BOLD,
            ),
            alignment=ft.alignment.center,
        )

    def tip(e):
        global dicas
        if dicas == 0:
            e.control.disabled = True
            return

        letter_to_reveal = choice(choiced)
        
        for pos, letter in enumerate(choiced):
            if letter == letter_to_reveal:
                word.controls[pos] = discover(letter)
        
        dicas -= 1
        e.control.parent.controls[1].value = f"Dicas: {dicas}"
        e.control.parent.controls[1].update()
        
        word.update()
        
    def validate(e):
        right = False

        for pos, letter in enumerate(choiced):
            if e.control.content.value == letter:
                word.controls[pos] = discover(letter)
                right = True

        if not right:
            character.data += 1

            if character.data > 5:
                main_container_gamer.controls[0].visible = True
                main_container_gamer.controls[1].visible = True
                main_container_gamer.controls[0].value = "YOU LOSE!"
                main_container_gamer.update()

            miss = character.data
            character.src = f"assets/imgs/forca_{miss}.png"
            character.update()

        word.update()
        e.control.disabled = True
        e.control.content.color = ft.colors.PRIMARY
        e.control.update()

        if all(c.content.value != '_' for c in word.controls):
            main_container_gamer.controls[0].visible = True
            main_container_gamer.controls[1].visible = True
            main_container_gamer.controls[0].value = "YOU WIN!"
            main_container_gamer.update()

        page.update()

    word = ft.Row(
        wrap=True,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            discover('_') for _ in choiced
        ]
    )

    character = ft.Image(
        data=0,
        src="assets/imgs/forca_0.png",
        width=400,
        height=400,
    )

    main_container_teclas = [
        ft.Container(
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
                weight=ft.FontWeight.BOLD,
            ),
            alignment=ft.alignment.center,
            on_click=validate,
        ) for letter in string.ascii_uppercase
    ]

    main_container_teclado = ft.Container(
        margin=ft.margin.only(bottom=50, top=50),
        opacity=0.8,
        padding=5,
        shadow=ft.BoxShadow(
            blur_radius=20,
            spread_radius=20,
            color=ft.colors.PRIMARY,
        ),
        border_radius=10,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                ft.Row(
                    expand=True,
                    wrap=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=main_container_teclas,
                )
            ]
        ),
    )

    main_container_gamer = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Text(
                value="YOU WIN!",
                font_family="MADE_TOMMY_BOLD",
                color=ft.colors.WHITE,
                size=30,
                text_align=ft.TextAlign.CENTER,
                weight=ft.FontWeight.BOLD,
                visible=False
            ),
            ft.IconButton(
                icon=ft.icons.REPLAY,
                icon_color=ft.colors.WHITE,
                visible=False,
                on_click=restart_game
            )
        ]
    )

    return ft.Container(
        opacity=0.8,
        padding=10,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                main_container_gamer,
                character,
                word,
                main_container_teclado,
                ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.TIPS_AND_UPDATES,
                            icon_color=ft.colors.WHITE,
                            on_click=tip
                        ),
                        ft.Text(
                            value=f"Dicas: {dicas}",)
                    ]
                )
            ]
        ),
    )
