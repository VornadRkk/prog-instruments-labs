CSV_FILE_PATH = "lab_3/5.csv"
JSON_PATH = "lab_3/result.json"
REGULAR_PATTERNS = {
        'column_1': r'^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        'column_2': r'^\d{3} [A-Za-z ]+$',
        'column_3': r'^\d{12}$',
        'column_4': r'^\d{2} \d{2} \d{6}$',
        'column_5': r'^((25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)$',
        'column_6': r'^-?(90(\.0+)?|[1-8]?\d(\.\d+)?)$',
        'column_7': r'^#[0-9A-Fa-f]{6}$',
        'column_8': r'^\d{3}-\d-\d{5}-\d{3}-\d$',
        'column_9': r'^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$',
        'column_10': r'^(?:[01]?\d|2[0-3]):(?:[0-5]?\d):(?:[0-5]?\d)(?:\.\d{1,6})?$'
}