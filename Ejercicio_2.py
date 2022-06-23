import math




def get_instument(archivo):
    instrument_list = []
    with open(archivo, "r") as f:
        for line in f:
            instrument_list.append(line)
    return instrument_list

def gen_mod(instrumento, d, fs):
    return

constant = 1
linear = lambda x,t: x/t
invlinear = lambda x,t: max(1-(x/t), 0)
sin = lambda x,a,f: 1 + a*math.sin(f*x)
Exp = lambda x,t: math.e ** (5*(x-t))/t
invexp = lambda x,t: math.e ** (-5*x)/t
quartcos = lambda x,t: math.cos((math.pi * x)/(2 * t))
quartsin = lambda x,t: math.sin((math.pi * x)/(2 * t))
halfcos = lambda x,t: (1 + math.cos((math.pi * x)/ t))/2
halfsin = lambda x,t: (1 + math.cos(math.pi * ((x/t)-(1/2))))/2
Log = lambda x,t: math.log(((9 * x)/ t)+1, 10)
invlog = lambda x,t:




