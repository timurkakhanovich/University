import inspect
import traceback as TB
import sys

def exception_info(func):
    def try_to_get_exception(*args):
        try:
            return func(*args)
        except Exception:
            return (getLine(), inspect.getcallargs(func, *args))
    
    return try_to_get_exception

def getLine():
    curframe = sys.exc_info()[2]

    # Path of the file.  
    filename = curframe.tb_frame.f_code.co_filename
    # Get the last frame where the exception was called.  
    exc_frame = inspect.getinnerframes(curframe)[-1].lineno - 1

    code_line = TB.linecache.getline(filename, exc_frame)

    return code_line.lstrip().replace('\n', '')

@exception_info
def division(a, b):
    print("I'm going to divide...")
    return a / b

def main():
    print(division(1, 0))
    print(division(2, 0))
    print(division(1, 2))

if __name__ == "__main__":
    main()
