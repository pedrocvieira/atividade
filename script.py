nome = input("Nome do aluno:")
notas = int(input('Nota:'))
if notas <= 5:
    notas = 6

if notas > 10:
    notas = 10

if notas == 0:
    exit()
f = open('dados.txt', "a")
f.write(f"{nome};{nome}\n")
f.close()
print(notas)