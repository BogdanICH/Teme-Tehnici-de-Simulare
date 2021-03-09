import random

# Problemă: Yahtzee - jocul presupune aruncatul simultan a doar 5 zaruri
# în scopul obținerii cât mai rapide a unei cifre care să se repete
# pe toate cele 5 fețe(cele de sus) ale zarurilor aruncate

# în plus, am afișat în final și cifra care apare
# cel mai des în formulă completă


def yahtzee_problem(num_trials): # funcția de bază
    num_of_yahtzee = 0
    #aruncăm zarurile de num_trials ori
    for i in range(num_trials):
        dice = []
        for j in range(5): # adăugăm în lista zarurilor, numere alese aleatoriu de la 1 la 6
            dice.append(random.randrange(1, 7))

        # presupunem că avem un Yahtzee - adică o formulă completă
        state = True
        for die in dice:
            # dacă găsim măcar 1 zar care nu este egal cu primul, atunci nu e un Yahtzee
            # si trecem mai departe
            if die != dice[0]:
                state = False

        # dacă am dat peste un yathzee, atunci îl afisăm
        # îi incrementăm variabila corespunzătoare și îi adăugăm
        # 1 punct la frecvență
        if state:
            print("Acesta este un Yahtzee")
            print(dice)
            num_of_yahtzee += 1
            list_of_dice[dice[0]] += 1

    print("Numărul de încercări: " + str(num_trials))
    print("Numărul de Yahtzee: " + str(num_of_yahtzee))
    # calculăm în rate șansa de a formulă completă din numărul de aruncări specificat
    rate = float(num_of_yahtzee)/num_trials
    return rate


#introducem de la tastatură numărul de aruncări pe care îl dorim
number_of_trials = int(input("Dați numărul de încercări: "))
# lista de frecveță
list_of_dice = [0, 0, 0, 0, 0, 0, 0]
print("Șansa de a pica 5 zaruri cu același număr din " + str(number_of_trials) + " aruncări este de " + str(yahtzee_problem(number_of_trials)))

maxim = 0
the_most_frequently_number = 0
#calculăm care a fost număr ce a creat cel mai des formula completă
for i in range(7):
    if maxim < list_of_dice[i]:
        maxim = list_of_dice[i]
        the_most_frequently_number = i

print("\n")
print("Numarul " + str(the_most_frequently_number) + " a picat în formulă completă de cele mai multe ori cu o frecventa de " + str(maxim)
      + "/" + str(sum(list_of_dice)))