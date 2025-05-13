"""
projekt_2.py: první projekt do Engeto Online Python Akademie

author: David Štefaník
email: stefanik.david@seznam.cz
"""
import random
import time

# Vypíše uvítací zprávu s instrukcemi pro uživatele a pozdraví ho
def greet_user():
    print("Hi there!")
    print("-----------------------------------------------")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")
    print("Enter a number:")
    print("-----------------------------------------------")

# Vygeneruje tajné, unikátní čtyřmístné číslo, nezačínající nulou
def generate_secret_number():
    digits = [str(i) for i in range(10)]
    while True:
        random.shuffle(digits)
        if digits[0] != '0':
            secret = ''.join(digits[:4])
            return secret

# Zkontroluje, zda je tip platný (4 různé číslice, nezačíná nulou)
def is_valid_guess(guess):
    if not guess.isdigit():
        print("Please enter only digits.")
        return False
    if len(guess) != 4:
        print("Number must have exactly 4 digits.")
        return False
    if guess[0] == '0':
        print("Number cannot start with zero.")
        return False
    if len(set(guess)) != 4:
        print("Digits must be unique.")
        return False
    return True

# Spočítá počet bulls (správná číslice na správném místě) a cows (správná číslice na špatném místě)
def count_bulls_and_cows(secret, guess):
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum((min(secret.count(d), guess.count(d)) for d in set(guess))) - bulls
    return bulls, cows

# Vrací jednotné nebo množné číslo podle počtu
def pluralize(count, singular, plural):
    return singular if count == 1 else plural

# Formátuje čas na minuty a sekundy
def format_time(seconds):
    minutes = int(seconds // 60)
    sec = int(seconds % 60)
    if minutes > 0:
        return f"{minutes} min {sec} sec"
    else:
        return f"{sec} sec"

# Hlavní funkce hry
def play_game():
    greet_user()  
    secret = generate_secret_number()  
    attempts = 0  
    start_time = time.time()  

    while True:
        guess = input(">>> ").strip()  
        if not is_valid_guess(guess): 
            continue
        attempts += 1  
        bulls, cows = count_bulls_and_cows(secret, guess)  
        print(f">>> {guess}")  

        if bulls == 4:
            # Pokud uživatel uhodl číslo, vypíše gratulaci a čas
            elapsed = time.time() - start_time
            print("Correct, you've guessed the right number")
            print(f"in {attempts} {pluralize(attempts, 'guess', 'guesses')}!")
            print(f"Time taken: {format_time(elapsed)}")
            print("-----------------------------------------------")
            print("That's amazing!")
            break
        else:
            # Pokud číslo nebylo uhodnuto, vypíše počet bulls a cows
            bulls_word = pluralize(bulls, 'bull', 'bulls')
            cows_word = pluralize(cows, 'cow', 'cows')
            print(f"{bulls} {bulls_word}, {cows} {cows_word}")
            print("-----------------------------------------------")

# Spuštění hry
if __name__ == "__main__":
    play_game()