from aiogram.types import ReplyKeyboardMarkup ,KeyboardButton


bosh_menu = ReplyKeyboardMarkup(
keyboard=[

    [
        KeyboardButton(text="14500 so'mlik pechenyalar"),
        KeyboardButton(text="19500 so'mlik pechenyalar"),

    ],
    [
        KeyboardButton(text="18700 so'mlik pechenyalar"),
        KeyboardButton(text="orqaga"),
    ],
],
   resize_keyboard=True

)



ikkinchi_menu = ReplyKeyboardMarkup(
keyboard=[

    [
        KeyboardButton(text="padushka"),
         KeyboardButton(text="orqaga"),
 
]
],

   resize_keyboard=True

)

uchinchi_menu = ReplyKeyboardMarkup(
keyboard=[

    [
     
        KeyboardButton(text="alonka"),
        KeyboardButton(text="orqaga")
 
]
],

   resize_keyboard=True

)
birinchi_menu = ReplyKeyboardMarkup(
keyboard=[

    [
        KeyboardButton(text="mini ko'rn"),
        KeyboardButton(text="mini yubileyniy"),

    ],
    [
        KeyboardButton(text="olma"),
        KeyboardButton(text="neskafe"),
    ],
        [
        KeyboardButton(text="abo"),
        KeyboardButton(text="davr"),
    ],
          [
        KeyboardButton(text="abo kvadrat"),
        KeyboardButton(text="medved"),
    ],
          [
        KeyboardButton(text="masha"),
        KeyboardButton(text="nejniy"),
    ],
           [
        KeyboardButton(text="makka joxori"),
        KeyboardButton(text="kapalak"),
    ],
           [
        KeyboardButton(text="oltin diyor"),
        KeyboardButton(text="toplonka"),
     
    ],
    [
            KeyboardButton(text="orqaga")
    ],
],

  resize_keyboard=True

)