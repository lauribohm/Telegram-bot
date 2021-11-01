import requests as requests
import bs4
import emoji
import random
import json

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

##################################################################################

# get contact info from config file
with open("config.json") as json_data_file:
    data = json.load(json_data_file)
    url = data['secret']['url']


# create function that get chat id
def get_chat_id(update):
    chat_id = update['message']["chat"]["id"]
    return chat_id


# create function that get message text
def get_message_text(update):
    message_text = update["message"]["text"]
    return message_text


# create function that get last_update
def last_update(req):
    response = requests.get(req + "getUpdates")
    response = response.json()
    result = response["result"]
    total_updates = len(result) - 1
    return result[total_updates]  # get last record message update


# create function that let bot send message to user
def send_message(chat_id, message_text):
    params = {"chat_id": chat_id, "text": message_text}
    response = requests.post(url + "sendMessage", data=params)
    return response

# create main function for navigate or reply message back
def main():
    update_id = last_update(url)["update_id"]
    while True:
        update = last_update(url)

        sick = emoji.emojize(':mask:', use_aliases=True)
        beer = emoji.emojize(':beers:', use_aliases=True)
        wave = emoji.emojize(':wave:', use_aliases=True)
        poop = emoji.emojize(':poop:', use_aliases=True)

        if update_id == update["update_id"]:

            if get_message_text(update).lower() == "menu" or get_message_text(update).lower() == "/start":
                send_message(get_chat_id(update), """Cheers! """ + beer + """ Welcome to Corona bot """ + wave + """
*************************************   
Type WORLD to see amount of all Corona cases and deaths caused by Corona in the world """ + sick + """
*************************************         
Type CONTINENT to see Corona stats of each continent """ + sick + """
*************************************
Type FINLAND to see Corona stats in Finland """ + sick + """
*************************************
Type MEME to see memes related to Corona virus """ + poop + sick + """
*************************************
Or you can type MENU to get this view at anytime!""")


            elif get_message_text(update).lower() == "world":
                res = requests.get('https://www.worldometers.info/coronavirus/')
                soup = bs4.BeautifulSoup(res.text, 'lxml')

                stats = soup.select('title')
                msg = stats[0].text
                msg = msg.replace('-', '')
                msg = msg.replace('Worldometer', '')

                u = soup.select('div')
                updated = str(u[14].text)

                earth = emoji.emojize(':earth_americas:', use_aliases=True)

                send_message(get_chat_id(update), earth + "" + msg + "" + earth)

            elif get_message_text(update).lower() == "continent":
                res = requests.get('https://www.worldometers.info/coronavirus/')
                soup = bs4.BeautifulSoup(res.text, 'lxml' )

                stats = soup.select('td')
                print(stats)
                u = soup.select('div')
                updated = str(u[14].text)

                one = emoji.emojize(':one:', use_aliases=True)
                two = emoji.emojize(':two:', use_aliases=True)
                three = emoji.emojize(':three:', use_aliases=True)
                four = emoji.emojize(':four:', use_aliases=True)
                five = emoji.emojize(':five:', use_aliases=True)
                six = emoji.emojize(':six:', use_aliases=True)

                #sound = emoji.emojize('/play story', use_aliases=True)

                bullet = emoji.emojize(':o:', use_aliases=True)
                earth = emoji.emojize(':earth_americas:', use_aliases=True)

                d1 = "NONE"
                d2 = "NONE"
                d3 = "NONE"

                if stats[3].text != "":
                    d1=stats[3].text
                if stats[16].text != "":
                    d2 = stats[16].text
                if stats[29].text != "":
                    d3 = stats[29].text
                if stats[42].text != "":
                    d4=stats[42].text
                if stats[55].text != "":
                    d5 = stats[55].text
                if stats[68].text != "":
                    d6 = stats[68].text

                n1="NONE"
                n2 = "NONE"
                n3 = "NONE"

                if stats[2].text != "":
                    n1=stats[2].text
                if stats[15].text != "":
                    n2 = stats[15].text
                if stats[28].text != "":
                    n3 = stats[28].text
                if stats[41].text != "":
                    n4=stats[41].text
                if stats[54].text != "":
                    n5 = stats[54].text
                if stats[67].text != "":
                    n6 = stats[67].text


                send_message(get_chat_id(update),
                             earth + "Below continents in order of confirmed Corona cases" + earth)
                send_message(get_chat_id(update),
                             one + stats[0].text + "\nTotal cases:\n " + bullet + stats[1].text + "\nNew cases:\n" +  bullet + n1 + "\nTotal deaths:\n" +   bullet + d1 + "\nTotal recovered:\n" + bullet + stats[5].text + "\nActive cases:\n" + bullet + stats[6].text)
                send_message(get_chat_id(update),
                             two + stats[13].text + "\nTotal cases:\n " + bullet + stats[14].text + "\nNew cases:\n" +  bullet + n2 + "\nTotal deaths:\n" + bullet + d2 + "\nTotal recovered:\n" + bullet + stats[18].text + "\nActive cases:\n" + bullet + stats[19].text)
                send_message(get_chat_id(update),
                             three + stats[26].text + "\nTotal cases:\n " + bullet + stats[27].text + "\nNew cases:\n" +  bullet + n3 + "\nTotal deaths:\n" + bullet + d3 + "\nTotal recovered:\n" + bullet + stats[31].text + "\nActive cases:\n" + bullet + stats[32].text)
                send_message(get_chat_id(update),
                             four + stats[39].text + "\nTotal cases:\n " + bullet + stats[40].text + "\nNew cases:\n" +  bullet + n4 + "\nTotal deaths:\n" + bullet + d4 + "\nTotal recovered:\n" + bullet + stats[44].text + "\nActive cases:\n" + bullet + stats[45].text)
                send_message(get_chat_id(update),
                             five + stats[65].text + "\nTotal cases:\n " + bullet + stats[66].text + "\nNew cases:\n" +  bullet + n6 + "\nTotal deaths:\n" + bullet + d6 + "\nTotal recovered:\n" + bullet + stats[70].text + "\nActive cases:\n" + bullet + stats[71].text)
                send_message(get_chat_id(update),
                             six + stats[52].text + "\nTotal cases:\n " + bullet + stats[53].text + "\nNew cases:\n" +  bullet + n5 + "\nTotal deaths:\n" + bullet + d5 + "\nTotal recovered:\n" + bullet + stats[57].text + "\nActive cases:\n" + bullet + stats[58].text)


            elif get_message_text(update).lower() == "daily":
                res = requests.get('https://www.worldometers.info/coronavirus/')
                soup = bs4.BeautifulSoup(res.text, 'lxml')

                stats = soup.select('td')
                u = soup.select('div')
                updated = str(u[14].text)

                leader = 0
                lnbr = 0
                second = 0
                snbr = 0
                third = 0
                tnbr = 0

                x = -7

                while x < 1340:

                    variable = str(stats[x+9].text)
                    print(variable)
                    variable = variable.replace("+", "")
                    variable = variable.replace(",", "")


                    if variable == '':
                        variable = 1

                    print(variable)
                    variable = int(variable)

                    if variable > leader:
                        second = leader
                        snbr = lnbr
                        leader = variable
                        lnbr = int(x+9)

                    elif  leader > variable > second:
                        third = second
                        tnbr = snbr
                        second = variable
                        snbr = x+9


                    elif  second > variable > third:
                        third = variable
                        tnbr = x+9

                    x = x+9

                # share of total cases

                variable1 = str(stats[lnbr-1].text)
                variable1 = variable1.replace("+", "")
                variable1 = variable1.replace(",", "")
                variable1 = int(variable1)
                variable2 = str(stats[snbr-1].text)
                variable2 = variable2.replace("+", "")
                variable2 = variable2.replace(",", "")
                variable2 = int(variable2)
                variable3 = str(stats[tnbr-1].text)
                variable3 = variable3.replace("+", "")
                variable3 = variable3.replace(",", "")
                variable3 = int(variable3)

                share1 = round(leader/variable1, 2)*100
                share2 = round(second/variable2, 2)*100
                share3 = round(third/variable3, 2)*100

                one = emoji.emojize(':one:', use_aliases=True)
                two = emoji.emojize(':two:', use_aliases=True)
                three = emoji.emojize(':three:', use_aliases=True)

                bullet = emoji.emojize(':o:', use_aliases=True)
                earth = emoji.emojize(':earth_americas:', use_aliases=True)

                d1 = "NONE"
                d2 = "NONE"
                d3 = "NONE"

                if stats[lnbr+2].text != "":
                    d1=stats[lnbr+2].text
                if stats[snbr+2].text != "":
                    d2 = stats[snbr+2].text
                if stats[tnbr+2].text != "":
                    d3 = stats[tnbr+2].text

                send_message(get_chat_id(update),
                             earth + "Below top 3 countries in sense of confirmed Corona cases today" + earth)
                send_message(get_chat_id(update),
                             one + str(stats[lnbr-2].text) + one + "\nNew cases today:\n" + bullet + "+" +  str(leader) + "\nNew deaths today:\n" + bullet + d1 + "\nShare of total cases:\n" + bullet + str(share1) + "%")
                send_message(get_chat_id(update),
                             two + stats[snbr-2].text + two + "\nNew cases today:\n" + bullet + "+" + str(second) + "\nNew deaths today:\n" + bullet + d2 + "\nShare of total cases:\n" + bullet + str(share2) + "%")
                send_message(get_chat_id(update),
                             three + stats[tnbr-2].text + three + "\nNew cases today:\n" + bullet + "+" + str(third) + "\nNew deaths today:\n" + bullet + d3 + "\nShare of total cases:\n" + bullet + str(share3) + "%")



            elif get_message_text(update).lower() == "finland":
                res = requests.get('https://www.worldometers.info/coronavirus/')
                soup = bs4.BeautifulSoup(res.text, 'lxml')

                stats = soup.select('td')
                u = soup.select('div')
                updated = str(u[14].text)

                x = -9
                f = 0

                while x < 1340:

                    variable = str(stats[x+9].text)
                    print(variable)

                    if variable == 'Finland':
                        f = int(x + 9)
                        print("osuma")

                    x = x + 9

                bullet = emoji.emojize(':o:', use_aliases=True)
                #fi = emoji.emojize(':fi:', use_aliases=True)

                d = "NONE"
                n = "NONE"

                if stats[f+3].text != "":
                    d = stats[f+3].text
                if stats[f+2].text != "":
                     n = stats[f+2].text

                send_message(get_chat_id(update),
                            "SUOMI PERKELE!"+ "\nTotal cases:\n" + bullet + stats[
                            f+1].text + "\nNew cases:\n" + bullet + n + "\nTotal deaths:\n" + bullet +
                            d + "\nTotal recovered:\n" + bullet + stats[f+5].text + "\nActive cases:\n" + bullet + stats[f+6].text)


            elif get_message_text(update).lower() == "meme":
                res = requests.get("https://ruinmyweek.com/memes/coronavirus-meme-list/")
                res2 = requests.get("https://ruinmyweek.com/memes/coronavirus-meme-list/2/")

                soup = bs4.BeautifulSoup(res.text, 'lxml')
                image = soup.select('img')
                image2 = soup.select('img')

                count = 0
                count2 = 0
                images = []
                images2 = []

                for x in range(0, len(image)):
                    if 22 > x > 0:
                        if x % 2 == 0:
                            images.append(image[x]['src'])

                for x in range(0, len(image2)):
                    if 22 > x > 0:
                        if x % 2 == 0:
                            images2.append(image2[x]['src'])

                for img in images:
                    print(img)

                print("\n\n**************  Lista 2  **************\n\n")

                for img2 in images2:
                    print(img2)

                nbr = random.randint(0, 9)
                print(nbr)

                send_message(get_chat_id(update),images[nbr])

            else:
                send_message(get_chat_id(update), "Sorry, not understanding what you're saying:( Try to type 'MENU' for example")
            update_id += 1


# call the function to make it reply
main()

def meme():
    res = requests.get("https://ruinmyweek.com/memes/coronavirus-meme-list/")
    print(res.content)

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    image = soup.select('img')
    print(image['src'])

    count = 0
    images = []

    for x in range(0, len(image)):
        if 16 > x > 2:
            if x % 2 == 0:
                images.append(image[x]['src'])

    for img in images:
        print(img)

#meme()

def update():
    res = requests.get('https://www.worldometers.info/coronavirus/')
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    stats = soup.select('td')
    print(stats)

    x = -9
    f = 0

    while x < 1340:

        variable = str(stats[x + 9].text)
        print(variable)

        if variable == ' Finland ':
            f = int(x + 9)

        x = x + 9

    bullet = emoji.emojize(':o:', use_aliases=True)
    # fi = emoji.emojize(':fi:', use_aliases=True)

    d = "NONE"
    n = "NONE"

    if stats[f + 3].text != " ":
        d = stats[f + 3].text
    if stats[f + 2].text != " ":
        n = stats[f + 2].text

#update()

