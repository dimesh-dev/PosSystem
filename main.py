from pos import POS


def main():
    pos = POS()
    while True:
        print("\nDM Sugar Crafts POS System:")
        print("1. Add Item")
        print("2. Display Basket")
        print("3. Delete Item")
        print("4. Update Item")
        print("5. Generate Bill")
        print("6. Search Bill")
        print("7. Generate Tax File")
        print("8. Exit")

        choice = input("Enter choice (1-8): ")

        if choice == '1':
            item_code = input("Item Code: ")
            internal_price = input("Internal Price: ")
            discount = input("Discount: ")
            sale_price = input("Sale Price: ")
            quantity = input("Quantity: ")
            print(pos.add_to_basket(item_code, internal_price, discount, sale_price, quantity))

        elif choice == '2':
            print(pos.display_basket())

        elif choice == '3':
            print(pos.display_basket())
            try:
                line = int(input("Line number to delete: "))
                print(pos.delete_item(line))
            except ValueError:
                print("DM Sugar Crafts: Invalid line number.")

        elif choice == '4':
            print(pos.display_basket())
            try:
                line = int(input("Line number to update: "))
                sale_price = input("New Sale Price (Enter to skip): ") or None
                discount = input("New Discount (Enter to skip): ") or None
                quantity = input("New Quantity (Enter to skip): ") or None
                print(pos.update_item(line, sale_price, discount, quantity))
            except ValueError:
                print("DM Sugar Crafts: Invalid line number.")

        elif choice == '5':
            result, bill_number = pos.generate_bill()
            print(result)

        elif choice == '6':
            bill_number = input("Enter Bill Number: ")
            print(pos.search_bill(bill_number))

        elif choice == '7':
            bill_number = input("Enter Bill Number: ")
            print(pos.generate_tax_file(bill_number))

        elif choice == '8':
            print("DM Sugar Crafts: Exiting POS system.")
            break

        else:
            print("DM Sugar Crafts: Invalid choice. Please enter 1-8.")


if __name__ == "__main__":
    main()