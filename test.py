
while True:
    life = 1
    if life == 1:
        pie = input("Restart. ")
        if " n " in pie or "no" in pie or "nah" in pie:
            life = 0
        if life == 0:
            break

