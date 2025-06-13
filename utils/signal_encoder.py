from database import db_handler  # ✅ Import added

vocab = {
    "🟥": "danger",
    "🟦": "safe",
    "🔺": "move up",
    "⬛": "stop"
}

reverse_vocab = {v: k for k, v in vocab.items()}

def encode(word):
    return reverse_vocab.get(word, "❓")

def decode(signal):
    return vocab.get(signal, "unknown")

def add_vocab(signal, word):
    vocab[signal] = word
    reverse_vocab[word] = signal

def get_vocab():
    return vocab

def update_vocab(signal, meaning):
    vocab[signal] = meaning
    reverse_vocab[meaning] = signal
    db_handler.save_vocab(vocab)  # ✅ Now works correctly
