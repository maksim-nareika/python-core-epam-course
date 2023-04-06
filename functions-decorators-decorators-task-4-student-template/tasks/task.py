
def decorator_apply(lambda_func):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            return fn(lambda_func(*args))
        return wrapper
    return decorator


@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int) ->int:
    return num


def print_function_info(should_count=False):
    def wrapper_func(func):
        def wrapper(*args, **kwargs):
            count = 0
            if should_count:
                count += 1
                print(f"Function was called {count} times")
            print(f"Calling function {func} with args: {args} and kwargs: {kwargs}")
           return func(*args, **kwargs)
        return wrapper
    return wrapper_func