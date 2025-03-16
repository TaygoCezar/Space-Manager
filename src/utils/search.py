import re

def ignore_case(s: str) -> str:
    return s.lower()

def ignore_accent_marks(s: str) -> str:
    s = re.sub(r"[àáâã]", "a", s)
    s = re.sub(r"[éê]", "e", s)
    s = re.sub(r"[í]", "i", s)
    s = re.sub(r"[óôõ]", "o", s)
    s = re.sub(r"[ú]", "u", s)
    s = re.sub(r"[ç]", "c", s)
    s = re.sub(r"[ñ]", "n", s)
    
    return s

def prefix_check(s: str, prefix: str) -> bool:
    prefix = ignore_accent_marks(ignore_case(prefix))
    s = ignore_accent_marks(ignore_case(s))
    return s.startswith(prefix)