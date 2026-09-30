print("Hello World!")

print("==============================")
print(" Healthcare Client Scheduling System ")
print("==============================")

client_name = input("Enter client name: ")
client_age = input("Enter client age: ")
client_phone = input("Enter client phone number: ")

print("\nClient Information")
print("-------------------")
print("Name: " + client_name)
print("Age: " + client_age)
print("Phone: " + client_phone)

print("\nAppointment Scheduling")
print("----------------------")

appointment_date = input("Enter appointment date (MM/DD/YYYY): ")
appointment_time = input("Enter appointment time: ")
print("\nSelect Appointment Type")
print("1. Annual Checkup")
print("2. Follow-Up Visit")
print("3. New Patient Visit")
print("4. Specialist Consultation")

appointment_choice = input("Enter your choice (1-4): ")

if appointment_choice == "1":
    appointment_type = "Annual Checkup"
elif appointment_choice == "2":
    appointment_type = "Follow-Up Visit"
elif appointment_choice == "3":
    appointment_type = "New Patient Visit"
elif appointment_choice == "4":
    appointment_type = "Specialist Consultation"
else:
    appointment_type = "Invalid Selection"
print("\nAppointment Confirmation")
print("------------------------")
print("Client: " + client_name)
print("Date: " + appointment_date)
print("Time: " + appointment_time)
print("Appointment Type: " + appointment_type)