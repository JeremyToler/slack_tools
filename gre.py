'''
grepy - Jeremy Toler
Sends a message to slack when grep gets a result you are waiting for. 
It will send any stdinput to slack..
'''
import slack_sdk as slack
 
def send_message(grep_output):
    client = slack.WebClient(token='YOUR-AUTH-TOKEN')
    client.chat_postMessage(
        channel='scripts',
        text=f'{grep_output}',
        icon_emoji = ':safety_vest:',
        username = 'grepy'
        )  

def main(grep_output):
    if grep_output:
        send_message(grep_output)
    else:
        pass

if __name__ == '__main__':
    grep_output = input()
    main(grep_output)
