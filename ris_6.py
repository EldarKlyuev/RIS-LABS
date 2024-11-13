import tkinter as tk
from tkinter import messagebox, simpledialog


# --- Продукционная система ---

class ProductionSystem:
    def __init__(self):
        self.rules = []

    def add_rule(self, condition, result):
        self.rules.append((condition, result))

    def evaluate(self, user_goal, user_level):
        for condition, result in self.rules:
            if condition(user_goal, user_level):
                return result
        return "Подходящей рекомендации нет."


# Функции условий
def weight_loss_condition(goal, level):
    return goal == "похудение" and level == "начальный"


def muscle_gain_condition(goal, level):
    return goal == "набор массы" and level in ["средний", "продвинутый"]


# Создание правил
production_system = ProductionSystem()
production_system.add_rule(weight_loss_condition,
                           "Рекомендуется кардио-тренировка 3 раза в неделю и диета с низким содержанием углеводов.")
production_system.add_rule(muscle_gain_condition,
                           "Рекомендуются силовые тренировки с акцентом на крупные группы мышц и высокобелковая диета.")


# --- Фреймовая система (Тренеры и режим питания) ---

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


# Пример тренеров и режимов питания
trainers = [
    Trainer("Анна", 5, "кардио"),
    Trainer("Иван", 8, "силовые тренировки")
]

diet_plans = [
    DietPlan("похудение", 1500, {"белки": 30, "жиры": 20, "углеводы": 50}),
    DietPlan("набор массы", 2500, {"белки": 40, "жиры": 30, "углеводы": 30})
]


def find_trainer(specialty):
    for trainer in trainers:
        if trainer.specialty == specialty:
            return trainer.name
    return "Тренер не найден."


# --- Семантическая сеть ---

class SemanticNetwork:
    def __init__(self):
        self.network = {}

    def add_relation(self, concept1, relation, concept2):
        if concept1 not in self.network:
            self.network[concept1] = []
        self.network[concept1].append((relation, concept2))

    def find_relations(self, concept):
        return self.network.get(concept, [])


# Создаем сеть
semantic_network = SemanticNetwork()
semantic_network.add_relation("бег", "развивает", "сердечно-сосудистая система")
semantic_network.add_relation("жим лежа", "развивает", "грудные мышцы")
semantic_network.add_relation("жим лежа", "цель", "набор массы")


# --- Система на базе прецедентов ---

class CaseBasedSystem:
    def __init__(self):
        self.cases = []

    def add_case(self, goal, level, success_rate, recommendation):
        self.cases.append(
            {"goal": goal, "level": level, "success_rate": success_rate, "recommendation": recommendation})

    def find_best_case(self, goal, level):
        best_case = None
        for case in self.cases:
            if case["goal"] == goal and case["level"] == level:
                if best_case is None or case["success_rate"] > best_case["success_rate"]:
                    best_case = case
        return best_case["recommendation"] if best_case else "Прецеденты не найдены."


# Прецеденты
case_based_system = CaseBasedSystem()
case_based_system.add_case("похудение", "начальный", 80, "Кардио тренировки 3 раза в неделю, 1500 ккал диета")
case_based_system.add_case("набор массы", "средний", 90, "Силовые тренировки 4 раза в неделю, 2500 ккал диета")


# --- UI на tkinter ---

class FitnessExpertSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Экспертная система для фитнес-зала")

        # Заголовок
        self.label_title = tk.Label(root, text="Выберите режим работы", font=("Arial", 16))
        self.label_title.pack(pady=10)

        # Кнопки
        self.button1 = tk.Button(root, text="Продукционная система", command=self.run_production_system)
        self.button2 = tk.Button(root, text="Фреймовая система", command=self.run_frame_system)
        self.button3 = tk.Button(root, text="Семантическая сеть", command=self.run_semantic_network)
        self.button4 = tk.Button(root, text="Система на базе прецедентов", command=self.run_case_based_system)
        self.button1.pack(pady=5)
        self.button2.pack(pady=5)
        self.button3.pack(pady=5)
        self.button4.pack(pady=5)

    def run_production_system(self):
        goal = self.get_goal_input()
        level = self.get_level_input()
        result = production_system.evaluate(goal, level)
        messagebox.showinfo("Результат", result)

    def run_frame_system(self):
        specialty = self.get_specialty_input()
        trainer_name = find_trainer(specialty)

        diet_goal = self.get_goal_input()
        diet_plan = next((plan for plan in diet_plans if plan.goal == diet_goal), None)

        diet_message = f"Режим питания для '{diet_goal}': Калории: {diet_plan.recommended_calories}, БЖУ: {diet_plan.macros}" if diet_plan else "Диета не найдена."
        messagebox.showinfo("Результат", f"Рекомендуемый тренер: {trainer_name}\n{diet_message}")

    def run_semantic_network(self):
        exercise = self.get_exercise_input()
        relations = semantic_network.find_relations(exercise)
        if relations:
            relations_text = "\n".join([f"- {relation} {concept}" for relation, concept in relations])
            messagebox.showinfo("Связи упражнения", f"Связи для '{exercise}':\n{relations_text}")
        else:
            messagebox.showinfo("Результат", "Связи не найдены.")

    def run_case_based_system(self):
        goal = self.get_goal_input()
        level = self.get_level_input()
        result = case_based_system.find_best_case(goal, level)
        messagebox.showinfo("Результат", result)

    def get_goal_input(self):
        return simpledialog.askstring("Цель", "Введите цель (похудение, набор массы):").strip().lower()

    def get_level_input(self):
        return simpledialog.askstring("Уровень",
                                      "Введите уровень подготовки (начальный, средний, продвинутый):").strip().lower()

    def get_specialty_input(self):
        return simpledialog.askstring("Специализация",
                                      "Введите тип тренера (кардио, силовые тренировки):").strip().lower()

    def get_exercise_input(self):
        return simpledialog.askstring("Упражнение", "Введите упражнение для поиска связей:").strip().lower()


# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    app = FitnessExpertSystemApp(root)
    root.mainloop()
