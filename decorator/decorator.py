from functools import wraps, update_wrapper

def logo(f):
    # @wraps(f)
    def wrapper(*args, **kwargs):
        print("<h1>Hytera</h1>")
        tmp = f(*args, **kwargs)
        print("copyright www.hytera.com")
        return tmp
    # return wrapper
    return update_wrapper(wrapper, f)


def logo_with_para(text):
    def logo(f):
        # @wraps(f)
        def wrapper(*args, **kwargs):
            print(text+"<h1>Hytera</h1>"+text)
            tmp = f(*args, **kwargs)
            print(text+"copyright www.hytera.com"+text)
            return tmp
        # return wrapper
        return update_wrapper(wrapper, f)
    return logo

@logo
def test():
    print(text)


@logo_with_para("-------")
def test_1(text):
    print(text)

# test("test")
# print(test.__name__)
test_1("test")
print(test_1.__name__)