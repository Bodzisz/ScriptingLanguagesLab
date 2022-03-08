def firstDot(text):
    words = text.split()
    result = []
    for word in words:
        if word == "OCaml":
            result = []
        else:
            result.append(word)
    return result


def countA(text):
    counter = 0
    for letter in text:
        if letter == 'a' or letter == 'A':
            counter += 1
    return counter


def changeCommaToSemicolon(text):
    return text.replace(',', ";")


def countFor(text):
    counter = 0
    for word in text.split():
        if word.lower() == "for":
            counter = counter + 1
    return counter


def getUniqueChars(text):
    unique_chars = []
    for char in text:
        if char not in unique_chars:
            unique_chars.append(char)
    return unique_chars


input_text = "The OCaml toolchain includes an interactive top-level interpreter, a bytecode compiler, an optimizing native code compiler, a reversible debugger, and a package manager (OPAM). OCaml was initially developed in the context of automated theorem proving, and has an outsize presence in static analysis and formal methods software. Beyond these areas, it has found serious use in systems programming, web development, and financial engineering, among other application domains. The acronym CAML originally stood for Categorical Abstract Machine Language, but OCaml omits this abstract machine.[3] OCaml is a free and open-source software project managed and principally maintained by the French Institute for Research in Computer Science and Automation (INRIA). In the early 2000s, elements from OCaml were adopted by many languages, notably F# and Scala."
text = "My text is Ocaml one two three"
print(firstDot(input_text), "\n")

print(countA(input_text), "\n")

print(countFor(input_text), "\n")

print(getUniqueChars(input_text), "\n")

print(changeCommaToSemicolon(input_text))
