import sshclient
import config

c = sshclient.SSH_Connect()
c.connect(config.ip, config.username, config.password)