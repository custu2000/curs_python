#ex 7


str1=raw_input('introduceti stringul: ')

print ("String : {} Caracterul al treilea: {}".format(str1,str1[2]))
print ("String : {} Caracterul al doilea pana la sfarsit: {}".format(str1,str1[1:]))
print ("String : {} primele 5 caractere: {}".format(str1,str1[0:5]))
print ("String : {} toate fara ultimele 2: {}".format(str1,str1[0:-2]))
print ("String : {} doar pe indici par: {}".format(str1,str1[0::2]))
print ("String : {} doar pe indici impar: {}".format(str1,str1[1::2]))
print ("String : {} doar pe indici impar: {}".format(str1,str1[1::2]))
print ("String : {} Afisare inversa: {}".format(str1,str1[::-1]))
print ("String : {} Afisare inversa fiecare al doilea caracter: {}".format(str1,str1[::-2]))
print ("String : {} length: {}".format(str1,len(str1)))

