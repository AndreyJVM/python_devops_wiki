import sys

# sys.argv[0] — имя скрипта
print(f"Скрипт: {sys.argv[0]}")

# sys.argv[1] — первый аргумент
name = sys.argv[1] if len(sys.argv) > 1 else "мир"
print(f"Привет, {name}!")
