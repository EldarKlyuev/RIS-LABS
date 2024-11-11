class SemanticNetwork:
    def __init__(self):
        self.concepts = {}  # Хранение понятий
        self.relationships = []  # Хранение связей

    def add_concept(self, name, attributes=None):
        """Добавление нового понятия в сеть."""
        if attributes is None:
            attributes = {}
        self.concepts[name] = attributes

    def add_relationship(self, concept1, concept2, relation):
        """Добавление связи между двумя понятиями."""
        if concept1 in self.concepts and concept2 in self.concepts:
            self.relationships.append((concept1, relation, concept2))
        else:
            print(f"Одна или обе концепции {concept1} и {concept2} не существуют.")

    def display(self):
        """Вывод всех понятий и связей."""
        print("Понятийная сеть:")
        for concept, attributes in self.concepts.items():
            print(f"{concept}: {attributes}")
        print("\nСвязи:")
        for relation in self.relationships:
            print(f"{relation[0]} --({relation[1]})--> {relation[2]}")

    def add_knowledge(self, concept1, concept2, relation):
        """Метод для пополнения базы знаний (добавление новых понятий и связей)."""
        self.add_relationship(concept1, concept2, relation)

    def get_concept(self, name):
        """Получение понятия из сети."""
        return self.concepts.get(name, "Понятие не найдено.")

    def search_relation(self, concept_name):
        """Поиск всех связей для указанного понятия."""
        return [rel for rel in self.relationships if rel[0] == concept_name or rel[2] == concept_name]

# Семантическая сеть

network = SemanticNetwork()

# Добавляем концепты
network.add_concept("Кафе", {"тип": "Общественное заведение", "местоположение": "Москва"})
network.add_concept("Меню", {"состав": "Блюда и напитки", "категория": "Основное"})
network.add_concept("Блюдо", {"тип": "Пища", "особенности": "Составляющие"})
network.add_concept("Напиток", {"тип": "Питье", "особенности": "Холодные и горячие"})
network.add_concept("Персонал", {"состав": "Официанты, повара", "роль": "Обслуживание"})
network.add_concept("Заказ", {"состав": "Блюда, напитки", "статус": "Ожидание, Выполнен"})
network.add_concept("Паста", {"категория": "Основное", "цена": 350})
network.add_concept("Кофе", {"категория": "Напиток", "цена": 150})
network.add_concept("Десерт", {"категория": "Десерты", "состав": "Сладкие блюда"})
network.add_concept("Официант", {"роль": "Обслуживание", "обязанности": "Принятие заказа"})
network.add_concept("Повар", {"роль": "Приготовление", "обязанности": "Приготовление блюд"})
network.add_concept("Стол", {"состояние": "Свободен, занят", "количество мест": 4})
network.add_concept("Скидка", {"тип": "Акция", "процент": 10})
network.add_concept("Оплата", {"методы": "Наличные, карта", "статус": "Ожидание"})
network.add_concept("Сценарий обслуживания", {"этапы": "Принять заказ, приготовить, подать"})
network.add_concept("Вегетарианское меню", {"состав": "Блюда без мяса"})
network.add_concept("Алкогольные напитки", {"состав": "Пиво, Вино"})
network.add_concept("Безалкогольные напитки", {"состав": "Соки, Чай, Кофе"})
network.add_concept("Ресторан", {"тип": "Заведение", "особенности": "Предоставление услуг по питанию"})

# Добавляем связи между концептами
network.add_relationship("Кафе", "Меню", "содержит")
network.add_relationship("Меню", "Блюдо", "содержит")
network.add_relationship("Меню", "Напиток", "содержит")
network.add_relationship("Персонал", "Официант", "включает")
network.add_relationship("Персонал", "Повар", "включает")
network.add_relationship("Заказ", "Блюдо", "содержит")
network.add_relationship("Заказ", "Напиток", "содержит")
network.add_relationship("Паста", "Блюдо", "является типом")
network.add_relationship("Кофе", "Напиток", "является типом")
network.add_relationship("Десерт", "Меню", "включает")
network.add_relationship("Официант", "Персонал", "является частью")
network.add_relationship("Повар", "Персонал", "является частью")
network.add_relationship("Стол", "Меню", "показывает")
network.add_relationship("Скидка", "Меню", "применяется к")
network.add_relationship("Сценарий обслуживания", "Заказ", "обрабатывает")
network.add_relationship("Вегетарианское меню", "Меню", "является подкатегорией")
network.add_relationship("Алкогольные напитки", "Меню", "является подкатегорией")
network.add_relationship("Безалкогольные напитки", "Меню", "является подкатегорией")
network.add_relationship("Ресторан", "Кафе", "является типом")

# Выводим все концепты и связи
network.display()

# Пример поиска связей
print("\nСвязи для 'Меню':")
relations = network.search_relation("Блюдо")
for relation in relations:
    print(relation)

# Пополнение базы знаний
network.add_knowledge("Кофе", "Сценарий обслуживания", "включает")

# Выводим обновленные данные
network.display()
