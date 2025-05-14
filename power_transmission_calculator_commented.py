
# Define a class to represent a single transmission stage (gear or pulley)
class Stage:
    def __init__(self, stage_type, ratio, efficiency_percent):
        # Store the type of stage ('gear' or 'pulley')
        self.stage_type = stage_type
        # Store the speed ratio for this stage
        self.ratio = ratio
        # Convert efficiency from percent to decimal (e.g. 90% → 0.90)
        self.efficiency = efficiency_percent / 100

    # Method to calculate output speed and power for this stage
    def process(self, input_speed, input_power):
        # Adjust speed by multiplying with the ratio
        output_speed = input_speed * self.ratio
        # Adjust power by multiplying with efficiency
        output_power = input_power * self.efficiency
        # Return the updated speed and power to be used in the next stage
        return output_speed, output_power


# Class to manage the entire power transmission system
class TransmissionSystem:
    def __init__(self, input_speed, input_power):
        # Store initial speed and power
        self.input_speed = input_speed
        self.input_power = input_power
        # List to hold all the stages added to the system
        self.stages = []

    # Add a stage object to the system
    def add_stage(self, stage):
        self.stages.append(stage)

    # Perform calculations through all stages
    def calculate(self):
        # Start with the initial input values
        current_speed = self.input_speed
        current_power = self.input_power

        print("\n--- Transmission Stages Breakdown ---")
        # Loop through each stage and process it
        for i, stage in enumerate(self.stages, start=1):
            print(f"\nStage {i}: {stage.stage_type.title()} System")
            print(f"  - Ratio: {stage.ratio}")
            print(f"  - Efficiency: {stage.efficiency * 100}%")

            # Process current stage
            current_speed, current_power = stage.process(current_speed, current_power)

            # Show the output after this stage
            print(f"  => Output Speed: {current_speed:.2f} RPM")
            print(f"  => Output Power: {current_power:.2f} Watts")

        # Final results after all stages
        print("\nFinal Output:")
        print(f"  >> Final Speed: {current_speed:.2f} RPM")
        print(f"  >> Final Power: {current_power:.2f} Watts")


# Main program execution starts here
def main():
    print("=== Multi-System Power Transmission Calculator ===")

    # Get user input for motor speed and power
    input_speed = float(input("Enter initial motor speed (RPM): "))
    input_power = float(input("Enter initial power (Watts): "))

    # Create a new system with the initial inputs
    system = TransmissionSystem(input_speed, input_power)

    # Ask how many stages the user wants to add
    num_stages = int(input("Enter number of stages: "))

    # Loop to collect info about each stage
    for i in range(num_stages):
        print(f"\n--- Stage {i + 1} ---")
        stage_type = input("Is this a gear or pulley stage? ").strip().lower()
        ratio = float(input("Enter speed ratio (e.g., 0.5 for reduction, 2.0 for increase): "))
        efficiency = float(input("Enter efficiency percentage (e.g., 90 for 90%): "))

        # Create the stage object and add it to the system
        system.add_stage(Stage(stage_type, ratio, efficiency))

    # Perform calculations and display results
    system.calculate()


# Ensures the main() function runs when this script is executed
if __name__ == "__main__":
    main()
