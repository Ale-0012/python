"""
Ahora están instalando un nuevo sistema de entrada (el requisito de altura es de 137 cm y el costo es de 10 créditos) ¡y necesitan tu ayuda para escribir el programa para ello!

Crea un nuevo archivo llamado the_cyclone.py .

Pregúntele al usuario cuál es su altura y cuántos créditos tiene, y almacene los valores en una heightvariable y una creditsvariable.

Utilice una combinación de operadores relacionales y lógicos para crear las reglas:

Si son lo suficientemente altos y tienen suficientes créditos, imprime "¡Disfruta el viaje!"
De lo contrario, si tienen suficientes créditos, pero no son lo suficientemente altos, imprime "No eres lo suficientemente alto para viajar".
De lo contrario, si son lo suficientemente altos, pero no tienen suficientes créditos, imprime "No tienes suficientes créditos".
De lo contrario, imprima un mensaje indicando que no han cumplido ninguno de los requisitos.
"""

# Write code below 💖

altura = float(input('Ingrese su altura en cm: '))
creditos = int(input('Ingrese el numero de creditos que tiene: '))

if altura > 137 and creditos >= 10:
  print('Disfruta del viaje')
elif creditos >= 10 and altura < 137 :
  print('No eres lo suficientemente alto')
elif altura > 137 and creditos < 10:
  print('No tienes suficientes creditos')
else:
  print('No cumples ninguno de nuestros requisitos')

