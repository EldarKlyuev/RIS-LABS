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


# Создание правил и запуск системы
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


# --- Основное меню и запуск ---

def main():
    while True:
        print("\nВыберите режим работы:")
        print("1: Продукционная система рекомендаций")
        print("2: Фреймовая система - Поиск тренера и диеты")
        print("3: Семантическая сеть - Поиск связи упражнений и целей")
        print("4: Система на базе прецедентов")
        print("0: Выход")
        choice = input("Введите номер выбора: ").strip()

        if choice == "1":
            goal = input("Введите цель (похудение, набор массы): ").strip().lower()
            level = input("Введите уровень подготовки (начальный, средний, продвинутый): ").strip().lower()
            print(production_system.evaluate(goal, level))

        elif choice == "2":
            specialty = input("Введите тип тренера (кардио, силовые тренировки): ").strip().lower()
            trainer_name = find_trainer(specialty)
            print(f"Рекомендуемый тренер: {trainer_name}")

            diet_goal = input("Введите цель для режима питания (похудение, набор массы): ").strip().lower()
            for plan in diet_plans:
                if plan.goal == diet_goal:
                    print(f"Режим питания для '{diet_goal}': Калории: {plan.recommended_calories}, БЖУ: {plan.macros}")
                    break

        elif choice == "3":
            exercise = input("Введите упражнение для поиска связей: ").strip().lower()
            relations = semantic_network.find_relations(exercise)
            print(f"Связи для {exercise}:")
            for relation, concept in relations:
                print(f"- {relation} {concept}")

        elif choice == "4":
            goal = input("Введите цель (похудение, набор массы): ").strip().lower()
            level = input("Введите уровень подготовки (начальный, средний, продвинутый): ").strip().lower()
            print(case_based_system.find_best_case(goal, level))

        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите от 1 до 4 или 0.")


# Запуск основного меню
main()
