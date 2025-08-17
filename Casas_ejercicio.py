# Write code below 💖

# Inicializar puntos
Gryffindor1 = Gryffindor2 = Gryffindor3 = 0
Slytherin1 = Slytherin2 = Slytherin3 = 0
Ravenclaw1 = Ravenclaw2 = Ravenclaw3 = 0
Hufflepuff1 = Hufflepuff2 = Hufflepuff3 = 0

print("Ahora veremos la casa ganadora del Colegio Hogwarts")
print("Comencemos!!!")

print('Q1. Te gusta mas el amanecer o el atardecer?')
print('1) Amanecer')
print('2) Atardecer')

#Pregunta 1
respQ1 = int(input('Ingresa el numero con tu respuesta: '))

if respQ1 == 1:
  Gryffindor1 = 1
  Ravenclaw1 = 1
  print("Gryffindor y Ravenclaw obtienen un +1.")
elif respQ1 ==2:
  Hufflepuff1 = 1
  Slytherin1 = 1
  print("Hufflepuff y Slytherin obtienen un +1.")
else:
  print("Entrada incorrecta")

  #Pregunta 2

print("Q2. Cuando muera, quiero que la gente me recuerde como:")
print("1. El bueno")
print("2. El grande")
print("3. El sabio")
print("4. El valiente")

Q2 = int(input("Ingresa el numero con tu respuesta: "))
if Q2 == 1:
  Hufflepuff2 = 2
  print("Hufflepuff +2")
elif Q2 ==2:
  Slytherin2 = 2
  print("Slytherin +2")
elif Q2 == 3:
  Ravenclaw2 = 2
  print("Ravenclaw +2.")
elif Q2 == 4:
  Gryffindor2 = 2
  print("Gryffindor +2")
else:
  print("Entrada incorrecta")

  #Pregunta 3

print("Q3. Qué tipo de instrumento complace más a tu oído?: ")
print("1. El violin")
print("2. La trompeta")
print("3. El piano")
print("4. El tambor")

Q3 = int(input("Ingresa el numero con tu respuesta: "))

if Q3 == 1:
  Slytherin3 = 4
  print("Slytherin +4")
elif Q3 ==2:
  Hufflepuff3 = 4
  print("Hufflepuff +4")
elif Q3 == 3:
  Ravenclaw3 = 4
  print("Ravenclaw +4")
elif Q3 == 4:
  Gryffindor3 = 4
  print("Gryffindor +4")
else:
  print("Entrada incorrecta")

Griffindor = Gryffindor1 + Gryffindor2 + Gryffindor3
print("Grifindor obtiene ", Griffindor, " puntos")

Slytherin = Slytherin1 + Slytherin2 + Slytherin3
print("Slytherin obtiene ", Slytherin, " puntos")

Ravenclaw = Ravenclaw1 + Ravenclaw2 + Ravenclaw3
print("Ravenclaw obtiene ", Ravenclaw, " puntos")

Hufflepuff = Hufflepuff1 + Hufflepuff2 + Hufflepuff3
print("Hufflepuff obtiene ", Hufflepuff, " puntos")

if Griffindor > Slytherin and Griffindor > Ravenclaw and Griffindor > Hufflepuff:
  print("La casa ganadora de Hogwarts es: Griffindor")
elif Slytherin > Griffindor and Slytherin > Ravenclaw and Slytherin > Hufflepuff:
  print("La casa ganadora de Hogwarts es: Slytherin")
elif Ravenclaw > Griffindor and Ravenclaw > Slytherin and Ravenclaw > Hufflepuff:
  print("La casa ganadora de Hogwarts es: Ravenclow ")
elif Hufflepuff > Griffindor and Hufflepuff > Slytherin and Hufflepuff > Ravenclaw:
  print("La casa ganadora de Hogwarts es: Hufflepuf")
  