# Решатель квадратных уравнений

Скрипт для вычисления корней квадратного уравнения.

# Как использовать

Скрипт на вход получает 3 числа, являющиеся коэффициентами.

Пример использования в коде:
```
>>> from quadratic_equation import get_roots
>>> print(get_roots(coef_a, coef_b, coef_c)) # где a, b и c - коэффициенты 
```

Возвращает два корня, если дискриминант квадратного уравнения больше нуля
Возвращает один корень и None, если дискриминант равен нулю
Возвращает два None, если дискриминант отрицателен

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash
python tests.py # может понадобиться вызов python3 вместо python, зависит от настроек операционной системы
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)
