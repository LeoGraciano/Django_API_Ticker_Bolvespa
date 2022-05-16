def isfloat(num):
    try:
        num = num.replace(',', '.')
        float(num)
        return True
    except Exception:
        return False
