import pandas as pd
import numpy as np

# Генерация данных
np.random.seed(42)

data = {
    'cash_flow': np.random.randint(50000, 150000, size=24),  # Денежные потоки за 24 месяца
    'production_cost': np.random.randint(80000, 120000, size=24),  # Затраты на производство
    'labor_cost': np.random.randint(30000, 50000, size=24),  # Затраты на оплату труда
    'materials_cost': np.random.randint(20000, 40000, size=24),  # Затраты на материалы
    'total_expenses': np.random.randint(150000, 200000, size=24),  # Общие расходы
    'current_assets': np.random.randint(200000, 400000, size=24),  # Оборотные активы
    'current_liabilities': np.random.randint(100000, 200000, size=24),  # Текущие обязательства
    'total_debt': np.random.randint(500000, 800000, size=24),  # Общий долг
    'equity': np.random.randint(300000, 600000, size=24)  # Собственный капитал
}

# Создание DataFrame
df = pd.DataFrame(data)

# Сохранение в CSV
df.to_csv("financial_data.csv", index=False)

print("Датасет сохранен в файл 'financial_data.csv'")
