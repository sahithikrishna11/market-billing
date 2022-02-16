# market-billing
Task - https://gist.github.com/jbartels/d75a9f5282abebe071694723a5f25f0e

Billing Overview: This app depends on DJango frameworl.

When the app is run users can add items from list available.
Coupons applied will be updated automatically once the user hits enter or click the "submit" button.

Implemented all coupons - BOGO, APPL, CHMK, APOM

Created two tables in the database - Product(Product_id, product_price, product_name), Discount(product_id, discount_id, discount_price)

# Pre-requisites

  1. Docker
  
# How to execute
Run the commands in powershell.

Build the docker image using the Dockerfile provided and following command:
~docker build -t billing:v1 .

Run the docker container using following command.

~docker run -itd -p 8000:8000 billing:v1

Django app will be up and running. Open the browser and hit http://localhost:8000/billing/ to see billing app. You can add new items from UI and the list will be automatically updated and coupons will be automatically applied. and final bill would be displayed once the "submit" button is entered

After cloning the repo locally, run test cases locally using below command:

python manage.py test

Once the app is up and running - ex - (https://user-images.githubusercontent.com/99655822/154225562-a8abf772-2516-4958-8c01-2fdb4209ca11.png)


