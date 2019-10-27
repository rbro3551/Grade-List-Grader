import statistics
top = ['Type', '#', 'min', 'max', 'avg', 'std']
tests = ['Tests', 0, 'n/a', 'n/a', 'n/a', 'n/a']
testscores = []
programs = ['Programs', 0, 'n/a', 'n/a', 'n/a', 'n/a']
programscores = []
def dchoice():
    '''Display all scores to the user and calculate the weighted if there is one'''
    for i in range(len(top)):
        print('{:<20}'.format(top[i]), end = '')
    print('\n')
    print('=' * 110)
    for i in range(len(tests)):
        print('{:<20}'.format(tests[i]), end = '')
    print('\n')
    for i in range(len(programs)):
        print('{:<20}'.format(programs[i]), end = '')
    print('\n')
    if (tests[2] != 'n/a') and (programs[2] != 'n/a'):
        scoreweight = ((tests[4] * .6) + (programs[4] * .4))
        print('The weighted scores is %f' % (scoreweight))
    else:
        print('The weighted scores is 0.00')
def choice1():
    '''Calculate all items in the list as if there was one specified test score added'''
    newtest = float(input('Enter the new test score 0-100'))
    testscores.append(newtest)
    tests[2] = min(testscores)
    tests[3] = max(testscores)
    tests[4] = (sum(testscores) / len(testscores))
    if len(testscores) > 1:
        tests[5] = statistics.stdev(testscores)
    tests[1] += 1
def choice2():
    global tests
    '''Calculate all items in the list as if there was one specified test score removed'''
    while True:
        testrem = float(input('Enter score of test to remove'))
        if testrem not in testscores:
            print('Does not exist')
            continue
        else:
            break
    testscores.remove(testrem)
    if len(testscores) == 0:
        tests = ['Tests', 0, 'n/a', 'n/a', 'n/a', 'n/a']
    else:
        tests[2] = min(testscores)
        tests[3] = max(testscores)
        tests[4] = (sum(testscores) / len(testscores))
        if len(testscores) > 1:
            tests[5] = statistics.stdev(testscores)
        else:
            tests[5] = 'n/a'
        tests[1] -= 1
def choice3():
    global tests
    '''Clear entries for tests'''
    tests = ['Tests', 0, 'n/a', 'n/a', 'n/a', 'n/a']
def choice4():
    '''Calculate all items in the list as if there was one specified program score added'''
    newprogram = float(input('Enter the new program score 0-100'))
    programscores.append(newprogram)
    programs[2] = min(programscores)
    programs[3] = max(programscores)
    programs[4] = (sum(programscores) / len(programscores))
    if len(programscores) > 1:
        programs[5] = statistics.stdev(programscores)
    programs[1] += 1
def choice5():
    '''Calculate all items in the list as if there was one specified program score removed'''
    global programs
    while True:
        progrem = float(input('Enter score of program to remove'))
        if progrem not in programscores:
            print('Does not exist')
            continue
        else:
            break
    programscores.remove(progrem)
    if len(programscores) == 0:
        programs = ['Programs', 0, 'n/a', 'n/a', 'n/a', 'n/a']
    else:
        programs[2] = min(programscores)
        programs[3] = max(programscores)
        programs[4] = (sum(programscores) / len(programscores))
        if len(programscores) > 1:
            programs[5] = statistics.stdev(programscores)
        else:
            programs[5] = 'n/a'
        programs[1] -= 1
def choice6():
    '''Clear all entries for programs'''
    global programs
    programs = ['Programs', 0, 'n/a', 'n/a', 'n/a', 'n/a']

while True:
    print('{:^24s}'.format('Grade Menu'))
    print('1 - Add Test')
    print('2 - Remove Test')                    #Display all options to user
    print('3 - Clear Tests')
    print('4 - Add Assignment')
    print('5 - Remove Assignments')
    print('6 - Clear Assignments')
    print('D - Display Scores')
    print('Q - Quit')
    choice = input()
    choice = choice.lower()
    if choice == 'd':
        print(dchoice())
    if choice == '1':
        choice1()
    if choice == '2':
        choice2()
    if choice == '3':
        choice3()
    if choice == '4':               #Perform specified user choices
        choice4()
    if choice == '5':
        choice5()
    if choice == '6':
        choice6()
    if choice == 'q':
        break