import tkinter as tk
from tkinter import messagebox

class Trainer:
    def __init__(self, name, experience, specialty):
        self.name = name
        self.experience = experience  # Опыт в годах
        self.specialty = specialty  # Специализация (кардио, силовые тренировки и т.д.)


class DietPlan:
    def __init__(self, goal, recommended_calories, macros):
        self.goal = goal
        self.recommended_calories = recommended_calories
        self.macros = macros  # Пропорции макронутриентов (белки, жиры, углеводы)


class Exercise:
    def __init__(self, name, target_muscle, goal):
        self.name = name
        self.target_muscle = target_muscle  # Задействуемые мышцы
        self.goal = goal  # Цель упражнения (похудение, набор массы и т.д.)


# Тренеры
trainers = [
    Trainer("Анна", 5, "кардио"),
    Trainer("Иван", 8, "силовые тренировки"),
    Trainer("Ольга", 4, "функциональные тренировки"),
    Trainer("Дмитрий", 10, "набор массы"),
    Trainer("Мария", 6, "гибкость и растяжка"),
    Trainer("Сергей", 7, "выносливость"),
    Trainer("Алексей", 3, "поддержание формы")
]

# Режимы питания
diet_plans = [
    DietPlan("похудение", 1500, {"белки": 30, "жиры": 20, "углеводы": 50}),
    DietPlan("набор массы", 3000, {"белки": 35, "жиры": 25, "углеводы": 40}),
    DietPlan("поддержание формы", 2000, {"белки": 30, "жиры": 30, "углеводы": 40}),
    DietPlan("сушка", 1600, {"белки": 45, "жиры": 20, "углеводы": 35}),
    DietPlan("увеличение выносливости", 2500, {"белки": 25, "жиры": 20, "углеводы": 55}),
    DietPlan("поддержка гибкости", 1800, {"белки": 20, "жиры": 30, "углеводы": 50})
]

# Упражнения
exercises = [
    Exercise("Бег", "сердечно-сосудистая система", "похудение"),
    Exercise("Жим лежа", "грудные мышцы", "набор массы"),
    Exercise("Приседания", "ягодицы и ноги", "набор массы"),
    Exercise("Планка", "корпус", "поддержание формы"),
    Exercise("Велотренажер", "сердечно-сосудистая система", "увеличение выносливости"),
    Exercise("Йога", "гибкость", "поддержка гибкости"),
    Exercise("Подтягивания", "спина", "набор массы"),
    Exercise("Скакалка", "сердечно-сосудистая система", "похудение"),
    Exercise("Мертвая тяга", "ягодицы и ноги", "набор массы"),
    Exercise("Прыжки на месте", "выносливость", "увеличение выносливости"),
    Exercise("Растяжка", "гибкость", "поддержка гибкости")
]


def find_trainer_by_specialty(goal):
    specialty_map = {
        "похудение": "кардио",
        "набор массы": "силовые тренировки",
        "поддержание формы": "функциональные тренировки",
        "сушка": "функциональные тренировки",
        "увеличение выносливости": "выносливость",
        "поддержка гибкости": "гибкость и растяжка"
    }
    specialty = specialty_map.get(goal)
    for trainer in trainers:
        if trainer.specialty == specialty:
            return f"{trainer.name} (опыт: {trainer.experience} лет)"
    return "Тренер не найден."


def find_diet_plan_by_goal(goal):
    for plan in diet_plans:
        if plan.goal == goal:
            return f"Калории: {plan.recommended_calories}, БЖУ: {plan.macros}"
    return "Диета не найдена."


def find_exercises_by_goal(goal):
    relevant_exercises = [ex.name for ex in exercises if ex.goal == goal]
    return relevant_exercises if relevant_exercises else ["Упражнения не найдены"]


class FitnessExpertSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Экспертная система для фитнес-зала")

        # Заголовок
        self.label_title = tk.Label(root, text="Экспертная система для фитнес-зала", font=("Arial", 16))
        self.label_title.pack(pady=10)

        # Поле ввода цели
        self.label_goal = tk.Label(root,
                                   text="Введите вашу цель (похудение, набор массы, поддержание формы, сушка, увеличение выносливости, поддержка гибкости):")
        self.label_goal.pack(pady=5)
        self.entry_goal = tk.Entry(root, width=50)
        self.entry_goal.pack(pady=5)

        # Кнопка запуска
        self.button_run = tk.Button(root, text="Получить рекомендации", command=self.get_recommendations)
        self.button_run.pack(pady=10)

    def get_recommendations(self):
        goal = self.entry_goal.get().strip().lower()

        # Получаем рекомендации
        trainer = find_trainer_by_specialty(goal)
        diet_plan = find_diet_plan_by_goal(goal)
        exercises = find_exercises_by_goal(goal)

        # Формируем сообщение
        result_message = f"Цель: {goal.capitalize()}\n\n"
        result_message += f"Рекомендуемый тренер: {trainer}\n\n"
        result_message += f"Режим питания: {diet_plan}\n\n"
        result_message += "Рекомендуемые упражнения:\n" + "\n".join(f"- {ex}" for ex in exercises)

        # Отображаем результат
        messagebox.showinfo("Рекомендации", result_message)


# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    app = FitnessExpertSystemApp(root)
    root.mainloop()
