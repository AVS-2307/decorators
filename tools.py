import pandas as pd
import os
from datetime import datetime


def link_info(file_name):
    url = os.path.join(r'D:\Python\Fullstack\Modules_Packages_Import_Python\decor', 'log.csv')
    print(f'Ссылка на лог-файл: {url}')
#вывод принта повторяется при декорировании каждой функции, но это лишнее.
#было б интереснее всё-таки получать лог-файл для каждой функции при такой реализации

    def _info(old_function):
        def new_function(*args, **kwargs):
            start_date = f'Время запуска функции {str(old_function.__name__).upper()}: ' \
                         f'{datetime.now().replace(microsecond=0)}'
            func_name = f'Название функции: {str(old_function.__name__).upper()}'
            arguments = f'Аргументы функции {str(old_function.__name__).upper()}: {args}, {kwargs}'
            result = old_function(*args, **kwargs)
            result_to_log = f'Результат функции {str(old_function.__name__).upper()}: {result}'
            total_log = [start_date, func_name, arguments, result_to_log]
            df = pd.DataFrame(total_log)
            df.to_csv('log.csv', mode='a', index=False, header=False)
            print(f'Создание лог-файла для функции {str(old_function.__name__).upper()} завершено успешно')
            return result

        return new_function

    return _info


# def info(old_function):
#     # @wraps(old_function)
#     # total_log = []
#
#     def new_function(*args, **kwargs):
#         key = f'{args}_{kwargs}'
#         # if key in total_log:
#         #     return total_log
#         start_date = f'Время запуска функции {str(old_function.__name__).upper()}: ' \
#                      f'{datetime.now().replace(microsecond=0)}'
#         func_name = f'Название функции: {str(old_function.__name__).upper()}'
#         arguments = f'Аргументы функции {str(old_function.__name__).upper()}: {args}, {kwargs}'
#         result = old_function(*args, **kwargs)
#         result_to_log = f'Результат функции {str(old_function.__name__).upper()}: {result}'
#         total_log = [start_date, func_name, arguments, result_to_log]
#         df = pd.DataFrame(total_log)
#         df.to_csv('log.csv', mode='a', index=False, header=False)
#         print(f'Создание лог-файла для функции {str(old_function.__name__).upper()} завершено успешно')
#         return result
#
#     return new_function


# Подскажите, пожалуйста, как переделать код, чтобы в лог-файл не записывались данные с одними и теми же функциями
# с одними и теми же аргументами?
# Попробовал сделать, как в лекции, но пишет, что total_log сначала надо создать, прежде чем вызывать. Хотя, в лекции с
# cache такая же логика была, вроде как...

# И ещё момент, например, я хочу создавать новый лог при каждом вызове функции, а не добавлять запись в один и тот же файл.
# С помощью записи в файл, а не библиотеки logging, это можно же как-то сделать...тогда проверка на запуск функции
# с одними и тем же параметрами уже и не нужна будет
