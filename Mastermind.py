from itertools import product

def Score(this, other):
    first = len([speg for speg, opeg in zip(this, other) if speg == opeg])

    return first, sum([min(this.count(j), other.count(j)) for j in '123456']) - first

possible = [''.join(p) for p in product('123456', repeat = 4)]
results = [(right, wrong) for right in range(5) for wrong in range(5 - right) if not (right == 3 and wrong == 1)]

def solveGuessingGame(guessingGame):
    attempt(set(possible), guessingGame, True)


def attempt(S, guessingGame, first = False):
    if first:
        a = '1122'
    elif len(S) == 1:
        a = S.pop()
    else:
        a = max(possible, key = lambda x : min(sum(1 for p in S if guessScore(p, x) != res) for res in results))



    gg = guessingGame(a)

    if gg != (4, 0):
        S.difference_update(set(p for p in S if guessScore(p, a) != gg))
        attempt(S, guessingGame)




if __name__ == '__main__':
    import sys
    secretCode = len(sys.argv) > 1 and sys.argv[1] or input("Please enter secret code(4 characters, 1-6): ")

    if len(secretCode) == 4 and not(set(secretCode) - set('123456')):
        print("Solving Please Wait...")

        attempts = 0
        
        def guessingGame(x):
            global attempts
            attempts += 1
            gg = Score(secretCode, x)
            print(x, '+' * gg[0] + '-' * gg[1])
            return gg
     
        solveGuessingGame(guessingGame)
        print("I WON and i found it in:", attempts, "attempts")

    else:
        print("Wrong input!!!")
        


