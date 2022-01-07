
import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 400)     # скорость речи
engine.setProperty('volume', 0.9)   # громкость (0-1)



pastry = {'наполеон': [['масло', 'мука', 'сахар'], 7, 1000],
          'медовик': [['мука', 'масло', 'сахар'], 4, 1025],
          'киевский': [['сахар', 'мука', 'масло'], 5, 985]}

engine.say('Добрый день! Только сегодня, только сейчас к вашим услугам торты наполеон, медовик и киевский')
engine.say("Введите торт, который Вас интересует")
engine.runAndWait()
cake = input('Введите торт, который Вас интересует').lower()

choices = 'Введите 1, если вы хотите узнать описание,' \
          'Введите 2, если вы хотите узнать стоимость,' \
          'Введите 3, если вы хотите узнать сколько торта есть в наличии,' \
          'Введите 4, если вы хотите приобрести торт,' \
          'Введите 0, если вы хотиту уйти'
engine.say(choices)
engine.runAndWait()


while True:
    know = int(input("Введите 1, 2, 3, 4 или 0: "))
    if know != 0:
        for k, v in pastry.items():
                if cake == k:
                    if know == 1:
                        print(f'{cake} состоит из', *v[0])
                    elif know == 2:
                        print(f'{cake} стоит {v[1]} рублей')
                    elif know == 3:
                        print(f'{cake} осталось {v[-1]} грамм')
                    elif know == 4:
                        count = int(input('Сколько торта вам положить: '))
                        print(f'к оплате {count * v[1] / 100}')
                        print(f'{cake} осталось {v[-1] - count}')
                    elif know == 0:
                        break
    else:
        engine.say("Пока-пока, приходите еще!")
        engine.runAndWait()
        break
try:
    know > 4
    cake != pastry.get()
except (ValueError, TypeError, KeyError):
    print('неправильно ввели запрос,введите от 0 до 4 ')
    print('такого торта в наличии нет')