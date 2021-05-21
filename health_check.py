#!/usr/bin/env python3

import emails
import shutil
import psutil
import time
import socket
import os

def email_status(subject):
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ["USER"])
  body = "Please check your system and resolve the issue as soon as possible."
  message = emails.generate_email(sender, receiver, subject, body, False)
  emails.send_email(message)

def main():
  cpu_usage = psutil.cpu_percent(1)
  cpu_status = cpu_usage > 80

  disk_usage = shutil.disk_usage("/").used / shutil.disk_usage("/").total * 100
  disk_status = disk_usage < 20

  memory_usage = psutil.virtual_memory().available / 1024**2
  memory_status = memory_usage > 500

  network_status = socket.gethostbyname('localhost') != "127.0.0.1"

  if cpu_status:
    print("Error - CPU usage is over 80%")
    email_status("Error - CPU usage is over 80%")

  if disk_status:
    print("Error - Available disk space is less than 20%")
    email_status("Error - Available disk space is less than 20%")

  if not memory_usage:
    print("Error - Available memory is less than 500MB")
    email_status("Error - Available memory is less than 500MB")

  if network_status:
    print("Error - localhost cannot be resolved to 127.0.0.1")
    email_status("Error - localhost cannot be resolved to 127.0.0.1")

if __name__ == "__main__":
  main()
