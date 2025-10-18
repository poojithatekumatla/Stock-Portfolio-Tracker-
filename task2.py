
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 130
}

portfolio = {}
total_investment = 0

print("📈 Welcome to the Stock Portfolio Tracker!")
print("Available stocks and their prices (USD):")
for stock, price in stock_prices.items():
    print(f"  {stock}: ${price}")

print("\nEnter your stocks (type 'done' when finished):")

while True:
    stock_name = input("\nEnter stock symbol (e.g., AAPL): ").upper()
    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("❌ Invalid stock symbol! Choose from the list above.")
        continue

    try:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("❌ Quantity must be positive.")
            continue
    except ValueError:
        print("❌ Please enter a valid number for quantity.")
        continue

    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

print("\n🧾 Portfolio Summary:")
for stock, qty in portfolio.items():
    investment = stock_prices[stock] * qty
    total_investment += investment
    print(f"{stock} - {qty} shares × ${stock_prices[stock]} = ${investment}")

print("\n💰 Total Investment Value: $", total_investment)

save_option = input("\nDo you want to save the result to a file? (yes/no): ").lower()
if save_option == "yes":
    filename = "portfolio_summary.txt"
    with open(filename, "w") as f:
        f.write("Stock Portfolio Summary\n")
        f.write("-----------------------\n")
        for stock, qty in portfolio.items():
            f.write(f"{stock}: {qty} × ${stock_prices[stock]} = ${stock_prices[stock]*qty}\n")
        f.write(f"\nTotal Investment: ${total_investment}\n")
    print(f"✅ Portfolio saved to '{filename}'")

print("\n✅ Thank you for using the Stock Portfolio Tracker!")
