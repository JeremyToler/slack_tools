'''
Site Snitch - Jeremy Toler
Sends a message to slack when a website is unreachable 
'''
import slack_sdk as slack
import requests
 
site_list = ['studiopeaches.com', 'httpbin.org/status/400']

def send_to_slack(error_text, code):
    error_emoji = ':sos:'

    if code >= 500:
        error_emoji = ':no_entry:'
    elif code >= 400:
        error_emoji = ':no_good:'
    elif not code == 0:
        error_emoji = ':shrug:'

    client = slack.WebClient(token='YOUR-OAUTH-TOKEN')
    client.chat_postMessage(
        channel='scripts',
        text=f'{error_text}',
        icon_emoji = error_emoji,
        username = 'sitesnitch'
        )  

def check_sites(site):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
    }
    try:
        response = requests.get(site, headers = headers, timeout=60)
    except:
        send_to_slack(
            f'{site} ERROR getting response',
            0,
            )
    else:
        if not response.ok:
            send_to_slack(
                f'''{site} has error {response.status_code}
                ---------------------------------------
                {response.headers}''',
                 response.status_code
                )

def main():
    for site in site_list:
        check_sites(f'http://{site}')

if __name__ == '__main__':
    main()
