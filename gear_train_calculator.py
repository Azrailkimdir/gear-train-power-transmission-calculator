print("\n⚙️ Gear Train & Power Transmission Calculator\n")

# User Inputs
driver_teeth = int(input("Driver Gear Teeth: "))
driven_teeth = int(input("Driven Gear Teeth: "))
input_rpm = float(input("Input RPM: "))
input_torque = float(input("Input Torque (Nm): "))

# Calculations
gear_ratio = driven_teeth / driver_teeth

output_rpm = input_rpm / gear_ratio

output_torque = input_torque * gear_ratio

# Results
print("\n===== Results =====")
print(f"Gear Ratio: {gear_ratio:.2f}:1")
print(f"Output RPM: {output_rpm:.2f}")
print(f"Output Torque: {output_torque:.2f} Nm")
