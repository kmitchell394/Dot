import win32com.client as win32
import time

timestr = time.strftime("%m-%d-%y")
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'k.mitchell@teammodern.com'
mail.Subject = 'Dot ' + timestr
mail.Body = ""
#mail.HTMLBody = '<h2>HTML Message body</h2>' #this field is optional

# To attach a file to the email (optional):
attachment = "D:\\Dot\\Dot EDI\\Dot "+timestr+".xlsx"
mail.Attachments.Add(attachment)

mail.Send()