import flet as ft


def main(page: ft.Page):
    contenedor = ft.Container(
        #alignment= ft.alignment.center_right,
        bgcolor= "#324359",
        #border= 2,
        border_radius= ft.border_radius.all(20),
        padding= 20,
        content= ft.Column(
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
            #alignment= ft.alignment.top_center,
            controls= [
                ft.Text("Iniciar Sesión", color= "white",font_family="Comfortaa"),
                ft.TextField(bgcolor="white",icon=ft.icons.EMOJI_EMOTIONS_ROUNDED,label="Nombre", hint_text="Coloca tu nombre", width=200, border= ft.InputBorder.UNDERLINE, adaptive=True),
                ft.TextField(bgcolor="white",icon=ft.icons.LOCK_ROUNDED, label="Contraseña",password=True, can_reveal_password=True, width=200, border= ft.InputBorder.UNDERLINE, adaptive=True, tooltip="Coloca tu contraseña"),
                ft.ElevatedButton("Entrar")
            ]
        )
    )
    page.theme = ft.Theme(color_scheme_seed="Indigo")
    page.title = "Sistema Administrativo"
    page.add(contenedor)
    # page.theme_mode = ft.ThemeMode.SYSTEM


ft.app(main)

    # container = ft.Container(
    #     width=300
    #     ft.Column(
    #         alignment=ft.alignment.center,
    #         col={"sm": 6},
    #         controls=[
    #             ft.Text("Iniciar Sesión", font_family="Comfortaa",),
    #             ft.TextField(icon=ft.icons.EMOJI_EMOTIONS_ROUNDED,
    #                          label="Nombre", hint_text="Coloca tu nombre", width=180, ),
    #             ft.TextField(icon=ft.icons.LOCK_ROUNDED, label="Contraseña",
    #                          password=True, can_reveal_password=True, width=180),
    #         ]
    #     ))