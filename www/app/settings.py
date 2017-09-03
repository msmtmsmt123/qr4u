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
UPLOAD_FOLDER = "/tmp"
ALLOWED_EXTENSIONS = set(['.txt', '.pdf', '.doc', '.docx'])
# due to mongo by default allows only 16 Mb
MAX_UPLOAD_FILE_SIZE = 10 * 1024 * 1024
# utilized to send via 3rd party smtp
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 465

SITE_DOMAIN = "transburo.org"
NO_REPLY_EMAIL = "noreply@" + SITE_DOMAIN

# those e-mails are used to receive messages from request and contact form
#CONTACT_EMAIL = "contact@" + SITE_DOMAIN
CONTACT_EMAIL = "garbagefenix@gmail.com"
REQUEST_EMAIL = "request@" + SITE_DOMAIN

DB_NAME = "translate_bureau_www"

# chronopay settings
CHRONOPAY_PRODUCT_ID = "007985-0001-0001"
CHRONOPAY_SHARED_SEC = "kQ75gc0yZau8zO25"
CHRONOPAY_PAYMENT_URL = "https://payments.chronopay.com/"
CHRONOPAY_SUCCESS_URL = "http://transburo.org/payment-success/"
CHRONOPAY_FAILURE_URL = "http://transburo.org/payment-failure/"
CHRONOPAY_MIN_AMOUNT = 1
CHRONOPAY_MAX_AMOUNT = 100000




