from abc import ABC, abstractmethod
import time

# Abstract base class for all moving entities
class MovingEntity(ABC):
    @abstractmethod
    def move(self):
        pass
    
    def describe(self):
        return f"I am a {self.__class__.__name__}"

# Animal classes
class Cheetah(MovingEntity):
    def move(self):
        return "Running swiftly across the savannah! 🐆"
    
    def describe(self):
        return super().describe() + " - the fastest land animal!"

class Dolphin(MovingEntity):
    def move(self):
        return "Swimming gracefully through the ocean! 🐬"
    
    def describe(self):
        return super().describe() + " - intelligent and playful!"

class Eagle(MovingEntity):
    def move(self):
        return "Soaring high in the sky! 🦅"
    
    def describe(self):
        return super().describe() + " - king of the skies!"

# Vehicle classes
class Car(MovingEntity):
    def move(self):
        return "Driving on the highway! 🚗"
    
    def describe(self):
        return super().describe() + " - perfect for road trips!"

class Plane(MovingEntity):
    def move(self):
        return "Flying through the clouds! ✈️"
    
    def describe(self):
        return super().describe() + " - fastest way to travel long distances!"

class Bicycle(MovingEntity):
    def move(self):
        return "Pedaling along the bike path! 🚴"
    
    def describe(self):
        return super().describe() + " - eco-friendly transportation!"

class Submarine(MovingEntity):
    def move(self):
        return "Diving deep under the sea! 🚢"
    
    def describe(self):
        return super().describe() + " - exploring the ocean depths!"

class Rocket(MovingEntity):
    def move(self):
        return "Blasting off into space! 🚀"
    
    def describe(self):
        return super().describe() + " - reaching for the stars!"

# Demonstration function
def demonstrate_movement(entities):
    print("🚀 Movement Demonstration 🚀")
    print("=" * 40)
    
    for i, entity in enumerate(entities, 1):
        print(f"\n{i}. {entity.describe()}")
        print(f"   {entity.move()}")
        time.sleep(0.5)  # Small delay for dramatic effect

# Create a zoo and garage of moving entities
def create_world():
    return [
        # Animals
        Cheetah(),
        Dolphin(),
        Eagle(),
        
        # Vehicles
        Car(),
        Plane(),
        Bicycle(),
        Submarine(),
        Rocket()
    ]

# Interactive demonstration
def interactive_demo():
    entities = create_world()
    
    while True:
        print("\n" + "=" * 50)
        print("🏎️  ANIMAL & VEHICLE MOVEMENT SIMULATOR 🐆")
        print("=" * 50)
        print("Choose an option:")
        print("1. See all movements")
        print("2. Choose specific type")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == "1":
            demonstrate_movement(entities)
            
        elif choice == "2":
            print("\nAvailable entities:")
            for i, entity in enumerate(entities, 1):
                print(f"{i}. {entity.__class__.__name__}")
            
            try:
                selection = int(input("\nSelect a number: ")) - 1
                if 0 <= selection < len(entities):
                    entity = entities[selection]
                    print(f"\n🎯 Selected: {entity.describe()}")
                    print(f"🎯 Action: {entity.move()}")
                else:
                    print("❌ Invalid selection!")
            except ValueError:
                print("❌ Please enter a valid number!")
                
        elif choice == "3":
            print("👋 Goodbye! Thanks for exploring movement!")
            break
            
        else:
            print("❌ Invalid choice! Please try again.")

# Main program
if __name__ == "__main__":
    print("Welcome to the Polymorphic Movement Simulator!")
    print("This program demonstrates how different animals and vehicles")
    print("can have the same action (move()) but implement it differently!\n")
    
    interactive_demo()