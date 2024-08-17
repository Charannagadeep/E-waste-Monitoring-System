from datetime import datetime, timedelta

class EWasteMonitor:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, purchase_date, lifespan_years, category):
        item = {
            "name": item_name,
            "purchase_date": datetime.strptime(purchase_date, "%Y-%m-%d"),
            "lifespan_years": lifespan_years,
            "end_of_life": datetime.strptime(purchase_date, "%Y-%m-%d") + timedelta(days=lifespan_years * 365),
            "category": category
        }
        self.items.append(item)

    def show_items(self):
        for item in self.items:
            print(f"Item: {item['name']}, Category: {item['category']}, Purchased on: {item['purchase_date'].date()}, End of Life: {item['end_of_life'].date()}")

    def check_for_replacement(self):
        today = datetime.today()
        for item in self.items:
            remaining_days = (item['end_of_life'] - today).days
            if remaining_days <= 0:
                print(f"Alert: {item['name']} needs replacement.")
            else:
                print(f"{item['name']} has {remaining_days} days remaining until replacement.")

    def show_recycling_options(self):
        recycling_guidelines = {
            "Computers": "Drop off at a local electronic waste collection center.",
            "Mobile Devices": "Use a mobile recycling kiosk or mail-in program.",
            "Office Equipment": "Contact local office supply stores for recycling options."
        }
        for item in self.items:
            print(f"{item['name']}: {recycling_guidelines.get(item['category'], 'Visit your local recycling center.')}")
