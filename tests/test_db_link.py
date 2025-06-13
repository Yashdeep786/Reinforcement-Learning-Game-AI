from utils import signal_encoder
from database import db_handler

if __name__ == "__main__":
    # Add a new signal-meaning pair
    signal_encoder.update_vocab("🟨", "caution")

    # Load vocab from DB
    loaded_vocab = db_handler.load_vocab()

    print("Vocabulary from DB:")
    for signal, meaning in loaded_vocab.items():
        print(f"{signal}: {meaning}")
