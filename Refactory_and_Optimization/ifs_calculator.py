import matplotlib.pyplot as plt

def graphic(currencies:int):
    
    if_cases=[]
    xlabel=[]
    
    for index,coins in enumerate(range(1,currencies+1)):
        
        case=coins**2
        if_cases.append(case)
        xlabel.append(coins)        
        print(xlabel[-1],if_cases[-1],"combinations")
    
    fig,ax = plt.subplots()
    ax.plot(xlabel,if_cases)
    ax.set(xlabel='currencies', ylabel='if_cases',title='maintainability')
    ax.grid()
    plt.show()

                
graphic(183)


