if x<0:
    print('sss')
  34: x=43
  35:
if x < 0:
    print('menorrr')
  36:
if x < 0:
    print('menorrr')
    x+=1
elif x > 0:
    print('mayorr')
  37:
if x < 0:
    print('menorrr')
    x+=1
elif x > 0:
    print('mayorr')
  38:
if x<0:
    print('neg')
    x=x+1
elif x == 0:
    print('Zero')
else:
    print('Positive')
  39:
if x<0:
    print('neg')
    x=x+1
elif x == 0:
    print('Zero')
else:
    print('Positive')
    x=x-1
  40: x=1
  41: x=1
  42:
if x<0:
    print('neg')
    x=x+1
elif x == 0:
    print('Zero')
else:
    print('Positive')
    x=x-1
  43:
if x<0:
    print('neg')
    x=x+1
elif x == 0:
    print('Zero')
else:
    print('Positive')
    x=x-1
  44:
if x<0:
    print('neg')
    x=x+1
elif x == 0:
    print('Zero')
else:
    print('Positive')
    x=x-1
  45: sequence = [1,2,None,4,None,5]
  46: total = 0
  47:
for value in sequence:
    print(value)
  48:
for value in sequence:
    print(value)
    total++
  49:
for value in sequence:
    print(value)
    total=total+1
    value[total] = value[total]+1
  50: sequence = [1,2,2,4,5,5]
  51:
for value in sequence:
    print(value)
    total=total+1
    value[total] = value[total]+1
  52:
for value in sequence:
    if value is None:
        continue
    total += value
  53: sequence
  54:
for value in sequence:
    if value is None:
        continue
    total += value
  55: sequence
  56: total
  57: x=256
  58: total=0
  59:
while x > 0:
    if total > 500:
        break
    total += x
    x=x//2
  60: def maximo(x,y,z)
  61:
def maximo(x,y,z):
    a = x
    if x>y:
        a = y
    if x > z:
        a = z
    if y > z
  62:
def maximo(x,y,z):
    a = 0
    if x>y:
        a = x
    if x > z:
        a = x
    if y > z:
        a = y
    return a
  63: maximo(1,2,3)
  64:
def maximo(x,y,z):
    a = x
    for value in [x,y,z]:
        if a > value:
            a = value
    return a
  65: maximo(x,y,z)
  66: maximo(1,2,3)
  67:
def maximo(x,y,z):
    a = x
    for value in [x,y,z]:
        if a < value:
            a = value
    return a
  68: maximo(1,2,3)
  69: maximo(3,2,1)
  70: maximo(2,3,1)
  71: def cenetario(name,year)
  72:
def cenetario(name,year):
    if !isinstance(year, int):
  73:
def cenetario(name,year):
    if not isinstance(year, int):
  74:
def cenetario(name,year):
    if isinstance(year, int):
  75:
def cenetario(name,year):
    if not isinstance(year, int):
        year = int(year)
    print(100-year)
  76: centenario('pepe', 1985)
  77:
def centenario(name,year):
    if not isinstance(year, int):
        year = int(year)
    print(100-year)
  78: centenario('pepe', 185)
  79:
def centenario(name,year):
    if not isinstance(year, int):
        year = int(year)
    print(100+year)
  80: centenario('ma', 1985)
  81:
def centenario(name,year):
    if not isinstance(year, int):
        year = int(year)
    print(name+' cumplirá los 100 años en '+str(100+year))
  82: centenario('ma',1985)
  83: z = "first line \n continues to second \n this is thrid \n"
  84: z.splitlines()
  85: a = 'dsd '
  86: b= 'aaa'
  87: a+b
  88: template = "%.2f %s are worth % d"
  89: tempalte % (4.3, 'Rupia', 2)
  90: template % (4.3, 'Rupia', 2)
  91: a='hola como estas'
  92: a
  93: a[::-1]
  94:
if a:
    print('aa')
  95: is a
  96:
if a is int:
    print('aa')
  97:
if a not is int:
    print('aa')
  98:
if a is not int:
    print('aa')
  99: a='hola'
 100: a*a
 101: a*3
 102: a
 103: a.split('o')
 104:
def wc(texto):
    print(texto.split(' ').length)
 105: wc('hola ma')
 106:
def wc(texto):
    print('Numero palabras: '+str(len(texto.split(' '))))
 107: wc('hola ma')
 108:
def wc(texto):
    print('Numero palabras: '+str(len(texto.split(' '))))
    print('Numero lineas: '+str(len(texto.split('\n'))))
 109: wc('hola ma\ncomo estas')
 110:
def wc(texto):
    print('Numero palabras: '+str(len(texto.split(' '))))
    print('Numero lineas: '+str(len(texto.split('\n'))))
 111: a='hola'
 112: len(a)
 113:
def wc(texto):
    print('Numero palabras: '+str(len(texto.split(' '))))
    print('Numero lineas: '+str(len(texto.split('\n'))))
    print('Numero letras: '+str(len(texto)))
 114: a.split()
 115:
def wc(texto):
    wordnumber = 0
    for line in texto.split('\n'):
        wordnumber += len(line.split(' '))
    print('Numero palabras: '+str(wordnumber))
    print('Numero lineas: '+str(len(texto.split('\n'))))
    print('Numero letras: '+str(len(texto)))
 116: wc('hola ma\ncomo estas')
 117:
def removechar(texto,letra):
    index = 1
    newtexto = ''
    for letra in texto:
        if letra == index:
             continue
        newtexto += letra
 118: removechar('hola',2)
 119:
def removechar(texto,letra):
    index = 1
    newtexto = ''
    for letra in texto:
        if letra == index:
             continue
        newtexto += letra
    print newtexto
 120:
def removechar(texto,letra):
    index = 1
    newtexto = ''
    for letra in texto:
        if letra == index:
             continue
        newtexto += letra
    print(newtexto)
 121: removechar('hola',2)
 122:
def removechar(texto,letra):
    index = 1
    newtexto = ''
    for letra in texto:
        if letra == index:
             continue
        newtexto += letra
        index+=1
    print(newtexto)
 123: removechar('hola',2)
 124:
def removechar(texto,letra):
    index = 1
    newtexto = ''
    for letra in texto.split():
        if letra == index:
             continue
        newtexto += letra
        index+=1
    print(newtexto)
 125: removechar('hola',2)
 126: %history -g
