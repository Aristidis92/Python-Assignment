class Smartphone:
    """
    Represents a generic smartphone.
    """
    def __init__(self, brand, model, storage_gb, color):
        """
        Initializes a new Smartphone object.

        """
        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb
        self.color = color
        self.is_on = False

    def power_on(self):
        """Powers on the smartphone."""
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is now powered on.")
        else:
            print(f"{self.brand} {self.model} is already on.")

    def power_off(self):
        """Powers off the smartphone."""
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} {self.model} is now powered off.")
        else:
            print(f"{self.brand} {self.model} is already off.")

    def display_info(self):
        """Displays basic information about the smartphone."""
        print(f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage_gb}GB, Color: {self.color}")

class GamingSmartphone(Smartphone):
    """
    Represents a gaming-focused smartphone, inheriting from Smartphone.
    """
    def __init__(self, brand, model, storage_gb, color, refresh_rate_hz, cooling_system):
        """
        Initializes a new GamingSmartphone object.
        """
        super().__init__(brand, model, storage_gb, color)
        self.refresh_rate_hz = refresh_rate_hz
        self.cooling_system = cooling_system

    def activate_game_mode(self):
        """Activates a special game mode for enhanced performance."""
        if self.is_on:
            print(f"{self.brand} {self.model}: Game mode activated! Enjoy {self.refresh_rate_hz}Hz refresh rate.")
        else:
            print(f"{self.brand} {self.model} needs to be powered on to activate game mode.")

    def display_info(self):
        """
        Overrides the display_info method to include gaming-specific details.
        Demonstrates polymorphism.
        """
        super().display_info()
        print(f"Refresh Rate: {self.refresh_rate_hz}Hz, Cooling System: {self.cooling_system}")

# Creating objects
my_phone = Smartphone("Samsung", "Galaxy S24", 256, "Black")
gaming_phone = GamingSmartphone("ROG", "Phone 8 Pro", 512, "Phantom Black", 165, "Vapor Chamber")

# Demonstrating methods and attributes
my_phone.power_on()
my_phone.display_info()
my_phone.power_off()

print("\n--- Gaming Smartphone ---")
gaming_phone.power_on()
gaming_phone.display_info() # Polymorphism in action
gaming_phone.activate_game_mode()
gaming_phone.power_off()