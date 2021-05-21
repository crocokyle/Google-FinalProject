#!/usr/bin/env python3

import reports
import emails
import os
import datetime

def parseData():

  desc_dir = "supplier-data/descriptions"
  item_collector = []

  for file in os.listdir(desc_dir):
    if file[-4:] == ".txt":
      with open(os.path.join(desc_dir, file), 'r') as f:
        content = f.readlines()
        item_collector.append("name: {}<br/>weight: {}<br/><br/>".format(content[0], content[1]))

  print("".join(item_collector))
  return "".join(item_collector)

if __name__ == "__main__":

  report_path = "/tmp/processed.pdf"
  report_title = "Processed on {}".format(datetime.date.today())
  report_data = parseData()

  reports.generate_report(report_path, report_title, data)

  sender = "automation@example.com"
  recipient = "student-02-35d77fd57627@example.com"
  subject = "Upload Comppleted - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detail list is attached to this email."
  message = emails.generate_email(sender, recipient, subject, body, report_path)

  emails.send_email(message)
