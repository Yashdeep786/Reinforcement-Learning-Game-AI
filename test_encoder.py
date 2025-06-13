from utils import signal_encoder
from database import db_handler

# 1. Test encode-decode loop
print("Test 1: Encode → Decode loop")
word = "danger"
signal = signal_encoder.encode(word)
decoded_word = signal_encoder.decode(signal)
print(f"Word: {word} → Signal: {signal} → Decoded: {decoded_word}")
print("✅ Passed" if word == decoded_word else "❌ Failed")

# 2. Add new vocab and update DB
print("\nTest 2: Add new vocab and save to DB")
new_signal = "🟨"
new_word = "caution"
signal_encoder.add_vocab(new_signal, new_word)
signal_encoder.update_vocab(new_signal, new_word)
print(f"Added: {new_signal} : {new_word}")
print("Vocab:", signal_encoder.get_vocab())

# 3. Decode unknown signal
print("\nTest 3: Decode unknown signal")
unknown_signal = "💀"
meaning = signal_encoder.decode(unknown_signal)
print(f"Signal: {unknown_signal} → Meaning: {meaning}")
print("✅ Passed" if meaning == "unknown" else "❌ Failed")
