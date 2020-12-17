import requests
import random
apiurl = ""

def get_chat_id(update):
    chat_id = update['message']["chat"]["id"]
    return chat_id

def get_message(update):
    msg = update["message"]["text"]
    return msg

def get_last_update(req):
    response = requests.get(req+"getUpdates")
    response = response.json()
    result = response["result"]
    totalUpdates = len(result)-1
    return result[totalUpdates]

def send_message(chatID, message):
    parameters = {"chat_id": chatID, "text": message}
    response = requests.post(apiurl + "sendMessage", parameters)
    return response


def main():
    updateID = get_last_update(apiurl)["update_id"]
    while True:
        update = get_last_update(apiurl)
        understand = 0
        if updateID == update["update_id"]:
            if get_message(update).lower() == "help" :
                send_message(get_chat_id(update), "Use 'play' to play a minigame\nUse 'Hello' or 'Hi' to greet\n\n"+
                             "More features is comin' up, just wait for it!!")
                understand = 1
                
                
            elif get_message(update).lower() == "hello" or get_message(update).lower() == "hi" or get_message(update) == "/start" :
                send_message(get_chat_id(update), "Hello, welcome to Cornel's bot :)")
                understand = 1
                
                
            elif get_message(update).lower() == "play":
                firstnum = random.randint(1, 10)
                secondnum = random.randint(1, 10)
                tosend = "what is " + str(firstnum) + "+" + str(secondnum) + "?"
                send_message(get_chat_id(update), tosend)
                updateID += 1
                while True:
                    playupdate = get_last_update(apiurl)
                    if updateID == playupdate["update_id"]:
                        if(get_message(playupdate).isnumeric() and int(get_message(playupdate)) == (firstnum + secondnum)):
                            send_message(get_chat_id(update), "Your answer is correct!")
                            break
                        else:
                            send_message(get_chat_id(update), "You entered wrong answer, try again later.")
                            break
                understand = 1
                
                
            if(understand == 0):
                send_message(get_chat_id(update), "Sorry, My Developer Haven't teach me that yet. :(" 
                    +"\nType 'help' to find out available features")
            
            updateID += 1


main()