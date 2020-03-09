from requests.exceptions import HTTPError
from onesignalclient.app_client import OneSignalAppClient
from onesignalclient.notification import Notification

player_id = 'player_id_subcriber'
os_app_id = 'your_os_app_id'
os_apikey = 'your_os_apikey'

# Init the client
client = OneSignalAppClient(app_id=os_app_id, app_api_key=os_apikey)

# Creates a new notification
notification = Notification(os_app_id, Notification.DEVICES_MODE)
notification.include_player_ids = [player_id]  # Must be a list!

try:
    # Sends it!
    result = client.create_notification(notification)
except HTTPError as e:
    result = e.response.json()

print(result)
