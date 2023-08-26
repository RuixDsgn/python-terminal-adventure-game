# Terminal adventure game

print("RuiGames presents: The Double Life of a Software Engineer/Professional Video Game Player")
print("Your objective: Choose your own destiny. Will you be coding? Or will you game?")

character_name = input("what is your character's name?")
character_age = int(input("How old is your character?"))
character_gender = int(input("What is your character's gender? 1)female 2)male"))

character_avatar = ''

if character_gender == 2:
    character_avatar = '👨🏻'
if character_gender == 1:
    character_avatar = '👧🏻'

print(f'your character name is: {character_avatar}{character_name} .')
print(f'{character_name} is {character_age} years old')

print(f"{character_name}'s adventure begins...")
