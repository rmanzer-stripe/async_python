# Basic Async Python Example

This repo contains a simple script that uses `stripe-python`s new async functions to make multiple customer and subscriptions quickly and efficiently.

## Usage

### Install Requirements
First create a local directory, create a python virutal environment, and install the requirements

```sh
$ mkdir async_python && cd async_python

$ python -m venv .venv

$ source .venv/bin/activate

$(.venv) pip install -r requirements.txt
```

### Configure `.env`

Create a `.env` file with your Stripe secret key.  The Python file will attempt to load this variable from the OS when initializing the `StripeClient`

```sh
echo "SECRET_KEY=sk_test_XXXXXXXX" >> .env
```

### Set a Price ID

In `async_stripe.py` there is a `RECURRING_PRICE` constant that you need to replace with a valid recurring Price ID from your account.

```python
REUCRRING_PRICE="price_XXXXXXXXX"  # Replace with your price id
```

### Run the file

Once all of those steps are completed, you are ready to run the file.  

In the terminal, run the following (with your `.venv` activated, of course).

```sh
python async_python.py
```

You will see a message printed out to the console when each object is created. 

For more insight into how the `asyncio` package and Aysnc design patterns in Python can be implemented, I recommend [this article](https://realpython.com/async-io-python/).