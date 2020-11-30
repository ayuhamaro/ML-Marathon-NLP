import re
import pandas as pd
import email

#讀入資料文本
with open('sample_emails.txt', 'r', encoding="utf8", errors='ignore') as f:
    sample_corpus = f.read()

print(sample_corpus)


#讀取寄件者資訊
pattern = r'From:.*'

match = re.findall(pattern, sample_corpus)

print(match)


#只讀取寄件者姓名
pattern = r'\".*\"'

for info in match:
    print(re.search(pattern, info).group())


#只讀取寄件者電子信箱
pattern = r'\w\S*@.*\b'

for info in match:
    print(re.search(pattern, info).group())


#只讀取電子信箱中的寄件機構資訊
pattern = r'(?<=@)\w\S*(?=\.)' #\b 是因為結尾一定為com

for info in match:
    print(re.search(pattern, info).group())


#結合上面的配對方式, 將寄件者的帳號與機構訊返回
address = re.findall(r'From:.*', sample_corpus)
for ad in address:
    for line in re.findall(r'\w\S*@.*(?=\.)', ad):
        username, domain_name = re.split("@", line)
        print("{}, {}".format(username, domain_name))


#讀取與切分Email
with open('all_emails.txt', 'r', encoding="utf8", errors='ignore') as f:
    corpus = f.read()

emails = re.split(r"From r", corpus, flags=re.M)
emails = emails[1:]
print(len(emails))


#從文本中擷取所有寄件者與收件者的姓名和地址
emails_list = []

for mail in emails[:10]:
    emails_dict = dict()

    sender = re.search(r"From:.*", mail)

    if sender is not None:
        sender_mail = re.search(r"\w\S*@.*\b", sender.group())
        sender_name = re.search(r"(?<=\").*(?=\")", sender.group())
    else:
        sender_mail = None
        sender_name = None

    if sender_mail is not None:
        emails_dict["sender_email"] = sender_mail.group()
    else:
        emails_dict["sender_email"] = sender_mail

    if sender_name is not None:
        emails_dict["sender_name"] = sender_name.group()
    else:
        emails_dict["sender_name"] = sender_name

    recipient = re.search(r"To:.*", mail)

    if recipient is not None:
        r_email = re.search(r"\w\S*@.*\b", recipient.group())
        r_name = re.search(r"(?<=\").*(?=\")", recipient.group())
    else:
        r_email = None
        r_name = None

    if r_email is not None:
        emails_dict["recipient_email"] = r_email.group()
    else:
        emails_dict["recipient_email"] = r_email

    if r_name is not None:
        emails_dict["recipient_name"] = r_name.group()
    else:
        emails_dict["recipient_name"] = r_name

    date_info = re.search(r"Date:.*", mail)

    if date_info is not None:
        date = re.search(r"\d+\s\w+\s\d+", date_info.group())
    else:
        date = None

    if date is not None:
        emails_dict["date_sent"] = date.group()
    else:
        emails_dict["date_sent"] = date

    subject_info = re.search(r"Subject: .*", mail)

    if subject_info is not None:
        subject = re.sub(r"Subject: ", "", subject_info.group())
    else:
        subject = None

    emails_dict["subject"] = subject

    try:
        full_email = email.message_from_string(mail)
        body = full_email.get_payload()
        emails_dict["email_body"] = body
    except:
        emails_dict["email_body"] = None

    emails_list.append(emails_dict)

emails_df = pd.DataFrame(emails_list)
print(emails_df)