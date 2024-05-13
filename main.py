import flet as ft


def main(page: ft.Page):
    contenedor2 = ft.Container(
        bgcolor='#1ED5B9',
        border_radius=ft.border_radius.all(20),
        content=ft.Column(
            width=300,
            height=500,
            controls=[
                ft.Image()
            ]
        )
    )
    contenedor = ft.Container(
        bgcolor="#324359",
        border_radius=ft.border_radius.all(20),
        content=ft.Row(
            width=750,
            controls=[
                ft.Column(
                    width=300,
                    height=500,
                    controls=[
                        ft.Image(
                            'paper.jpg', fit=ft.ImageFit.COVER, height=1000)
                    ]
                ),
                ft.Column(
                    spacing=50,
                    width=300,
                    height=500,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text("Iniciar Sesión", color="white",font_family="Comfortaa"),
                        ft.TextField(icon=ft.icons.EMOJI_EMOTIONS_ROUNDED, label="Nombre",
                                     hint_text="Coloca tu nombre", width=200, border=ft.InputBorder.UNDERLINE, adaptive=True),
                        ft.TextField(color='#2BD9A8', icon=ft.icons.LOCK_ROUNDED, label="Contraseña", password=True,
                                     can_reveal_password=True, width=200, border=ft.InputBorder.UNDERLINE, adaptive=True),
                        ft.ElevatedButton("Entrar", bgcolor='#1ED5B9')
                    ]
                )])
    )

    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.theme = ft.Theme(color_scheme_seed="Indigo")
    page.title = "Sistema Administrativo"
    page.add(contenedor)

    # page.theme_mode = ft.ThemeMode.SYSTEM


ft.app(main)
