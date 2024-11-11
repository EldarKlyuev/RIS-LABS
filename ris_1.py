import datetime

# База знаний: 20 правил для рекомендаций
rules = [
    {"if": {"time_of_day": "morning", "preference": "coffee"}, "then": "coffee", "explanation": "Утром рекомендуем кофе для любителей кофе"},
    {"if": {"time_of_day": "afternoon", "preference": "tea"}, "then": "tea", "explanation": "Днем рекомендуем чай для любителей чая"},
    {"if": {"time_of_day": "evening", "preference": "juice"}, "then": "juice", "explanation": "Вечером рекомендуем сок для любителей сока"},
    {"if": {"weather": "cold", "preference": "hot_drink"}, "then": "hot chocolate", "explanation": "В холодную погоду рекомендуем горячий шоколад"},
    {"if": {"weather": "hot", "preference": "cold_drink"}, "then": "iced tea", "explanation": "В жару рекомендуем холодный чай"},
    {"if": {"time_of_day": "morning", "preference": "tea"}, "then": "green tea", "explanation": "Утром рекомендуем зеленый чай для легкости и бодрости"},
    {"if": {"time_of_day": "afternoon", "preference": "coffee"}, "then": "espresso", "explanation": "Днем для бодрости рекомендуем эспрессо"},
    {"if": {"time_of_day": "evening", "preference": "hot_drink"}, "then": "chamomile tea", "explanation": "Вечером для расслабления рекомендуем чай из ромашки"},
    {"if": {"meal_type": "breakfast", "preference": "sweet"}, "then": "pancakes", "explanation": "На завтрак с предпочтением к сладкому рекомендуем панкейки"},
    {"if": {"meal_type": "lunch", "preference": "salty"}, "then": "salad", "explanation": "На обед с предпочтением к соленому рекомендуем салат"},
    {"if": {"meal_type": "dinner", "preference": "heavy"}, "then": "steak", "explanation": "На ужин для тех, кто предпочитает тяжёлую пищу, рекомендуем стейк"},
    {"if": {"meal_type": "breakfast", "allergy": "gluten"}, "then": "fruit salad", "explanation": "Для людей с аллергией на глютен на завтрак рекомендуем фруктовый салат"},
    {"if": {"meal_type": "lunch", "allergy": "lactose"}, "then": "vegan burger", "explanation": "Для людей с аллергией на лактозу на обед рекомендуем веганский бургер"},
    {"if": {"meal_type": "dinner", "allergy": "nuts"}, "then": "vegetable soup", "explanation": "Для людей с аллергией на орехи на ужин рекомендуем овощной суп"},
    {"if": {"meal_type": "any", "preference": "light"}, "then": "salad with chicken", "explanation": "Для лёгкого приема пищи рекомендуем салат с курицей"},
    {"if": {"meal_type": "any", "preference": "sweet"}, "then": "ice cream", "explanation": "Для сладкоежек рекомендуем мороженое"},
    {"if": {"meal_type": "any", "preference": "spicy"}, "then": "spicy pizza", "explanation": "Для любителей острого рекомендуем пиццу с перцем чили"},
    {"if": {"meal_type": "lunch", "preference": "vegetarian"}, "then": "vegetarian pizza", "explanation": "Для вегетарианцев на обед рекомендуем вегетарианскую пиццу"},
    {"if": {"meal_type": "dinner", "preference": "fish"}, "then": "grilled salmon", "explanation": "Для любителей рыбы на ужин рекомендуем гриль-лосось"},
    {"if": {"weather": "rainy", "preference": "warm_food"}, "then": "soup", "explanation": "В дождливую погоду рекомендуем тёплый суп"},
    {"if": {"weather": "sunny", "preference": "light_food"}, "then": "salad with tuna", "explanation": "В солнечную погоду рекомендуем лёгкий салат с тунцом"}
]

# Функция для прямого вывода
def direct_inference(facts):
    recommendations = []
    for rule in rules:
        if all(facts.get(k) == v for k, v in rule["if"].items()):
            recommendations.append((rule["then"], rule["explanation"]))
    return recommendations

# Функция для обратного вывода
def backward_inference(goal):
    explanations = []
    for rule in rules:
        if rule["then"] == goal:
            conditions = rule["if"]
            explanation = rule["explanation"]
            explanations.append((conditions, explanation))
    return explanations

# Логирование
def log_recommendations(recommendations):
    with open("recommendations_log.txt", "a") as log_file:
        for recommendation, explanation in recommendations:
            log_file.write(f"{datetime.datetime.now()}: Recommendation: {recommendation} - Explanation: {explanation}\n")

# Основной блок для работы с экспертной системой
def main():
    # Пример фактов
    facts = {
        "time_of_day": "evening",       # Время суток
        "preference": "juice",         # Предпочтение клиента
        "weather": "cold",              # Погода
        "meal_type": "breakfast",       # Тип еды
        "allergy": "none"               # Аллергии
    }

    # Прямой вывод
    print("Прямой вывод:")
    recommendations = direct_inference(facts)
    for rec, explanation in recommendations:
        print(f"Рекомендуем: {rec} - Объяснение: {explanation}")

    # Логирование рекомендаций
    log_recommendations(recommendations)

    # Обратный вывод
    print("\nОбратный вывод:")
    goal = "tea"
    explanations = backward_inference(goal)
    for conditions, explanation in explanations:
        print(f"Для достижения цели '{goal}' нужны условия {conditions} - Объяснение: {explanation}")

# Запуск системы
if __name__ == "__main__":
    main()
