import win32com.client
import os
from datetime import datetime, timedelta

outlook = win32com.client.Dispatch("Outlook.Application")
mapi = outlook.GetNamespace("MAPI")

for account in mapi.Accounts:
    print(account.DeliveryStore.DisplayName)

inbox = mapi.GetDefaultFolder(6).Folders("Dot")

messages = inbox.Items

received_dt = datetime.now() - timedelta(hours=35)
received_dt = received_dt.strftime('%m/%d/%Y %H:%M %p')
messages = messages.Restrict("[ReceivedTime] >= '" + received_dt + "'")
messages = messages.Restrict("[SenderEmailAddress] = 'customeredi@dotfoods.com'")
messages = messages.Restrict("[Subject] = 'Dot Foods/Modern Distributing ASN'")

#Let's assume we want to save the email attachment to the below directory
outputDir = r"D:\Dot\Dot EDI"
try:
    for message in list(messages):
        try:
            s = message.sender
            for attachment in message.Attachments:
                attachment.SaveASFile(os.path.join(outputDir, attachment.FileName))
            print(f"attachment {attachment.FileName} from {s} saved")
        except Exception as e:
            print("error when saving the attachment:" + str(e))
except Exception as e:
        print("error when processing emails messages:" + str(e))

print("main done")

exec(open("D:\Programs\Dot\MergeCSV.py").read())
print("Merge CSV - Done")
exec(open("D:\Programs\Dot\DropColumns.py").read())
print("DropColumns - Done")
exec(open("D:\Programs\Dot\Concat.py").read())
print("Concat - Done")
exec(open("D:\Programs\Dot\HouseCleaning.py").read())
print("House Cleaning - Done")
exec(open("D:\Programs\Dot\ExcelConversion.py").read())
print("Excel Conversion - Done")
exec(open("D:\Programs\Dot\EmailExcel.py").read())
print("Dot Emailed - Done")
exec(open("D:\Programs\Dot\Archive.py").read())
print("Files Moved - Done")