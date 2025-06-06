import stripe
from django.conf import settings
from decouple import config

settings.configure()
stripe.api_key = config('STRIPE_SECRET_KEY')
print(stripe.api_key)



