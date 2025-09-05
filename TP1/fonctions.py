# TP1/fonctions.py
def puissance(a, b) -> int:
    """Retourne a**b si a et b sont des entiers, sinon lève TypeError."""
    if not type(a) is int or not type(b) is int:
        raise TypeError("Only integers are allowed")
    return a ** b

