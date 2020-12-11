print("Programa de notas")

nota = int(input("Dime una nota--> "))
nota = int(nota)
while nota < 0 or nota >10:
    nota = int(input("Dime una nota valida anda--> "))
    

if nota >=0 and nota <5:
    print("Hay que estudiar, estas Suspenso")

elif nota >=5 and nota <6:
    print("Aprobaito pero a estudiar, Aprobado")
    
elif nota >=6 and nota <7:
    print("Vale vale pero aprieta un poco mas, Bien")
    
elif nota >=7 and nota <9:
    print("Bueno un pedazo de Notable")
    
elif nota >=9 and nota <10:
    print("Ni tan mal un Sobresaliente")

elif nota==10:
    print("Perfecto, Matricula de honor")




