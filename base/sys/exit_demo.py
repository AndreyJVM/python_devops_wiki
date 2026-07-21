#!/usr/bin/env python3

# ./exit_demo.py production
# sys.exit(0) — успех (CI/CD продолжает)
# sys.exit(45) — ошибка (CI/CD останавливает)

import sys

if len(sys.argv) < 2:
    print("Ошибка: не указана среда")
    print(f"Использование: {sys.argv[0]} <production|staging>")
    sys.exit(1)

env = sys.argv[1]

if env == "production":
    print("Деплой на production")
    sys.exit(0)
elif env == "test":
    print("Деплой на test")
    sys.exit(0)
else:
    print(f"Ошибка: неизвестная среда {env}")
    sys.exit(1)