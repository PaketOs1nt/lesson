import sys

def safe(func):
    def hooked(expr: str):
        if all([a in " 1234567890*/-()+~><&^%~=" for a in expr]):
            try:
                return func(expr)

            except BaseException as e:
                frame = sys._getframe().f_back

                print(f'[!] error in {func.__name__}')
                while frame:
                    print(f' | [stack] function: {frame.f_code.co_name}, line: {frame.f_lineno}') # по прiколу
                    frame = frame.f_back

                print(f' L error: {e.args}')
        else:
            return 'used forbidden symbol!'

    
    return hooked

@safe
def calculate(expression):
    return eval(expression)

while True:
    print(calculate(input('> ')))

    """
> 1 + 99 * (~-257 * (10 > 3)) // 20
1268
> 9 ** 9  
387420489
> print(1)
used forbidden symbol!
> zcxczx
used forbidden symbol!
> 1/0
[!] error in calculate
 | [stack] function: <module>, line: 29
 L error: ('division by zero',)
None
>
    """

# fully without gpt