
# Time
# Однажды ночью вы отправляетесь кататься на мотоцикле.
# В 00:00 вы запускаете двигатель, и встроенный таймер
# автоматически начинает отсчитывать продолжительность
# вашей поездки в минутах. Вы отправляетесь исследовать
# окрестности. Когда вы, наконец, решаете вернуться назад,
# вы понимаете, что есть вероятность, что мосты на вашем
# пути домой разведены, и вы останетесь в затруднительном
# положении! К сожалению, у вас нет с собой часов и вы не
# знаете, который час. Благодаря таймеру мотоцикла вы знаете
# только то, что с 00:00 прошло n минут.
# Используя таймер мотоцикла, рассчитайте текущее время.
# Возвращает ответ в виде суммы цифр, которую покажет цифровой таймер в формате чч:мм.
# Пример:
# Для n = 240, результат должен быть: 4
# 240 минут прошло, текущее время 04:00. Сумма чисел: 0 + 4 + 0 + 0 = 4, это и есть ответ.
# Для n = 808, результат должен быть: 14
# 808 минут прошло, и это означает что сейчас 13:28, так что ответ должен быть 1 + 3 + 2 + 8 = 14.

def timer_data_to_time(current_timer):
    time_summary, hours, minutes = 0, 0, 0
    if isinstance(current_timer, int):
        hours, minutes = current_timer // 60, current_timer % 60
        time_in_str = (str(hours) + str(minutes))
        for i in time_in_str:
            time_summary += int(i)
    return print(f'Ну, тип ты герой асфальта уже '
                 f'{hours} ч. {minutes} мин. - {time_summary} то бишь.')


timer_data_to_time(808)


# Level Up
# Вы играете в ролевую игру. В настоящее время
# общее количество ваших очков опыта (XP) равно опыту.
# Чтобы достичь следующего уровня, ваш XP должен
# быть как минимум на пороге. Если вы убьете монстра
# перед собой, вы получите больше очков опыта в размере награды.
# Учитывая значения опыта, порога и награды, проверьте,
# достигнете ли вы следующего уровня после убийства монстра.
# Пример:
# Для experience = 10, threshold = 15, и
# reward = 5, результат должен быть: true
# Для experience = 10, threshold = 15, и
# reward = 4, результат должен быть: false

def skyrim_2(exp, rew, thresh):
    if exp + rew >= thresh:
        return print(f'experience = {exp}, threshold = {rew}, '
                     f'и reward = {thresh} ---- result is... true')
    else:
        return print(f'experience = {exp}, threshold = {rew}, '
                     f'и reward = {thresh} ---- result is... false')


experience = 10
threshold = 15
reward = 4


skyrim_2(experience, reward, threshold)


# Time converter
# Ваша задача - конвертировать время из
# 24-часового формата в 12-часовой, используя
# следующие правила:
# выходной формат должен быть 'чч:мм a.m.'
# (для часов до полудня) или 'чч:мм p.m.'
# (для часов после полудня), если часы меньше
# 10 - не пишите '0' перед ними. Например: '9:05 a.m.'
# Пример:
# '12:30' == '12:30 p.m.'
# '09:00' == '9:00 a.m.'
# '23:15' == '11:15 p.m.'
# '00:00' == '12:00 a.m.'


def time_converter(time_pandas):
    if (isinstance(time_pandas, str)
            and time_pandas[:2].isdigit()
            and time_pandas[-2:].isdigit()
            and ':' in time_pandas):
        if int(time_pandas[:2]) < 12:
            part_of_day = ' a.m.'
        else:
            part_of_day = 'p.m.'
        time_pandas = time_pandas + part_of_day
    return print(time_pandas)


def input_time():
    ewige = True
    while ewige is True:
        get_time = input('Пожалуйста, введите время в формате: "00:00":')
        try:
            if int(get_time[:2]) < 25 and int(get_time[-2:]) < 60:
                time_converter(get_time)
                ewige = False
        except ValueError:
            continue
    return ''

input_time()
