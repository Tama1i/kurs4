import tkinter as tk
from tkinter import ttk
from model import add_fundament, stretch_wall_between_columns, add_roof, building_model
from model import export_to_obj


def create_editor_window():
    window = tk.Tk()
    window.title("Редактирование модели")

    # Поля ввода для параметров фундамента
    tk.Label(window, text="Фундамент:").grid(row=0, column=0)
    foundation_length = tk.Entry(window)
    foundation_length.grid(row=0, column=1)
    foundation_length.insert(0, "5")

    tk.Label(window, text="Ширина фундамента:").grid(row=1, column=0)
    foundation_width = tk.Entry(window)
    foundation_width.grid(row=1, column=1)
    foundation_width.insert(0, "4")

    tk.Label(window, text="Высота фундамента:").grid(row=2, column=0)
    foundation_height = tk.Entry(window)
    foundation_height.grid(row=2, column=1)
    foundation_height.insert(0, "1")

    tk.Label(window, text="Выберите сторону:").grid(row=3, column=0)
    relative_side = tk.StringVar(window)
    relative_side.set("right")
    side_menu = tk.OptionMenu(window, relative_side, "right", "left", "front", "back")
    side_menu.grid(row=3, column=1)


    def apply_fundament_changes():
        try:
            length = float(foundation_length.get())
            width = float(foundation_width.get())
            height = float(foundation_height.get())
            add_fundament(length, width, height, relative_side.get())
            print("Фундамент добавлен!")
        except ValueError:
            print("Ошибка: Некорректные значения.")

    tk.Button(window, text="Добавить фундамент", command=apply_fundament_changes).grid(row=4, column=0, columnspan=2)
    tk.Button(window, text="Установить крышу", command=add_roof).grid(row=5, column=0, columnspan=2)
    tk.Button(window, text="Сохранить модель", command=lambda: export_to_obj("saved_model.obj")).grid(row=12, column=0, columnspan=2)

    window.mainloop()
