from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/')
def home():
    html = open('index.html', encoding='utf-8').read()
    return Response(html, content_type='text/html; charset=utf-8')

@app.route('/api/generate')
def generate():
    prompt = request.args.get('prompt')
    if not prompt:
        return "Нет запроса", 400
    # Пример ответа (заменить на YandexGPT)
    return f"<p>Вы написали: {prompt}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
