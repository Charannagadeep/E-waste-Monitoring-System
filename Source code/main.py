from e_waste_monitor import EWasteMonitor

def main():
    monitor = EWasteMonitor()
    
    # Sample data
    monitor.add_item("Laptop", "2022-01-15", 3, "Computers")
    monitor.add_item("Smartphone", "2021-05-10", 2, "Mobile Devices")
    monitor.add_item("Printer", "2020-11-20", 5, "Office Equipment")
    
    # Displaying registered items
    print("\nRegistered Items:")
    monitor.show_items()
    
    # Checking for replacements
    print("\nReplacement Alerts:")
    monitor.check_for_replacement()
    
    # Showing recycling options
    print("\nRecycling Options:")
    monitor.show_recycling_options()

if __name__ == "__main__":
    main()
