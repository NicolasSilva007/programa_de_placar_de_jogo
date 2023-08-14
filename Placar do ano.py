placar1 = int(input("Santos: "))
placar2 = int(input("Barcelona: "))

print (f"Santos {placar1}-{placar2} Barcelona")

if placar1 > placar2:
   print ("Vitoria Santos")
elif placar1 < placar2:
   print("Vitoria Barcelona")
elif placar1 == placar2:
   print ("empate")


