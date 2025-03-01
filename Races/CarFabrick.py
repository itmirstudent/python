# CarFabrick
from Car import Car
from CarComponent import Engine

class CarFabrick():
    _cars = []
    _engine_list = [
        Engine("Ford", 1.5),
        Engine("Ford", 1.8),
        Engine("Ferrari", 2)
    ]
    _engine_dict = {index: value for index, value in enumerate(_engine_list)}

    def _print_engine(self):
        for index, engine in self._engine_dict.items():
            print(index, engine.get_name(), engine.get_power())

    def _pick_engine(self):
        index = input("Введите номер выбранного мотора: ")
        return self._engine_dict[int(index)]

    def create_car(self):
        self._print_engine()
        while True:
            maker = input("Введите марку: ")
            model = input("Введите модель: ")
            year = input("Введите год производства: ")
            car = Car(maker, model, year)
            car.add_component_to_car(engine = self._pick_engine())
            self._cars.append(car)
            choice = input('Введите "выход" для завершения: ').strip().lower()
            if choice == "выход":
                break

    def get_cars(self):
        return self._cars