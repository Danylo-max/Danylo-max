# База даних тренінгів
trainings = {
    'Ігри': {
        'відповідальний': 'Григоров О. С.' 'Буковський А. М',
        'теми': ['техніка безпеки', 'робота в команді'],
        'дата': '15.05'
    },
    'Робота': {
        'відповідальний': 'Череватий К. І.',
        'теми': ['лідерство', 'комп. грамотність'],
        'дата': '20.11'
    }
}

print('Fly kids 🤸🏽‍♂️')
print('1 - Ім\'я слідкувачів за парком, 2 - про роботу')

while True:

    action = input('Введіть номер дії (off вийти з сайту): ')

    if action == 'off':
        break
    elif action == '1':

            print('- відповідальний: Григоров О. С. Буковський А. М.')
    elif action == '2':
        print("Fly Kids — це мережа дитячих центрів активного відпочинку, яка пропонує батутні арени, мотузкові парки, ігрові майданчики та освітні майстер-класи. Вони також організовують дитячі дні народження та інші святкові заходи. Основна мета — забезпечити дітям безпечне, цікаве та розвиваюче середовище для активного проведення часу.")

    else:
        print('Невірний номер дії. Спробуйте ще раз.')
