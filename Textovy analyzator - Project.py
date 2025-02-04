
header1 = "První projekt do Engeto Online Python Akademie"
header2 = "     autor: Adéla Hrabovská Glosová "
header3 = "     email: adel.hrabovska@seznam.cz"

TEXTS = ['''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30N and the Union Pacific Railroad,
    which traverse the valley. ''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
    ]

registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

def login_and_analyze():
    import re
    import time

    print("")
    print('*' * 46)
    print(header1)
    print(header2)
    print(header3)
    print('*' * 46)
    time.sleep(1)  # Pauza 1 sekunda

    username = input("Zadejte přihlašovací jméno: ")
    password = input("Zadejte heslo: ")

    if username in registered_users and registered_users[username] == password:
        print(f"\n*** Ahoj, {username}! Vítej v analyzátoru textu. ***")
        print()
    else:
        print("Neplatné přihlašovací údaje. Program bude ukončen.")
        return

    print("    Vyberte si jeden z textů ( 1 -", len(TEXTS), ")")
    print()
    time.sleep(0.5)

    for i, text in enumerate(TEXTS, start=1):
        print(f"{i}. {text}")
    print()

    user_input = input("Zadejte číslo textu: ")

    while not user_input.isdigit() or not (1 <= int(user_input) <= len(TEXTS)):
        print("Neplatný vstup. Prosím, zadejte číslo mezi 1 a", len(TEXTS))
        user_input = input("Zadejte číslo textu: ")

    choice = int(user_input) - 1
    selected_text = TEXTS[choice]

    words = selected_text.split()
    num_words = len(words)
    capitalized_words = len([word for word in words if word[0].isupper()])
    all_upper_words = len([word for word in words if word.isupper()])
    all_lower_words = len([word for word in words if word.islower()])

    numbers = re.findall(r'\b\d+\.?\d*\b', selected_text)
    num_numbers = len(numbers)
    sum_numbers = sum(float(number) for number in numbers) if num_numbers > 0 else 0

    print(f"\nStatistiky pro vybraný text:")
    print(f"Počet slov: {num_words}")
    time.sleep(0.5)
    print(f"Počet slov začínajících velkým písmenem: {capitalized_words}")
    time.sleep(0.5)
    print(f"Počet slov psaných velkými písmeny: {all_upper_words}")
    time.sleep(0.5)
    print(f"Počet slov psaných malými písmeny: {all_lower_words}")
    time.sleep(0.5)
    print(f"Počet čísel: {num_numbers}")
    time.sleep(0.5)
    print(f"Suma všech čísel: {sum_numbers}")
    time.sleep(1)

    length_counts = {}
    for word in words:
        length = len(word)
        length_counts[length] = length_counts.get(length, 0) + 1

    max_length = max(length_counts.keys())
    print("-" * 30)
    print("Délka slova | Počet výskytů")
    print("-" * 30)

    for length in range(1, max_length + 1):
        count = length_counts.get(length, 0)
        print(f"{length:>12}| {'*' * count} {count}")

    print("")
    print("Toto je konec programu, děkuji za použití.")
  
login_and_analyze()
