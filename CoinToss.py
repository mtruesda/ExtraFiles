import random

# coin toss file for determining who gets an extra shift on dates where I have an opening. guards like to fight over things like this so I will let the computer decide.

def main():
    strs = ['Myron',
            'Ella A',
            'Bennett',
            'Ali',
            'Lucy',
            'Andrew',
            'Julia',
            'Claire',
            'Olivia',
            'Ella B',
            'Ryan',
            'Danielle',
            'Kyle',
            'Jeremiah',
            'Owen',
            'Molly',
            'Max',
            'Sean',
            'Evan',
            'William',
            'Sophie',
            'Emily',
            'Elizabeth',
            'Makenzie',
            'Adrienne',
            'Charlotte',
            'Solana']
    
    boole = input('Do we want to remove any names? ') # get rid of non-considered individuals
    while (boole != 'no' and boole != 'No'):          # multiple
        try:                                          # if not in list, ignore input
            strs.remove(boole)
        except:
            print('name is not in the list')
        
        boole = input('Do we want to remove any names? ')
    
    print('Number of names:', str(len(strs)))         # let's me know the remaining
    val = int(input('How many generations? '))        # how many names do I want?
    
    rands = []
    for i in range(0, val):                           # gets random numbers
        rands.append(random.randint(0,len(strs)-1))
    for i in range(0, val):
        print(i+1, ': ', strs[rands[i]])              # puts together output

main()
