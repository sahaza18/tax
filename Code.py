import itertools


def covertTocode (langage) : 
    result = []
    iteration = 1
    while (iteration < len(langage)) :
        combinaisons = generateCombinaison(langage , iteration)
        for combinaison in combinaisons : 
            langage_copy = langage.copy()
            for item in combinaison:
                if item in langage_copy :
                    langage_copy.remove(item)
            if (isCode(langage_copy)) :
                return langage_copy       
        iteration += 1
    return result
    

def generateCombinaison(langage, nbr):
    combinations = itertools.combinations(langage, nbr)
    return  list(combinations)


def isCode(langage) : 
    L1 = getL1(langage)
    # print(L1)
    if len(L1) == 0 :
        return True     
    LPasser = []
    LPasser.append([L1])
    Ln = L1
    
    while ( True ) : 
        Lmoins1Ln = quotient(langage , Ln)
        LNmoins1L = quotient(Ln , langage)
        
        Lmoins1Ln.extend(LNmoins1L)
        
        qutoienLSuivant = list(set(Lmoins1Ln))
        # print(qutoienLSuivant)

        if len(qutoienLSuivant) == 0 :
            return True
        if qutoienLSuivant.count("£") > 0:
            return False       
        if any(item == qutoienLSuivant for sublist in LPasser for item in sublist):
            return True
        
        LPasser.append([qutoienLSuivant]) 
        Ln = qutoienLSuivant


def getL1(langage) :
    result = []
    quotients = quotient(langage, langage)
    
    for item in quotients :
        if item != "£" :
            result.append(item)
    
    return result


def quotient(langage , langage1) : 
    result = []  
    for motof1 in langage1 :      
        residu = residual(langage , motof1)
        result.extend(residu)
    return result


def residual(langage, word) :
    result = []
    for mot in langage :
        if mot.startswith(word) :
            mot_without_Word = mot.replace(word, "", 1)  # Supprimer le préfixe 'mot' une seule fois
            if not mot_without_Word :  
                result.append("£")
            else:
                result.append(mot_without_Word)
    return result



# ----------------- main --------------------------

# L = ["000", "010", "011", "01001"]   #True
# L = ["0", "01", "100", "010"]   #False


# L = ["0" ,"10", "001", "110", "111" , "0111" , "111" , "110" , "01" ]  # Manala roa

# residu = residual(L , "01")
# print(residu)


# L1 = ["01"]
# quotients = quotient(["010" , "101" , "110" , "001"] , ["010" , "101" , "110" , "001"])
# print(quotients)


# print(getL1(L))


# print(isCode(L))


# -------------------   Alea Mardi ------------
# print(generateCombinaison(L , 2))
# print(covertTocode(L))