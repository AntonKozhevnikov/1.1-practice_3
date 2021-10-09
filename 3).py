n = int(input("Ведите число: "))
if ((n % 5 != 0) and (n % 7 != 0)):
    print("00")
if ((n % 5 != 0) and (n % 7 == 0)):
    print('10')
if ((n % 5 == 0) and (n % 7 != 0)):
    print("01")
if ((n % 5 == 0) and (n % 7 == 0)):
    print("11")
