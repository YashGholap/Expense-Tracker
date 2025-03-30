import flet as ft


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.title = "Expense Tracker"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    header = ft.Container(
        content = ft.Text("Welcome to Expense Tracker!", weight=ft.FontWeight.BOLD, size=36),
        padding=ft.padding.only(top=50)
    )
    page.add(header)
    page.update()
    
    
ft.app(main)