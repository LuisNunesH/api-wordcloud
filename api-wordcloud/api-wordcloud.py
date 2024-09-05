from flask import Flask
import random
import threading
import time

app = Flask(__name__)

current_words = []
words_fixed = []

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

def swap_frequencies():
    global words_fixed
    while True:
        melon_count = words_fixed.count("melon")
        watermelon_count = words_fixed.count("watermelon")

        new_words_fixed = [word for word in words_fixed if word not in ("melon", "watermelon")]
        new_words_fixed.extend(["melon"] * watermelon_count)
        new_words_fixed.extend(["watermelon"] * melon_count)

        words_fixed = new_words_fixed
        time.sleep(5)

def update_words():
    global current_words
    while True:
        current_words = generate_words()
        time.sleep(10)

@app.route('/words', methods=['GET'])
def get_words():
    formatted_words = ",\n".join(current_words)
    return formatted_words, 200, {'Content-Type': 'text/plain'}

@app.route('/words2', methods=['GET'])
def get_words2():
    formatted_words = ",\n".join(words_fixed)
    return formatted_words, 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    current_words = generate_words()
    words_fixed = generate_words()

    update_thread = threading.Thread(target=update_words)
    update_thread.daemon = True
    update_thread.start()

    swap_thread = threading.Thread(target=swap_frequencies)
    swap_thread.daemon = True
    swap_thread.start()

    app.run(debug=True)
