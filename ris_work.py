import pandas as pd
import numpy as np
from tkinter import *
from tkinter import ttk, messagebox
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Загрузка данных
data = pd.read_csv("it_financial_data.csv")

# Инициализация модели линейной регрессии
X = data[['development_cost', 'marketing_cost', 'infrastructure_cost']]
y = data['total_expenses']
model = LinearRegression()
model.fit(X, y)

# Настройка окна tkinter
root = Tk()
root.title("Экспертная система финансового планирования в ИТ")
root.geometry("700x500")

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
    try:
        # Обработка данных
        cash_flow = data['cash_flow']

        # Прогнозирование с использованием ARIMA
        model = ARIMA(cash_flow, order=(2, 1, 2))  # Параметры модели подобраны для примера
        arima_model = model.fit()

        # Прогноз на 12 месяцев
        forecast = arima_model.forecast(steps=12)

        # Создание дат для прогноза
        dates = pd.date_range(start='2023-12-01', periods=12, freq='ME')
        forecast_df = pd.DataFrame({'Дата': dates, 'Прогноз': forecast})

        # Отображение прогноза
        plt.figure(figsize=(10, 6))
        plt.plot(cash_flow, label='Исторический денежный поток')
        plt.plot(range(len(cash_flow), len(cash_flow) + 12), forecast, label='Прогноз', color='red')
        plt.legend()
        plt.title("Прогноз денежных потоков")
        plt.xlabel("Месяцы")
        plt.ylabel("Денежный поток")
        plt.grid(True)
        plt.show()

        messagebox.showinfo("Прогноз",
                            f"Прогноз денежных потоков на 12 месяцев:\n{forecast_df.to_string(index=False)}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка в прогнозировании: {e}")


# Вкладка Прогнозирования
forecast_label = Label(tab_forecasting, text="Прогноз денежных потоков", font=("Arial", 14))
forecast_label.pack(pady=10)
forecast_button = Button(tab_forecasting, text="Рассчитать прогноз", command=forecast_cash_flow)
forecast_button.pack(pady=10)


# Функция для оптимизации бюджета
def optimize_budget():
    try:
        # Получаем значения затрат от пользователя
        development_cost = float(entry_development_cost.get())
        marketing_cost = float(entry_marketing_cost.get())
        infrastructure_cost = float(entry_infrastructure_cost.get())

        # Создаем DataFrame с будущими затратами
        future_costs = pd.DataFrame({
            'development_cost': [development_cost],
            'marketing_cost': [marketing_cost],
            'infrastructure_cost': [infrastructure_cost]
        })

        # Прогнозируем общие расходы с использованием линейной регрессии
        predicted_expenses = model.predict(future_costs)

        # Выводим прогнозируемые расходы
        messagebox.showinfo("Прогнозируемые расходы", f"Прогнозируемые расходы: {predicted_expenses[0]:,.2f}")

        # Логика оптимизации бюджета
        target_expenses = 500000  # Максимально допустимые расходы

        optimized_development_cost = target_expenses - (marketing_cost + infrastructure_cost)
        if optimized_development_cost < 0:
            optimized_development_cost = 0

        optimized_expenses = optimized_development_cost + marketing_cost + infrastructure_cost

        # Выводим результаты оптимизации
        messagebox.showinfo("Оптимизация бюджета",
                            f"Оптимизированные затраты на разработку: {optimized_development_cost:,.2f}\n"
                            f"Общие оптимизированные расходы: {optimized_expenses:,.2f}")

        # Графическое представление результатов
        labels = ['Разработка ПО', 'Маркетинг', 'Инфраструктура', 'Оптимизированная разработка']
        values = [development_cost, marketing_cost, infrastructure_cost, optimized_development_cost]

        plt.figure(figsize=(8, 5))
        plt.bar(labels, values, color=['blue', 'orange', 'green', 'red'])
        plt.title("Сравнение затрат до и после оптимизации")
        plt.ylabel("Затраты")
        plt.show()

    except ValueError:
        messagebox.showerror("Ошибка", "Введите числовые значения для всех затрат.")


# Вкладка Оптимизации бюджета
Label(tab_budget, text="Оптимизация бюджета", font=("Arial", 14)).pack(pady=10)
Label(tab_budget, text="Затраты на разработку ПО:").pack()
entry_development_cost = Entry(tab_budget)
entry_development_cost.pack()
Label(tab_budget, text="Затраты на маркетинг:").pack()
entry_marketing_cost = Entry(tab_budget)
entry_marketing_cost.pack()
Label(tab_budget, text="Затраты на инфраструктуру:").pack()
entry_infrastructure_cost = Entry(tab_budget)
entry_infrastructure_cost.pack()
optimize_button = Button(tab_budget, text="Рассчитать расходы", command=optimize_budget)
optimize_button.pack(pady=10)


# Функция для анализа риска
def risk_analysis():
    iterations = 1000
    forecast_values = []

    for i in range(iterations):
        development_cost = np.random.normal(200000, 30000)
        marketing_cost = np.random.normal(100000, 15000)
        infrastructure_cost = np.random.normal(50000, 10000)
        total_expenses = development_cost + marketing_cost + infrastructure_cost
        forecast_values.append(total_expenses)

    plt.hist(forecast_values, bins=50, color='skyblue')
    plt.xlabel('Общие расходы')
    plt.ylabel('Частота')
    plt.title('Анализ риска на основе Монте-Карло для ИТ')
    plt.show()


# Вкладка Анализа рисков
Label(tab_risk, text="Анализ риска", font=("Arial", 14)).pack(pady=10)
risk_button = Button(tab_risk, text="Запустить анализ риска", command=risk_analysis)
risk_button.pack(pady=10)

# Запуск интерфейса
root.mainloop()
