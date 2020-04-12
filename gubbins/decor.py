def me():
    return 'Coded by Ashley Pursglove \nProperty of Red Sea Farms \n\n '

def top(h):
    h=h
    i=0
    line = ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-']

    
    out = ''
    for hyp in line:
        if(i == h or i == 2*h or i == 1.5*h or i == 3*h or i == 4*h or i == 1.2*h or i == 1.1*h):
            hyp = '*'     
        out = out + hyp
        i +=1
    return out
    


def bottom():
    return '------------------------------'

# top(1)
# def top():
#     return '-----------------------------'