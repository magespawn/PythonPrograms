Name = input ("What is your name?:")
if Name == "Darius" or Name == "darius":
    print ("Hello world!")
else:
    print ("Goodbye world!")

Input = input ("What do you like to do?:")
if Input == "basketball" or Input == "tennis" or Input == "playing tennis" or Input=="playing basketball":
    print ("That sucks. I prefer chess.")
else:
    import random
    p = random.randint(0, 2)
    if p == 1:
        print ("That is nice!")
    else:
            print ("My brother is also interrested in %s." %(Input))
