# F - Strings

name = "Bob"

print(f"Hello, {name}")

name = "Rolf"

print(f"Hello, {name}")

# Template strings with .format()

name = "Bob1"
greeting = "Hello, {}"
with_name = greeting.format(name)

print(with_name)

longer_phrase = "Hello, {}. Today is {}."

formatted = longer_phrase.format(name, "Terça")

print(formatted)