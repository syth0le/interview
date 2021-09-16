def repeater(f):
    def wrapper(*args, **kwargs):
        try:
            result = f(*args, **kwargs)
            return result
        except Exception:
            return "I caught an error!"
    return wrapper


@repeater
def errors_and_mistakes(num: int) -> str:
    if num > 5:
        return num / 0
    else:
        return "success"


if __name__ == "__main__":
    for elem in range(10):
        print(errors_and_mistakes(elem))

