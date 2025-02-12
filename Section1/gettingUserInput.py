# Primeiro exemplo
#name = input("Enter your name: ")
#print(name)

size_input = input("Tamanho da sua casa (em pés quadrados)")
square_feet = int(size_input)
square_meters = square_feet / 10.8
print(size_input + " Pés quadrados equivalem a " + str(square_meters) + " metros quadrados") # equivalente ao string.Format()
print(f"{square_feet} Pés quadrados equivalem a {square_meters:.2f} metros quadrados") # equivalente ao $""