import flet as ft
import string
from random import choice

list_fruits = [
    "ABACATE",
    "ABACAXI",
    "ACEROLA",
    "AMEIXA",
    "AMORA",
    "AÇAÍ",
    "BANANA",
    "CAQUI",
    "CARAMBOLA",
    "CEREJA",
    "CUPUAÇU",
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
    "LIMÃO",
    "LICHIA",
    "MAÇÃ",
    "MAMÃO",
    "MANGA",
    "MARACUJÁ",
    "MELANCIA",
    "MELÃO",
    "MIRTIILO",
    "MORANGO",
    "NECTARINA",
    "NOZ-PECÃ",
    "PÊSSEGO",
    "PERA",
    "PITANGA",
    "PITAYA",
    "ROMÃ",
    "SAPOTI",
    "SERIGUELA",
    "TAMARINDO",
    "TANGERINA",
    "TORANJA",
    "UMBU",
    "UVA",
    "UVAS-PASSAS",
    "COCO",
    "ABRICO",
    "JATOBÁ",
    "BACABA",
    "CAMU-CAMU",
    "MACADÂMIA",
    "CASTANHA-DO-PARÁ",
    "BURITI",
    "PISTACHE",
    "MEXERICA",
    "GUABIROBA",
    "TUCUMÃ",
    "MUNGUBA",
    "PAINEIRA",
    "GRUMIXAMA",
    "CAMU",
    "BIRIBÁ",
    "JENIPAPO",
    "ARATICUM",
    "JAMBO",
    "QUINCE",
    "MARAJOARA",
    "SAPUCAIA",
    "CAJÁ",
    "GUAVIRA",
    "ACARI",
    "MANJERICÃO",
    "BERGAMOTA",
    "BUCHA",
    "CACAU",
    "CITRON",
    "FOIÁ",
    "MANGABA",
    "ADELFA",
    "BERIBA",
    "OLIVEIRA",
    "BIMBIM",
    "BATAUÁ",
    "CAJUEIRO",
    "MOCOTÓ",
    "CASCUDO",
    "GUACÁ",
    "CACAUEIRO",
    "CAMUCAMU",
    "ANONA",
    "CAJUEIRO",
    "CORINDA",
    "CAMBUCI",
    "CAMARÃO",
    "COROCO",
    "BACUPARI",
    "BUTIÁ",
    "CAÁ-ATÃ",
    "GUAMÁ",
    "ARACUÃ"
]


list_countrys = [
    "AFEGANISTÃO",
    "ÁFRICA DO SUL",
    "ALBÂNIA",
    "ALEMANHA",
    "ANDORRA",
    "ANGOLA",
    "ANTÍGUA E BARBUDA",
    "ARÁBIA SAUDITA",
    "ARGÉLIA",
    "ARGENTINA",
    "ARMÊNIA",
    "AUSTRÁLIA",
    "ÁUSTRIA",
    "AZERBAIJÃO",
    "BAHAMAS",
    "BANGLADESH",
    "BARBADOS",
    "BAREIN",
    "BÉLGICA",
    "BELIZE",
    "BENIM",
    "BIELORRÚSSIA",
    "BOLÍVIA",
    "BÓSNIA E HERZEGOVINA",
    "BOTSUANA",
    "BRASIL",
    "BRUNEI",
    "BULGÁRIA",
    "BURKINA FASO",
    "BURUNDI",
    "BUTÃO",
    "CABO VERDE",
    "CAMARÕES",
    "CAMBOJA",
    "CANADÁ",
    "CATAR",
    "CAZAQUISTÃO",
    "CHILE",
    "CHINA",
    "CHIPRE",
    "COLÔMBIA",
    "COMORES",
    "COREIA DO NORTE",
    "COREIA DO SUL",
    "COSTA DO MARFIM",
    "COSTA RICA",
    "CROÁCIA",
    "CUBA",
    "DINAMARCA",
    "DOMÍNICA",
    "EGITO",
    "EMIRADOS ÁRABES UNIDOS",
    "EQUADOR",
    "ERITREIA",
    "ESLOVÁQUIA",
    "ESLOVÊNIA",
    "ESPANHA",
    "ESTADOS UNIDOS",
    "ESTÔNIA",
    "ETIÓPIA",
    "FILIPINAS",
    "FINLÂNDIA",
    "FRANÇA",
    "GABÃO",
    "GÂMBIA",
    "GANA",
    "GEÓRGIA",
    "GRÉCIA",
    "GRANADA",
    "GUATEMALA",
    "GUIANA",
    "GUINÉ",
    "GUINÉ-BISSAU",
    "GUINÉ EQUATORIAL",
    "HAITI",
    "HOLANDA",
    "HONDURAS",
    "HUNGRIA",
    "IÊMEN",
    "ILHAS FIJI",
    "ILHAS MALDIVAS",
    "ÍNDIA",
    "INDONÉSIA",
    "IRÃ",
    "IRAQUE",
    "IRLANDA",
    "ISLÂNDIA",
    "ISRAEL",
    "ITÁLIA",
    "JAMAICA",
    "JAPÃO",
    "JORDÂNIA",
    "KÊNIA",
    "KIRGUISTÃO",
    "KIRIBATI",
    "KUWAIT",
    "LAOS",
    "LESOTO",
    "LETÔNIA",
    "LÍBANO",
    "LIBÉRIA",
    "LÍBIA",
    "LIECHTENSTEIN",
    "LITUÂNIA",
    "LUXEMBURGO",
    "MACEDÔNIA DO NORTE",
]


def keyboard(page: ft.Page, theme="Frutas"):
    choiced = choice(list_fruits) if theme == "Frutas" else choice(list_countrys)

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

    def validate(e):
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

    return ft.Container(
        opacity=0.8,
        padding=10,
        content=ft.Column(
            expand=True,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                character,
                word,
                main_container_teclado,
            ]
        ),
    )
