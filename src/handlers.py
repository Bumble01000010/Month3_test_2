from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

from db.user import create_user
from src.keyboards import reply_buttons, tasks_btn_generator
from src.states import AddTask
from db.tasks import create_task, create_task, get_all_tasks, toggle_task_status

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    user = create_user(
        telegram_id=message.from_user.id,
        username=message.from_user.username or "Аноним"
    )
    await message.answer(
        f"Здравствуйте {message.from_user.full_name}\nЯ бот который регистирует постваленные и выполненные задачи",
        reply_markup=reply_buttons
    )

@router.message(Command('add'))
async def add_new_task(message:Message, state:FSMContext):
    await state.set_state(AddTask.waiting_for_task)
    await message.answer("Введите новую задачу")


@router.message(AddTask.waiting_for_task)
async def process_task_title(message: Message, state: FSMContext):
    task = message.text
    create_task(task)
    await state.clear()
    await message.answer("Задание добвлено в список")

@router.message(Command("tasks"))
async def cmd_tasks(message: Message):
    tasks = get_all_tasks()
    
    if not tasks:
        await message.answer("Список задач пуст")
        return
        
    keyboard = tasks_btn_generator(tasks)
    await message.answer("Список задач:", reply_markup=keyboard)

@router.callback_query(F.data.startswith("toggle_"))
async def process_toggle_task(callback: CallbackQuery):
    task_id = int(callback.data.split("_")[1])
    
    toggle_task_status(task_id)

    tasks = get_all_tasks()
    updated_keyboard = tasks_btn_generator(tasks)
    
    await callback.message.edit_reply_markup(reply_markup=updated_keyboard)
