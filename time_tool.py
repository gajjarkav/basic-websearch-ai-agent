# any time related tools are described here
import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
# i am using this module for create custom tool
from langchain_core.tools import tool

@tool
def get_current_time(location : str | None = None) -> str:
    """
    if user entered any location tool will first find timezone and then provide time
    or
    if user just ask time without any specified location it will return device time
    """
    if location :
        try :
            time_zone = ZoneInfo(location)
            current_time_in_tz = datetime.datetime.now(time_zone)
            return current_time_in_tz.strftime("%A %B %d, %Y %I:%M:%S %p (%Z)")
        except ZoneInfoNotFoundError:
            return f"Sorry I couldn't fetch the timezone for {location} can you try again with a different city or state which is near by your location"
    else :
    # here we display time with user's device current local time
        now_local_time = datetime.datetime.now()
        return now_local_time.strftime("%A %B %d, %Y %I:%M:%S %p (%Z)")
