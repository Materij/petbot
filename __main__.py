from aiogram import executor

from bot_deletion import PetDeletion
from bot_adding import BotAdding
from py_searching import SearchPet
from bot_editing import PetEditing
from pets_tests import TestE2EPet
from init_bot import init_bot


def startup():
    PetDeletion()
    BotAdding()
    SearchPet()
    PetEditing()
    TestE2EPet()


if __name__ == '__main__':
    executor.start_polling(init_bot.dp, on_startup=startup())
