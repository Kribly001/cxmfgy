numero1=int(input("Ingresa el primer numero: "))
numero2=int(input("Ingresa el segundo numero:"))
print("1-Suma")
print("2-Resta")
print("3-Multiplicacion")
print("4-Division")
calculo=int(input("que calculo desea hacer"))

if calculo==1:
    print(numero1+numero2)
elif calculo==2:
    print(numero1-numero2)
elif calculo==3:
    print(numero1*numero2) 
elif calculo==4:
    print(numero1/numero2)
else:
    print("No ingreso una opcion correcta")    
    







