"""
Основное Flask пиложение для API учета товаров
"""
from http.cookiejar import debug

from flask import Flask, jsonify
from flask_cors import CORS
import os

#Создаем Flask приложение
app = Flask(__name__)

#ключаем CORS для работы с фронтендом
CORS(app)

#Основной маршрут
@app.route('/')
def home():
    """Главная страница"""
    return jsonify({
        'message': 'API системы учета товаров',
        'version': '1.0.0',
        'endpoints': {
            'GET /': 'Информация об API' ,
            'GET /health': 'Проверка состояния сервера'
        }
    })

#маршрут для проверки состояния

@app.route('/health')
def health_check():
    """Проверка работоспособности сервера"""
    return jsonify({'status':'ok'}) , 200

#Запуск приложения
if __name__ == '__main__':
    # Создаем папку для данных,если ее нет
    if not os.path.exists('api'):
        os.mkdir('api')
        print("Сщздана папка 'data'")

    print("="*40)
    print("Сервер зпущен")
    print("API доступен по адресу: http://localhost:5000")
    print("Фронтенд: frontend/index.html")
    print("="*40)

    #Запуск сервер
    app.run(debug=True, host='0.0.0.0', port=5000)


