l = ["Bob", "Rolf", "Anne"] # List
t = ("Bob", "Rolf", "Anne") # Tuple, diferença é que ela é imutavel
s = {"Bob", "Rolf", "Anne"} # Sets, não permite duplicadas, a ordem não é garantida

print(l[0]) # Nome é subscript notation 
print(t[1])

#sets não deixam usar subscript notation

l[0] = "Smith"
print(l[0])

l.append("Smith")
print(l)
l.remove("Smith")
print(l)

s.add("Queirol")
print(s)
s.add("Queirol")
print(s)