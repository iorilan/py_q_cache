import helper
import threading

def listen():
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
    helper.listen(q='hello',call_back=callback)

if __name__ == "__main__":
    t = threading.Thread(target=listen, daemon=True)
    t.start()
    
    while True:
        print('press q to exit')
        if input() == 'q':
            exit()