from areas import Areas

figuras = Areas()

print("1. Cuadrado")
print("2. Rectángulo")
print("3. Triángulo")
print("4. Círculo")
opcion = input("Elige una figura (1-4): ")

if opcion == "1":
    lado = float(input("Lado: "))
    print("Área:", figuras.cuadrado(lado))

elif opcion == "2":
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    print("Área:", figuras.rectangulo(base, altura))

elif opcion == "3":
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    print("Área:", figuras.triangulo(base, altura))

elif opcion == "4":
    radio = float(input("Radio: "))
    print("Área:", figuras.circulo(radio))
    
else:
    print("Opción inválida")
