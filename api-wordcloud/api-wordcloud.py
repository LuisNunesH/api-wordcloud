from flask import Flask, jsonify
import random
import threading
import time

app = Flask(__name__)

current_words = []

def generate_words():
    base_words = [f"word{i}" for i in range(20)]
    final_words = []

    for word in base_words:
        repetitions = random.randint(0, 5)
        final_words.extend([word] * repetitions)

    random.shuffle(final_words)
    return final_words[:50]

def update_words():
    """Atualiza o array de palavras a cada 10 segundos."""
    global current_words
    while True:
        current_words = generate_words()
        time.sleep(10)

@app.route('/words', methods=['GET'])
def get_words():
    return jsonify(current_words)

if __name__ == '__main__':
    current_words = generate_words()

    update_thread = threading.Thread(target=update_words)
    update_thread.daemon = True
    update_thread.start()

    app.run(debug=True)