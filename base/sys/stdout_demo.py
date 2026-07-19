import sys

# Сохраняем оригинал
original = sys.stdout

# Пишем в файл
sys.stdout = open('log.txt', 'w')
print("Это в логе")
sys.stdout = original  # Восстанавливаем

print("А это в консоли")