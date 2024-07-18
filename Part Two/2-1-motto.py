import os

path = os.path.dirname(os.path.abspath(__file__))

file = open(path+'/'+'motto.txt','w')
file.write("Fiat Lux!")


file.close()

file = open(path+'/'+'motto.txt','a')
file.write("\nLight Speed!")
file.close()