import time
# Initial dataset 
data = []

# Metrics (state)
metrics = {
    "count": 0,
    "sum": 0,
    "avg": 0
}

# Load initial data (FULL computation)
def load_data():
    global data, metrics
    data = [10, 20, 30, 40]

    metrics["count"] = len(data)
    metrics["sum"] = sum(data)
    metrics["avg"] = metrics["sum"] / metrics["count"]

    print("\n📦 Initial Data Loaded")
    display()


# Incremental update (DELTA)
def add_new_data():
    global data, metrics

    new_value = int(input("\nEnter new value: "))
    data.append(new_value)

    # Incremental update (NO full recompute)
    metrics["count"] += 1
    metrics["sum"] += new_value
    metrics["avg"] = metrics["sum"] / metrics["count"]

    print("⚡ Using Incremental Update (FAST)")

    print("✅ Incremental update done")
    display()


# Full recompute (for comparison)
def full_recompute():
    global metrics

    metrics["count"] = len(data)
    metrics["sum"] = sum(data)
    metrics["avg"] = metrics["sum"] / metrics["count"]

    print("🐢 Using Full Recompute (SLOW)")

    print("⚠️ Full recompute done")
    display()


# Display metrics
def display():
    print("\n📊 Metrics:")
    print("Count:", metrics["count"])
    print("Sum:", metrics["sum"])
    print("Average:", round(metrics["avg"], 2))


# Menu system
def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Load Initial Data")
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


# Run program
menu()