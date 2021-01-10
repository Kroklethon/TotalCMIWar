def cree_table():
    """
    entree: rien
    sortie: rien 

    crée le tableau vide correspondant au case du tableau
    """
    tailletab = 30 # 0..29 (31)
    tailleligne = 30 # 0..29 (31)
    #####cration variable ######
    #tableau = []                   #TABLEAU ->
    #dico = {}                      #DICTIONNAIRE 
    #dico['statue'] = 'vide'        #statue vide (case vide)
    #####cration variable ######
    dico_init={}
    tableau = []
    for i in range(tailletab):
        tableau.append(['vide']*tailleligne)
    return tableau 
