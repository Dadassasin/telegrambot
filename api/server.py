from flask import Flask, request, jsonify

app = Flask(__name__)

# Хранилище для текста (в реальном проекте используйте базу данных)
messages = {}

@app.route('/api/webapp', methods=['POST'])
def handle_telegram_message():
    data = request.json
    chat_id = data['message']['chat']['id']
    text = data['message'].get('text', '')

    # Сохраняем текст сообщения в словарь
    messages[chat_id] = text

    # Отправляем ответ пользователю через Telegram API
    response_message = {
        "method": "sendMessage",
        "chat_id": chat_id,
        "text": f"Ваше сообщение: '{text}' сохранено."
    }

    return jsonify(response_message)

@app.route('/api/get-message/<int:chat_id>', methods=['GET'])
def get_message(chat_id):
    # Возвращаем сохраненное сообщение для конкретного chat_id
    text = messages.get(chat_id, 'Сообщений нет.')
    return jsonify({"message": text})

if __name__ == '__main__':
    app.run(debug=True)
