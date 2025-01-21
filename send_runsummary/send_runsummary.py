import sys
from module_send import Sender


if __name__ == "__main__":
    args = sys.argv

    sender = Sender(args)
    sender.send_info()
