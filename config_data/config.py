from dataclasses import dataclass

from environs import Env

@dataclass
class TgBot:
    token: str

@dataclass
class Config:
    tg_bot : TgBot

# функция считывания в Config информации из .env
def load_config(path: str | None = None):
    env = Env()
    env.read_env(path)

    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))