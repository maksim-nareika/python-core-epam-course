import functools
def validate(fn):
    # @functools.wraps(fn)
    def wrapper(*args):
        if all(0 <= arg <= 256 for arg in args):
            return fn(*args)
        else:
            return "Function call is not valid!"

    return wrapper



@validate
def set_pixel(x: int, y: int, z: int) -> str:
    """
        Creates a pixel with the specified RGB values.

        Args:
            r (int): Red component of the pixel, between 0 and 256 inclusive.
            g (int): Green component of the pixel, between 0 and 256 inclusive.
            b (int): Blue component of the pixel, between 0 and 256 inclusive.

        Returns:
            str: "Pixel created!" if all parameters are valid, otherwise "Function call is not valid!".
    """
    return "Pixel created!"