"""Calculateur d'expression arithmétique"""

# Permet de savoir si le paramètre est un nombre
def is_digit(s: str) -> bool:
    """Renvoie True si s est un nombre, False sinon"""
    try:
        int(s)
        return True
    except ValueError:
        return False

# Permet de savoir la longueur d'une chaine de caractère
def longueur(string: str) -> int:
    """Renvoie la longueur d'une chaine de caractère"""
    count = 0
    while string[count:]:
        count += 1
    return count

# Permet de récupérer le dernier élément d'une liste
def pop_1(liste):
    """Renvoie le dernier élément d'une liste"""
    if longueur(liste) == 0:
        return None
    last = liste[-1]
    return last

# Permet de supprimer le dernier élément d'une liste
def pop_2(liste):
    """Supprime le dernier élément d'une liste"""
    if longueur(liste) == 0:
        return None
    liste = liste[:-1]
    return liste

# Permet d'ajouter un élément à la fin d'une liste
def append(liste, element):
    """Ajoute un élément à la fin d'une liste"""
    liste += [element]
    return liste

# Permet d'effectuer l'opération sur les deux derniers éléments de la liste
def operande(stack, element):
    """Effectue l'opération sur les deux derniers éléments de la liste"""
    op2 = pop_1(stack)
    stack = pop_2(stack)
    op1 = pop_1(stack)
    stack = pop_2(stack)
    resultat = checkOperande(element, op1, op2)
    stack = append(stack, resultat)
    return stack

# Permet de séparer l'expression en éléments
def split(expression):
    """Sépare l'expression en éléments"""
    elements = []
    i = 0
    while i < longueur(expression):
        if expression[i] == ' ':
            i += 1
        elif expression[i] == '+' or expression[i] == '-' \
         or expression[i] == '*' or expression[i] == '/':
            elements = append(elements, expression[i])
            i += 1
        else:
            number = ''
            while i < longueur(expression) and is_digit(expression[i]):
                number += expression[i]
                i += 1
            elements = append(elements, number)
    return elements

# Permet de vérifier l'opérateur et d'effectuer l'opération
def checkOperande(element, op1, op2):
    """Vérifie l'opérateur et effectue l'opération"""
    if element == '+':
        resultat = op1 + op2
    elif element == '-':
        resultat = op1 - op2
    elif element == '*':
        resultat = op1 * op2
    elif element == '/':
        resultat = op1 / op2
    else :
        print("Erreur : opérateur inconnu")
        resultat = 0
    return resultat

# Permet de calculer l'expression
def calculate(expression, i = 0):
    """Calcule l'expression"""
    # initialise une liste vide
    stack = []
    # Sépare l'expression en elements
    elements = split(expression)
    # Pour chaque element dans l'expression
    while i < longueur(elements):
        # Si le element est un opérateur
        if elements[i] == '+' or elements[i] == '-' \
         or elements[i] == '*' or elements[i] == '/':
            # On effectue l'opération sur les deux derniers éléments de la liste
            stack = operande(stack, elements[i])
            i += 1

        # Si le element est un nombre	
        else:
            # On l'ajoute à la liste des éléments à traiter
            append(stack, int(elements[i]))
            i += 1
    # On retourne le dernier élément de la liste
    return pop_1(stack)

# Permet de récupérer l'expression saisie par l'utilisateur
def saisie() -> str:
  """Récupère l'expression saisie par l'utilisateur"""
  expression = input("Veuillez saisir l'expression à évaluer \
    (ne pas oublier de mettre des espaces entre tous les characteres) : ")
  # On vérifie que l'expression saisie est bien une expression
  if expression is not None:
    # On vérifie que l'expression commence par un nombre
    if(expression != '' and is_digit(expression[0])):
      # On vérifie que l'expression ne contient que des nombres, des espaces et des opérateurs
      for i in range(0, longueur(expression)):
        if not (is_digit(expression[i]) or expression[i] == ' ' \
        or expression[i] == '+' or expression[i] == '-' \
        or expression[i] == '*' or expression[i] == '/'):
          print("Erreur : l'expression saisie n'est pas valide")
          return None
    else:
        print("Erreur : l'expression saisie n'est pas valide")
        return None
    return expression
  print("Erreur : l'expression saisie n'est pas valide")
  return None

# Permet de lancer le programme 
def main() :
    """Lance le programme"""
    #Appel de la fonction saisie() pour récupérer l'expression saisie par l'utilisateur.
    expression = saisie()
    print ("L'expression saisie est : ", expression)
    if expression is not None:
        try :
            print(calculate(expression))
        except TypeError:
            print("Erreur : l'expression saisie n'est pas valide")


if __name__ == "__main__":
    main()