# "Бронирование мест".


def book_seat(all_seats):
    seat_name = input('Введите место для бронирования (от Б1 до Б9):')
    status = all_seats.get(seat_name)
    if not status:
        print(f'Место {seat_name} не существует.')
        return
    elif status == 'забронировано':
        print(f'Место {seat_name} уже забронировано.')
        return
    all_seats.update({seat_name: 'забронировано'})
    # try:
    #     i = all_seats.index([seat_name, 'свободно'])
    #     all_seats[i][1] = 'забронировано'
    #     print(f'Место {seat_name} успешно забронировано.')
    # except ValueError:
    #     print(f'Место {seat_name} уже забронировано или не существует.')
    # except Exception as e:
    #     print(f'Произошла неожиданная ошибка: {e}')


seats = {f'Б{i}': 'свободно' for i in range(1, 10)}
print(seats)
# if seats[s] == 'свободно'

while True:
    book_seat(seats)
    booking = input('Хотите забронировать еще одно место? (да/нет): ')
    if booking.lower() != "да":
        break

print('Итоговое состояние бронирования мест.')
for key in seats.keys():
    print(f'{key}: {seats.get(key)}')



