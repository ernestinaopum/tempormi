import datetime

# Your Unix timestamp
epoch = 1710502379

# Convert to a datetime object
timestamp = datetime.datetime.utcfromtimestamp(epoch)

# Format the datetime as a string
formatted_date = timestamp.strftime("%Y-%m-%d %H:%M:%S UTC")

print(f"The Unix timestamp {epoch} corresponds to: {formatted_date}")
