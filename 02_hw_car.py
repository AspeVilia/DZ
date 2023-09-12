"""
## Автомобиль

Описать класс Car
``` python
class Car:
  ...

car1 = Car()
```

а) У машины должны быть атрибуты
* "сколько бензина в баке" (gas)
* "вместимость бака" - сколько максимум влезаем бензина (capacity)
* "расход топлива на 100 км" (gas_per_km)
* "пробег" (mileage)

б) метод "залить столько-то литров в бак"

``` python
car1.fill(5)  # залили 5 литров
```
должна учитываться вместительность бака
если пытаемся залить больше, чем вмещается, то заполняется полностью +
print'ом выводится сообщение о лишних литрах

в) метод "проехать сколько-то км"

``` python
car1.ride(50)  # едем 50 км (если хватит топлива) 
```
выведет сообщение "проехали ... километров"
в результате поездки потратится бензин и увеличится пробег
Если топлива не хватает на указанное расстояние, едем пока хватает топлива.

г) реализовать метод: car1.info() (количество бензина в баке и пробег)
"""


class Car:
    def __init__(self, gas: float | int = 0,capacity: float | int = 50,gas_per_km: float | int = 5,mileage: float | int = 0):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.mileage = mileage
    def info(self) -> None:
        print(f'В баке топлива {self.gas}, пробег {self.mileage}')

    def fill(self, infill: float) -> None:
        if self.gas + infill > self.capacity:
            print(f'Лишнее топливо {self.gas + infill - self.capacity}')
            self.gas = self.capacity
        else:
            self.gas += infill
    def ride(self, dist: float) -> None:
        curr_gas = 0.01 * dist * self.gas_per_km
        if curr_gas > self.gas:
            self.mileage += (new_dist := 100 * self.gas / self.gas_per_km)
            self.gas = 0
            print(f'Хватило на{new_dist:.2f} км')
        else:
            self.mileage += dist
            self.gas -= curr_gas
            print(f'Проехали{dist}')
if __name__ == 'main':
    car1 = Car(40, 40,10, mileage=1000)
    car1.info()
    print('=' * 40)

    car1.ride(200)
    car1.info()
    print('=' * 40)

    car1.fill(50)
    car1.info()
    print('=' * 40)

    car1.ride(2000)
    car1.info()
    print('=' * 40)

    car2 = Car(40, 90, 20, mileage=1000)
    car2.info()
    print('=' * 40)

    car2.ride(300)
    car2.info()
    print('=' * 40)

    car2.fill(70)
    car2.info()
    print('=' * 40)

    car2.ride(3000)
    car2.info()
    print('=' * 40)


