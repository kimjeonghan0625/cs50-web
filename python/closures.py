# Closures


def outer_func(msg: str):
    def inner_func():
        print(msg)

    return inner_func


hi_func = outer_func("Hi")
hello_func = outer_func("Hello")
hi_func()
hello_func()

# A closure is an inner function that remembers and has access to
# variables in the local scope in which it was created
# even after the outer function has finished executing
# 클로저는 함수 안의 함수다 클로저가 만들어진 로컬 스코프의 변수들을
# 기억하고 접근할 수 있는
# 심지어 외부 함수의 실행이 끝난 후에도
