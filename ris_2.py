class Frame:
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes

    def __str__(self):
        return f"Фрейм: {self.name}, Атрибуты: {self.attributes}"

class MenuItem(Frame):
    def __init__(self, name, category, price, description):
        super().__init__(name, {
            'category': category,
            'price': price,
            'description': description
        })

class Order(Frame):
    def __init__(self, order_id, customer_name, items):
        super().__init__(order_id, {
            'customer_name': customer_name,
            'items': items
        })

class Discount(Frame):
    def __init__(self, name, percentage, valid_until):
        super().__init__(name, {
            'percentage': percentage,
            'valid_until': valid_until
        })

class Staff(Frame):
    def __init__(self, name, position, working_hours):
        super().__init__(name, {
            'position': position,
            'working_hours': working_hours
        })

class Table(Frame):
    def __init__(self, table_number, status, seats):
        super().__init__(table_number, {
            'status': status,  # Free or Occupied
            'seats': seats
        })

class ServiceScenario(Frame):
    def __init__(self, name, actions):
        super().__init__(name, {
            'actions': actions
        })

    def execute(self):
        for action in self.attributes['actions']:
            print(f"Executing action: {action}")


class CafeExpertSystem:
    def __init__(self):
        self.frames = []

    def add_frame(self, frame):
        self.frames.append(frame)

    def search_frame(self, search_name):
        # Преобразуем search_name в нижний регистр, если это строка
        if isinstance(search_name, str):
            search_name = search_name.lower()

        results = []
        for frame in self.frames:
            if isinstance(frame.name, str) and search_name in frame.name.lower():
                results.append(frame)
        return results


# Примеры
menu_item1 = MenuItem("Паста", "Основное", 350, "Паста с соусом и овощами")
menu_item2 = MenuItem("Кофе", "Напиток", 150, "Свежезаваренный кофе")
menu_item3 = MenuItem("Чай", "Напиток", 150, "Свежезаваренный чай")

order1 = Order("001", "Иванов Иван", ["Паста", "Кофе"])
order2 = Order("002", "Петров Петр", ["Кофе"])

discount1 = Discount("Скидка 10%", 10, "2024-12-31")

staff1 = Staff("Сергей", "Официант", "9:00 - 18:00")
staff2 = Staff("Марина", "Повар", "8:00 - 16:00")

table1 = Table(1, "Свободен", 4)
table2 = Table(2, "Занят", 2)

scenario = ServiceScenario("Сценарий обслуживания", [
    "Принять заказ",
    "Приготовить блюдо",
    "Подать клиенту",
    "Ожидание оплаты",
    "Запросить отзыв"
])

# Создаем экспертную систему и добавляем фреймы
expert_system = CafeExpertSystem()
expert_system.add_frame(menu_item1)
expert_system.add_frame(menu_item2)
expert_system.add_frame(menu_item3)
expert_system.add_frame(order1)
expert_system.add_frame(order2)
expert_system.add_frame(discount1)
expert_system.add_frame(staff1)
expert_system.add_frame(staff2)
expert_system.add_frame(table1)
expert_system.add_frame(table2)
expert_system.add_frame(scenario)

# Поиск по фреймам
search_results = expert_system.search_frame("паста")
for result in search_results:
    print(result)

scenario.execute()
