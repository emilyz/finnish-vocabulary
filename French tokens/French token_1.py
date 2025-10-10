# Install tiktoken if not already installed
# pip install tiktoken

import tiktoken

# Load GPT-4/5 tokenizer
enc = tiktoken.get_encoding("o200k_base")

# French living room vocabulary (you can add more)
words = [
    "le salon",
    "le canapé",
    "le fauteuil",
    "la table basse",
    "le tapis",
    "le lampadaire",
    "la lampe",
    "la télévision",
    "la télécommande",
    "l’étagère",
    "la bibliothèque",
    "le tableau",
    "le rideau",
    "les rideaux",
    "la plante",
    "le coussin",
    "le plafond",
    "le mur",
    "la fenêtre",
    "la porte",
    "le feu de cheminée",
    "cuillère"  # added spoon as well
]

# Function to print tokens and IDs for each word
def show_tokens(word):
    token_ids = enc.encode(word, allowed_special=set())
    decoded = [enc.decode([t]) for t in token_ids]
    print(f"\nWord: {word}")
    for piece, tid in zip(decoded, token_ids):
        print(f"   '{piece}' -> {tid}")

# Run through list
for w in words:
    show_tokens(w)
for f in words:
    show_tokens (f)
    