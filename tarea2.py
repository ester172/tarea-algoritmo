# Pedir al usuario un número N
N = int(input("Ingrese un número para la cuenta regresiva: "))

# Cuenta regresiva
for i in range(N, -1, -1):
    print(i)

# Mensaje de despegue
print("¡Despegue!")