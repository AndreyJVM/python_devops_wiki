#!/usr/bin/env python3

import sys

print("Это в терминале")

# Сохраняем оригинал
original = sys.stdout

# Пишем в файл
sys.stdout = open('log.txt', 'w')
print("Это в логе")
print("Это в логе 1")
print("Это в логе 2")
sys.stdout = original  # Восстанавливаем

print("И это в терминале")