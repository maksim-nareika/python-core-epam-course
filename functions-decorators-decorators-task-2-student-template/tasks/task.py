import inspect
import time

def log(fn):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        with open("log.txt", "a") as file:

            param_list = []
            for param in inspect.signature(fn).parameters.values():
                param_list.append(param.name)
            arg_list = []
            for arg in args:
                arg_list.append(arg)
                args_dict = {}
            for i in range(0,len(arg_list)):
                args_dict[param_list[i]] = arg_list[i]

            args_str = ", ".join([f"{key}={value}" for key, value in args_dict.items()])
            kwargs_str = ", ".join([f"{key}={value}" for key, value in kwargs.items()])
            func_name = fn.__name__
            execution_time = round(end_time - start_time, 2)
            log_msg = f"{func_name}; args: {args_str}; kwargs: {kwargs_str}; execution time: {execution_time} sec.\n"
            file.write(log_msg)
        return result
    return wrapper