# milestone_01.py
import random, os

def load_words(path):
    with open(path, 'r', encoding='utf-8') as f:
        words = [w.strip() for w in f if len(w.strip())==5]
    return words

if __name__ == "__main__":
    path = os.path.join(os.path.dirname(__file__), "words.txt")
    words = load_words(path)
    print(f"Loaded {len(words)} words. Example random word: {random.choice(words).upper()}")
