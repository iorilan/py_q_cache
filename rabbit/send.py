import threading
import helper

if __name__ == "__main__":
    while True:
        print('key in message to send ,press q to exit. ')
        msg = input()
        if msg == 'q':
            break
        helper.send(q='hello',msg=msg)