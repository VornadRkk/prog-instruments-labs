CSV_FILE_PATH = "5.csv"
JSON_PATH = "result.json"
REGULAR_PATTERNS = {
    "column_1": r"^[\w\.-]+@[\w\.-]+\.\w+$",
    "column_2": r"^\d{3}(?:\s\w+)+$",
    "column_3": r"^\d{12}$",
    "column_4": r"^\d{2}\s\d{2}\s\d{6}$",
    "column_5": r"^(\d{1,3}\.){3}\d{1,3}$",
    "column_6": r"^-?(90(\.0+)?|[1-8]?\d(\.\d+)?)$",
    "column_7": r"^#([A-Fa-f0-9]{6})$",
    "column_8": r"(?:\d{3}-)?\d-\d{5}-\d{3}-\d",
    "column_9": r"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$",
    "column_10": r"^^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)\.\d{6}$",
}
