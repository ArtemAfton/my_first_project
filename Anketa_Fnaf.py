import telebot
from telebot import types
from data import load_user_data, save_user_data

token = "Your Token"

bot = telebot.TeleBot(token)



data_path = "user_data.json"
user_data = load_user_data(data_path)



def first(message):
    if(message.text == "Да❗❗❗"):
        return "Да❗❗❗" in message.text

def first2(message):
    if(message.text == "Нет 😢"):
        return "Нет 😢" in message.text

def second(message):
    if(message.text == "Человекоподобных"):
       return "Человекоподобных" in message.text

def second2(message):
    if(message.text == "Животных"):
        return "Животных" in message.text

def height1(message):
    if(message.text == "С щёчками"):
        return "С щёчками" in message.text

def height2(message):
    if(message.text == "Без щёчек"):
        return "Без щёчек" in message.text

def material1(message):
    if(message.text == "Пластиковые"):
        return "Пластиковые" in message.text

def material2(message):
    if(message.text == "Плюшевые"):
        return "Плюшевые" in message.text

def material3(message):
    if(message.text == "Металлические"):
        return "Металлические" in message.text

def pol(message):
    if(message.text == "С Щёчками"):
        return "С Щёчками" in message.text

def type1(message):
    if(message.text == "Женский"):
        return "Женский" in message.text

def type2(message):
    if(message.text == "Неопределённый"):
        return "Неопределённый" in message.text

def sing_and_ice_cream(message):
    if(message.text == "Петь и раздавать мороженное"):
        return "Петь и раздавать мороженное" in message.text

def dance(message):
    if(message.text == "Танцевать как балерина"):
        return "Танцевать как балерина" in message.text

def min(message):
    if(message.text == "женский"):
        return "женский" in message.text

def bid(message):
    if(message.text == "мужской"):
        return "мужской" in message.text

def toy(message):
    if(message.text == "Той"):
        return "Той" in message.text

def toy_bonnie(message):
    if(message.text == "Играть на рок-гитаре"):
        return "Играть на рок-гитаре" in message.text

def toy_chica(message):
    if(message.text == "Обожать пиццу и иметь кекс"):
        return "Обожать пиццу и иметь кекс" in message.text

def toy_freddy(message):
    if(message.text == "Петь"):
        return "Петь" in message.text

def mangle(message):
    if(message.text == "Уметь лазать по стенам"):
        return "Уметь лазать по стенам" in message.text

def puppet(message):
    if(message.text == "Жить в музыкальной шкатулке"):
        return "Жить в музыкальной шкатулке" in message.text

def rockstar(message):
    if(message.text == "Рокстар"):
        return "Рокстар" in message.text

def rockstar_freddy(message):
    if(message.text == "петь"):
        return "петь" in message.text

def rockstar_bonnie(message):
    if(message.text == "играть на рок-гитаре"):
        return "играть на рок-гитаре" in message.text

def rockstar_chica(message):
    if(message.text == "Играть на маракасах"):
        return "Играть на маракасах" in message.text

def pigpath(message):
    if(message.text == "Играть на банджо"):
        return "Играть на банджо" in message.text

def security_puppet(message):
    if(message.text == "Охранять"):
        return "Охранять" in message.text

def without_cheeks(message):
    if(message.text == "Без Щёчек"):
        return "Без Щёчек" in message.text

def tell_stories(message):
    if(message.text == "Рассказывать истории"):
        return "Рассказывать истории" in message.text

def sing_frog(message):
    if(message.text == "ПЕТЬ"):
        return "ПЕТЬ" in message.text

def jokes(message):
    if(message.text == "Шутить"):
        return "Шутить" in message.text

def magic(message):
    if(message.text == "Показывать магию"):
        return "Показывать магию" in message.text

def accordion(message):
    if(message.text == "Играть на аккордионе"):
        return "Играть на аккордионе" in message.text

def old(message):
    if(message.text == "Олд"):
        return "Олд" in message.text

def classic(message):
    if(message.text == "Классические"):
        return "Классические" in message.text

def old_freddy(message):
    if(message.text == "Петь на сцене"):
        return "Петь на сцене" in message.text

def old_bonnie(message):
    if(message.text == "ИГРАТЬ НА РОК-ГИТАРЕ"):
        return "ИГРАТЬ НА РОК-ГИТАРЕ" in message.text

def old_chica(message):
    if(message.text == "ИМЕТЬ КЕКС"):
        return "ИМЕТЬ КЕКС" in message.text

def old_foxy(message):
    if(message.text == "БЫТЬ ПИРАТОМ"):
        return "БЫТЬ ПИРАТОМ" in message.text

def classic_animatronics(message):
    if(message.text == "Классические"):
        return "Классические" in message.text

def classic_freddy(message):
    if(message.text == "Петь на Сцене"):
        return "Петь на Сцене" in message.text

def classic_bonnie(message):
    if(message.text == "Играть на Рок-гитаре"):
        return "Играть на Рок-гитаре" in message.text

def classic_chica(message):
    if(message.text == "Иметь Кекс"):
        return "Иметь Кекс" in message.text

def classic_foxy(message):
    if(message.text == "Быть Пиратом"):
        return "Быть Пиратом" in message.text

def metal_male(message):
    if(message.text == "Мужской"):
        return "Мужской" in message.text

def metal_female(message):
    if(message.text == "ЖЕНСКИЙ"):
        return "ЖЕНСКИЙ" in message.text

def metal_unknown(message):
    if(message.text == "неопределённый"):
        return "неопределённый" in message.text

#@bot.message_handler(commands=["start"])
#def start(message):
   # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
   # btn1 = types.KeyboardButton("Да!!!!")
    #btn2 = types.KeyboardButton("Нет :(")
    #markup.add(btn1, btn2)
    #bot.send_message(message.from_user.id, "Добро пожаловать в анкету 'Какой ты персонаж из фнаф'! Тебе "
                                          # "предстоит ответить на пять моих вопросов, чтобы узнать результат :). "
                                          # "Но для начала тебе нужно пройти коротенькую"
                                          # "регистрацию.", reply_markup=markup)


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Да❗❗❗")
    btn2 = types.KeyboardButton("Нет 😢")
    markup.add(btn1, btn2)
    global user_data
    user_data[message.chat.id] = {"name": message.from_user.full_name,
                                  "progress": ""}
    save_user_data(user_data, data_path)

    photo1_1 = open("Fazbear_Ent.jpg", "rb")

    bot.send_photo(message.chat.id, photo1_1, f"Поздравляю {user_data[message.chat.id]['name']}! Вы только что были "
                   "зарегистрированы в анкете 'Какой ты персонаж из вселенной FNaF'! Вам предстоит ответить на несколько моих вопросов "
                   "чтобы узнать правду :)\n Итак, вы готовы?\n P.S. Компания Fazbear Ent. не несёт ответственность "
                   "за приченённый моральный ущерб, а также за взломку аккаунта, украденные данные и много-много "
                   "чего ещё.", reply_markup=markup)


@bot.message_handler(commands=["help"])
def help(message):
    photo1_0 = open("You_cant_prove.jpg", "rb")
    bot.send_photo(message.from_user.id, photo1_0, "/start - рестарт\n"
                                           "/help - помощь\n"
                                           "Fazbear Ent. не несёт ответственность за ущерб имуществу или человеку.")


@bot.message_handler(commands=["progress"])
def progression(message):
    bot.send_message(message.chat.id, user_data[message.chat.id]['progress'])


# Человекоподобные или животные
@bot.message_handler(content_types=["text"], func=first)
def question(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    cl1 = types.KeyboardButton("Человекоподобных")
    cl2 = types.KeyboardButton("Животных")
    markup.add(cl1, cl2)
    bot.send_message(message.from_user.id, "Отлично! Первый вопрос:\n"
                                            "Каких аниматроников вы больше предпочитаете:"
                                            "человекоподобных или животных?", reply_markup=markup)
    #user_data[message.chat.id]['question'] = "Первый вопрос:\n Каких аниматроников ты больше предпочитаешь: человекоподобных или животных?"
    #save_user_data(user_data, data_path)


@bot.message_handler(content_types=["text"], func=first2)
def answer(message):
    bot.send_message(message.from_user.id, "Ничего, видимо это тематика просто не для вас 💁‍♂️\n"
                                           "Но если вы захотите вернуться, жмякайте /start \n"
                                           "Но имейте ввиду, вы зря нажали эту кнопку, советуем вам вернуться и пройти "
                                           "анкету в течении 24 часов, а иначе один из наших аниматроников может нагрянуть"
                                           " к вам в гости :)", reply_markup=types.ReplyKeyboardRemove())

#Человекоподобные: с щёчками или без
@bot.message_handler(content_types=["text"], func=second)
def people_animatronics(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1 = types.KeyboardButton("С щёчками")
    bt2 = types.KeyboardButton("Без щёчек")
    markup.add(bt1, bt2)
    bot.send_message(message.from_user.id, "Второй вопрос:\n"
                                           "Вам нравятся аниматроники с щёчками или без?", reply_markup=markup)

#Животные: пластиковые, плюшевые или металлические
@bot.message_handler(content_types=["text"], func= second2)
def animals_animatronics(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    cn1 = types.KeyboardButton("Пластиковые")
    cn2 = types.KeyboardButton("Плюшевые")
    cn3 = types.KeyboardButton("Металлические")
    markup.add(cn1, cn2, cn3)
    bot.send_message(message.from_user.id, "Второй вопрос:\n"
                                           "Вам нравятся пластиковые, плюшевые или металлические?", reply_markup=markup)

#Человекоподобные: с щёчками: женский или неопределённый пол (Бэйби/Баллора ил Эннард)
@bot.message_handler(content_types=["text"], func=height1)
def gender1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kn1 = types.KeyboardButton("Женский")
    kn2 = types.KeyboardButton("Неопределённый")
    markup.add(kn1, kn2)
    bot.send_message(message.from_user.id, "Третий вопрос:\n "
                                           "Какой пол аниматроников вам больше нравится? ", reply_markup=markup)

#Человекоподобные: без щёчек: мужской (Бидибаб) или женский (Минирина)
@bot.message_handler(content_types=["text"], func=height2)
def gender(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kn1 = types.KeyboardButton("женский")
    kn2 = types.KeyboardButton("мужской")
    markup.add(kn1, kn2)
    bot.send_message(message.from_user.id, "Третий вопрос:\n "
                                           "Какой пол аниматроников вам больше нравится? ", reply_markup=markup)

#Животные: пластиковые: С щёчками или без(Оливер, Мр Хиппо, Хэппи Фрог, Рокстар Фокси)
@bot.message_handler(content_types=["text"], func= material1)
def plastic(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    cp1 = types.KeyboardButton("С Щёчками")
    cp2 = types.KeyboardButton("Без Щёчек")
    markup.add(cp1, cp2)
    bot.send_message(message.from_user.id, "Третий вопрос:\n "
                                           "Вам нравятся аниматроники с щёчками или без? ", reply_markup=markup)

#Животные: плюшевые: Олд или Классик
@bot.message_handler(content_types=["text"], func=material2)
def plush(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kp1 = types.KeyboardButton("Олд")
    kp2 = types.KeyboardButton("Классические")
    markup.add(kp1, kp2)
    bot.send_message(message.from_user.id, "Третий вопрос:\n "
                                           "Вам нравятся Олд или Классические аниматроники? ", reply_markup=markup)

#Животные: металлические: мужской, женский или неопределённый
@bot.message_handler(content_types=["text"], func=material3)
def metal(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Мужской")
    button2 = types.KeyboardButton("ЖЕНСКИЙ")
    button3 = types.KeyboardButton("неопределённый")
    markup.add(button1, button2, button3)
    bot.send_message(message.from_user.id, "Третий вопрос:\n "
                                           "Какой пол аниматроников вам нравится? ", reply_markup=markup)

#Животные: пластиковые: той или рокстар
@bot.message_handler(content_types=["text"], func=pol)
def plastic(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Той")
    but2 = types.KeyboardButton("Рокстар")
    markup.add(but1, but2)
    bot.send_message(message.from_user.id, "Четвёртый вопрос:\n "
                                           "Вам нравятся Той или Рокстар аниматроники? ", reply_markup=markup)

#Человекоподобные: с щёчками: женский или неопределённый пол (Бэйби/Баллора ил Эннард): Петь и раздавать мороженное или танцевать
@bot.message_handler(content_types=["text"], func=type1)
def ty_pe(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1 = types.KeyboardButton("Петь и раздавать мороженное")
    bt2 = types.KeyboardButton("Танцевать как балерина")
    markup.add(bt1, bt2)
    bot.send_message(message.from_user.id, "Четвёртый вопрос:\n "
                                           "Вам нравится петь и раздавать мороженное или танцевать как балерина? "
                     , reply_markup=markup)
#Еннард
@bot.message_handler(content_types=["text"], func=type2)
def ty_pe2(message):
    photo = open("Ennard.jpg", "rb")
    bot.send_photo(message.chat.id, photo, "Внимание! Вы ответили на все вопросы. Идёт анализ приведённых вами ответов...\n "
                                           "1% ... 45% ... 61% ... 88% ... 91% ... 99.9999999999999999999999999999999999"
                                           "99999E999999999999R9999999999999999R999999999999999999999O9999999%%R%%%\?//\.,...\n "
                                           "Итак, из ваших ответов следует, что вы похожи на аниматроника 'Эннард'! Мои "
                                           "поздравления! Это означает что вы не любите одиночество, а больше предпочитаете "
                                           "сплочённость с коллективом, но только не всегда ваши приоритеты совпадают с "
                                           "приоритетами коллектива, и это может привести к тому, что коллектив выкенет вас "
                                           "за борт... Что ж, вот вы и прошли анкету 'Какой ты персонаж из вселенной FNaF' "
                                           "и узнали, что вы похожи на Эннарда! Надеюсь, он придёт к вам, ведь теперь он "
                                           "ваш тотем! Если захотите ещё раз пройти анкету, просто нажмите /start .\n "
                                           "Fazbear Ent.", reply_markup=types.ReplyKeyboardRemove())
    #user_data[message.chat.id]['progress'] = "Ты Эннард!"
   # save_user_data(user_data, data_path)
#Цирковая Бэйби
@bot.message_handler(content_types=["text"], func=sing_and_ice_cream)
def cirqus_baby(message):
    photo1 = open("Cirqus_Baby.jpg", "rb")
    bot.send_photo(message.chat.id, photo1, "Внимание! Вы ответили на все вопросы. Идёт анализ приведённых вами ответов...\n "
                                           "1% ... 45% ... 61% ... 88% ... 91% ... 99.9999999999999999999999999999999999"
                                           "99999E999999999999R9999999999999999R999999999999999999999O9999999%%R%%%\?//\.,...\n "
                                           "Итак, из ваших ответов следует, что вы похожи на аниматроника 'Цирковая Бэйби'! "
                                            "Мои поздравления! Это означает что вы очень любите петь и есть мороженное, но "
                                            "это не главное! Главное, это то что вы можете быть главным в коллективе и другие "
                                            "будут этому рады, но со временем ваше командование может надоесть коллективу "
                                            "и тогда вас могут снять с этой должности... А ещё внутри вас есть маленький сюрприз,"
                                            "продемонстрируйте его друзьям, они это оценят! Что ж, вот вы и прошли анкету "
                                            "'Какой ты персонаж из вселенной FNaF' и узнали, что вы похожи на Цирковую"
                                            "Бэйби! Надеюсь, она придёт к вам, ведь теперь она ваш тотем! Если захотите ещё "
                                            "раз пройти анкету, просто нажмите /start .\n Fazbear Ent."
                   , reply_markup=types.ReplyKeyboardRemove())
    #user_data[message.chat.id]['progress'] = "Ты Цирковая Бэйби!"
    #save_user_data(user_data, data_path)
#Баллора
@bot.message_handler(content_types=["text"], func=dance)
def ballora(message):
    photo2 = open("Ballora.jpg", "rb")
    bot.send_photo(message.chat.id, photo2, "Внимание! Вы ответили на все вопросы. Идёт анализ приведённых вами ответов...\n "
                                           "1% ... 45% ... 61% ... 88% ... 91% ... 99.9999999999999999999999999999999999"
                                           "99999E999999999999R9999999999999999R999999999999999999999O9999999%%R%%%\?//\.,...\n "
                                           "Итак, из ваших ответов следует, что вы похожи на аниматроника 'Баллора'! Мои "
                                            "поздравления! Помимо того что вы очень любите танцевать, вы сохраняете контроль "
                                            "во всех сложных ситуациях и просто закрываете глаза на проблемы, ведь вы не одни! " 
                                            "У вас есть ваши друзья, которые всегда помогут вам в сложных ситуациях! Особенно "
                                            "помогут вам если к вам придёт сама Баллора, ведь теперь она ваш тотем! Если "
                                            "захотите ещё раз пройти анкету, просто нажмите /start .\n Fazbear Ent."
                   , reply_markup=types.ReplyKeyboardRemove())
#Минирина
@bot.message_handler(content_types=["text"], func=min)
def minireena(message):
    photo3 = open("Minireena.jpg", "rb")
    bot.send_photo(message.chat.id, photo3, "Внимание! Вы ответили на все вопросы. Идёт анализ приведённых вами ответов...\n "
                                           "1% ... 45% ... 61% ... 88% ... 91% ... 99.9999999999999999999999999999999999"
                                           "99999E999999999999R9999999999999999R999999999999999999999O9999999%%R%%%\?//\.,...\n "
                                           "Итак, из ваших ответов следует, что вы похожи на аниматроника 'Минирина'! Мои "
                                            "поздравления! Это означает вы любите командную работу с общей целью, которую "
                                            "вам назначил командир. Ещё это означает что вы не любите одиночество, а предпочитаете "
                                            "проводить всё  время в кругу друзей. Что ж, вот вы и прошли анкету "
                                            "'Какой ты персонаж из вселенной FNaF' и узнали, что вы похожи на Минирину! "
                                            "Надеюсь, она придёт к вам, ведь теперь она ваш тотем! Если захотите ещё "
                                            "раз пройти анкету, просто нажмите /start .\n Fazbear Ent."
                   , reply_markup=types.ReplyKeyboardRemove())
#Бидибаб
@bot.message_handler(content_types=["text"], func=bid)
def bidybab(message):
    photo4 = open("Bidybab.jpg", "rb")
    bot.send_photo(message.chat.id, photo4, "Внимание! Вы ответили на все вопросы. Идёт анализ приведённых вами ответов...\n "
                                           "1% ... 45% ... 61% ... 88% ... 91% ... 99.9999999999999999999999999999999999"
                                           "99999E999999999999R9999999999999999R999999999999999999999O9999999%%R%%%\?//\.,...\n "
                                           "Итак, из ваших ответов следует, что вы похожи на аниматроника 'Бидибаб'! Мои "
                                            "поздравления! Это означает, что вы любите командную работу с общей целью, которую "
                                            "вы назначили с вашими друзьями вместе. Но, к сожалению, не всегда вам всё сойдёт "
                                            "с рук, и найдётся тот, кто будет вам мешать или станет вашим начальником. "
                                            "Что ж, вот вы и прошли анкету 'Какой ты персонаж из вселенной FNaF' и узнали, "
                                            "что вы похожи на Бидибаба! Надеюсь, он придёт к вам, ведь теперь он ваш тотем! "
                                            "Если захотите ещё раз пройти анкету, просто нажмите /start .\n Fazbear Ent."
                   , reply_markup=types.ReplyKeyboardRemove())

#Той Бонни или Той Фредди или Мангл или Той Чика или Марионетка
@bot.message_handler(content_types=["text"], func=toy)
def to_y(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bp1 = types.KeyboardButton("Играть на рок-гитаре")
    bp2 = types.KeyboardButton("Петь")
    bp3 = types.KeyboardButton("Уметь лазать по стенам")
    bp4 = types.KeyboardButton("Обожать пиццу и иметь кекс")
    bp5 = types.KeyboardButton("Жить в музыкальной шкатулке")
    markup.add(bp1, bp2, bp3, bp4, bp5)
    bot.send_message(message.from_user.id, "Пятый вопрос:\n "
                                           "Вам нравится играть на рок-гитаре, петь, уметь лазать по стенам, обожать пиццу "
                                           "и иметь кекс или жить в музыкальной шкатулке? ", reply_markup=markup)
#Той Бонни
@bot.message_handler(content_types=["text"], func=toy_bonnie)
def rock_guitar(message):
    photo5 = open("Toy_Bonnie.jpg", "rb")
    bot.send_photo(message.chat.id, photo5, "Внимание! Вы ответили на все вопросы. Идёт анализ приведённых вами ответов...\n "
                                           "1% ... 45% ... 61% ... 88% ... 91% ... 99.9999999999999999999999999999999999"
                                           "99999E999999999999R9999999999999999R999999999999999999999O9999999%%R%%%\?//\.,...\n "
                                           "Итак, из ваших ответов следует, что вы похожи на аниматроника 'Той Бонни'! Мои "
                                            "поздравления! Помимо того, что вы любите играть на гитаре, вы очень цените красоту "
                                            "и тщательно следите за своим внешним видом, чтобы понравиться окружающим. У вас "
                                            "есть и тёмная сторона, от которой неизвестно что можно ожидать. Что ж, вот "
                                            "вы и прошли анкету 'Какой ты персонаж из вселенной FNaF' и узнали, что вы "
                                            "похожи на Той Бонни! Надеюсь, он придёт к вам, ведь теперь он ваш тотем! Если захотите ещё "
                                            "раз пройти анкету, просто нажмите /start .\n Fazbear Ent.", reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(content_types=["text"], func=toy_chica)
def pizza_keks(message):
    photo6 = open("Toy_Chica.jpg", "rb")
    bot.send_photo(message.chat.id, photo6, "Внимание! Вы ответили на все вопросы. Идёт анализ приведённых вами ответов...\n "
                                           "1% ... 45% ... 61% ... 88% ... 91% ... 99.9999999999999999999999999999999999"
                                           "99999E999999999999R9999999999999999R999999999999999999999O9999999%%R%%%\?//\.,...\n "
                                           "Итак, из ваших ответов следует, что вы похожи на аниматроника 'Той Чика'! Мои "
                                            "поздравления! Вы очень любите покушать, но тем не менее вы сохраняете свою "
                                            "стройную фигуру! Но вы очень зациклены на своей красоте и пытаетесь влюбить "
                                            "в себя как можно больше людей, что может не понравиться вашим друзьям. Что ж, вот "
                                            "вы и прошли анкету 'Какой ты персонаж из вселенной FNaF' и узнали, что вы "
                                            "похожи на Той Чику! Надеюсь, она придёт к вам, ведь теперь она ваш тотем! Если "
                                            "захотите ещё раз пройти анкету, просто нажмите /start .\n Fazbear Ent."
                   , reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(content_types=["text"], func=toy_freddy)
def sing(message):
    photo7 = open("Toy_Freddy.jpg", "rb")
    bot.send_photo(message.chat.id, photo7, "Внимание! Вы ответили на все вопросы. Идёт анализ приведённых вами ответов...\n "
                                           "1% ... 45% ... 61% ... 88% ... 91% ... 99.9999999999999999999999999999999999"
                                           "99999E999999999999R9999999999999999R999999999999999999999O9999999%%R%%%\?//\.,...\n "
                                           "Итак, из ваших ответов следует, что вы похожи на аниматроника 'Той Фредди'! "
                                            "Мои поздравления! Несмотря на ваш лишний вес, который вы возможно не замечали, "
                                            "вы отлично ладите с микрофоном и вытворяете с ним удивительные вещи! Если вы "
                                            "слышите как вас называют 'жирным' или что-то в этом роде, не обращайте внимания. "
                                            "Вам просто завидуют, ведь вы просто суперзвезда на сцене! Что ж, вот вы и прошли "
                                            "анкету 'Какой ты персонаж из вселенной FNaF' и узнали, что вы похожи на Той "
                                            "Фредди! Надеюсь, он придёт к вам, ведь теперь он ваш тотем! Если захотите ещё "
                                            "раз пройти анкету, просто нажмите /start .\n Fazbear Ent.", reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(content_types=["text"], func=mangle)
def lazat_po_stenam(message):
    photo8 = open("Mangle.jpg", "rb")
    bot.send_photo(message.chat.id, photo8)
    bot.send_message(message.chat.id, "Внимание! Вы ответили на все вопросы. Идёт анализ приведённых вами ответов...\n "
                                           "1% ... 45% ... 61% ... 88% ... 91% ... 99.9999999999999999999999999999999999"
                                           "99999E999999999999R9999999999999999R999999999999999999999O9999999%%R%%%\?//\.,...\n "
                                           "Итак, из ваших ответов следует, что вы похожи на аниматроника 'Мангл'! Мои поздравления! "
                                            "Вы очень гибкий человек, а также склонны к пиратской тематике, просто вы об этом никому "
                                            "не рассказываете. Но для окружающих вы обычный конструктор, то есть вы не имеете "
                                            "как таковой вес в обществе и окружающие за вас решают что и как вам нужно. Вас"
                                            "очень легко переконструировать, но тем не менее вы сохраняете гибкость. А ещё "
                                            "многим не понятно, кто же вы на самом деле. Ещё у вас есть вторая личность, некий помощник, "
                                            "который вам подсказывает в каких-то делах, но окружающие не видят в нём что-то необходимое "
                                            "и считают, что вы сами способны принимать решения. Что ж, вот вы и прошли анкету "
                                            "'Какой ты персонаж из вселенной FNaF' и узнали, что вы похожи на Мангл!  Надеюсь, "
                                            "ДА придёт к вам, ведь теперь ДА ваш тотем! Если захотите ещё "
                                            "раз пройти анкету, просто нажмите /start .\n Fazbear Ent.", reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(content_types=["text"], func=puppet)
def live_in_music(message):
    photo9 = open("Puppet.jpg", "rb")
    bot.send_photo(message.chat.id, photo9, "Внимание! Вы ответили на все вопросы. Идёт анализ приведённых вами ответов...\n "
                                           "1% ... 45% ... 61% ... 88% ... 91% ... 99.9999999999999999999999999999999999"
                                           "99999E999999999999R9999999999999999R999999999999999999999O9999999%%R%%%\?//\.,...\n "
                                           "Итак, из ваших ответов следует, что вы похожи на аниматроника 'Марионетка'! Мои "
                                            "поздравления! Вы очень добрый человек, уметее сострадать и помогать людям. В вас "
                                            "спрятаны секретные силы, с помощью которых вы помогаете друзьям, но обычно вы "
                                            "не рассказываете про эти силы и храните их в тайне от всех. А ещё вы меломан, так как "
                                            "обожаете слушать музыку. Что ж, вот вы и прошли анкету 'Какой ты персонаж из "
                                            "вселенной FNaF' и узнали, что вы похожи на Марионетку! Надеюсь, она придёт "
                                            "к вам, ведь теперь она ваш тотем! Если захотите ещё раз пройти анкету, просто "
                                            "нажмите /start .\n Fazbear Ent.", reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(content_types=["text"], func=rockstar)
def rockstar_animatronics(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bk1 = types.KeyboardButton("петь")
    bk2 = types.KeyboardButton("играть на рок-гитаре")
    bk3 = types.KeyboardButton("Играть на маракасах")
    bk4 = types.KeyboardButton("Играть на банджо")
    bk5 = types.KeyboardButton("Охранять")
    markup.add(bk1, bk2, bk3, bk4, bk5)
    bot.send_message(message.chat.id, "Пятый вопрос:\n "
                                      "Вам нравится петь, играть на рок-гитаре/маракасах/банджо или просто охранять "
                                      "кого-то/что-то?", reply_markup=markup)

@bot.message_handler(content_types=["text"], func=rockstar_freddy)
def rock_start_freddy(message):
    photo10 = open("Rockstar_Freddy.jpg", "rb")
    bot.send_photo(message.chat.id, photo10, "Внимание! Вы ответили на все вопросы. Идёт анализ приведённых вами ответов...\n "
                                           "1% ... 45% ... 61% ... 88% ... 91% ... 99.9999999999999999999999999999999999"
                                           "99999E999999999999R9999999999999999R999999999999999999999O9999999%%R%%%\?//\.,...\n "
                                           "Итак, из ваших ответов следует, что вы похожи на аниматроника 'Рокстар Фредди'! "
                                            "Мои поздравления! Вы пока непонятны никому, и многие не понимают для чего вы нужны. "
                                             "Но возможно вы  таите в себе скрытый посыл, и скоро все узнают что вы "
                                             "не безнадёжны! Единственное что понятно, вы звезда на сцене! Вы отлично ладите с микрофоном! "
                                             "Что ж, вот вы и прошли анкету 'Какой ты персонаж из вселенной "
                                             "FNaF' и узнали, что вы похожи на Рокстар Фредди! Надеюсь, он придёт к вам, "
                                             "ведь теперь он ваш тотем! Если захотите ещё раз пройти анкету, просто "
                                            "нажмите /start .\n Fazbear Ent.", reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(content_types=["text"], func=rockstar_bonnie)
def rock_star_bonnie(message):
    photo11 = open("Rockstar_Bonnie.jpg", "rb")
    bot.send_photo(message.chat.id, photo11, "Внимание! Вы ответили на все вопросы. Идёт анализ приведённых вами ответов...\n "
                                           "1% ... 45% ... 61% ... 88% ... 91% ... 99.9999999999999999999999999999999999"
                                           "99999E999999999999R9999999999999999R999999999999999999999O9999999%%R%%%\?//\.,...\n "
                                           "Итак, из ваших ответов следует, что вы похожи на аниматроника 'Рокстар Фредди'! "
                                            "Мои поздравления! Вы пока непонятны никому, и многие не понимают для чего вы нужны. "
                                             "Но возможно вы  таите в себе скрытый посыл, и скоро все узнают что вы "
                                             "не безнадёжны! Единственное что понятно, вы звезда на сцене! Вы отлично ладите с "
                                             "рок-гитарой! Что ж, вот вы и прошли анкету 'Какой ты персонаж из вселенной "
                                             "FNaF' и узнали, что вы похожи на Рокстар Бонни! Надеюсь, он придёт к вам, "
                                             "ведь теперь он ваш тотем! Если захотите ещё раз пройти анкету, просто "
                                            "нажмите /start .\n Fazbear Ent.", reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(content_types=["text"], func=rockstar_chica)
def rock_star_chica(message):
    photo12 = open("Rockstar_Chica.jpg", "rb")
    bot.send_photo(message.chat.id, photo12, "Внимание! Вы ответили на все вопросы. Идёт анализ приведённых вами ответов...\n "
                                           "1% ... 45% ... 61% ... 88% ... 91% ... 99.9999999999999999999999999999999999"
                                           "99999E999999999999R9999999999999999R999999999999999999999O9999999%%R%%%\?//\.,...\n "
                                           "Итак, из ваших ответов следует, что вы похожи на аниматроника 'Рокстар Чика'! "
                                           "Мои поздравления! Вы пока непонятны никому, и многие не понимают для чего вы нужны. "
                                           "Но возможно вы  таите в себе скрытый посыл, и скоро все узнают что вы не безнадёжны! "
                                             "Единственное что понятно, вы звезда на сцене! Вы отлично ладите с маракасами! "
                                             "Что ж, вот вы и прошли анкету 'Какой ты персонаж из вселенной FNaF' и узнали, "
                                             "что вы похожи на Рокстар Чику! Надеюсь, она придёт к вам, ведь теперь она ваш "
                                             "тотем! Если захотите ещё раз пройти анкету, просто нажмите /start .\n Fazbear Ent."
                   , reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(content_types=["text"], func=pigpath)
def pig_path(message):
    photo13 = open("Pigpath.jpg", "rb")
    bot.send_photo(message.chat.id, photo13, "Внимание! Вы ответили на все вопросы. Идёт анализ приведённых вами ответов...\n "
                                           "1% ... 45% ... 61% ... 88% ... 91% ... 99.9999999999999999999999999999999999"
                                           "99999E999999999999R9999999999999999R999999999999999999999O9999999%%R%%%\?//\.,...\n "
                                           "Итак, из ваших ответов следует, что вы похожи на аниматроника 'Пигпатч'! Мои "
                                           "поздравления! Вы пока непонятны никому, и многие не понимают для чего вы нужны. "
                                           "Но возможно вы  таите в себе скрытый посыл, и скоро все узнают что вы не безнадёжны! "
                                           "Некоторые пока вас превосходят на сцене, но на банджо вы играете великолепно, в "
                                           "этом вы мастер! Что ж, вот вы и прошли анкету 'Какой ты персонаж из вселенной FNaF' "
                                           "и узнали, что вы похожи на Пигпатча! Надеюсь, он придёт к вам, ведь теперь он ваш "
                                           "тотем! Если захотите ещё раз пройти анкету, просто нажмите /start .\n Fazbear Ent."
                   , reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(content_types=["text"], func=security_puppet)
def security__puppet(message):
    photo14 = open("Security_puppet.jpg", "rb")
    bot.send_photo(message.chat.id, photo14, "Внимание! Вы ответили на все вопросы. Идёт анализ приведённых вами ответов...\n "
                                           "1% ... 45% ... 61% ... 88% ... 91% ... 99.9999999999999999999999999999999999"
                                           "99999E999999999999R9999999999999999R999999999999999999999O9999999%%R%%%\?//\.,...\n "
                                           "Итак, из ваших ответов следует, что вы похожи на аниматроника 'Марионетка-охранник'! "
                                           "Мои поздравления! Вы рождены для того чтобы защищать людей от опасности, но возможно "
                                           "многие пока не успели понять, что вы действительно стоите чего-то. Что ж, вот "
                                           "вы и прошли анкету 'Какой ты персонаж из вселенной FNaF' и узнали, что вы похожи на "
                                           "Марионетку-охранника! Надеюсь, она придёт к вам, ведь теперь она ваш тотем! "
                                             "Если захотите ещё раз пройти анкету, просто нажмите /start .\n Fazbear Ent."
                   , reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(content_types=["text"], func=without_cheeks)
def rockstar_without_cheeks(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btnn1 = types.KeyboardButton("Рассказывать истории")
    btnn2 = types.KeyboardButton("ПЕТЬ")
    btnn3 = types.KeyboardButton("Шутить")
    btnn4 = types.KeyboardButton("Показывать магию")
    btnn5 = types.KeyboardButton("Играть на аккордионе")
    markup.add(btnn1, btnn2, btnn3, btnn4, btnn5)
    bot.send_message(message.from_user.id, "Четвёртый вопрос:\n "
                                           "Вам нравится рассказывать истории, петь, шутить, показывать магию или играть "
                                           "на аккордионе?", reply_markup=markup)

@bot.message_handler(content_types=["text"], func=tell_stories)
def mr_hippo(message):
    photo15 = open("Mr_Hippo.jpg", "rb")
    bot.send_photo(message.chat.id, photo15, "Внимание! Вы ответили на все вопросы. Идёт анализ приведённых вами ответов...\n "
                                           "1% ... 45% ... 61% ... 88% ... 91% ... 99.9999999999999999999999999999999999"
                                           "99999E999999999999R9999999999999999R999999999999999999999O9999999%%R%%%\?//\.,...\n "
                                           "Итак, из ваших ответов следует, что вы похожи на аниматроника 'Мистер Хиппо'! "
                                           "Мои поздравления! Вы сказочный болтун! Вы очень любите говорить о жизни и часто "
                                           "надоедаете окружающим. Также вы очень любите пофилосовствовать, при этом "
                                           "запинаясь и отходя от темы. Что ж, вот вы и прошли анкету 'Какой ты персонаж "
                                           "из вселенной FNaF' и узнали, что вы похожи на Мистера Хиппо! Надеюсь, он придёт "
                                           "к вам, ведь теперь он ваш тотем! Если захотите ещё раз пройти анкету, просто "
                                             "нажмите /start .\n Fazbear Ent.", reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(content_types=["text"], func=sing_frog)
def happy_frog(message):
    photo16 = open("Happy_Frog.jpg", "rb")
    bot.send_photo(message.chat.id, photo16, "Внимание! Вы ответили на все вопросы. Идёт анализ приведённых вами ответов...\n "
                                           "1% ... 45% ... 61% ... 88% ... 91% ... 99.9999999999999999999999999999999999"
                                           "99999E999999999999R9999999999999999R999999999999999999999O9999999%%R%%%\?//\.,...\n "
                                           "Итак, из ваших ответов следует, что вы похожи на аниматроника 'Хэппи Фрог' ! "
                                           "Мои поздравления! Многие вас называют глупым(-ой), не обращайте на них внимания. "
                                           "Может вы таите в себе скрытый посыл, и скоро все узнают что вы не безнадёжны! "
                                           "Что ж, вот вы и прошли анкету 'Какой ты персонаж из вселенной FNaF' и узнали, "
                                           "что вы похожи на Хэппи Фрог! Надеюсь, она придёт к вам, ведь теперь она ваш тотем! "
                                             "Если захотите ещё раз пройти анкету, просто нажмите /start .\n Fazbear Ent.",
                   reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(content_types=["text"], func=magic)
def orville_the_eliphant(message):
    photo17 = open("Orville_Elephant.jpg", "rb")
    bot.send_photo(message.chat.id, photo17, "Внимание! Вы ответили на все вопросы. Идёт анализ приведённых вами ответов...\n "
                                           "1% ... 45% ... 61% ... 88% ... 91% ... 99.9999999999999999999999999999999999"
                                           "99999E999999999999R9999999999999999R999999999999999999999O9999999%%R%%%\?//\.,...\n "
                                           "Итак, из ваших ответов следует, что вы похожи на аниматроника 'Слон Орвилл'! "
                                           "Мои поздравления! Вы очень любите магию и всё магическое. Вы вероятно сами любите "
                                           "вытворять всякие фокусы. Многие пока вероятно в это не верят, а всё потому что "
                                           "у вас вероятно есть друг болтун, который говорит что не надо. Что ж, вот вы и "
                                           "прошли анкету 'Какой ты персонаж из вселенной FNaF' и узнали, что вы похожи на "
                                           "Слона Орвилла! Надеюсь, он придёт к вам, ведь теперь он ваш тотем! Если захотите "
                                           "ещё раз пройти анкету, просто нажмите /start .\n Fazbear Ent.", reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(content_types=["text"], func=jokes)
def nedd_bear(message):
    photo18 = open("Nedd_Bear.jpg", "rb")
    bot.send_photo(message.chat.id, photo18, "Внимание! Вы ответили на все вопросы. Идёт анализ приведённых вами ответов...\n "
                                           "1% ... 45% ... 61% ... 88% ... 91% ... 99.9999999999999999999999999999999999"
                                           "99999E999999999999R9999999999999999R999999999999999999999O9999999%%R%%%\?//\.,...\n "
                                           "Итак, из ваших ответов следует, что вы похожи на аниматроника 'Медведь Нэд'! "
                                           "Мои поздравления! Вы очень любите шутить, бывает даже не в тему. Некоторые ваши "
                                           "шутки действительно смешные, но в основном вы выставляете себя глупцом. Завязывайте "
                                           "с этим. Шутите, когда это уместно. Что ж, вот вы и прошли анкету 'Какой ты персонаж "
                                           "из вселенной FNaF' и узнали, что вы похожи на Медведя Нэда! Надеюсь, он придёт "
                                             "к вам, ведь теперь он ваш тотем! Если захотите ещё раз пройти анкету, просто "
                                             "нажмите /start .\n Fazbear Ent.",  reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(content_types=["text"], func=accordion)
def rockstar_foxy(message):
    photo19 = open("Rockstar_Foxy.jpg", "rb")
    bot.send_photo(message.chat.id, photo19, "Внимание! Вы ответили на все вопросы. Идёт анализ приведённых вами ответов...\n "
                                           "1% ... 45% ... 61% ... 88% ... 91% ... 99.9999999999999999999999999999999999"
                                           "99999E999999999999R9999999999999999R999999999999999999999O9999999%%R%%%\?//\.,...\n "
                                           "Итак, из ваших ответов следует, что вы похожи на аниматроника 'Рокстар Фокси'! "
                                           "Мои поздравления! Вы добры, любите помогать, но если вам что-то не понравится, "
                                           "вы можете сорваться. Вы вероятно любите пиратскую тематику, и если это так, вы "
                                           "всерьёз увлекаетесь ей. Что ж, вот вы и прошли анкету 'Какой ты персонаж из "
                                           "вселенной FNaF' и узнали, что вы похожи на Рокстар Фокси! Надеюсь, он придёт "
                                           "к вам, ведь теперь он ваш тотем! Если захотите ещё раз пройти анкету, просто "
                                             "нажмите /start .\n Fazbear Ent.",  reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(content_types=["text"], func=old)
def old_animatronics(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bttn1 = types.KeyboardButton("Петь на сцене")
    bttn2 = types.KeyboardButton("ИГРАТЬ НА РОК-ГИТАРЕ")
    bttn3 = types.KeyboardButton("ИМЕТЬ КЕКС")
    bttn4 = types.KeyboardButton("БЫТЬ ПИРАТОМ")
    markup.add(bttn1, bttn2, bttn3, bttn4)
    bot.send_message(message.from_user.id, "Четвёртый вопрос:\n"
                                           "Вам нравится петь, играть на рок-гитаре, иметь кекс или быть пиратом?", reply_markup=markup)

@bot.message_handler(content_types=["text"], func=old_freddy)
def sing_old_freddy(message):
    photo20 = open("Old_Freddy.jpg", "rb")
    bot.send_photo(message.chat.id, photo20, "Внимание! Вы ответили на все вопросы. Идёт анализ приведённых вами ответов...\n "
                                           "1% ... 45% ... 61% ... 88% ... 91% ... 99.9999999999999999999999999999999999"
                                           "99999E999999999999R9999999999999999R999999999999999999999O9999999%%R%%%\?//\.,...\n "
                                           "Итак, из ваших ответов следует, что вы похожи на аниматроника 'Олд Фредди'! "
                                           "Мои поздравления! Несмотря на то, что вас знатно помотала жизнь, вы ещё держитесь. "
                                           "Это похвально! Так держать! Правда вы можете страдать из-за какого-то новенького "
                                             "в вашей жизни, который скорее всего специально так делает. Что ж, вот вы и "
                                             "прошли анкету 'Какой ты персонаж из вселенной FNaF' и узнали, что вы похожи на"
                                             "Олд Фредди! Надеюсь, он придёт к вам, ведь теперь он ваш тотем! Если захотите "
                                             "ещё раз пройти анкету, просто нажмите /start .\n Fazbear Ent.",  reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(content_types=["text"], func=old_bonnie)
def rock_guitar_old_bonnie(message):
    photo21 = open("Old_Bonnie.jpg", "rb")
    bot.send_photo(message.chat.id, photo21, "Внимание! Вы ответили на все вопросы. Идёт анализ приведённых вами ответов...\n "
                                           "1% ... 45% ... 61% ... 88% ... 91% ... 99.9999999999999999999999999999999999"
                                           "99999E999999999999R9999999999999999R999999999999999999999O9999999%%R%%%\?//\.,...\n "
                                           "Итак, из ваших ответов следует, что вы похожи на аниматроника 'Олд Бонни'! "
                                           "Мои поздравления! Несмотря на то, что вас знатно помотала жизнь, вы ещё держитесь. "
                                           "Это похвально! Так держать! Правда вы можете страдать из-за какого-то новенького "
                                             "в вашей жизни, который скорее всего специально так делает. Что ж, вот вы и "
                                             "прошли анкету 'Какой ты персонаж из вселенной FNaF' и узнали, что вы похожи на"
                                             "Олд Бонни! Надеюсь, он придёт к вам, ведь теперь он ваш тотем! Если захотите "
                                             "ещё раз пройти анкету, просто нажмите /start .\n Fazbear Ent.",  reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(content_types=["text"], func=old_chica)
def cupcake_old_chica(message):
    photo22 = open("Old_Chica.jpg", "rb")
    bot.send_photo(message.chat.id, photo22, "Внимание! Вы ответили на все вопросы. Идёт анализ приведённых вами ответов...\n "
                                           "1% ... 45% ... 61% ... 88% ... 91% ... 99.9999999999999999999999999999999999"
                                           "99999E999999999999R9999999999999999R999999999999999999999O9999999%%R%%%\?//\.,...\n "
                                           "Итак, из ваших ответов следует, что вы похожи на аниматроника 'Олд Чика'! "
                                           "Мои поздравления! Несмотря на то, что вас знатно помотала жизнь, вы ещё держитесь. "
                                           "Это похвально! Так держать! Правда вы можете страдать из-за какого-то новенького "
                                             "в вашей жизни, который скорее всего специально так делает. Что ж, вот вы и "
                                             "прошли анкету 'Какой ты персонаж из вселенной FNaF' и узнали, что вы похожи на"
                                             "Олд Чику! Надеюсь, она придёт к вам, ведь теперь она ваш тотем! Если захотите "
                                             "ещё раз пройти анкету, просто нажмите /start .\n Fazbear Ent.",  reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(content_types=["text"], func=old_foxy)
def be_a_pirate_old_foxy(message):
    photo23 = open("Old_Foxy.jpg", "rb")
    bot.send_photo(message.chat.id, photo23,
                   "Внимание! Вы ответили на все вопросы. Идёт анализ приведённых вами ответов...\n "
                   "1% ... 45% ... 61% ... 88% ... 91% ... 99.9999999999999999999999999999999999"
                   "99999E999999999999R9999999999999999R999999999999999999999O9999999%%R%%%\?//\.,...\n "
                   "Итак, из ваших ответов следует, что вы похожи на аниматроника 'Олд Фокси'! "
                   "Мои поздравления! Несмотря на то, что вас знатно помотала жизнь, вы ещё держитесь. "
                   "Это похвально! Так держать! Правда вы можете страдать из-за какого-то новенького "
                   "в вашей жизни, который скорее всего специально так делает. Что ж, вот вы и "
                   "прошли анкету 'Какой ты персонаж из вселенной FNaF' и узнали, что вы похожи на "
                   "Олд Фокси! Надеюсь, она придёт к вам, ведь теперь она ваш тотем! Если захотите "
                   "ещё раз пройти анкету, просто нажмите /start .\n Fazbear Ent.",
                   reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(content_types=["text"], func=classic_animatronics)
def classic__animatronics(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bbtn1 = types.KeyboardButton("Петь на Сцене")
    bbtn2 = types.KeyboardButton("Играть на Рок-гитаре")
    bbtn3 = types.KeyboardButton("Иметь Кекс")
    bbtn4 = types.KeyboardButton("Быть Пиратом")
    markup.add(bbtn1, bbtn2, bbtn3, bbtn4)
    bot.send_message(message.from_user.id, "Четвёртый вопрос:\n"
                                           "Вам нравится петь, играть на рок-гитаре, иметь кекс или быть пиратом?", reply_markup=markup)

@bot.message_handler(content_types=["text"], func=classic_freddy)
def classic__freddy(message):
    photo24 = open("Classic_freddy.jpg", "rb")
    bot.send_photo(message.chat.id, photo24, "Внимание! Вы ответили на все вопросы. Идёт анализ приведённых вами ответов...\n "
                   "1% ... 45% ... 61% ... 88% ... 91% ... 99.9999999999999999999999999999999999"
                   "99999E999999999999R9999999999999999R999999999999999999999O9999999%%R%%%\?//\.,...\n "
                   "Итак, из ваших ответов следует, что вы похожи на аниматроника 'Классический Фредди(или просто Фредди)'! "
                   "Мои поздравления! Вы храните много тайн в себе, которые остальные люди пытаются разгадать. Вы многое повидали "
                    "в жизни, и можете что-то знать лучше других. А ещё вы звезда на сцене! Что ж, вот вы и прошли анкету "
                   "'Какой ты персонаж из вселенной FNaF' и узнали, что вы похожи на Фредди! Надеюсь, он придёт к вам, ведь теперь он ваш тотем! "
                    "Если захотите ещё раз пройти анкету, просто нажмите /start .\n Fazbear Ent.", reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(content_types=["text"], func=classic_bonnie)
def classic__bonnie(message):
    photo25 = open("Classic_Bonnie.jpg", "rb")
    bot.send_photo(message.chat.id, photo25, "Внимание! Вы ответили на все вопросы. Идёт анализ приведённых вами ответов...\n "
                   "1% ... 45% ... 61% ... 88% ... 91% ... 99.9999999999999999999999999999999999"
                   "99999E999999999999R9999999999999999R999999999999999999999O9999999%%R%%%\?//\.,...\n "
                   "Итак, из ваших ответов следует, что вы похожи на аниматроника 'Классический Бонни(или просто Бонни)'! Мои поздравления! "
                    "Вы храните много тайн в себе, которые остальные люди пытаются разгадать. Вы многое повидали в жизни, "
                    "и можете что-то знать лучше других. А ещё вы явно кому-то снитесь в кошмарах. Что ж, вот вы и прошли "
                    "анкету 'Какой ты персонаж из вселенной FNaF' и узнали, что вы похожи на Бонни! Надеюсь, он придёт к "
                    "вам, ведь теперь он ваш тотем! Если захотите ещё раз пройти анкету, просто нажмите /start .\n Fazbear Ent."
                   , reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(content_types=["text"], func=classic_chica)
def classic__chica(message):
    photo26 = open("Classic_Chica.jpg", "rb")
    bot.send_photo(message.chat.id, photo26, "Внимание! Вы ответили на все вопросы. Идёт анализ приведённых вами ответов...\n "
                   "1% ... 45% ... 61% ... 88% ... 91% ... 99.9999999999999999999999999999999999"
                   "99999E999999999999R9999999999999999R999999999999999999999O9999999%%R%%%\?//\.,...\n "
                   "Итак, из ваших ответов следует, что вы похожи на аниматроника 'Классическая Чика(или просто Чика)'! "
                    "Мои поздравления! Вы храните много тайн в себе, которые остальные люди пытаются разгадать. Вы многое "
                    "повидали в жизни, и можете что-то знать лучше других. А ещё у вас есть верный друг, держитесь ближе к нему. "
                    "Что ж, вот вы и прошли анкету 'Какой ты персонаж из вселенной FNaF' и узнали, что вы похожи на Чику! "
                    "Надеюсь, она придёт к вам, ведь теперь она ваш тотем! Если захотите ещё раз пройти анкету, просто "
                                             "нажмите /start .\n Fazbear Ent.", reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(content_types=["text"], func=classic_foxy)
def classic__foxy(message):
    photo27 = open("Classic_Foxy.jpg", "rb")
    bot.send_photo(message.chat.id, photo27, "Внимание! Вы ответили на все вопросы. Идёт анализ приведённых вами ответов...\n "
                   "1% ... 45% ... 61% ... 88% ... 91% ... 99.9999999999999999999999999999999999"
                   "99999E999999999999R9999999999999999R999999999999999999999O9999999%%R%%%\?//\.,...\n "
                   "Итак, из ваших ответов следует, что вы похожи на аниматроника 'Классический Фокси(или просто Фокси)'! "
                    "Мои поздравления! Вы храните много тайн в себе, которые остальные люди пытаются разгадать. Вы многое "
                    "повидали в жизни, и можете что-то знать лучше других. А ещё вы явный пират. Что ж, вот вы и прошли "
                    "анкету 'Какой ты персонаж из вселенной FNaF' и узнали, что вы похожи на Фокси! Надеюсь, он придёт "
                    "к вам, ведь теперь он ваш тотем! Если захотите ещё раз пройти анкету, просто нажмите /start .\n Fazbear Ent.", reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(content_types=["text"], func=metal_male)
def funtime_freddy(message):
    photo28 = open("Funtime_Freddy.jpg", "rb")
    bot.send_photo(message.chat.id, photo28, "Внимание! Вы ответили на все вопросы. Идёт анализ приведённых вами ответов...\n "
                   "1% ... 45% ... 61% ... 88% ... 91% ... 99.9999999999999999999999999999999999"
                   "99999E999999999999R9999999999999999R999999999999999999999O9999999%%R%%%\?//\.,...\n "
                   "Итак, из ваших ответов следует, что вы похожи на аниматроника 'Фантайм Фредди'! Мои поздравления! "
                   "Вы огромный весельчак, любите веселье и шутки. Хоть вы и любите веселье, вглубине вас спит агрессия и "
                   "в любой момент она может выйти на свободу. Но у вас есть верный друг, который понимает, когда вас надо успокоить. "
                   "Что ж, вот вы и прошли анкету 'Какой ты персонаж из вселенной FNaF' и узнали, что вы похожи на Фантайм Фредди! "
                   "Надеюсь, он придёт к вам, ведь теперь он ваш тотем! Если захотите ещё раз пройти анкету, просто нажмите /start .\n Fazbear Ent."
                   , reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(content_types=["text"], func=metal_female)
def funtime_chica(message):
    photo29 = open("Funtime_Chica.jpg", "rb")
    bot.send_photo(message.chat.id, photo29, "Внимание! Вы ответили на все вопросы. Идёт анализ приведённых вами ответов...\n "
                   "1% ... 45% ... 61% ... 88% ... 91% ... 99.9999999999999999999999999999999999"
                   "99999E999999999999R9999999999999999R999999999999999999999O9999999%%R%%%\?//\.,...\n "
                   "Итак, из ваших ответов следует, что вы похожи на аниматроника 'Фантайм Чика'! Мои поздравления! Вы "
                   "полны тайн, никто ничего про вас толком не знает. Может стоить немного смягчиться и приоткрыть занавес в "
                   "свой внутренний мир? Что ж, вот вы и прошли анкету 'Какой ты персонаж из вселенной FNaF' и узнали, что вы похожи на "
                   "Фантайм Чику! Надеюсь, она придёт к вам, ведь теперь она ваш тотем! Если захотите ещё раз пройти анкету, просто нажмите /start .\n Fazbear Ent."
                   , reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(content_types=["text"], func=metal_unknown)
def funtime_foxy(message):
    photo30 = open("Funtime_Foxy.jpg", "rb")
    bot.send_photo(message.chat.id, photo30, "Внимание! Вы ответили на все вопросы. Идёт анализ приведённых вами ответов...\n "
                   "1% ... 45% ... 61% ... 88% ... 91% ... 99.9999999999999999999999999999999999"
                   "99999E999999999999R9999999999999999R999999999999999999999O9999999%%R%%%\?//\.,...\n "
                   "Итак, из ваших ответов следует, что вы похожи на аниматроника 'Фантайм Фокси'! Мои поздравления! "
                   "Вы любите рассказывать истории и у вас это отлично получается, так держать! Вы любите устраивать разные шоу, "
                   "но вы слишком придирчивы к тем, кто опаздывает на него. Всё-таки надо быть более сдержанным. "
                   "Что ж, вот вы и прошли анкету 'Какой ты персонаж из вселенной FNaF' и узнали, что вы похожи на Фантайм Фокси! "
                   "Надеюсь, он/она придёт к вам, ведь теперь он/она ваш тотем! Если захотите ещё раз пройти анкету, просто нажмите /start .\n Fazbear Ent."
                   , reply_markup=types.ReplyKeyboardRemove())

bot.polling()