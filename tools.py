#single file containing all the features

def avg_set_error(prediction,outcome):
    if type(prediction) != list or type(outcome) != list:
        raise TypeError("Incorrect input, both parameters must be lists")

    elif len(prediction) != len(outcome):
        raise Exception("Both lists are different lengths")
    dfs=[]
    for x in range(0,len(prediction)):
        dfs.append(abs(prediction[x]-outcome[x]))
        
    return (sum(dfs)/len(dfs))
