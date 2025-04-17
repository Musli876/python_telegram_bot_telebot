import telebot
from telebot import types
from datetime import datetime
import time

TOKEN = "7798738903:AAF6bcDXIWVYlnmTPbb8mI8o4x7GESy8hqw"
bot = telebot.TeleBot(TOKEN)

user_carts = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    phone_button = types.KeyboardButton("📱 Отправить номер телефона", request_contact=True)
    markup.add(phone_button)
    
    welcome_text = """
PICS | Доставка bridge, добро пожаловать!

Отправьте ваш номер телефона,
или наберите в формате +9980X 500000X.

https://evos.ur/uz/about/
    """
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    if message.contact is not None:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(
            types.KeyboardButton("🍴 Меню"),
            types.KeyboardButton("📋 Мои заказы"),
            types.KeyboardButton("📥 Корзина"),
            types.KeyboardButton("📞 Контакты"),
            types.KeyboardButton("⚙️ Настройки"),
            types.KeyboardButton("📨 Отправить сообщение")
        )
        
        response_text = """
Номер телефона принят✅
🛒 Главное меню
Можете оформить заказ!
        """
        
        bot.send_message(message.chat.id, response_text, reply_markup=markup, parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, "Пожалуйста, отправьте ваш номер телефона")

@bot.message_handler(func=lambda message: True)
def handle_main_menu(message):
    current_time = datetime.now().strftime("%H:%M")
    
    if message.text == "🍴 Меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(
            types.KeyboardButton("Лаваш (9)"),
            types.KeyboardButton("Бургер (4)"),
            types.KeyboardButton("Сеты (8)"),
            types.KeyboardButton("Напитки (11)"),
            types.KeyboardButton("Шаурма (4)"),
            types.KeyboardButton("Хот-дог (8)"),
            types.KeyboardButton("⬅️ Назад")
        )
        bot.send_message(message.chat.id, "Выберите:", reply_markup=markup)
        
    elif message.text == "Лаваш (9)":
        photo_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQcU6c_CZCTpXJM2xVs2r-j4vN-VPLclIuOkg&s"  
        bot.send_photo(message.chat.id, photo_url, caption="Меню лаваша:")
        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(
            types.KeyboardButton("Лаваш с говядиной и перцем"),
            types.KeyboardButton("Лаваш с курицей и перцем"),
            types.KeyboardButton("Лаваш с говядиной и сыром Стандарт"),
            types.KeyboardButton("Лаваш с сыром и курицей Стандарт"),
            types.KeyboardButton("Лаваш с курицей"),
            types.KeyboardButton("Лаваш с говядиной"),
            types.KeyboardButton("Мини лаваш с говядиной"),
            types.KeyboardButton("Мини лаваш с курицей"),
            types.KeyboardButton("Лаваш с сыром Комбо"),
            types.KeyboardButton("⬅️ Назад")
        )
        bot.send_message(message.chat.id, "Пожалуйста, выберите:", reply_markup=markup)
        
    elif message.text == "Бургер (4)":
        photo_url = "https://telegra.ph/file/edfd4bca6677d4df24b33.jpg"
        try:
            bot.send_photo(message.chat.id, photo_url, caption="Меню бургеров:")
        except:
            bot.send_message(message.chat.id, "Меню бургеров:")
        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(
            types.KeyboardButton("Гамбургер"),
            types.KeyboardButton("Чизбургер"),
            types.KeyboardButton("Двойной бургер"),
            types.KeyboardButton("Двойной чизбургер"),
            types.KeyboardButton("⬅️ Назад")
        )
        bot.send_message(message.chat.id, "Пожалуйста, выберите:", reply_markup=markup)
        
    elif message.text == "Сеты (8)":
        photo_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFxLdCUHiklfqwr_y9nbHE_lJUhWvxdEzY3w&s" 
        try:
            bot.send_photo(message.chat.id, photo_url, caption="Меню сетов:")
        except:
            bot.send_message(message.chat.id, "Меню сетов:")
        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(
            types.KeyboardButton("Лаваш + Coca-Cola"),
            types.KeyboardButton("Бургер + Fanta"),
            types.KeyboardButton("Лаваш + Бургер + Pepsi"),
            types.KeyboardButton("Детский сет"),
            types.KeyboardButton("Семейный сет"),
            types.KeyboardButton("Двойной лаваш сет"),
            types.KeyboardButton("Бургер Комбо"),
            types.KeyboardButton("Лаваш Комбо"),
            types.KeyboardButton("⬅️ Назад")
        )
        bot.send_message(message.chat.id, "Пожалуйста, выберите:", reply_markup=markup)
        
    elif message.text == "Напитки (11)":
        photo_url = "https://avatars.mds.yandex.net/i?id=a5309da55efcb06225483fa5e54857e5_l-5282542-images-thumbs&n=13"
        try:
            bot.send_photo(message.chat.id, photo_url, caption="Меню напитков:")
        except:
            bot.send_message(message.chat.id, "Меню напитков:")
        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(
            types.KeyboardButton("Coca-Cola 0.5L"),
            types.KeyboardButton("Coca-Cola 1L"),
            types.KeyboardButton("Fanta 0.5L"),
            types.KeyboardButton("Fanta 1L"),
            types.KeyboardButton("Pepsi 0.5L"),
            types.KeyboardButton("Pepsi 1L"),
            types.KeyboardButton("Вода 0.5L"),
            types.KeyboardButton("Сок апельсиновый"),
            types.KeyboardButton("Сок яблочный"),
            types.KeyboardButton("Чай черный"),
            types.KeyboardButton("Чай зеленый"),
            types.KeyboardButton("⬅️ Назад")
        )
        bot.send_message(message.chat.id, "Пожалуйста, выберите:", reply_markup=markup)
        
    elif message.text == "Шаурма (4)":
        photo_url = "https://avatars.mds.yandex.net/i?id=39a644ac20799137c9110047f7bfad2c_l-4340501-images-thumbs&n=13"
        try:
            bot.send_photo(message.chat.id, photo_url, caption="Меню шаурмы:")
        except:
            bot.send_message(message.chat.id, "Меню шаурмы:")
        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(
            types.KeyboardButton("Шаурма с говядиной"),
            types.KeyboardButton("Шаурма с курицей"),
            types.KeyboardButton("Шаурма с сыром и говядиной"),
            types.KeyboardButton("Шаурма с сыром и курицей"),
            types.KeyboardButton("⬅️ Назад")
        )
        bot.send_message(message.chat.id, "Пожалуйста, выберите:", reply_markup=markup)
        
    elif message.text == "Хот-дог (8)":
        photo_url = "https://avatars.mds.yandex.net/i?id=2e0018ede5819b1bbd487e10bd42e3be_l-2352943-images-thumbs&n=13"
        try:
            bot.send_photo(message.chat.id, photo_url, caption="Меню хот-догов:")
        except:
            bot.send_message(message.chat.id, "Меню хот-догов:")
        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(
            types.KeyboardButton("Классический хот-дог"),
            types.KeyboardButton("Хот-дог с сыром"),
            types.KeyboardButton("Двойной хот-дог"),
            types.KeyboardButton("Острый хот-дог"),
            types.KeyboardButton("Хот-дог с курицей"),
            types.KeyboardButton("Мини хот-дог"),
            types.KeyboardButton("Хот-дог Комбо"),
            types.KeyboardButton("Хот-дог Экстра"),
            types.KeyboardButton("⬅️ Назад")
        )
        bot.send_message(message.chat.id, "Пожалуйста, выберите:", reply_markup=markup)
        
    elif message.text in ["Лаваш с говядиной и перцем", 
                         "Лаваш с курицей и перцем",
                         "Лаваш с говядиной и сыром Стандарт",
                         "Лаваш с сыром и курицей Стандарт",
                         "Лаваш с курицей",
                         "Лаваш с говядиной",
                         "Мини лаваш с говядиной",
                         "Мини лаваш с курицей",
                         "Лаваш с сыром Комбо"]:
        prices = {
            "Лаваш с говядиной и перцем": "50 000 сум",
            "Лаваш с курицей и перцем": "45 000 сум",
            "Лаваш с говядиной и сыром Стандарт": "55 000 сум",
            "Лаваш с сыром и курицей Стандарт": "50 000 сум",
            "Лаваш с курицей": "40 000 сум",
            "Лаваш с говядиной": "45 000 сум",
            "Мини лаваш с говядиной": "35 000 сум",
            "Мини лаваш с курицей": "30 000 сум",
            "Лаваш с сыром Комбо": "60 000 сум"
        }
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Добавить в корзину", callback_data=f"add_to_cart_{message.text}"))
        bot.send_message(message.chat.id, f"Вы выбрали: {message.text}\nЦена: {prices.get(message.text, '50 000 сум')}", reply_markup=markup)
        
    elif message.text in ["Гамбургер", "Чизбургер", "Двойной бургер", "Двойной чизбургер"]:
        prices = {
            "Гамбургер": "35 000 сум",
            "Чизбургер": "40 000 сум",
            "Двойной бургер": "55 000 сум",
            "Двойной чизбургер": "60 000 сум"
        }
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Добавить в корзину", callback_data=f"add_to_cart_{message.text}"))
        bot.send_message(message.chat.id, f"Вы выбрали: {message.text}\nЦена: {prices.get(message.text, '')}", reply_markup=markup)
        
    elif message.text in ["Лаваш + Coca-Cola", 
                         "Бургер + Fanta",
                         "Лаваш + Бургер + Pepsi",
                         "Детский сет",
                         "Семейный сет",
                         "Двойной лаваш сет",
                         "Бургер Комбо",
                         "Лаваш Комбо"]:
        prices = {
            "Лаваш + Coca-Cola": "60 000 сум",
            "Бургер + Fanta": "55 000 сум",
            "Лаваш + Бургер + Pepsi": "85 000 сум",
            "Детский сет": "45 000 сум",
            "Семейный сет": "120 000 сум",
            "Двойной лаваш сет": "90 000 сум",
            "Бургер Комбо": "65 000 сум",
            "Лаваш Комбо": "70 000 сум"
        }
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Добавить в корзину", callback_data=f"add_to_cart_{message.text}"))
        bot.send_message(message.chat.id, f"Вы выбрали: {message.text}\nЦена: {prices.get(message.text, '')}", reply_markup=markup)
        
    elif message.text in ["Coca-Cola 0.5L", 
                         "Coca-Cola 1L",
                         "Fanta 0.5L",
                         "Fanta 1L",
                         "Pepsi 0.5L",
                         "Pepsi 1L",
                         "Вода 0.5L",
                         "Сок апельсиновый",
                         "Сок яблочный",
                         "Чай черный",
                         "Чай зеленый"]:
        prices = {
            "Coca-Cola 0.5L": "10 000 сум",
            "Coca-Cola 1L": "15 000 сум",
            "Fanta 0.5L": "10 000 сум",
            "Fanta 1L": "15 000 сум",
            "Pepsi 0.5L": "10 000 сум",
            "Pepsi 1L": "15 000 сум",
            "Вода 0.5L": "5 000 сум",
            "Сок апельсиновый": "12 000 сум",
            "Сок яблочный": "12 000 сум",
            "Чай черный": "8 000 сум",
            "Чай зеленый": "8 000 сум"
        }
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Добавить в корзину", callback_data=f"add_to_cart_{message.text}"))
        bot.send_message(message.chat.id, f"Вы выбрали: {message.text}\nЦена: {prices.get(message.text, '')}", reply_markup=markup)
        
    elif message.text in ["Шаурма с говядиной", 
                         "Шаурма с курицей",
                         "Шаурма с сыром и говядиной",
                         "Шаурма с сыром и курицей"]:
        prices = {
            "Шаурма с говядиной": "30 000 сум",
            "Шаурма с курицей": "28 000 сум",
            "Шаурма с сыром и говядиной": "35 000 сум",
            "Шаурма с сыром и курицей": "33 000 сум"
        }
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Добавить в корзину", callback_data=f"add_to_cart_{message.text}"))
        bot.send_message(message.chat.id, f"Вы выбрали: {message.text}\nЦена: {prices.get(message.text, '')}", reply_markup=markup)
        
    elif message.text in ["Классический хот-дог", 
                         "Хот-дог с сыром",
                         "Двойной хот-дог",
                         "Острый хот-дог",
                         "Хот-дог с курицей",
                         "Мини хот-дог",
                         "Хот-дог Комбо",
                         "Хот-дог Экстра"]:
        prices = {
            "Классический хот-дог": "20 000 сум",
            "Хот-дог с сыром": "25 000 сум",
            "Двойной хот-дог": "30 000 сум",
            "Острый хот-дог": "22 000 сум",
            "Хот-дог с курицей": "18 000 сум",
            "Мини хот-дог": "15 000 сум",
            "Хот-дог Комбо": "35 000 сум",
            "Хот-дог Экстра": "28 000 сум"
        }
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Добавить в корзину", callback_data=f"add_to_cart_{message.text}"))
        bot.send_message(message.chat.id, f"Вы выбрали: {message.text}\nЦена: {prices.get(message.text, '')}", reply_markup=markup)
        
    elif message.text == "📋 Мои заказы":
        bot.send_message(message.chat.id, "⛔️ Заказов нет!")
    elif message.text == "📥 Корзина":
        chat_id = message.chat.id
        if chat_id in user_carts and user_carts[chat_id]:
            cart_items = user_carts[chat_id]
            cart_message = "🛒 Ваша корзина:\n\n"
            total_price = 0
            
            prices = {
                "Лаваш с говядиной и перцем": 50000, "Лаваш с курицей и перцем": 45000,
                "Лаваш с говядиной и сыром Стандарт": 55000, "Лаваш с сыром и курицей Стандарт": 50000,
                "Лаваш с курицей": 40000, "Лаваш с говядиной": 45000,
                "Мини лаваш с говядиной": 35000, "Мини лаваш с курицей": 30000,
                "Лаваш с сыром Комбо": 60000, "Гамбургер": 35000, "Чизбургер": 40000,
                "Двойной бургер": 55000, "Двойной чизбургер": 60000,
                "Лаваш + Coca-Cola": 60000, "Бургер + Fanta": 55000,
                "Лаваш + Бургер + Pepsi": 85000, "Детский сет": 45000,
                "Семейный сет": 120000, "Двойной лаваш сет": 90000,
                "Бургер Комбо": 65000, "Лаваш Комбо": 70000,
                "Coca-Cola 0.5L": 10000, "Coca-Cola 1L": 15000,
                "Fanta 0.5L": 10000, "Fanta 1L": 15000,
                "Pepsi 0.5L": 10000, "Pepsi 1L": 15000,
                "Вода 0.5L": 5000, "Сок апельсиновый": 12000,
                "Сок яблочный": 12000, "Чай черный": 8000,
                "Чай зеленый": 8000, "Шаурма с говядиной": 30000,
                "Шаурма с курицей": 28000, "Шаурма с сыром и говядиной": 35000,
                "Шаурма с сыром и курицей": 33000, "Классический хот-дог": 20000,
                "Хот-дог с сыром": 25000, "Двойной хот-дог": 30000,
                "Острый хот-дог": 22000, "Хот-дог с курицей": 18000,
                "Мини хот-дог": 15000, "Хот-дог Комбо": 35000,
                "Хот-дог Экстра": 28000
            }
            
            for item in cart_items:
                price = prices.get(item, 0)
                cart_message += f"{item} - {price:,} сум\n"
                total_price += price
            
            cart_message += f"\nИтого: {total_price:,} сум"
            
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Оформить заказ", callback_data="place_order"))
            markup.add(types.InlineKeyboardButton("Очистить корзину", callback_data="clear_cart"))
            
            bot.send_message(chat_id, cart_message, reply_markup=markup)
        else:
            bot.send_message(chat_id, "🛒 Ваша корзина пуста 🗑")
            
    elif message.text == "📞 Контакты":
        contact_info = """
<b>Контакты</b>
<u>Колл-центр</u>

+998 71-203-12-12
+998 71-203-55-55

<b>Телефоны доставки:</b>

<b>Ташкент</b>
+998 71-203-12-12

<b>Наманган</b>
+998 78-147-12-12

<b>Фергана</b>
+998 73-249-12-12

<b>Коканд</b>
+998 73-542-78-78

<b>Андижан</b>
+998 74-224-12-12

<b>Самарканд</b>
+998 78-129-16-16

<b>Карши</b>
+998 78-129-17-17
        """
        photo_url = "https://f.invest.gov.tr/en/Sectors/PublishingImages/pages/business-services/Business-Services.jpg"  
        bot.send_photo(message.chat.id, photo_url, caption=contact_info, parse_mode="HTML")
        
    elif message.text == "⚙️ Настройки":
        bot.send_message(message.chat.id, "📋 | Добро пожаловать в раздел настроек!")
    elif message.text == "📨 Отправить сообщение":
        bot.send_message(message.chat.id, "📩 Сообщение отправлено")
    elif message.text == "⬅️ Назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(
            types.KeyboardButton("🍴 Меню"),
            types.KeyboardButton("📋 Мои заказы"),
            types.KeyboardButton("📥 Корзина"),
            types.KeyboardButton("📞 Контакты"),
            types.KeyboardButton("⚙️ Настройки"),
            types.KeyboardButton("📨 Отправить сообщение")
        )
        bot.send_message(message.chat.id, "Главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Неверная команда! Пожалуйста, используйте меню")

@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    chat_id = call.message.chat.id
    
    if call.data.startswith("add_to_cart_"):
        item = call.data.replace("add_to_cart_", "")
        
        if chat_id not in user_carts:
            user_carts[chat_id] = []
        
        user_carts[chat_id].append(item)
        
        bot.answer_callback_query(call.id)
        bot.send_message(chat_id, f"✅ {item} добавлен в корзину!")
        
    elif call.data == "place_order":
        if chat_id in user_carts and user_carts[chat_id]:
            bot.answer_callback_query(call.id)
            bot.send_message(chat_id, "📦 Ваш заказ принят!")
            time.sleep(3)
            bot.send_message(chat_id, "🚚 Ваш заказ в пути!")
            user_carts[chat_id] = []  
        else:
            bot.answer_callback_query(call.id)
            bot.send_message(chat_id, "🛒 Ваша корзина пуста!")
            
    elif call.data == "clear_cart":
        if chat_id in user_carts:
            user_carts[chat_id] = []
        bot.answer_callback_query(call.id)
        bot.send_message(chat_id, "🛒 Корзина очищена!")

bot.polling()