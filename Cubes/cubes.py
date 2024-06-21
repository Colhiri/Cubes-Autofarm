import asyncio
import json
import logging
import random
from time import sleep
from requests import Session
from settings import URL_MINED, TOKEN_FILE, HEADERS

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s [%(name)s]    %(message)s")

class CubesClient(Session):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.headers = HEADERS.copy()

    ### Майнинг Куба выполняется от 1 до 6 секунд, в среднем конечно это 4
    async def play_game(self, token):
        result = self.post(URL_MINED, json={"token": token})
        if result.status_code == 200:
            data = json.loads(f'{result.text}')
            if len(data["mystery_ids"]) > 0:
                step_seconds = 10
            else:
                step_seconds = random.randint(3, 6)
            logging.info(result.text)
        else:
           step_seconds = random.randint(3, 6)
        await asyncio.sleep(step_seconds)


class ForgivingTaskGroup(asyncio.TaskGroup):
    _abort = lambda self: None

### Запуск майнера возможен без какого-то ни было запуска самого окна
### нужен только токен самого пользователя в игре
async def main():
    with open(TOKEN_FILE, 'r') as tok_file:
        auth_data = json.load(tok_file)
    async with ForgivingTaskGroup() as tg:
        for token_account in auth_data.values():
            tg.create_task(client.play_game(token_account))

if __name__ == '__main__':
    client = CubesClient()
    while True:
        asyncio.run(main())

