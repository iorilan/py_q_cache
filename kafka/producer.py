import helper

if __name__ == "__main__":
    while True:
        msg = input()
        if msg == 'q':
            break
        helper.produce(msg)
    