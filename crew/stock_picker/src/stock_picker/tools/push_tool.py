from crewai.tools import tool
import os
import requests

@tool("send_push_notification")
def send_push_notification(message: str) -> str:
    """
    Use this tool to send a push notification to the user.
    Args:
        message: The message to send to the user
    Returns:
        The message that was sent to the user
    """
    pushover_user = os.getenv("PUSHOVER_USER")
    pushover_token = os.getenv("PUSHOVER_TOKEN")
    pushover_url = f"https://api.pushover.net/1/messages.json"
    payload = {
        "user": pushover_user,
        "token": pushover_token,
        "message": message,
    }
    result = requests.post(pushover_url, data=payload)
    return f"Push notification sent with API response code: {result.status_code}"