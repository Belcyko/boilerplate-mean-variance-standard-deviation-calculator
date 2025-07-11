import numpy as np

def calculate(data):
    if len(data) != 9:
        raise ValueError('List must contain nine numbers.')
    
    m = np.array(data).reshape(3, 3)
    
    funcs = {
        'mean':               m.mean,
        'variance':           m.var,
        'standard deviation': m.std,
        'max':                m.max,
        'min':                m.min,
        'sum':                m.sum
    }
    
    result = {}
    for name, fn in funcs.items():
        cols  = fn(axis=0).tolist()
        rows  = fn(axis=1).tolist()
        whole = fn().item()
        result[name] = [cols, rows, whole]
    
    return result

