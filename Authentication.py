from robin_stocks import robinhood


stocks = ["ZSC"]



class DummyStrategy:
    def __init__(self, username, password):
        try:
            robinhood.login(username=username, password=password,pickle_path="/home/ubuntu/robin_tokens")
        except:
            mfa_code = input("Enter your mfa code here: ")
            robinhood.login(username=username, password=password,mfa_code=mfa_code,pickle_path="/home/ubuntu/robin_tokens")

    def run(self):
        for stock in stocks:
            try:
                stock_price = robinhood.get_latest_price(stock)

                if stock_price:
                    half_stock_price = round(float(stock_price[0]) / 2, 2)

                    order = robinhood.order_buy_limit(
                        symbol=stock, quantity=1, limitPrice=half_stock_price)

                    if order:
                        print(f"Order was placed for {stock}")
                    else:
                        print(f"Order was not placed for {stock}")

            except Exception as e:
                print(f"Error occurred while placing the order for {stock} with error : {e}")


if __name__ == "__main__":

    username = "username"
    password = "password"

    strategy = DummyStrategy(username=username, password=password)
    strategy.run()