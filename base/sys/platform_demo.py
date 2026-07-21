#!/usr/bin/env python3

# ./platform_demo.py
# sys.platform — определяет ОС (linux, darwin, win32)
# sys.version_info — версия Python (major, minor, micro)
#
# Зачем в DevOps:
#   • Выбор правильных команд для ОС (ls vs dir)
#   • Проверка версии Python перед деплоем
#   • Кросс-платформенные скрипты

import sys

# 1. Определяем операционную систему
print(f"ОС: {sys.platform}")

# 2. Проверяем версию Python
ver = sys.version_info
print(f"Python: {ver.major}.{ver.minor}.{ver.micro}")

# 3. Выбираем команду в зависимости от ОС
if sys.platform == "win32":
    cmd = "dir"
elif sys.platform in ["linux", "darwin"]:
    cmd = "ls -la"
else:
    cmd = "unknown"

print(f"Команда для ОС: {cmd}")

# 4. Проверяем, подходит ли версия Python
if ver.major < 3 or (ver.major == 3 and ver.minor < 8):
    print("Требуется Python 3.8+")
    sys.exit(1)
else:
    print("Версия Python подходит")