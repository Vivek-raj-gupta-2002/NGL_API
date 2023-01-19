import module
from time import sleep

username = ""
message = ""

for i in range(50):

    print(i)

    data = module.SendMessage(username, message)

    print(data)
    sleep(3)
    