import typing as t


def callLimit(limit: int):
    """Function decorator to apply a limit"""
    count = 0

    def callLimiter(function):
        """Sub decorator function for function"""
        def limit_function(*args: t.Any, **kwds: t.Any):
            """applies the limit on how much the function
            will be called"""
            nonlocal count
            count += 1
            if count > limit:
                print(f'Error: {function} call to many times')
                return
            result = function(*args, **kwds)
            return result
        return limit_function
    return callLimiter


def main():
    """Main entrypoint for call limit"""
    @callLimit(3)
    def f():
        print("f()")

    @callLimit(1)
    def g():
        print("g()")

    for i in range(3):
        f()
        g()


if __name__ == '__main__':
    main()
