import secrets

NUM_WORDS = 4

def load_wordlist(path):
    words = []

    with open(path, "r") as f:
        for line in f:
            line = line.strip()      # remove newline + whitespace
            if not line:             # skip empty lines
                continue
            words.append(line)

    return words

def generate_password(words):
    selected = []

    for _ in range(NUM_WORDS):
        selected.append(secrets.choice(words))

    number = secrets.randbelow(1000)   # 0–999
    password = "-".join(selected) + f"-{number:03d}"

    return password

words = load_wordlist("words.txt")
pw = generate_password(words)
print(pw)
