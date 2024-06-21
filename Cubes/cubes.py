import json
import logging
import random
from time import sleep
from requests import Session
from settings import URL_MINED, TOKEN_FILE, HEADERS

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s [%(name)s]    %(message)s")

class CubesClient(Session):
    banned_until_restore = False
    boxes_amount = 28
    drops_amount = 126
    energy = 999
    last_energy_update = "024-06-21T10:38:34.334Z"
    mined_count = 2540

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.headers = HEADERS.copy()

    def play_game(self):
        with open(TOKEN_FILE, 'r') as tok_file:
            self.auth_data = json.load(tok_file)

        result = self.post(URL_MINED, json={"token": self.auth_data.get("token")})

        sleep(random.randint(3, 6))  # Майнинг Куба выполняется от 1 до 6 секунд, в среднем конечно это 4

        if result.status_code == 200:
            logging.info(result.text)

### Запуск майнера возможен без какого-то ни было запуска самого окна
### нужен только токен самого пользователя в игре
client = CubesClient()
while True:
    client.play_game()
