class CarNotFoundError(Exception):
    pass


class CarNotAvailableError(Exception):
    pass


class InvalidRentalDaysError(Exception):
    pass


class CarAlreadyAvailableError(Exception):
    pass


class InvalidChoiceError(Exception):
    pass


cars = {
    "CAR101": {
        "model": "Toyota Camry",
        "price_per_day": 2500,
        "available": True
    },
    "CAR102": {
        "model": "Honda City",
        "price_per_day": 1800,
        "available": True
    },
    "CAR103": {
        "model": "Hyundai Creta",
        "price_per_day": 2200,
        "available": False
    },
    "CAR104": {
        "model": "Mahindra Thar",
        "price_per_day": 3000,
        "available": True
    }
}


try:

    while True:

        print("\n========== CAR RENTAL SYSTEM ==========")
        print("1. View Cars")
        print("2. Rent a Car")
        print("3. Return a Car")
        print("4. Exit")
        print("=======================================")

        choice = input("Enter your choice: ")

        # =========================
        # VIEW CARS
        # =========================

        if choice == "1":

            print("\n========== AVAILABLE CARS ==========")

            for car_id, car in cars.items():

                if car["available"]:
                    status = "Available"
                else:
                    status = "Rented"

                print(
                    f"{car_id} - {car['model']} - "
                    f"₹{car['price_per_day']}/day - {status}"
                )

        # =========================
        # RENT A CAR
        # =========================

        elif choice == "2":

            try:

                car_id = input("Enter Car ID: ").strip().upper()

                if car_id not in cars:
                    raise CarNotFoundError(
                        "Car does not exist."
                    )

                if not cars[car_id]["available"]:
                    raise CarNotAvailableError(
                        "This car is currently unavailable."
                    )

                try:
                    days = int(
                        input("Enter number of days: ")
                    )

                except ValueError:
                    print(
                        "Error: Number of days must be a number."
                    )
                    raise

                if days <= 0:
                    raise InvalidRentalDaysError(
                        "Rental days must be greater than zero."
                    )

                price = cars[car_id]["price_per_day"]
                total_cost = price * days

            except CarNotFoundError as e:
                print(f"Error: {e}")

            except CarNotAvailableError as e:
                print(f"Error: {e}")

            except ValueError:
                print(
                    "Error: Please enter a valid number of days."
                )

            except InvalidRentalDaysError as e:
                print(f"Error: {e}")

            else:

                cars[car_id]["available"] = False

                print("\nCar rented successfully!")
                print(f"Car: {cars[car_id]['model']}")
                print(f"Days: {days}")
                print(f"Total Cost: ₹{total_cost}")

            finally:
                print("Rental operation completed.")

        # =========================
        # RETURN A CAR
        # =========================

        elif choice == "3":

            try:

                car_id = input("Enter Car ID: ").strip().upper()

                if car_id not in cars:
                    raise CarNotFoundError(
                        "Car does not exist."
                    )

                if cars[car_id]["available"]:
                    raise CarAlreadyAvailableError(
                        "This car has not been rented."
                    )

            except CarNotFoundError as e:
                print(f"Error: {e}")

            except CarAlreadyAvailableError as e:
                print(f"Error: {e}")

            else:

                cars[car_id]["available"] = True

                print("\nCar returned successfully!")
                print(f"Car: {cars[car_id]['model']}")

            finally:
                print("Return operation completed.")

        # =========================
        # EXIT
        # =========================

        elif choice == "4":

            print(
                "\nThank you for using our "
                "car rental system!"
            )
            break

        # =========================
        # INVALID CHOICE
        # =========================

        else:

            try:
                raise InvalidChoiceError(
                    "Invalid choice. "
                    "Please select 1, 2, 3, or 4."
                )

            except InvalidChoiceError as e:
                print(f"Error: {e}")


except Exception as e:
    print(f"Unexpected Error: {e}")