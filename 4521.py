from random import randint as random
import pickle  # Полезный модуль для хранения сложных объектов, в данном случае - словаря с заметками

from colorama import init
from termcolor import colored  # Подключение модулей, связанных с покраской текста в консоли.

class Settings:
    font_color = ""
    autosave = bool()
    custom_id = bool()


    def __init__(self):        # Настройки по умолчанию
        self.font_color = "white"
        self.autosave = False
        self.custom_id = False

    def change_settings(self):
        print("Выберите настройку, которую хотите изменить (font_color, autosave, custom_id): ")
        setting = input()

        if setting == "font_color":
            color = input("Введите цвет выводиой заметки (red, green, yellow, white)\n")
            if color in set_colors:
                self.set_font_color(color)
                return
            else:
                print("Данные были введены некорректно, попробуйте ещё раз")
                self.change_settings()
                return

        elif setting == "autosave":
            state = input("Включить автосохранение только что введённой заметки в отдельный файл? (on, off)\n")
            if state == "on":
                self.set_autosave(True)
                return
            elif state == "off":
                self.set_autosave(False)
                return
            else:
                print("Данные были введены некорректно, попробуйте ещё раз")
                self.change_settings()
                return

        elif setting == "custom_id":
            state = input("Включить возможность задавать свой id только что введённой заметке? (on, off)\n")
            if state == "on":
                self.set_id(True)
                return
            elif state == "off":
                self.set_id(False)
                return
            else:
                print("Данные были введены некорректно, попробуйте ещё раз")
                self.change_settings()
                return

        else:
                print("Данные были введены некорректно, попробуйте ещё раз")
                self.change_settings()
                return

    def set_font_color(self, color):
        self.font_color = color
        return

    def set_autosave(self, state):
        self.autosave = state
        return

    def set_id(self, state):
        self.custom_id = state
        return


def main_menu():
    print("\nГлавное меню\n")
    selected_point = input("Выберите что вы хотите сделать(write a note, get a note, change settings, exit the program)\n")
    if selected_point == "write a note":
        add_note(my_settings)
    elif selected_point == "get a note":
        get_id_note()
    elif selected_point == "change settings":
        my_settings.change_settings()
    elif selected_point == "exit the program":
        return exit_the_program()
    else:
        print("Ответ был введён некорректно. попробуйте ещё раз.")
        return main_menu()
    return

def exit_the_program():
    return True

def add_note(my_settings):
    note = input("Введите новую заметку\n")

    if my_settings.custom_id == True:
        key = input("Введите id вашей заметки\n")
        print("id вашей заметки: ", colored(key, "red"))
    else:
        key = str(random(1, 99))
        print("id вашей заметки: ", colored(key, "green"))

    if my_settings.autosave == True:
        print("Ваша заметка сохранена в отдельный файл и находится там же где файл программы")
        path = str(key) + ".txt"
        with open(path, "w") as file:
            file.write(note)

    notebook[key] = note
    return

def get_id_note():
    print("Список всех доступных заметок:")
    for key in notebook.keys():
        print("--->", colored(key, "red"))

    id = input("Укажите id заметки, которую хотите прочесть:  ")
    if id in notebook:
        get_note(id, my_settings)
    else:
        print("Ошибка! Заметки нет в дневнике. Попробуйте ещё раз")
        get_id_note(my_settings)

    return

def get_note(id, my_settings):
    note = notebook.get(id)
    print(colored(note, my_settings.font_color))
    return


"""
Блок самой программы, все объявленные функции зациклены между собой, то есть перевызывают друг друга.
                                            Только одна функция выходит обратно в основную программу.
"""
init()                         # Функция, адаптирующая модуль для Windows
try:
    with open("Notebook.txt", "rb") as file:
        notebook = pickle.load(file)               # Вытаскивание словаря из файла

except FileNotFoundError:
    notebook = {}
    print("\n{} \n{} \n{}" .format(\
            "Вы запускаете эту программу в первый раз, желаем вам приятного использования))", \
            "В данный момент ни один дневник не найден.", \
            "Будет создан новый после завершения программы", \
    ))

set_colors = {"red", "green", "yellow", "white"}
my_settings = Settings() #создаётся профиль настроек

end_the_progam = False

while end_the_progam is not True:
    end_the_progam = bool(main_menu())


with open("Notebook.txt", "wb") as file:
    pickle.dump(notebook, file)

