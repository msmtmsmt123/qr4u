#
# Update the settings as needed
#
TEMPLATE_DIR = "templates/"

# MailChimp settings to subscribe users after signup
MAILCHIMP_API_KEY = ""

# Find it on mailchimp.com via "settings" -> "list settings and unique id"
MAILCHIMP_LIST_ID = ""

# Use this switch to turn the MailChimp API calls on and off. Set to True only
# for testing and production. Set to False during development.
MAILCHIMP_ENABLED = False


EN_LOCALE = "en"
RU_LOCALE = "ru"
DEFAULT_LOCALE = EN_LOCALE

SITE_DOMAIN = "qr4u.online"
NO_REPLY_EMAIL = "noreply@" + SITE_DOMAIN

# those e-mails are used to receive messages from request and contact form
#CONTACT_EMAIL = "contact@" + SITE_DOMAIN
CONTACT_EMAIL = "noreply@qr4u.online"




