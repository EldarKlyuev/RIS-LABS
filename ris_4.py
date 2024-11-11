import difflib


class Precedent:
    def __init__(self, case_id, description, solution):
        self.case_id = case_id  # Уникальный идентификатор прецедента
        self.description = description  # Описание проблемы
        self.solution = solution  # Решение этой проблемы

    def __str__(self):
        return f"Прецедент {self.case_id}: {self.description} -> {self.solution}"


class CafeExpertSystem:
    def __init__(self):
        self.precedents = []  # Список прецедентов
        self.case_counter = 0  # Счётчик для уникальных идентификаторов прецедентов

    def add_precedent(self, description, solution):
        """Добавление нового прецедента."""
        self.case_counter += 1
        new_case = Precedent(self.case_counter, description, solution)
        self.precedents.append(new_case)

    def find_similar_precedents(self, current_description):
        """Поиск похожих прецедентов на основе описания."""
        similarities = []
        for precedent in self.precedents:
            # Используем difflib для нахождения схожести описаний
            similarity = difflib.SequenceMatcher(None, current_description, precedent.description).ratio()
            similarities.append((precedent, similarity))

        # Сортируем по убыванию схожести
        similarities.sort(key=lambda x: x[1], reverse=True)
        return similarities

    def recommend_solution(self, current_description):
        """Рекомендация решения на основе схожих прецедентов."""
        similar_precedents = self.find_similar_precedents(current_description)
        if similar_precedents:
            # Рекомендуем решение из наиболее похожего прецедента
            best_match = similar_precedents[0]
            print(f"Рекомендуемое решение (с прецедента {best_match[0].case_id}): {best_match[0].solution}")
        else:
            print("Не найдено схожих прецедентов. Требуется новая рекомендация.")


# Экспертная система
system = CafeExpertSystem()

# Добавление прецедентов
system.add_precedent("Проблема с заказом: клиент недоволен блюдом из-за его температуры", "Перепроверить температуру подачи блюд, улучшить контроль на кухне.")
system.add_precedent("Клиент запросил замену блюда, так как оно оказалось слишком острым", "Предложить клиенту вариант блюда с меньшей остротой и извиниться.")
system.add_precedent("Клиент жалуется на долгую подачу заказа", "Ускорить процесс подачи, улучшить координацию между официантами и кухней.")
system.add_precedent("Запрос клиента: как лучше подавать десерты на банкетах", "Рекомендовать десерты, которые легко подаются в больших количествах и быстро готовы.")

# Поиск и рекомендация решения для текущей ситуации
current_problem = "клиент недоволен блюдом из-за его температуры."
system.recommend_solution(current_problem)

# Пример добавления прецедентов
system.add_precedent("Клиент не удовлетворён качеством кофе", "Предложить новый кофе или вернуть деньги, извиниться.")
system.recommend_solution("Клиент недоволен качеством кофе")
