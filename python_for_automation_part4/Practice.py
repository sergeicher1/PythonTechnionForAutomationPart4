# ------------------------------------------------------------------------------------------------
# -- coding                                   | utf-8
# -- Author                                   | Sergei Chernyahovsky
# -- Site                                     | https://www.zero-to-hero.dev/
# -- Favorite Quote                           | “Always code as if the guy who ends up
#                                                   maintaining your code will be a violent
#                                                       psychopath who knows where you live”
# -- Language                                 | Python
# -- Version                                  | 3.09
# -- Description                              | # This is a sample Python script for Learning Modules #
# -- Modules                                  | # os,time, datetime, shutil,subprocess #
# צרו תכנית הבודקת תקשורת עם מחשב אחר באמצעות  PING וכותבת תוצאות לקובץ טקסט
# התכנית תרוץ ותשלח פינג לכתובת מחשב לפי נתונים שיקלטו על ידי INPUT
#
# הנחיות:
#  להשתמש במודולים שלמדנו SUBPROCESS TIME
# הגדרת משתנים, פונקציה הקולטת נתונים מהמשתמש (כתובת היעד)
# פונקציה שמקבלת יעד לשליחת פינג ומבצעת בהתאם.
# תכנית עיקרית שבודקת פינג ליעד וקוראת לפונקציות בהתאם

# Usage Example
# For fast show uncomment and run the program
# ------------------------------------------------------------------------------------------------

""" Using with open """
import subprocess

def ping_and_save_results():
    # Get IP address or hostname from the user
    address = input("Enter the IP address or hostname to ping: ")

    # Run ping command with 4 requests (for Windows)
    result = subprocess.run(f"ping -n 4 {address}", shell=True, capture_output=True, text=True)

    # Save the ping output to a text file
    with open("ping_results.txt", "w", encoding="utf-8") as file:
        file.write(result.stdout)

    print("Ping test completed. Results saved to ping_results.txt")

if __name__ == "__main__":
    ping_and_save_results()


''' Using subprocess'''
import subprocess
import time

# Function to get target address from the user
def get_target_address():
    address = input("Enter the IP address or hostname to ping: ")
    return address

# Function to perform ping and save output to a file
def ping_and_save(address):
    # Create the command with output redirection
    command = f"ping -n 4 {address} > ping_results.txt"

    print(f"Pinging {address}...\nPlease wait.")
    time.sleep(1)  # Small delay for user experience

    # Run the ping command and redirect output to a file
    subprocess.run(command, shell=True)

    print("Ping completed. Results saved to 'ping_results.txt'.")

# Main program
if __name__ == "__main__":
    target = get_target_address()
    ping_and_save(target)
