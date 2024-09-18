from datetime import datetime


def format_datetime(dt, fmt="%Y-%m-%d %H:%M:%S.%f"):
    if isinstance(dt, str):
        dt = datetime.strptime(dt, fmt)
    return dt.strftime(fmt)


def parse_datetime(date_string, fmt="%Y-%m-%d %H:%M:%S.%f"):
    """Parse a string into a datetime object."""
    return datetime.strptime(date_string, fmt)
