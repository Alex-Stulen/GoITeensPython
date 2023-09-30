import random

from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = "6422112698:AAG8opOLOuAsuXkYidb91gfr--a0qTzheiU"
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

GAME_TABLE = [
    ["[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]"],
]

EMPTY_CELL_COUNT = 9
EMPTY_CELL = "[ ]"
X_MOVE = "[X]"
O_MOVE = "[O]"

PLAYER_USER = "User"
PLAYER_PC = "PC"
CURRENT_MOVE_PLAYER = PLAYER_USER


def set_player_user_move(row: int, col: int):
    global PLAYER_USER, GAME_TABLE, X_MOVE, EMPTY_CELL_COUNT
    if GAME_TABLE[row][col] == EMPTY_CELL:
        GAME_TABLE[row][col] = X_MOVE
        EMPTY_CELL_COUNT -= 1
        return True
    return False


def set_player_pc_move():
    global GAME_TABLE, O_MOVE, EMPTY_CELL, EMPTY_CELL_COUNT
    random_row = random.randint(0, 2)
    random_cell = random.randint(0, 2)
    current_cell = GAME_TABLE[random_row][random_cell]
    if current_cell == EMPTY_CELL:
        GAME_TABLE[random_row][random_cell] = O_MOVE
        EMPTY_CELL_COUNT -= 1
        return True
    else:
        while current_cell != EMPTY_CELL:
            if EMPTY_CELL_COUNT < 1:
                break
            random_row = random.randint(0, 2)
            random_cell = random.randint(0, 2)
            current_cell = GAME_TABLE[random_row][random_cell]
            if current_cell == EMPTY_CELL:
                GAME_TABLE[random_row][random_cell] = O_MOVE
                EMPTY_CELL_COUNT -= 1
                return True
    return False


def get_game_kb():
    markup = types.InlineKeyboardMarkup()

    for row_index, row in enumerate(GAME_TABLE):
        buttons = []
        for col_index, cell in enumerate(row):
            callback_data = f"{row_index}_{col_index}"
            btn = types.InlineKeyboardButton(text=cell, callback_data=callback_data)
            buttons.append(btn)
        markup.row(*buttons)

    return markup


def set_empty_game_table():
    global GAME_TABLE, EMPTY_CELL, EMPTY_CELL_COUNT
    for row_index, row in enumerate(GAME_TABLE):
        for col_index, _ in enumerate(row):
            GAME_TABLE[row_index][col_index] = EMPTY_CELL

    EMPTY_CELL_COUNT = 9


class GameState(StatesGroup):
    started = State()
    finished = State()


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer("Введіть команду /startgame щоб почати гру")


@dp.message_handler(commands=["startgame"], state=GameState.started)
async def startgame_command_fail(message: types.Message, state: FSMContext):
    await message.answer("Гра вже почалася")


@dp.message_handler(commands=["startgame"], state="*")
async def startgame_command(message: types.Message, state: FSMContext):
    await GameState.started.set()
    await message.answer(f"Хід: Гравця, {X_MOVE}\nПоле:", reply_markup=get_game_kb())


@dp.callback_query_handler(state=GameState.started)
async def process_game_move(callback: types.CallbackQuery, state: FSMContext):
    global CURRENT_MOVE_PLAYER, X_MOVE, O_MOVE, PLAYER_USER, PLAYER_PC, EMPTY_CELL_COUNT
    row_index, col_index = callback.data.split("_")
    row_index = int(row_index)
    col_index = int(col_index)

    if CURRENT_MOVE_PLAYER == PLAYER_USER:
        changed_cell = set_player_user_move(row=row_index, col=col_index)
        if changed_cell:
            set_player_pc_move()
    if EMPTY_CELL_COUNT < 1:
        await state.reset_state()
        await callback.message.edit_text("Дякуємо за гру, гру завершено. Нова гра: /startgame", reply_markup=get_game_kb())
        set_empty_game_table()
    else:
        await callback.message.edit_text(f"Хід: {CURRENT_MOVE_PLAYER} {X_MOVE}\nПоле:", reply_markup=get_game_kb())


if __name__ == "__main__":
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True
    )
