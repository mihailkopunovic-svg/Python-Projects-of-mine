import webbrowser
import serpapi

API_KEY = "ccf1efcd1b9e927eb37752d516a6705b843060bc43d2ce259d2b15320a77d714"

ALLOWED_SITES = ["goat.com", "nike.com", "champssports.com", "footlocker.com", "stockx.com"]

def get_cheapest(sneaker, max_price, size):
    client = serpapi.Client(api_key=API_KEY)

    results = client.search({
        "engine": "google_shopping",
        "q": f"{sneaker} sneaker size {size}",
        "tbs": "p_ord:p",
        "num": 20,
    })

    print("\n--- Raw results from SerpApi ---")
    for item in results.get("shopping_results", []):
        print(f"Store: {item.get('source')} | Price: {item.get('price')} | Title: {item.get('title')[:40]}")
    print("--------------------------------\n")

    filtered = []
    for item in results.get("shopping_results", []):
        source = item.get("source", "").lower()
        price_str = item.get("price", "").replace("$", "").replace(",", "").strip()

        if not any(site in source for site in ALLOWED_SITES):
            continue

        try:
            price = float(price_str)
            if price <= max_price:
                filtered.append({
                    "title": item.get("title"),
                    "price": price,
                    "source": item.get("source"),
                    "link": item.get("link"),
                })
        except ValueError:
            continue

    return sorted(filtered, key=lambda x: x["price"])


question = input("Would you like to find a sneaker? (yes/no) ").strip().lower()

if question == "yes":
    sneaker = input("What sneaker are you looking for? ").strip()
    size = input("What is your shoe size? (e.g. 10, 10.5) ").strip()
    max_price = float(input("What is your max budget? (e.g. 200) $").strip())

    print(f"\nSearching for cheapest {sneaker} in size {size}...\n")
    deals = get_cheapest(sneaker, max_price, size)

    if deals:
        cheapest = deals[0]
        print(f"Cheapest: {cheapest['title']}")
        print(f"Price:    ${cheapest['price']:.2f}")
        print(f"Store:    {cheapest['source']}")
        print(f"Link:     {cheapest['link']}")

        if input("\nOpen in browser? (yes/no) ").strip().lower() == "yes":
            webbrowser.open(cheapest["link"])

        if len(deals) > 1:
            print("\nOther deals:")
            for deal in deals[1:5]:
                print(f"  ${deal['price']:.2f} — {deal['source']} — {deal['title']}")
    else:
        print("No results found within your budget from those sites.")
else:
    print("Okay, maybe next time!")