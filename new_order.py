import tkinter
from tkinter import ttk


class App(tkinter.Tk):
    def __init__(self):
        super().__init__()

        # Sets up cateogires and their images for the for loop
        self.food_categories = ["taco", "drink"]
        self.food_images = [tkinter.PhotoImage(
            file=f"./assets/{category}_icon.png") for category in self.food_categories]

        # Sets up items and their images for the for loop
        self.items = ["Taco 1", "Taco 2", "Taco 3", "Taco 4", "Taco 5", "Taco 6",
                      "Taco 7", "Taco 8", "Taco 9", "Taco 10", "Taco 11", "Taco 12"]
        self.item_images = [tkinter.PhotoImage(
            file="./assets/taco_item.png") for items in self.items]

        # Lays out base window
        self.geometry("490x685")
        self.title("Bruh Eats(tm)")
        self.widgets()
        self.resizable(0, 0)
        self.columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=5)

    def widgets(self):
        # creates the categories frame, and the configuration for its grid
        categories = tkinter.Frame(
            self, background="#d5e8d4", height=610
        )
        categories.columnconfigure(0, weight=1)

        # creates the items frame
        items = tkinter.Frame(
            self, background="#ffffff", height=610, width=490)

        # creates the bottom bar frame
        bottom = tkinter.Frame(
            self, background="#000000", height=75, width=585)
        bottom.columnconfigure(0, weight=1)
        bottom.columnconfigure(1, weight=2)
        bottom.columnconfigure(2, weight=2)

        # packs the 3 main components into a grid
        categories.grid(column=0, row=0, sticky="NESW")
        items.grid(column=1, row=0, sticky="NESW")
        bottom.grid(column=0, row=1, columnspan=2, sticky="NESW")

        # for loop for categories.
        for index in range(len(self.food_categories)):
            # sets the image for the item
            self.photo_image = self.food_images[index]
            # creates button
            category_button = ttk.Button(
                categories, text=self.food_categories[index], image=self.photo_image, compound="top")
            category_button.grid(row=index, sticky="EW",
                                 padx=10, pady=10, ipadx=4, ipady=4)

        # counts for item columns for the 3 column design.
        column_count = -1
        # counts when a new row is required
        row_count = -1
        # for loop for items
        for index in range(len(self.items)):
            # places items into correct column
            if column_count < 2:
                column_count = column_count + 1
            else:
                column_count = 0
            # places items into correct row
            if column_count == 0:
                row_count = row_count + 1

            # sets image for the item
            self.photo_image = self.item_images[index]
            # creates button
            item_button = ttk.Button(
                items, text=f"{self.items[index]}\n$6.50", image=self.photo_image, compound="top")
            item_button.grid(column=column_count, row=row_count, sticky="EW", padx=10,
                             pady=10, ipadx=4, ipady=4)

        # bottom bar buttons
        # sets image for cart button
        self.photo_image = tkinter.PhotoImage(file="./assets/small_cart.png")
        # cart / view items button
        cart_button = ttk.Button(
            bottom, text="1", image=self.photo_image, compound="bottom"
        )
        cart_button.grid(column=0, row=0, sticky="NSW", padx=10,
                         pady=10, ipady=2, ipadx=2)
        # cancel order button
        cancel_button = ttk.Button(
            bottom, text="Cancel Order"
        )
        cancel_button.grid(column=1, row=0, sticky="NS",
                           padx=10, pady=10, ipady=2, ipadx=2)
        # purchase order button
        purchase_button = ttk.Button(
            bottom, text="Purchase Order\n$6.50"
        )
        purchase_button.grid(column=2, row=0, sticky="NS",
                             padx=10, pady=10, ipady=2, ipadx=2)


if __name__ == "__main__":
    app = App()
    app.mainloop()
