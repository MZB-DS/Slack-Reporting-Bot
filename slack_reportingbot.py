from slackclient import SlackClient
import time
from tabulate import tabulate
import datetime
import traceback
import sys
from datetime import datetime as dt
from sql_query_to_df import get_data

token="" #Enter here your slack user bot access token

slack_client = SlackClient(token)
RTM_READ_DELAY = 1  # 1 second delay between reading from RTM
EXAMPLE_COMMAND = 'getme help :- For supported features and commands'
START_WITH = 'getme' #Start of the slack bot command

allowed_users=['Mustafa Bohra',"Mohammad","Kshitij"] #Enter the slack username of those to whom you want to give access of this bot.

def slack_connection():  
  slack_client.rtm_connect()
  try:
    while True:
      command, channel = parse_bot_commands(slack_client.rtm_read())
      if command:
         handle_command(command, channel)
      time.sleep(RTM_READ_DELAY)
  except:    
    slack_connection()

def parse_bot_commands(slack_events):

  for event in slack_events:
    if event["type"] == "desktop_notification" and event['subtitle'] in allowed_users:
        
      with open("Generated_Logs.csv", 'a') as newFile: # The file "Generated_Logs.csv" will store the time, user and command for every entered command.
        newFileWriter = csv.writer(newFile)
        newFileWriter.writerow(
            [event['subtitle'], event['content'], datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
      return event["content"], event["channel"]
  return None, None


def handle_command(command, channel):

  default_response = "Not sure what you mean. Try typing *{}* for help.".format(EXAMPLE_COMMAND)

  response = None
  if command.startswith(START_WITH):
      response = reports(command)

  else:
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=response or default_response
    )

def reports(query):
  try:  

    if 'help' in query:
      help_section='''getme people_info <city>: Fetches people's information which lives in given city.''' # This is the help menu where you can describe all the commands and their respective features.
      return help_section

    elif 'people_info' in query:
      city=query.split(' ')[2]
      queries = "select name, address, contact, email, city from people_information where city='{}';".format(city) # Enter your sql query here

      output = pretty_format(queries,'people_info')
      if output:
        return output

      return "No Data against this city. Please cross-check city spelling once."

  except Exception:
    print(traceback.format_exc())
    return "Invalid syntax please Try *{}* for help".format(EXAMPLE_COMMAND)

def pretty_format(queries, flag):

  if flag=='people_info':
    column_names = ["Name", "Address", "Contact", "Email", "City"] #Column names for your output dataframe after parsing your
    df = get_data(queries, column_names)

  text = tabulate(df, headers='keys', tablefmt='psql') #The tabulate package helps us convert a dataframe into sql table like format. This will help us visualise better in the bot chat window.

  text = "```" +str(text)+ "```"
  return text

slack_connection()

