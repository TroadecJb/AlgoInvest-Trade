def listToDict(liste: list) -> dict:
    # returns a dictionnary from a list where every elements is a tuple/list of two subelements
    dico = dict()
    for idx, e in enumerate(liste):
        dico[f"action-{idx+1}"] = [e[0], e[1]]

    return dico
