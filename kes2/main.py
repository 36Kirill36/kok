from character import  Character
from  colorama import  Fore

player1 = Character(name='Vasya', health=70, damage=5, color=Fore.LIGHTRED_EX)
print((player1.get_stats()))

player2 = Character( name='Petya', health=70, damage=5, color=Fore.LIGHTBLUE_EX)
print(player2.get_stats())

player1.is_alive(health=5 )
player2.is_alive(health=5 )

player1.attack(player2)
player2.attack(player1)

print(player1.get_stats())
print(player2.get_stats())

