import threading

def first_run(age):
    while 1:
        print('first thread : ' ,age) 
    return
def second_run(age):
    while 1:
        print('second thread : ' ,age) 
    return


if __name__=='__main__':
    first = threading.Thread(target=first_run, args=(5,))
    second = threading.Thread(target=second_run, args=(3,))
    first.start()
    second.start()
    first.join()
    second.join()
    while True:
        print('Parent')
    pass