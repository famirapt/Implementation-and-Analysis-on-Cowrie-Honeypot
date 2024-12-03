import os
import json

# Directory containing Cowrie JSON log files
log_dir = '/home/cowrie/cowrie/var/log/cowrie'
# Function to parse Cowrie JSON log data
def parse_json_log(log_data):
  timestamp = log_data['timestamp']
  ip = log_data['src_ip']
  event_id = log_data['eventid']
  username = log_data.get('username', '') # 'username' may not exist in all log entries
  password = log_data.get('password', '') # 'password' may not exist in all log entries
  message = log_data['message']
  cmd = log_data.get('CMD', '') # 'CMD' may not exist in all log entries
  sensor = log_data.get('sensor', '') # 'sensor' may not exist in all log entries
  input_data = log_data.get('input', '') # 'input' may not exist in all log entries
  print("Timestamp:", timestamp)
  print("IP:", ip)
  print("Event ID:", event_id)
  if username:
    print("Username:", username)
  if password:
    print("Password:", password)
  print("Message:", message)
  print("Command:", cmd)
  print("Sensor:", sensor)
  print("Input:", input_data)
  print() # Add a newline for better readability

# Iterate through files in the directory
for filename in os.listdir(log_dir):
  if filename.endswith('.json'):
    # If file is JSON, read and parse it
    with open(os.path.join(log_dir, filename), 'r') as file:
      logs = file.readlines()
      for log_line in logs:
        log_data = json.loads(log_line)
        parse_json_log(log_data)
