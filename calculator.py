#calculator app
#imports from .txt file, will make operation and will export results into another .txt file

with open('expresii.txt') as fp:
    ex = fp.readlines()

iesire2 = [eval(e.split('=')[0]) for e in ex if e.strip()]

with open('iesire.txt', 'w') as fp:
    for e, a in zip(ex, iesire2):
        fp.write(e.strip() + '=' + str(a) + '\n')
