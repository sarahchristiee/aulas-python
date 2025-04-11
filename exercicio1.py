primos = 0
i = 0
for i in range(1,11):
    num = int(input(f"{i}° Digite um número: "))
    i += 1
    if num % 3 == 0:
        primos += 1
print(f"Total de núemros que são divisivés por 3: {primos}")