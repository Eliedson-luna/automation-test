import pyautogui as p
p.PAUSE = 0.3
def c():
    p.mouseDown()
    p.mouseUp()
def limpa():
    p.moveTo(x=1137, y=132)
    c()
def open():
    p.PAUSE = 0.5
    busca = input('insira o link:\n')
    p.press('winleft')
    p.write('chrome')
    p.press('enter')
    p.write(busca)
    p.press('enter')
    p.moveTo(x=695, y=128)
    c()
    p.moveTo(x=-1094, y=705)
    c()
def busca():
    p.PAUSE = 0.5
    busca = input('digite o termo de busca:\n')
    limpa()
    p.moveTo(x=731, y=126)
    c()
    p.write(busca)
    p.press('enter')
    p.moveTo(x=-1094, y=705)
    c()
def selector():
    while True:
        func = input('qual a função desejada ?\nOpen ou Busca?\n').lower()
        if func == 'open':
            print('funçao de abrir selecionada')
            open()
        elif func == 'busca':
            busca()
        elif func != 'open' or func != 'busca':  
            p = input('deseja encerrar ?\n(S/N)').lower()
            if p == 's':
                break
            else:
                continue
selector()