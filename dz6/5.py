# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationary():

    def __init__(self, title):
        self.title = title
        print(f'Создан новый объект класса Stationary \n {self.title}\n')

    def Draw(self):
        print('Запуск отрисовки для базового класса\n')

class Pen(Stationary):
    def Draw(self):
        print('Запуск отрисовки для класса Pen\n')

class Pencil(Stationary):
    def Draw(self):
        print('Запуск отрисовки для класса Pencil\n')

class Handle(Stationary):
    def Draw(self):
        print('Запуск отрисовки для класса Handle\n')

new_stationary = Stationary('Здесь должен быть title для вызова базового класса')
new_stationary.Draw()

new_pen = Pen('Здесь должен быть title для вызова дочернего класса Pen')
new_pen.Draw()

new_pencil = Pencil('Здесь должен быть title для вызова дочернего класса Pencil')
new_pencil.Draw()

new_handle = Handle('Здесь должен быть title для вызова дочернего класса Handle')
new_handle.Draw()