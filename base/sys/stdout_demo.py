#!/usr/bin/env python3

# ./stdout_demo.py
# sys.stdout — куда пишутся логи
# sys.stderr — отдельный поток для ошибок

import sys

print("Это в консоли")

# Сохраняем и перенаправляем stdout в файл
original = sys.stdout
sys.stdout = open("log.txt", "w")

print("Это в файле log.txt")
print("Тоже в файле")

# Восстанавливаем stdout
sys.stdout = original

print("Снова в консоли")

# Показываем содержимое лога
with open("log.txt", "r") as f:
    print(f"\nСодержимое log.txt:\n{f.read()}")

# stderr — для ошибок
print("Это ошибка", file=sys.stderr)