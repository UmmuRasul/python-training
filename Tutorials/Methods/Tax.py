def calculateNetTax(gross, state):

    """
    calculate de net income tax after the fedal ans de state tax
    parametre gross: gross income
    parameter state: state name
    :return: net income
    """
    state_Tax = {'msa': 10, 'nai': 9, 'mal': 8}

    #calculate net income after fedal tax
    net = gross - (gross *10)

    #calcualta  net income Tax  affter state tax
    if state in state_Tax:
        net = net - (gross * state_Tax[state] / 100)
        print("Your net income tax after all de heavy taxes is :" + str(net))
        return net
    else:
        print("state not in the list")
        return None


calculateNetTax(100000, 'msa')