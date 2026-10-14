def caesar(text, key, mode, alphabet):
    if mode == 2:
        key = -key

    result = ""
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index + key) % len(alphabet)
            result += alphabet[new_index]
        else:
            result += "_"

    return result

def getcontent():
    content = ""

    src = input("Möchtest du eine (D)atei verarbeiten oder einen (T)ext eingeben?: ")
    if src.upper() == "D":
        name = input("Gib den Namen der Quelldatei ein: ")
        with open(f"{name}", "r", encoding="utf-8") as file:
            content = file.read()
    else:
        content = input("Was möchtest du verarbeiten?\n")

    return content

def write_result(result: str):
    file_name = "ergebnis.txt"

    with open(file_name, "w", encoding="utf-8") as file:
        file.write(result)

    print(" ")
    print(f"Das Ergebnis wurde in der {file_name} gespeichert.")
    print(" ")
    return

def main():
    print("Programm startet...")

    alphabet = "abcdefghijklmnopqrstuvwxyzäöüßABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ0123456789 .,!?"

    option = int(input("Möchtest du etwas ver- oder entschlüsseln?\n1 - Verschlüsseln\n2 - Entschlüsseln\n"))

    if option == 1:
        n = int(input("Wähle für deine Verschlüsselung einen Verschiebungsindex: "))
        clear = getcontent()
        res = caesar(clear, n, option, alphabet)

        write_result(res)
        print("\nDein Verschlüsselter Text lautet:")
        print(res)

    elif option == 2:
        n = int(input("Was ist dein erwarteter Verschiebungsindex: "))
        cipher = getcontent()
        res = caesar(cipher, n, option, alphabet)
        
        write_result(res)
        print("\nDein Entschlüsselter Text lautet:")
        print(res)

if __name__ == "__main__":
    main()