import sys
from sender import Sender


if __name__ == "__main__":
    args = sys.argv

    sender = Sender(args)
    sender.send_info()
