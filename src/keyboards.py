from aiogram.types import  InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
                     
reply_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="/add")],
        [KeyboardButton(text="/tasks")],
        [KeyboardButton(text="/done")]
    ],
    resize_keyboard=True
)

def tasks_btn_generator(tasks):
    keyboard = []
    for index, (task_id, task_text, is_done) in enumerate(tasks, start=1):
        status_symbol = "✅" if is_done else "⬜"
        button_text = f"{index}: {task_text} {status_symbol}"
        
        keyboard.append([
            InlineKeyboardButton(text=button_text, callback_data=f"toggle_{task_id}")
        ])
        
    return InlineKeyboardMarkup(inline_keyboard=keyboard)