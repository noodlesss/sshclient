import paramiko, logging, time, multiprocessing, threading,  sendrecv, config


class SSH_Connect(object):        
    def connect(self, ip, username, password):
        con = paramiko.SSHClient()
        con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        con.connect(ip, username = username, password = password)
        c = con.invoke_shell()
        __input_command = ''
        __jobs = []
        __event = threading.Event()
        sendr = sendrecv.Send_Recv(__event)
        send_command = sendr.send_command
        print_output = sendr.print_output
        for i in [send_command, print_output]:
            p = threading.Thread(target = i, args=(__input_command,c))
            __jobs.append(p)
            p.start()
        for i in __jobs:
            i.join()
        c.close()
        

