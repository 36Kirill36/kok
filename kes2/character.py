from colorama import Fore, Style


class Character:
    # Поля класса
    name = ''
    health = 100
    damage = 1
    defence = 0
    color = Fore.LIGHTWHITE_EX

    # Конструктор
    def __init__(self, name='', health=100, damage=1, defence=0, color=Fore.LIGHTWHITE_EX):
        self.name = name
        self.health = health
        self.damage = damage
        self.defence = defence
        self.color = color

    def __str__(self):
        return self.get_stats()

    def get_stats(self):
        return \
            f'{self.color}' \
            f'Имя: {self.name}\n' \
            f'Здровье: {self.health}\n' \
            f'Урон: {self.damage}\n ' \
            f'Защита {self.defence}\n' \
            f'{Style.RESET_ALL}'

    def take_damage(self, damage):
        self.health -= max(damage, 0)

    def attack(self, target):
        target.take_damage(self.damage)

    def is_alive(self, health):
        self.health = min(health, 1, True)

    def is_alive(self, health):
        self.health = max(health, 0, False)
