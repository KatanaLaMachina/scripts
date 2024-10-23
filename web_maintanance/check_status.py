import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def check_website_status(urls):
    working_websites = []
    not_working_websites = []

    for url in urls:
        try:
            response = requests.get(url, timeout=30)  # Timeout after 10 seconds
            if response.status_code == 200:
                working_websites.append(url)
            else:
                not_working_websites.append(url)
        except requests.RequestException:
            not_working_websites.append(url)

    return working_websites, not_working_websites

def send_email(subject, body, to_email):
    from_email = 'blacknihojini@gmail.com'
    app_password = 'yzmc blom mpst mnsk'

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(from_email, app_password)
            server.send_message(msg)
            print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email: {e}')

def format_report(working_websites, not_working_websites):
    report = "Working websites:\n"
    report += "\n".join(working_websites)
    report += "\n\nWebsite not working:\n"
    report += "\n".join(not_working_websites)
    return report

# Main Program
if __name__ == "__main__":
    urls = [
        "https://tngsolutions.co.za/",
        "https://www.simboti.digital/",
        "http://www.tambanuka.co.zw/",
        "https://kago.digital/"
    ]

    working_websites, not_working_websites = check_website_status(urls)
    report = format_report(working_websites, not_working_websites)

    # Send email
    subject = 'Websites Report'
    to_email = 'iamkeadevs@gmail.com'
    send_email(subject, report, to_email)
