import time

def capturetime(func):
    def patched(*a, **kwa):
        print(f'capturing time for function {func.__name__}')
        time_s = time.time()
        result = func(*a, **kwa)
        time_e = time.time()
        print(f'function {func.__name__} works {time_e-time_s:.1f} seconds')
        return result, round(time_e - time_s, 2)
    
    return patched