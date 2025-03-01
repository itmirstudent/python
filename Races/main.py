# main.py
from Track import Track
from CarFabrick import CarFabrick

if __name__ == '__main__':
    fabric = CarFabrick()
    fabric.create_car()
    track = Track(int(input("Введите длину трассы: ")), fabric.get_cars())
    track.ride()