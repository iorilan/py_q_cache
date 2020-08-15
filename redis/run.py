import helper

if __name__ == "__main__":
    host='192.168.11.137'
    port=6379
    
    while True:
        print('[cmd key value] or press q to exit')    
        cmd = input().split(' ')
        if cmd == 'q':
            break
        if cmd[0] == 'set':
            helper.set(host,port,cmd[1],cmd[2])
        elif cmd[0] == 'get':
            print(helper.get(host,port,cmd[1]))
        else:
            print('unknown command!')