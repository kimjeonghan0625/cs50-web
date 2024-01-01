def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function")
    return wrapper

@announce
def hello():
    print("Hello, world") # 사실상 hello = wrapper 와 동일하게 동작함

hello()
hello()