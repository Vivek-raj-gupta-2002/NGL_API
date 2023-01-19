import requests
import random
import string


def randomDevId(k):
    return "".join(random.choices(string.ascii_lowercase+string.digits, k=k))




def SendMessage(userName: str, message: str):

    url = "https://ngl.link/api/submit"

#"1f294057-ff52-44e0-a260-d211af05258a"

    data = {
    "username": userName,
    "question": message,
    "deviceId": "{eight}-{four1}-{four2}-{four3}-{twelve}".format(
        eight = randomDevId(8),
        four1 = randomDevId(4),
        four2 = randomDevId(4),
        four3 = randomDevId(4),
        twelve = randomDevId(12),
    ),
    "gameSlug": "",
    "referrer": ""
    }

    data = requests.post(url, json=data)

    return data


