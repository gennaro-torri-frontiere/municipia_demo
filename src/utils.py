from datetime import datetime
import re

def parse_date(date_str: str) -> datetime:
    """
    Converts a date string into a datetime object by recognizing its format.

    Args:
        date_str (str): The date string to be converted.

    Returns:
        datetime: The corresponding datetime object.

    Raises:
        ValueError: If the date string does not match any known format.
    """
    if re.match(r"^\d{2}/\d{2}/\d{4}$", date_str):  # DD/MM/YYYY
        date_format = "%d/%m/%Y"
    elif re.match(r"^\d{8}$", date_str):  # YYYYMMDD
        date_format = "%Y%m%d"
    elif re.match(r"^\d{4}-\d{2}-\d{2}$", date_str):  # YYYY-MM-DD
        date_format = "%Y-%m-%d"
    elif re.match(r"^\d{2}-\d{2}-\d{4}$", date_str):  # DD-MM-YYYY
        date_format = "%d-%m-%Y"
    elif re.match(r"^\d{4}/\d{2}/\d{2}$", date_str):  # YYYY/MM/DD
        date_format = "%Y/%m/%d"
    else:
        raise ValueError(f"Date format not recognized for: {date_str}")
    
    return datetime.strptime(date_str, date_format)
