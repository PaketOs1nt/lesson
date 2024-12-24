import colorama

colorama.init(autoreset=True)

def asd(a, b):
    return a+b

table = {
    'colorama.init': "Дуже важлива функцiя для того щоб модуль працював нормально, по словам ChatGPT - патчить консоль (якщо на windows) для того щоб вона пiдтримувала ANSI",
    'colorama.Fore/Back': "Списки ANSI кодiв для того щоб мiняти кольор тексту або фону у деяких участках",
    'colorama.Cursor': "Функкцiя для управлiнням курсором ввода у консолi"
}

for obj, text in table.items():
    print(f"{colorama.Fore.GREEN}[{obj}]:\n{colorama.Fore.LIGHTGREEN_EX}{text}\n\n")

input(colorama.Fore.YELLOW + 'На мою думку це найважливiшi компоненти для користувача бiблiотеки colorama')