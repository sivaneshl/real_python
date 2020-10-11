import pymsteams

# Add an incoming webhook to a Teams channel:
# Navigate to the channel where you want to add the webhook and select (•••) More Options from the top navigation bar.
# Choose Connectors from the drop-down menu and search for Incoming Webhook.
# Select the Configure button, provide a name, and, optionally, upload an image avatar for your webhook.
# The dialog window will present a unique URL that will map to the channel. Make sure that you copy and save the URL—you will need to provide it to the outside service.
# Select the Done button. The webhook will be available in the team channel.

my_teams_message = pymsteams.connectorcard("<Microsoft Webhook URL>")
my_teams_message.text("testing the webhook again")
my_teams_message.send()