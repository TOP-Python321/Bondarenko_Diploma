
from dataclasses import dataclass
from environs import Env


# TODO: добавит класс базы данных

@dataclass
class TgBot:
    token: str
 #   admin_ids: list[int]

@dataclass
class Config:
    tg_bot: TgBot


# инициализация Config
def load_config(path: str | None = None) -> Config:
    env: Env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
#            admin_ids=list(map(env.list('ADMIN_IDS')))
        )
    )