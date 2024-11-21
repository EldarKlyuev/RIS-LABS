import pandas as pd
import numpy as np
from tkinter import *
from tkinter import ttk, messagebox
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Загрузка данных
data = pd.read_csv("financial_data.csv")

# Инициализация модели линейной регрессии
X = data[['production_cost', 'labor_cost', 'materials_cost']]
y = data['total_expenses']
model = LinearRegression()
model.fit(X, y)

# Настройка окна tkinter
root = Tk()
root.title("Экспертная система финансового планирования")
root.geometry("600x400")

# Создание вкладок
tabControl = ttk.Notebook(root)
tab_forecasting = ttk.Frame(tabControl)
tab_budget = ttk.Frame(tabControl)
tab_risk = ttk.Frame(tabControl)
tabControl.add(tab_forecasting, text='Прогнозирование')
tabControl.add(tab_budget, text='Оптимизация бюджета')
tabControl.add(tab_risk, text='Анализ риска')
tabControl.pack(expand=1, fill="both")


# Функция для прогноза денежных потоков
def forecast_cash_flow():
    cash_flow = data['cash_flow']
    model = ARIMA(cash_flow, order=(1, 1, 1))
    arima_model = model.fit()
    forecast = arima_model.forecast(steps=12)
    messagebox.showinfo("Прогноз", f"Прогноз денежных потоков на 12 месяцев: {forecast}")


# Вкладка Прогнозирования
forecast_label = Label(tab_forecasting, text="Прогноз денежных потоков", font=("Arial", 14))
forecast_label.pack(pady=10)
forecast_button = Button(tab_forecasting, text="Рассчитать прогноз", command=forecast_cash_flow)
forecast_button.pack(pady=10)


# Функция для оптимизации бюджета
def optimize_budget():
    try:
        production_cost = float(entry_production_cost.get())
        labor_cost = float(entry_labor_cost.get())
        materials_cost = float(entry_materials_cost.get())

        future_costs = pd.DataFrame({
            'production_cost': [production_cost],
            'labor_cost': [labor_cost],
            'materials_cost': [materials_cost]
        })

        predicted_expenses = model.predict(future_costs)
        messagebox.showinfo("Прогнозируемые расходы", f"Прогнозируемые расходы: {predicted_expenses[0]}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите числовые значения.")


# Вкладка Оптимизации бюджета
Label(tab_budget, text="Оптимизация бюджета", font=("Arial", 14)).pack(pady=10)
Label(tab_budget, text="Стоимость производства:").pack()
entry_production_cost = Entry(tab_budget)
entry_production_cost.pack()
Label(tab_budget, text="Затраты на рабочую силу:").pack()
entry_labor_cost = Entry(tab_budget)
entry_labor_cost.pack()
Label(tab_budget, text="Стоимость материалов:").pack()
entry_materials_cost = Entry(tab_budget)
entry_materials_cost.pack()
optimize_button = Button(tab_budget, text="Рассчитать расходы", command=optimize_budget)
optimize_button.pack(pady=10)


# Функция для анализа риска
def risk_analysis():
    iterations = 1000
    forecast_values = []

    for i in range(iterations):
        production_cost = np.random.normal(100000, 10000)
        labor_cost = np.random.normal(50000, 8000)
        materials_cost = np.random.normal(30000, 5000)
        total_expenses = production_cost + labor_cost + materials_cost
        forecast_values.append(total_expenses)

    plt.hist(forecast_values, bins=50, color='skyblue')
    plt.xlabel('Общие расходы')
    plt.ylabel('Частота')
    plt.title('Анализ риска на основе Монте-Карло')
    plt.show()


# Вкладка Анализа рисков
Label(tab_risk, text="Анализ риска", font=("Arial", 14)).pack(pady=10)
risk_button = Button(tab_risk, text="Запустить анализ риска", command=risk_analysis)
risk_button.pack(pady=10)

# Запуск интерфейса
root.mainloop()
