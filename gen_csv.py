import pandas as pd
import numpy as np

# Установка параметров для генерации данных
np.random.seed(42)
n_samples = 100

# Генерация данных
data = {
    "development_cost": np.random.normal(200000, 30000, n_samples),
    "marketing_cost": np.random.normal(100000, 20000, n_samples),
    "infrastructure_cost": np.random.normal(50000, 15000, n_samples),
    "cash_flow": np.random.normal(300000, 50000, n_samples),
}
data["total_expenses"] = data["development_cost"] + data["marketing_cost"] + data["infrastructure_cost"]

# Преобразование в DataFrame
df = pd.DataFrame(data)

# Сохранение в файл
file_path = "it_financial_data.csv"
df.to_csv(file_path, index=False)
