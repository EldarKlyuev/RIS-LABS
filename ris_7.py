import tkinter as tk
from tkinter import messagebox, ttk

# --- Основные классы ---

class Trainer:
    def __init__(self, name, experience, specialty):
        self.name = name
        self.experience = experience
        self.specialty = specialty

class DietPlan:
    def __init__(self, goal, calorie_modifier, macros):
        self.goal = goal
        self.calorie_modifier = calorie_modifier
        self.macros = macros

class Exercise:
    def __init__(self, name, target_muscle, goal, level, sets, reps):
        self.name = name
        self.target_muscle = target_muscle
        self.goal = goal
        self.level = level
        self.sets = sets
        self.reps = reps

# --- Данные ---

trainers = [
    Trainer("Анна", 5, "кардио"),
    Trainer("Иван", 8, "силовые тренировки"),
    Trainer("Ольга", 4, "функциональные тренировки"),
    Trainer("Михаил", 10, "выносливость"),
    Trainer("Дарья", 6, "йога и растяжка"),
    Trainer("Алексей", 7, "общая физическая подготовка"),
]

diet_plans = [
    DietPlan("похудение", -500, {"белки": 30, "жиры": 20, "углеводы": 50}),
    DietPlan("набор массы", 500, {"белки": 35, "жиры": 25, "углеводы": 40}),
    DietPlan("поддержание формы", 0, {"белки": 30, "жиры": 30, "углеводы": 40}),
    DietPlan("увеличение выносливости", 200, {"белки": 25, "жиры": 20, "углеводы": 55}),
]

exercises = [
    # Новичок
    Exercise("Бег", "сердечно-сосудистая система", "похудение", "новичок", 3, 10),
    Exercise("Планка", "корпус", "поддержание формы", "новичок", 3, "30 секунд"),
    Exercise("Приседания без веса", "ноги", "похудение", "новичок", 3, 12),
    Exercise("Растяжка спины", "спина", "поддержание формы", "новичок", 2, "1 минута"),
    # Любитель
    Exercise("Жим лёжа", "грудные мышцы", "набор массы", "любитель", 4, 12),
    Exercise("Подтягивания", "спина и бицепс", "увеличение выносливости", "любитель", 3, 10),
    Exercise("Прыжки на месте", "сердечно-сосудистая система", "увеличение выносливости", "любитель", 3, "1 минута"),
    Exercise("Приседания с весом", "ягодицы и ноги", "набор массы", "любитель", 4, 10),
    # Профессионал
    Exercise("Мёртвая тяга", "спина и ноги", "набор массы", "профессионал", 5, 8),
    Exercise("Бёрпи", "всё тело", "увеличение выносливости", "профессионал", 3, 15),
    Exercise("Становая тяга", "спина и ягодицы", "поддержание формы", "профессионал", 5, 10),
    Exercise("Подъём штанги", "бицепс", "набор массы", "профессионал", 4, 12),
]

# --- Логика системы ---

def calculate_bmr(weight, height, age, gender):
    if gender == "мужской":
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161

def find_trainer_by_specialty(goal):
    specialty_map = {
        "похудение": "кардио",
        "набор массы": "силовые тренировки",
        "поддержание формы": "общая физическая подготовка",
        "увеличение выносливости": "выносливость",
    }
    specialty = specialty_map.get(goal, "")
    for trainer in trainers:
        if trainer.specialty == specialty:
            return f"{trainer.name} (опыт: {trainer.experience} лет)"
    return "Тренер не найден."

def find_diet_plan_by_goal(bmr, goal):
    for plan in diet_plans:
        if plan.goal == goal:
            total_calories = bmr + plan.calorie_modifier
            return f"Калории: {total_calories}, БЖУ: {plan.macros}"
    return "Диета не найдена."

def find_exercises_by_goal(goal, level):
    relevant_exercises = [
        ex for ex in exercises if ex.goal == goal and ex.level == level
    ]
    return relevant_exercises if relevant_exercises else []

# --- UI на ttk ---

class FitnessExpertSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Экспертная система для фитнес-зала")
        self.root.geometry("600x600")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", font=("Arial", 12))
        style.configure("TButton", font=("Arial", 12))

        ttk.Label(root, text="Экспертная система для фитнес-зала", font=("Arial", 16)).pack(pady=10)

        self.create_input_fields(root)
        ttk.Button(root, text="Получить рекомендации", command=self.get_recommendations).pack(pady=20)

    def create_input_fields(self, root):
        frame = ttk.Frame(root)
        frame.pack(pady=10)

        # Поля для выбора роста, веса и возраста
        ttk.Label(frame, text="Рост (см):").grid(row=0, column=0, padx=5, pady=5)
        self.height_var = tk.IntVar(value=170)
        ttk.Spinbox(frame, from_=100, to=250, textvariable=self.height_var, width=10).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Вес (кг):").grid(row=1, column=0, padx=5, pady=5)
        self.weight_var = tk.IntVar(value=70)
        ttk.Spinbox(frame, from_=30, to=200, textvariable=self.weight_var, width=10).grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Возраст (лет):").grid(row=2, column=0, padx=5, pady=5)
        self.age_var = tk.IntVar(value=25)
        ttk.Spinbox(frame, from_=10, to=100, textvariable=self.age_var, width=10).grid(row=2, column=1, padx=5, pady=5)

        # Пол и цель через выпадающие списки
        ttk.Label(frame, text="Пол:").grid(row=3, column=0, padx=5, pady=5)
        self.gender_var = tk.StringVar(value="мужской")
        ttk.Combobox(frame, textvariable=self.gender_var, values=["мужской", "женский"], state="readonly", width=15).grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Цель:").grid(row=4, column=0, padx=5, pady=5)
        self.goal_var = tk.StringVar(value="похудение")
        ttk.Combobox(frame, textvariable=self.goal_var, values=["похудение", "набор массы", "поддержание формы", "увеличение выносливости"], state="readonly", width=30).grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Уровень:").grid(row=5, column=0, padx=5, pady=5)
        self.level_var = tk.StringVar(value="новичок")
        ttk.Combobox(frame, textvariable=self.level_var, values=["новичок", "любитель", "профессионал"], state="readonly", width=20).grid(row=5, column=1, padx=5, pady=5)

    def get_recommendations(self):
        try:
            height = self.height_var.get()
            weight = self.weight_var.get()
            age = self.age_var.get()
            gender = self.gender_var.get()
            goal = self.goal_var.get()
            level = self.level_var.get()

            bmr = calculate_bmr(weight, height, age, gender)
            trainer = find_trainer_by_specialty(goal)
            diet_plan = find_diet_plan_by_goal(bmr, goal)
            exercises = find_exercises_by_goal(goal, level)

            result_message = f"Ваш BMR: {bmr:.2f} ккал\n"
            result_message += f"Рекомендуемый тренер: {trainer}\n"
            result_message += f"Режим питания: {diet_plan}\n"
            result_message += "Рекомендуемые упражнения:\n"
            for ex in exercises:
                result_message += f"- {ex.name} ({ex.target_muscle}): {ex.sets}x{ex.reps}\n"

            messagebox.showinfo("Рекомендации", result_message)
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    app = FitnessExpertSystemApp(root)
    root.mainloop()
