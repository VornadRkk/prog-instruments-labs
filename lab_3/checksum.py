import re
import json
import hashlib
import pandas as pd
from typing import List



from regular import CSV_FILE_PATH, JSON_PATH, REGULAR_PATTERNS
"""
В этом модуле обитают функции, необходимые для автоматизированной проверки результатов ваших трудов.
"""


def calculate_checksum(row_numbers: List[int]) -> str:
    """
    Вычисляет md5 хеш от списка целочисленных значений.

    ВНИМАНИЕ, ВАЖНО! Чтобы сумма получилась корректной, считать, что первая строка с данными csv-файла имеет номер 0
    Другими словами: В исходном csv 1я строка - заголовки столбцов, 2я и остальные - данные.
    Соответственно, считаем что у 2 строки файла номер 0, у 3й - номер 1 и так далее.

    Надеюсь, я расписал это максимально подробно.
    Хотя что-то мне подсказывает, что обязательно найдется человек, у которого с этим возникнут проблемы.
    Которому я отвечу, что все написано в докстринге ¯\_(ツ)_/¯

    :param row_numbers: список целочисленных номеров строк csv-файла, на которых были найдены ошибки валидации
    :return: md5 хеш для проверки через github action
    """
    row_numbers.sort()
    return hashlib.md5(json.dumps(row_numbers).encode('utf-8')).hexdigest()


def load_csv(file_path: str) -> pd.DataFrame:
    """
    Loads a CSV file.

    :param file_path: The path to the CSV file as a string.
    :return: A pandas DataFrame containing the loaded data.
    """
    data = pd.read_csv(file_path, encoding="utf-16", sep=";", header=0)
    return data


def write_to_file(variant: int, checksum: str) -> None:
    """
    Serializes the results of the lab work into the result.json file.

    :param variant: The variant number of the lab work.
    :param checksum: The checksum calculated using calculate_checksum().
    """
    with open(JSON_PATH, "r") as f:
        data = json.load(f)
    data["variant"] = variant
    data["checksum"] = checksum
    with open(JSON_PATH, "w") as f:
        json.dump(data, f, indent=4)


def validate_data(file_path: str) -> list:
    """
    Loads, validates the data, and calculates the checksum.
    :param file_path: The path to the CSV file as a string.
    :return: A list of indices of rows that contain errors.
    """
    data = load_csv(file_path)
    data.columns = [f"column_{i+1}" for i in range(10)]
    error = []
    for index, row in data.iterrows():
        row_has_error = False
        for col, pattern in REGULAR_PATTERNS.items():
            if not re.match(pattern, str(row[col])):
                row_has_error = True
                break
        if row_has_error:
            error.append(index)

    return error


if __name__ == "__main__":
    result = validate_data(CSV_FILE_PATH)
    checksum = calculate_checksum(result)
    write_to_file(variant="5", checksum=checksum)
    print("Контрольная сумма:", checksum)
    print(f"Невалидные записи: {len(result)}")
