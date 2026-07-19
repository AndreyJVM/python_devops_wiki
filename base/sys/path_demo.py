import sys

# Показываем первые 3 пути
print("Python ищет модули в:")
for p in sys.path[:3]:
    print(f"  • {p}")

# Добавляем свою папку
sys.path.append('/opt/my_libs')
print(f"\nВсего путей: {len(sys.path)}")