"""Vérifie si une chaine est un palindrome, excluant accents et caractères spéciaux"""

#### Fonction secondaire


def ispalindrome(p):
    """
    Vérifie si une chaine de caractère est un palindrome.

    Args:
        p (str): Un mot ou une phrase.

    Returns:
        bool: Retourne vrai si p est un palindrome, faux sinon
    """
    # votre code ici
    accents = str.maketrans("àèùâêîôûäëïöüÿéç",
                            "aeuaeiouaeiouyec",
                            r""".,;:!?'"()[]{}-/@# """)
    p = p.lower().translate(accents)
    if p == p[::-1]:
        return True
    return False

#### Fonction principale


def main():
    """
    Vérifie si les mots de la liste sont des palindromes
    """
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
