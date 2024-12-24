class Counter: ...

count = Counter(16)
for i in count:
   print(i)

def raise_to_the_degress(num, maximum):
    i = 0
    for _ in range(maximum):
        yield num ** i
        i += 1
        
resssss = raise_to_the_degress(2, 90)
for i in resssss:
    print(i)

def helper(work):
    work_in_mem = work

    def asdasd(work):
        return f'bla bla bla "{work_in_mem}" bobob ababa "{work}"'
    
    return asdasd

print(helper('asd')('workkkk'))

def checker(func):
    def dbg(*a, **kwa):
        try:
            return func(*a, **kwa)
        except BaseException as err:
            print(F"Error in {func.__name__}: {err}")

    return dbg

@checker
def test(asd):
    return eval(asd)

test('0/0')