from flask import Flask
import random
import threading
import time

app = Flask(__name__)

current_words = []

word_list = [
    "apple", "banana", "grape", "orange", "strawberry", "mango", "lemon", "pineapple", "peach",
    "cherry", "melon", "watermelon", "blueberry", "kiwi", "pear", "plum", "coconut", "fig", 
    "papaya", "raspberry"
]

def generate_words():
    final_words = []

    for _ in range(50):
        word = random.choice(word_list)
        repetitions = random.randint(1, 5)
        final_words.extend([word] * repetitions)

    random.shuffle(final_words)
    return final_words[:50]

def update_words():
    global current_words
    while True:
        current_words = generate_words()
        time.sleep(5)  # Atualiza as palavras a cada 5 segundos

@app.route('/words2', methods=['GET'])
def get_words2():
    formatted_words = ",\n".join(current_words)  # Usar current_words em vez de words_fixed
    return formatted_words, 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    current_words = generate_words()

    update_thread = threading.Thread(target=update_words)
    update_thread.daemon = True
    update_thread.start()

    app.run(debug=True)
