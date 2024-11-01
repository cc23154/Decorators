__memoizacao = {}
def Memoizacao(function):
    aux = {}
    __memoizacao[function] = aux
    def func(*args, **kwargs):
        _ = (args, tuple(kwargs.items()))
        try:
            return aux[_]
        except:
            aux[_] = function(*args, **kwargs)
        return aux[_]
    return func