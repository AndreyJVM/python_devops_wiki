#!/usr/bin/env python3

# ./platform_demo.py
# sys.platform - определяет ОС (linux, darwin, win32)
# sys.version_info - версия Python (major, minor, micro)
#   - Выбор правильных команд для ОС (ls vs dir)
#   - Кросс-платформенные скрипты

import sys

print(f"ОС: {sys.platform}")

ver = sys.version_info
print(f"Python: {ver.major}.{ver.minor}.{ver.micro}")

if sys.platform == "win32":
    cmd = "dir"
elif sys.platform in ["linux", "darwin"]:
    cmd = "ls -la"
else:
    cmd = "ОС не определена"
    sys.exit(4)

print(f"Команда для ОС: {cmd}")

if ver.major < 3 or (ver.major == 3 and ver.minor < 8):
    print("Требуется Python 3.8+")
    sys.exit(1)
else:
    print("Версия Python подходит")