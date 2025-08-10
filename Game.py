import random, os

def load_words(path):
    with open(path, 'r', encoding='utf-8') as f:
        return [w.strip() for w in f if len(w.strip())==5]

if __name__ == "__main__":
    path = os.path.join(os.path.dirname(__file__),"words.txt")
    words = load_words(path)
    secret = random.choice(words).upper()
    attempts = 6
    for i in range(attempts):
        guess = input(f"Attempt {i+1}/{attempts}: ").strip().upper()
        if len(guess)!=5:
            print("Must be 5 letters.")
            continue
        if guess.lower() not in words:
            print("Word not in list.")
            continue
        if guess==secret:
            print("Correct! You win.")
            break
    else:
        print("Out of attempts. Secret:", secret)
