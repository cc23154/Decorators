__memoizacao = {}
def Memoizacao(function):
    __memoizacao[function] = {}
    def func(*args, **kwargs):
        _ = (args, tuple(kwargs.items()))
        try:
            return __memoizacao[function][_]
        except:
            __memoizacao[function][_] = function(*args, **kwargs)
        return __memoizacao[function][_]
    return func