from datetime import datetime
import pytz  # for handling time zones

# Get the current date and time
current_datetime = datetime.now(pytz.timezone('Asia/Kolkata'))

# Format the date as per the specified format
formatted_date = current_datetime.strftime("%a %b %d %H:%M:%S %Z %Y")

# Print the formatted date
print("Current Date:", formatted_date)
