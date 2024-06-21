# Cubes-Autofarm
Cubes? autofarm cubes

Отдельное спасибо этому человеку - https://github.com/TotalAwesome 
за то, что выложил код для фарма в BLUM.
Только благодаря нему, я понял, как можно обходить нудные тапалки, но и получать поинты/токены и тд.

Бот умеет:
Фармить кубы через POST-запрос.

В Telegram Desktop необходимо включить режим отладки WebView:

Settings -> Advanced -> Experimental settings -> Enable WebView inspecting

Как получить токен, чтобы вообще не заходить больше в игру и фармить пассивно без открытия Cubes?.
Переходим в бота https://t.me/cubesonthewater_bot
Нажимаем "Играть"
Нажимаем "Начать"
Майним 1 куб

На поверхности открывшегося приложения вызвать меню и выбрать Inspect element
ИЛИ
Нажимаем правой кнопкой и тащим в сторону после чего появляется меню выбираем "Проверить"
![image](https://github.com/Colhiri/Cubes-Autofarm/assets/118454025/ed1a776e-4ff1-4bca-a143-22a466744274)

В моем случае открывается DevTools
Далее переходим в "Сеть"
Нажимаем на фильтр, выбираем "Fetch/XHR"
Ищем в списке запросов "mined"
Нажимаем на него и выбираем вкладку "Полезные данные"
Копируем свой токен и вставляем его в "token.json"
Запускаем скрипт "cubes.py"
Схема:
![Для ГИТ Cubes](https://github.com/Colhiri/Cubes-Autofarm/assets/118454025/d1ac1c4e-26dc-4b5a-b3e9-2460a9d7b14c)

