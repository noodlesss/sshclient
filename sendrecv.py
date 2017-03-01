import logging, msvcrt, sys, time

class Send_Recv(object):
    def __init__(self, event):
        self.__event = event
        self.logging = logging
        
    def send_command(self, input_command, c):
        try:
            self.logging.info('running command loop')
            __d = ''
            while __d != 'bye':
                input_command = msvcrt.getch()
                if input_command == '\b':
                    __d = __d[:-1]
                    msvcrt.putch(' ')
                    msvcrt.putch('\b')
                    c.send(input_command)
                elif input_command == '\r':
                    __d = ''
                    c.send('\n')
                else:
                    __d = ''.join((__d,input_command))
                    c.send(input_command)
            self.__event.set()
            logging.info('exiting command loop')
        except Exception, e:
            #logging.info(e)
            print e
            self.__event.set()

    def print_output(self, input_command, c):
        try:
            logging.info('running print loop')
            while not self.__event.set():
                sys.stdout.write(c.recv(9999))
                time.sleep(0.1)
            logging.info('exiting print loop')
        except Exception, e:
            logging.info(e)
            print e
            self.__event.set()
        