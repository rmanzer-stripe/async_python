import os
import asyncio

from dotenv import load_dotenv

import stripe

load_dotenv()
SK = os.getenv('SECRET_KEY', False)

if not SK:
    raise Exception('Secret key not found')

SK = str(SK)
http_client = stripe.HTTPXClient(allow_sync_methods=True)
client=stripe.StripeClient(SK, http_client=http_client)


REUCRRING_PRICE="price_XXXXXXXX"  # Replace with your price id

async def create_customer_subscription(email):
    customer_kwargs = {
        'email': email,
        'name': 'Rudolpho Hedgehog',
        'payment_method': 'pm_card_visa',
        'invoice_settings': {
            'default_payment_method': 'pm_card_visa',
        },
    }
    customer = await client.customers.create_async(
        params=customer_kwargs # type: ignore
        )
    print("Customer created")
    sub_kwargs = {
        'customer': customer.id,
        'items': [{'price': REUCRRING_PRICE}],
    }
    subscription = await client.subscriptions.create_async(
       params=sub_kwargs # type: ignore
    )
    print("Subscription created")
    return subscription

async def main():
    emails = ['test!@bufo.io', 'test2@bufo.io', 'test3@bufo.io']
    await asyncio.gather(*[create_customer_subscription(email) for email in emails])

if __name__ == '__main__':
    asyncio.run(main())