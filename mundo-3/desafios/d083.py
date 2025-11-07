ex = str(input('Digite a expressão: '))
pare = 0
for ltr in ex:
    if ltr == '(':
        pare += 1
    elif ltr == ')':
        pare -= 1
if pare != 0:
    print('Sua expressão está incorreta!')
else:
    print('Sua expressão está correta!')