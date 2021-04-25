# program solves Tower of Hanoi puzzle for any even amount of rings from 2 to 8
import time # I used time to show that no matter how long is the code for cycle function, it is way faster


def user_choice(choice):
    if choice == 1:
        rings = int(input('Amount of rings from 1 to 8 '))
        core1 = 'First core'
        core2 = 'Second core'
        core3 = 'Third core'
        start = time.time()
        tower_recursive(rings, core1, core2, core3)
        print(time.time() - start)
    if choice == 2:
        rings = int(input('Even number of  rings from 1 to 8 '))
        core1 = ''
        for i in range(1,rings+1):
            core1 = core1 + str(i)
        print(core1[::-1])
        core1 = core1[::-1]
        core2 = ''
        core3 = ''
        start = time.time()
        tower_cycle(core1, core2, core3, core1)
        print(time.time() - start)


def tower_recursive(rings, main_core, ex_core, end_core):
    '''

    :param rings: amount of rings
    :param main_core: core you take from
    :param ex_core: extra core
    :param end_core: core you place to
    :return:
    '''
    if rings > 0:
        tower_recursive(rings - 1, main_core, end_core, ex_core)
        print('Replace ring from', main_core, 'to', end_core)
        tower_recursive(rings - 1, ex_core, main_core, end_core)


def tower_cycle(main_core, ex_core, end_core, result):
    '''

    :param main_core: core where rings at the beginning
    :param ex_core: just second core
    :param end_core: core where we need to move rings
    :return:
    '''

    while end_core != result:
        if ex_core == '':
            ex_core = ex_core = main_core[-1]
            main_core = main_core[:-1]
            print('From 1 to 2')
        elif main_core == '':
            main_core = main_core + ex_core[-1]
            ex_core = ex_core[:-1]
            print('From 2 to 1')
        elif main_core != '' and ex_core != '':
            if main_core[-1] < ex_core[-1]:
                ex_core = ex_core + main_core[-1]
                main_core = main_core[:-1]
                print('From 1 to 2')
            else:
                main_core = main_core + ex_core[-1]
                ex_core = ex_core[:-1]
                print('From 2 to 1')
        if end_core == '':
            end_core = end_core + main_core[-1]
            main_core = main_core[:-1]
            print('From 1 to 3')
        elif main_core == '':
            main_core = main_core + end_core[-1]
            end_core = end_core[:-1]
            print('From 3 to 1')
        elif end_core != '' and main_core !='':
            if main_core[-1] < end_core[-1]:
                end_core = end_core + main_core[-1]
                main_core = main_core[:-1]
                print('From 1 to 3')
            else:
                main_core = main_core + end_core[-1]
                end_core = end_core[:-1]
                print('From 3 to 1')
        if end_core == '':
            end_core = end_core + ex_core[-1]
            ex_core = ex_core[:-1]
            print('From 2 to 3')
        elif ex_core == '':
            ex_core = ex_core + end_core[-1]
            end_core = end_core[:-1]
            print('From 3 to 2')
        elif ex_core != '' and ex_core != '':
            if ex_core[-1] < end_core[-1]:
                end_core = end_core + ex_core[-1]
                ex_core = ex_core[:-1]
                print('From 2 to 3')
            else:
                ex_core = ex_core + end_core[-1]
                end_core = end_core[:-1]
                print('From 3 to 2')


def main():
    print('Yoy can chose what variant of puzzle solving you would like to use')
    print('1 - recursive\n2 - cycle')
    choice = int(input())
    user_choice(choice)


main()
