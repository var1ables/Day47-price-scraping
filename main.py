from bs4 import BeautifulSoup
import requests
import smtplib

#Product URL you're trying to keep update on
URL ='https://www.amazon.com/dp/B08164VTWH/ref=cm_sw_em_r_mt_dp_ASY15TZ3W96V00MCC12D?_encoding=UTF8&psc=1'


#headers to get past the bot detector on the website
header = {'User-Agent':'Defined', 'Accept-Language':'en-US,en;q=0.5'}

#The email account and the password to the account you'll be sending this to
my_email = 'YOUR_EMAIL_ACCOUNT@HERE'
my_pass = 'YOUR_PASSWORD_HERE'

#your strike price
set_price = '$400.00'

#getting hold of the product website in HTML text
response = requests.get(URL,headers=header)
product_price_website = response.text

#setting up soup to read HTML
soup = BeautifulSoup(product_price_website, 'html.parser')

#scrapping the price from soup
price = soup.find(name='span', class_='a-offscreen').getText()

#scrapping the product name from soup
product = soup.find(name='span', class_='a-size-large product-title-word-break').getText()


#determining if you should send an email to alert yourself to the deal
if price < set_price:
    msg = f'Hey you should really look at this {price} for {product} at {URL}'
    with smtplib.SMTP('YOUR.EMAIL.HOST') as connection:
        connection.starttls()
        connection.login(my_email, my_pass)
        connection.sendmail(from_addr=my_email, to_addrs=my_email)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg = msg
        )