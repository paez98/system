import flet as ft
# from windows.login import contenedor

contenedor = ft.Container(
    ft.Column([
        ft.Container(
            ft.Text(
                "Iniciar Sesión",
                width=320,
                size=25,
                weight="w900",
                font_family="Comfortaa",
                text_align="center"),
            padding=ft.padding.only(20, 20)
        ),
        ft.Container(
            ft.TextField(
                width=280,
                label="Usuario",
                prefix_icon=ft.icons.PERSON,
                border="underline",
                hint_text="Coloca tu nombre de usuario",
            ),
            padding=ft.padding.only(20, 20)
        ),
        ft.Container(
            ft.TextField(
                width=280,
                label="Contraseña",
                prefix_icon=ft.icons.LOCK,
                border="underline",
                password=True,
                can_reveal_password=True
            ),
            padding=ft.padding.only(20, 20)
        ),
        ft.Container(
            ft.Checkbox(
                label="Recordar contraseña"
            ),
            padding=ft.padding.only(80)
        ),
        ft.Container(
            ft.ElevatedButton(
                text= "Entrar",
                width= 120,
            ),
            padding=ft.padding.only(left=100, right=100)
        )
    ],
        ft.MainAxisAlignment.SPACE_EVENLY),



    width=320,
    height=400,
    alignment=ft.alignment.center,
    border_radius=20,
    gradient=ft.LinearGradient([
        "#3E97D3"
    ]),

)


def main(page: ft.Page):
    page.bgcolor = "black"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.add(contenedor)


ft.app(target=main)
