import threading
from editor import create_editor_window
from renderer import start_render

def main():
    # Запуск окна редактора в отдельном потоке
    editor_thread = threading.Thread(target=create_editor_window)
    editor_thread.start()

    # Параллельно запускаем рендеринг в Pygame
    start_render()

if __name__ == "__main__":
    main()
