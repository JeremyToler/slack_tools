# GREPY 
example use case:

```cat oci/oci.log | grep -v '{"code": "InternalError", "message": "Out of host capacity."}' | python3 slack_tools/gre.py```

If the log returns any output other than the out of capacity error I will get a slack notification. 
In my case the script generating the log file runs every two minutes, so I can add the above line to my crontab and run it every 10 min and no longer need to log into the server to see if there is finally capacity. 

# Site Snitch
Update the following line to include all web sites you want to test. 
```site_list = ['studiopeaches.com', 'httpbin.org/status/400']```


# How to use these scripts

You will need to make a slack bot:

- Go to https://api.slack.com/apps/
- Click Create New App and follow the wizard
- Go to your app and go to ‘OAuth & Permissions’
- Under Scopes give the bot the following permissions chat:write, chat:write.customize, chat:write.public
- Update token='YOUR-AUTH-TOKEN' in the script
- Add the bot to your slack channel. 

You can customize further by changing the username, icon_emoji, and channel under ```client.chat_postMessage```
