import csv

data = []

metrics = {
    "count": 0,
    "sum": 0,
    "avg": 0
}

# Load data from CSV
def load_data():
    global data, metrics
    data = []

    with open("data.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(int(row["value"]))

    # FULL computation
    metrics["count"] = len(data)
    metrics["sum"] = sum(data)
    metrics["avg"] = metrics["sum"] / metrics["count"]

    print("\n📦 Data Loaded from CSV")
    display()


# Add new data (DELTA)
def add_new_data():
    global data, metrics

    new_value = int(input("\nEnter new value: "))
    data.append(new_value)

    # Save to CSV (append)
    with open("data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([new_value])

    # Incremental update
    metrics["count"] += 1
    metrics["sum"] += new_value
    metrics["avg"] = metrics["sum"] / metrics["count"]

    print("⚡ Incremental Update (FAST)")
    display()


# Full recompute
def full_recompute():
    global metrics

    metrics["count"] = len(data)
    metrics["sum"] = sum(data)
    metrics["avg"] = metrics["sum"] / metrics["count"]

    print("🐢 Full Recompute (SLOW)")
    display()


# Display
def display():
    print("\n📊 Metrics:")
    print("Count:", metrics["count"])
    print("Sum:", metrics["sum"])
    print("Average:", round(metrics["avg"], 2))


# Menu
def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Load Data from CSV")
        print("2. Add New Data (Delta)")
        print("3. Full Recompute")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            load_data()
        elif choice == "2":
            add_new_data()
        elif choice == "3":
            full_recompute()
        elif choice == "4":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice")


menu()
