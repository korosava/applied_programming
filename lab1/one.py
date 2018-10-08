# завдання 1
#_I_D_L_E___



# завдання 2

hel = 'hello, world'
print(hel)



# завдання 3

def func(x, y):

    if(abs(x/y) > abs(int(x/y))):
    
        return False
    else:
        return True
    pass



# завдання 4

def func1(x, y):

# провірка входу
    # немає простих чисел менших за 2
    if(y<2):
        return('No Simple Digits')
        pass
    elif(x<2):
        x=2
        pass
    

    # масив простих чисел
    simple = []
    # запобіжник, спрацьовує якщо число з діапазону [x; y] не просте,
    # запобігає його добавлення в масив простих чисел 
    fuse = False


    # перебір всіх елементів на відрізку [x; y]
    for r in range(x, y+1):
        # перевірка цілого ділення кожного з них націло на менше число [2,r)
        for a in range(2, r):
            # якщо воно ділиться націло на менше число значить воно не просте
            # вихід з циклу, застосування запобіжника
            if (func(r,a)):
                fuse = True
                break
            pass
        # якщо запобіжник виключений -> число просте, добавляємо його до масиву
        if (fuse == False):
            simple.append(r)
            pass
        # відключаємо запобіжник для наступного числа
        fuse = False
        
        pass
    # поврнення масиву простих чисел на проміжку [x;y]

    if (simple):
        return simple
    else:
        class NSDException(Exception):
            pass
        raise NSDException("немає простих чисел на даному відрізку")



# завдання 5

def func2(a):
    b = []
    listExist = 0
    for x in a:
        if isinstance(x, list):
            b.extend(x)
            listExist+=1
        else:
            b.append(x)
    if listExist == 0:
        b = None
    
    return b

# a - вхідний масив
def func3(a):
    
    while(True):
        if func2(a) == None:
            break
        a = func2(a)
    return a






