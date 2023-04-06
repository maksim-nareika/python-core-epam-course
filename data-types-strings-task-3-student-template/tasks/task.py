def replacer(s: str) -> str:
    s = s.replace('"', 'TEMPQUOTE')
    s = s.replace("'", '"')
    s = s.replace('TEMPQUOTE', "'")

    return s
