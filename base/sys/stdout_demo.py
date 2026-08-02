#!/usr/bin/env python3

# ./stdout_demo.py
# sys.stdout - куда пишутся логи
# sys.stderr - отдельный поток для ошибок

import sys

print("[info: Это в консоли]")
print("[Записываю логи приложения в файл...]")
# Сохраняем и перенаправляем stdout в файл
original = sys.stdout
sys.stdout = open("log.txt", "w")

print("Это в файле log.txt")
print("Тоже в файле")

# Восстанавливаем stdout в консоль
sys.stdout = original

print("[Конец записи логов...]")
print("[info: вывод в консоли]")

# stderr — для ошибок
print("[Это ошибка]", file=sys.stderr)