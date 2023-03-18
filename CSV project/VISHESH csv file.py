
import pandas as pd
import numpy as np
import time
path = "america1.csv"
x1 = pd.read_csv("america1.csv")
# "C:\Users\MY LENOVO\Desktop\Vishesh\Python Progarms\america1.csv"

#x1 = pd.DataFrame({'Month':['jan','feb','march','april','mqy','june','july','aug','sep'],'Cases':[3333,86677,76567,5433,6544,665,754,655,644],'TotalCases':[3838,7666,4335,75335,86544,8754,86543,9864,334],'Death':[727,7772,2872,2827,4949,626,30,39,47], 'totalCases':[2772,33,887,546,654,665,654,543,765],'Recovery':[7272,7626,9494,2726,727,73773,3737,262598,2727],'TotalRecovery':[4345,457,526,747,854,75,7765,756,85]})
df = x1
headingList = ["Month", "Cases", "TotalDeathCases","Death", "TotalCases", "Recovered", "TotalRecovery"]


def menu():
    startingline = '''================================================================================
                             Covid-19 Program File
================================================================================
      • Basic task -
         1. Reading CSV file
         2. Reading CSV file with index
         3. Assign new column name

       • Data Manipulation -
          4. Adding new column
          5. Deleting existing column
          6. Statistical Functions
          7. Mathematical Functions
          8. Display specific column
          9. Read n number of records from top
          10. Read n number of records from bottom
          11. Arrange records

================================================================================
    Press q to quit
'''
    
    print(startingline)


def end():
    print("================================================================================")


def csv():  # 1
    print('''Reading CSV file - America

    ''')
    print(x1)


def no_index():  # 2
    print('\n')
    print('Reading CSV America without indexing')
    x2 = pd.read_csv(path, index_col=0)
    print('\n')
    print(x2)


def new_name():  # 3
    x200 = []
    for I in range(0, 7):
        x3 = str(
            input(f'Enter new column name for {headingList[I]} column -      '))
        x200.append(x3)

    print('Adding new column name ....     ')
    print('\n')
    x4 = pd.read_csv(path, skiprows=1, names=x200)
    print(x4)


def add_col():  # 4
    x5 = str(input('Enter new column name -  '))
    print(f'Adding {x5} column in America file')
    print('\n')
    print('Enter values')
    y1 = []
    for i in range(12):
        y2 = str(input(''))
        y1.append(y2)
    x1[x5] = y1
    print(df)


def del_col():  # 5
    try:
        x6 = str(input('Enter column name -  ')).capitalize()
        df1 = x1.drop(x6, axis=1)
        print(f'deleting {x6}')
        print('\n')
        print(df1)
    except Exception:
        print('Please enter valid column name')
        del_col()


def columns():
    print('''

    • Choose one of these column
    1. Cases
    2. Total cases
    3. Death
    4. Total death
    5. Recovery
    6. Total recovery
    ''')

    # opti = int(input('Enter here \t ')) → not working here
    print('\n')


def mean():  # 6.1

    print('Finding mean ')
    columns()
    opti = int(input('Enter here \t '))
    if opti == 1:
        print('    Mean is ', round(x1.Cases.mean(),2))
    elif opti == 2:
        print('    Mean is ', round(x1.TotalCases.mean(),2))
    elif opti == 3:
        print('    Mean is ', round(x1.Death.mean(),2))
    elif opti == 4:
        print('   Mean is ', round(x1.totalCases.mean(),2))
    elif opti == 5:
        print('    Mean is ', round(x1.Recovery.mean(),2))
    elif opti == 6:
        print('    Mean is ', round(x1.TotalRecovery.mean(),2))
    else:
        print('bad choose ')


def mode():  # 6.2

    print('Finding mode')
    columns()
    opti = int(input('Enter here \t '))

    if opti == 1:
        print('    Mode is ', round(x1.Cases.mod(),2))
    elif opti == 2:
        print('    Mode is ', round(x1.TotalCases.mod(),2))
    elif opti == 3:
        print('    Mode is ', round(x1.Death.mod(),2))
    elif opti == 4:
        print('    Mode is ', round(x1.totalCases.mod(),2))
    elif opti == 5:
        print('    Mode is ', round(x1.Recovery.mod(),2))
    elif opti == 6:
        print('    Mode is ', round(x1.TotalRecovery.mod(),2))
    else:
        print('bad choose ')


def median():  # 6.3

    print('Finding median')
    columns()
    opti = int(input('Enter here \t '))

    if opti == 1:
        print('    Median is ', round(x1.Cases.median(),2))
    elif opti == 2:
        print('    Median is ', round(x1.TotalCases.median(),2))
    elif opti == 3:
        print('    Median is ', round(x1.Death.median(),2))
    elif opti == 4:
        print('    Median is ', round(x1.totalCases.median(),2))
    elif opti == 5:
        print('    Median is ', round(x1.Recovery.median(),2))
    elif opti == 6:
        print('    Median is ', round(x1.TotalRecovery.median(),2))
    else:
        print('bad choose ')


def var():  # 6.4

    print('Finding Variation')
    columns()
    opti = int(input('Enter here \t '))

    if opti == 1:
        print('    Variation is ', round(x1.Cases.var(),2))
    elif opti == 2:
        print('    Variation is ', round(x1.TotalCases.var(),2))
    elif opti == 3:
        print('    Variation is ', round(x1.Death.var,2))
    elif opti == 4:
        print('    Variation is ', round(x1.totalCases.var,2))
    elif opti == 5:
        print('    Variation is ', round(x1.Recovery.var,2))
    elif opti == 6:
        print('    Variation is ', round(x1.TotalRecovery.var,2))
    else:
        print('bad choose ')


def std():  # 6.5
    print('Finding Standard Variation')
    columns()
    opti = int(input('Enter here \t '))

    if opti == 1:
        print('    Standard Variation is ', round(x1.Cases.std(),2))
    elif opti == 2:
        print('    Standard Variation is ', round(x1.TotalCases.std,2))
    elif opti == 3:
        print('    Standard Variation is ', round(x1.Death.std,2))
    elif opti == 4:
        print('    Standard Variation is ', round(x1.totalCases.std,2))
    elif opti == 5:
        print('    Standard Variation is ', round(x1.Recovery.std,2))
    elif opti == 6:
        print('    Standard Variation is ', round(x1.TotalRecovery.std,2))
    else:
        print('bad choose ')


def allstastical():  # 6.6
    print('Ok')
    columns()
    opti = int(input('Enter here \t '))

    if opti == 1:
        print(x1.cases.describe())
    elif opti == 2:
        print(x1.totalcases.describe())
    elif opti == 3:
        print(x1.death.describe())
    elif opti == 4:
        print(x1.totalCases.describe())
    elif opti == 5:
        print(x1.recover.describe())
    elif opti == 6:
        print(x1.totalrecover.describe())
    else:
        print('bad choose ')


def statistics():  # 6.0
    print('Choose one of the following options')
    print('\n')
    print('  1. Mean \n  2. Median \n  3. Mode \n  4. Variation \n  5. Standard Variation \n  6. All Statistical Function')
    option = int(input('  '))
    print(x1)
    print('\n')
    if option == 1:
        mean()
    elif option == 2:
        median()
    elif option == 3:
        mode()
    elif option == 4:
        var()
    elif option == 5:
        std()
    elif option == 6:
        allstastical()
    else:
        print('bad choose')


def max():  # 7.1
    print('Finding maximum value')
    columns()
    opti = int(input('Enter here \t '))

    if opti == 1:
        print('    Maximum is ', x1.Cases.max())
    elif opti == 2:
        print('    Maximum is ', x1.TotalCases.max())
    elif opti == 3:
        print('    Maximum is ', x1.Death.max())
    elif opti == 4:
        print('    Maximum is ', x1.totalCases.max())
    elif opti == 5:
        print('    Maximum is ', x1.Recovery.max())
    elif opti == 6:
        print('    Maximum is ', x1.TotalRecovery.max())
    else:
        print('bad choose ')


def min():  # 7.2
    print('Finding minimum value')
    columns()
    opti = int(input('Enter here \t '))

    opti = int(input(''))
    print('\n')
    if opti == 1:
        print('    Minimum is ', x1.Cases.min())
    elif opti == 2:
        print('    Minimum is ', x1.TotalCases.min())
    elif opti == 3:
        print('    Minimum is ', x1.Death.min())
    elif opti == 4:
        print('    Minimum is ', x1.totalCases.min())
    elif opti == 5:
        print('    Minimum is ', x1.Recovery.min())
    elif opti == 6:
        print('    Minimum is ', x1.TotalRecovery.min())
    else:
        print('bad choose ')


def avg():  # 7.3
    print('Finding average ')
    columns()
    opti = int(input('Enter here \t '))

    if opti == 1:
        print('    Average is ', x1.Cases.avg())
    elif opti == 2:
        print('    Average is ', x1.TotalCases.avg())
    elif opti == 3:
        print('    Average is ', x1.Death.avg())
    elif opti == 4:
        print('    Average is ', x1.totalCases.avg())
    elif opti == 5:
        print('    Average is ', x1.Recovery.avg())
    elif opti == 6:
        print('    Average is ', x1.TotalRecovery.mean())
    else:
        print('bad choose ')


def count():  # 7.4
    print('Counting all values    ')
    columns()
    opti = int(input('Enter here \t '))

    if opti == 1:
        print('    Count is ', x1.Cases.count())
    elif opti == 2:
        print('    Count is ', x1.TotalCases.count())
    elif opti == 3:
        print('    Count is ', x1.Death.count())
    elif opti == 4:
        print('    Count is ', x1.totalCases.count())
    elif opti == 5:
        print('    Count is ', x1.Recovery.count())
    elif opti == 6:
        print('    Count is ', x1.TotalRecovery.count())
    else:
        print('bad choose ')


def add():  # 7.5
    z1 = int(input('Enter value  '))
    x27 = str(input('Enter column name    ')).capitalize()
    print('\n')
    x1[x27] = x1[x27]+z1
    print(x1)


def sub():  # 7.6
    z2 = int(input('Enter value  '))
    x28 = str(input('Enter column name    ')).capitalize()
    print('\n')
    x1[x28] = x1[x28]-z2
    print(x1)


def mult():  # 7.7
    z3 = int(input('Enter value  '))
    x29 = str(input('Enter column name    ')).capitalize()
    print('\n')
    x1[x29] = x1[x29]*z3
    print(x1)


def div():  # 7.8
    z4 = int(input('Enter value  '))
    x30 = str(input('Enter column name    ')).capitalize()
    print('\n')
    if z4 == 0:
        print('bad choice')
    else:
        x1[x30] = x1[x30]/z4
    print(x1)


def mathematical():  # 7.0
    print('Choose one of the following options')
    print('\n')
    print('  1. Maximum \n  2. Minimum \n  3. Addition \n  4. Subtraction \n  5. Division \n  6. Multiplication \n  7. Count \n  8. Average')
    optio = int(input('  '))
    print(x1)
    print('\n')
    if optio == 1:
        max()
    elif optio == 2:
        min()
    elif optio == 3:
        add()
    elif optio == 4:
        sub()
    elif optio == 5:
        mult()
    elif optio == 6:
        div()
    elif optio == 7:
        count()
    elif optio == 8:
        avg()
    else:
        print('bad choose')



def specific():  # 8
    x17 = int(input('Enter no of records    '))
    x18 = int(input('Enter no of columns    '))
    print('Wait...')
    print('\n')
    try:
        if x18 == 1:
            x19 = str(input('Enter column name    ')).capitalize()
            print(pd.read_(path, usecols=[x19], nrows=x17))
        elif x18 == 2:
            x19 = str(input('Enter column name    ')).capitalize()
            x20 = str(input('Enter column name    ')).capitalize()
            print(pd.read_csv(path, usecols=[x19, x20], nrows=x17))
        elif x18 == 3:
            x19 = str(input('Enter column name    ')).capitalize()
            x20 = str(input('Enter column name    ')).capitalize()
            x21 = str(input('Enter column name    ')).capitalize()
            print(pd.read_csv(path, usecols = [x19, x20, x21], nrows = x17))
        elif x18 == 4:
            x19 = str(input('Enter column name    ')).capitalize()
            x20 = str(input('Enter column name    ')).capitalize()
            x21 = str(input('Enter column name    ')).capitalize()
            x22 = str(input('Enter column name   ')).capitalize()
            print(pd.read_csv(path, usecols = [x19, x20, x21,x22], nrows = x17))
        elif x18 == 5:
            x19 = str(input('Enter column name    ')).capitalize()
            x20 = str(input('Enter column name    ')).capitalize()
            x21 = str(input('Enter column name    ')).capitalize()
            x22 = str(input('Enter column name   ')).capitalize()
            x23 = str(input('Enter column name   ')).capitalize()
            print(pd.read_csv(path, usecols = [x19, x20, x21,x22,x23], nrows = x17))
        elif x18 == 6:
            x19 = str(input('Enter column name    ')).capitalize()
            x20 = str(input('Enter column name    ')).capitalize()
            x21 = str(input('Enter column name    ')).capitalize()
            x22 = str(input('Enter column name   ')).capitalize()
            x23 = str(input('Enter column name   ')).capitalize()
            x24 = str(input('Enter column name   ')).capitalize()
            print(pd.read_csv(path, usecols = [x19, x20, x21,x22,x23,x24], nrows = x17))
        elif x18 == 7:
            x19 = str(input('Enter column name    ')).capitalize()
            x20 = str(input('Enter column name    ')).capitalize()
            x21 = str(input('Enter column name    ')).capitalize()
            x22 = str(input('Enter column name   ')).capitalize()
            x23 = str(input('Enter column name   ')).capitalize()
            x24 = str(input('Enter column name   ')).capitalize()
            x25 = str(input('Enter column name   ')).capitalize()
            print(pd.read_csv(path, usecols = [x19, x20, x21,x22,x23,x24,x25], nrows = x17))
        else:
            print('Out of range')
    except Exception:
        print('Error - Write column name correctly')

def nTop():  # 9
    try:
        x23 = int(input('Enter no of records    '))
        print('Reading ', x23, ' rows from top')
        print('\n')
        print(df.head(x23))
    except Exception:
        print('Error - Please enter number as input')
        nTop()
    


def nBottom():  # 10
    try:
        x24 = int(input('Enter no of records     '))
        print('Reading ', x24, ' rows from bottom')
        print('\n')
        print(df.tail(x24))
    except Exception:
        print('Error - Please enter number as input')
        nBottom()


def arrange():  # 11
    print('Arranging values')
    print('\n')
    x25 = str(input('Enter column name    ')).capitalize()
    order = str(
        input('Arrang in ascending order or descending order (a,o)   ')).lower()
    if order == 'a':
        x26 = x1.sort_values(by= x25, ascending = True)
    else:
        x26 = x1.sort_values(by= x25, ascending =False)
    print('\n')
    print(x26)


def outro():
    print('''================================================================================

                                                     Thank You
                                                     Create By Vishesh
                                                     Cource - B.Tech 
                                                            (1st year)
                                                     Section - V 
                                                     
================================================================================
    

''')


try:
    while (True):
        menu()
        user = input('Choose appropriate option for menu -  ')
        opt = int(user)
        if opt == 1:
            csv()
            outro()
        elif opt == 2:
            print(x1)
            no_index()
            outro()
        elif opt == 3:
            print(x1)
            new_name()
            outro()
        elif opt == 4:
            print(x1)
            add_col()
            outro()
        elif opt == 5:
            print(x1)
            del_col()
            outro()
        elif opt == 6:
            statistics()
            outro()
        elif opt == 7:
            mathematical()
            outro()
        elif opt == 8:
            print(x1)
            specific()
            outro()
        elif opt == 9:
            print(x1)
            nTop()
            outro()
        elif opt == 10:
            print(x1)
            nBottom()
            outro()
        elif opt == 11:
            print(x1)
            arrange()
            outro()
        else:
            print('nope')

        userrepeat = input('do you want to restart (Y/N):    ')
        userrepeat = userrepeat.lower()
        if userrepeat != 'y':
            print('\n')
            break
except Exception:
    print('error occurred')
