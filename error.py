import colorama
from colorama import Fore, Style
import time
import timeout_decorator
# Making a function error() to print an error
def error():
  time.sleep(2)
  ERROR_MESSAGE = "Oops..seems like that isn't a choice from the choices above, please try again.."
  print(Fore.RED + '----' * 9)
  print(ERROR_MESSAGE)
  print('----' * 9)
