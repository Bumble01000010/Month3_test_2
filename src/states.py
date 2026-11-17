from aiogram.fsm.state import State, StatesGroup

class AddTask(StatesGroup):
    waiting_for_task = State()

class DoneTask(StatesGroup):
    waiting_for_task_number = State()