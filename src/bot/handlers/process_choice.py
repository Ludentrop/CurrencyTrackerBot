from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command

from keyboards.make_choice import make_choice


router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(
        'Make your choice...',
        reply_markup=make_choice()
    )


@router.message(F.text.lower() == 'red pill')
async def red_pill(message: Message):
    await message.answer(
        'Right choice',
        reply_markup=ReplyKeyboardRemove()
    )


@router.message(F.text.lower() == 'blue pill')
async def blue_pill(message: Message):
    await message.answer(
        'Fuck off, bastard!',
        reply_markup=ReplyKeyboardRemove()
    )
