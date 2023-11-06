<div align="center">
<img src="https://i.imgur.com/sAq1GKK.png" height="250" >  
<h1 align="center">Bulk Mail Sender</h1>
<strong><i>A simple yet powerful tool to send email to everyone at same time.</i></strong>
<br>
<br>
<a href="https://www.python.org/">
<img src="https://img.shields.io/badge/MADE%20WITH-PYTHON-red?logoColor=red&logo=Python&style=for-the-badge">
</a>
<a href="/stargazers">
<img src="https://img.shields.io/github/stars/CYCNO/bulk-mail-sender?logo=adguard&style=for-the-badge">
</a>
<a href="/graphs/contributors">
<img src="https://img.shields.io/github/contributors/CYCNO/bulk-mail-sender?style=for-the-badge&color=green&logo=GitHub">
</a>
</div>

---
# Features
- Send individualized emails with recipient's names.
- Easy setup using JSON files for data and credentials.
- Modify email templates and placeholders.
- Script automates sending process.
- Receive success notifications for each email.
- No Limit of usage
- Secure email transmission via SSL encryption.
- Included guide for step-by-step usage.
- Modular and maintainable code structure.

# Getting Started

Follow these steps to use the code:

**1. Clone or download this repository to your local machine.**

  For Cloning The repository
  ```bash
  git clone https://github.com/CYCNO/bulk-mail-sender
  ```

**2. Configure the email and template data:**
   - Replace sample recipient data in `data/recipient_data.json` with your recipients' details.
   - Enter your Gmail credentials (email and app password) in `data/credential.json`. **[How to get your app password](https://www.youtube.com/watch?v=J4CtP1MBtOE)**
   - Personalize the email template in `data/email_template.txt`. 
   - **Note:** Do not modify the `{name}` placeholder.

**3. Run the script:**
   - Open a terminal or command prompt.
   - Navigate to the script's directory using `cd`.
   - Execute the script with `python bulk_mail.py`.

**4. Emails will be sent automatically, personalized with recipients' names using the `{name}` placeholder.**

## Support
Star ⭐ this repository! Your support will greatly boost its visibility and attract more users.

## Contributors
### <a href="https://github.com/CYCNO"><img src="https://avatars.githubusercontent.com/u/90704569?v=4" alt="CYCNO" width="50" height="50" style="border-radius: 50%;"></a>
