#!/usr/bin/env python3

import sys

# Показываем первые 3 пути
print("Python ищет модули в:")
for p in sys.path[:4]:
    print(f"  • {p}")

# Отображаем общее кл-во
print(f"\nВсего путей: {len(sys.path)}")