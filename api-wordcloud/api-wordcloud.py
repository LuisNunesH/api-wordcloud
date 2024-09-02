from flask import Flask, jsonify
import random

app = Flask(__name__)

def generate_words():
    # Lista base de palavras únicas
    base_words = [f"word{i}" for i in range(20)]  # Exemplo de 20 palavras base
    
    # Criação do array final de palavras com possíveis repetições
    final_words = []

    for word in base_words:
        # Define um número aleatório de repetições (0 a 5)
        repetitions = random.randint(0, 5)
        # Adiciona a palavra o número de vezes definido ao array final
        final_words.extend([word] * repetitions)

    # Embaralha a lista final para criar aleatoriedade na ordem
    random.shuffle(final_words)

    # Limita a lista final a 50 palavras
    return final_words[:50]

@app.route('/words', methods=['GET'])
def get_words():
    words = generate_words()
    return jsonify(words)

if __name__ == '__main__':
    app.run(debug=True)
