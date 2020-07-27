# Slack_chatbot
This repository contains python code for programming slack user bot. Slack is both free and paid messenger. The basic idea behind this code is to provide a setup where our python program is ready to receive whatever command is given to the slack user bot and also what to reply back to the bot. The feature provided in the code is to receive the command from bot in particular syntax, execute a sql query based on the received command and reply the sql out put in a proper table format back to the slack user bot.

## How to use this code
1. Sign in to the slack.
2. Create a slack app from this link "https://api.slack.com/apps/new" to recieve an API token for your bot.
3. Provide proper mysql host ip, username, password and any database name in ```sqlquery_to_df.py``` file.
4. Provide in ```slack_reportingbot.py```, your slack bot api token in 'token' variable, your mysql select query and the respective column names for your output dataframe.
5. Default sleeping time for bot is 1sec. If you want to increase or reduce that do make change in the 'RTM_READ_DELAY' variable.
6. In order for the bot to recognise when an approprite command starts, we have programmed it to check and behave whenever a command starts with "getme". If you want to change the start command to something like "giveme", "do", "get", etc you can edit it in the 'START_WITH' variable.
7. The code also handles to which user we need to provide access to the slack bot. Enter the username of the slack users in the "allowed_users" list to whom we need to provide the access. Anyone other than these users tries to provide command, bot won't respond.
8. Code generates a "Generated_Logs.csv" file, where we log: The datetime at which command entered, user which entered the command and the command itself.
9. Execute ```slack_reportingbot.py```.
10. Now go to the slack user bot and type "getme help". This will enlist all the features and commands you mentioned in the help section. For this code, enter the command ```getme people_info pune```. This will give us the output of the entered sql query in the sql table format. We have used tabulate package for that.

## Future Features
Adding the feature of responding with csv, xlsx or txt file to the bot.

## Dependencies
- Python3 any version
- Slack account
- python package: slackclient==1.3.1, time, tabulate==0.8.3, datetime, traceback
```pip3 install slackclient==1.3.1 tabulate==0.8.3 traceback```
