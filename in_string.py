def check_vowels():
    # Código a implementar utilizando input.
    nombre = input()
    name = nombre.lower()
    Tienea = "a" in name 
    print(f"Contiene a: {Tienea}")
    Tienee = "e" in name
    print(f"Contiene e: {Tienee}")
    Tienei = "i" in name
    print(f"Contiene i: {Tienei}")
    Tieneo = "o" in name
    print(f"Contiene o: {Tieneo}")
    Tieneu = "u" in name
    print(f"Contiene u: {Tieneu}")

check_vowels()
# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
