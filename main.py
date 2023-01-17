import random

play_game = 'y'
start = 1
end = 100
direction = 'N'
smallest = start
largest = end
 

while play_game == 'y':
    smallest = start
    largest = end
    print('Guesss a number!between 1 and 100: ')
    try_number = random.randint(start,end)
    print(try_number)
    counter = 10
    direction = 'N'
    
    while direction  != 'c':
        direction= input('Is it too large(L), too small(S), or correct(C)')
        if direction == 'S':
            if try_number > smallest:
                smallest = try_number + 1
            try_number = random.randint(smallest,largest)
            print(try_number)
        if direction == 'L':
            if try_number < largest:
                largesr = try_number
            try_number = random.randint(smallest,largest)
            print(try_number)
        counter = counter + 1
    print('I got it! I trid ' + str(counter) + 'times.')
    play_game = input('continue? ')
