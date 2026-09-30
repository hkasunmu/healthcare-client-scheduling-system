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
appointment_type = input("Enter appointment type: ")
print("\nAppointment Confirmation")
print("------------------------")
print("Client: " + client_name)
print("Date: " + appointment_date)
print("Time: " + appointment_time)
print("Appointment Type: " + appointment_type)