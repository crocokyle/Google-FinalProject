#!/usr/bin/env python3

import shutil
import psutil
import time
import os

def email_status(subject):
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ["USER"])
  body = "Please check your system and resolve the issue as soon as possible."
  message = emails.generate_email(sender, receiver, subject, body)
  emails.server_email(message)

def main():
  cpu_usage = psutil.cpu_percent(1)
  cpu_status = spu_usage > 80

  disk_usage = shutil.disk_usage("/").used / shutil.disk_usage("/").total * 100
  disk_status = disk_usage > 20

  memory_usage = psutil.virtual_memory().available / 1024**2
  memory_status = memory_usage > 500

  network_status = socket.gethostbyname('localhost') == "127.0.0.1"

  if not cpu_status:
    email_status("Error - CPU usage is over 80%")

  if not disk_status:
    email_status("Error - Available disk space is less than 20%")

  if not memory_usage:
    email_status("Error - Available memory is less than 500MB")

  if not network_status:
    email_status("Error - localhost cannot be resolved to 127.0.0.1")
