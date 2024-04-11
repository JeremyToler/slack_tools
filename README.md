# GREPY 
example use case:

```cat oci/oci.log | grep -v '{"code": "InternalError", "message": "Out of host capacity."}' | python3 slack_tools/gre.py```

If the log returns any output other than the out of capacity error I will get a slack notification. 
In my case the script generating the log file runs every two minutes, so I can add the above line to my crontab and run it every 10 min and no longer need to log into the server to see if there is finally capacity. 

You will need to make a slack bot:

   1. Go to https://api.slack.com/apps/
   2. Click Create New App and follow the wizard
   3. Go to your app and go to ‘OAuth & Permissions’
   4. Under Scopes give the bot the following permissions chat:write, chat:write.customize, chat:write.public
   5. Update token='YOUR-AUTH-TOKEN' in the script
   6. Add the bot to your slack channel. 

You can customize further by changing the username, icon_emoji, and channel under ```client.chat_postMessage```
