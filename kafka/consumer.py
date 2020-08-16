import helper
import threading
def listen():
    #helper.consume_exact_once()
    helper.consume_at_least_once()
    #helper.consume_from_beginning()

if __name__ == "__main__":
    t = threading.Thread(target=listen, daemon=True)
    t.start()

    while True:
        if input() == 'q':
            break