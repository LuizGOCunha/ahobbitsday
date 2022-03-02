import random

def hour_cycle():
    print("O que deseja fazer?")
    action = input(">")
    global cooked_meal
    if action == "cozinhar":
        cooked_meal = True
        print("Você cozinha uma farta ceia.")
        pass
    if action == "comer":
        if cooked_meal:
            print("Você come sua refeição")
            cooked_meal = False
        elif not cooked_meal:
            print("Você abre sua dispensa.")
            snacks()
            

def day_cycle():
    print("Você acorda de um sonho agradável.")
    hour_counter = 0
    cooked_meal = False
    while True:
        print(f"O horário é {8+hour_counter}:00")
        hour_cycle()
        hour_counter += 1
        if hour_counter >= 15:
            break
    print("Você busca o calor da sua cama.")

def snacks():
    random_number = random.randint(0,11)
    if random_number == 0:
        print("Você encontra maçãs maduras.")
    if random_number == 1:
        print("Você encontra uvas.")
    if random_number == 2:
        print("Você encontra uma roda de queijo.")
    if random_number == 3:
        print("Você encontra bolachas.")
    if random_number == 4:
        print("Você encontra biscoitos.")
    if random_number == 5:
        print("Você encontra peru defumado.")
    if random_number == 6:
        print("Você encontra bolo de cenoura.")
    if random_number == 7:
        print("Você encontra torradas.")
    if random_number == 8:
        print("Você encontra brioche.")
    if random_number == 9:
        print("Você encontra escones.")
    if random_number == 10:
        print("Você encontra pudim.")
    



    #print(f"Você encontra {lista[random_number]}")