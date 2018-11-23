pali = False
print('Sprawdzę, czy Twoje słowo jest palindromem!')
slowo = input('Podaj słowo: ')
x = len(slowo)/2
y = 0

while x>=1:
        if slowo[0+y] == slowo[-1-y]:
            y = y + 1
            x = x - 1
            pali = True
        else:
            print('Słowo "' + slowo + '" nie jest palindromem.')
            break
if x<1:
    pali == True
    print('Slowo "' + slowo + '" jest palindromem')
 
        
                            
                
