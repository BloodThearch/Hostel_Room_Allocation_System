from db.models import Room, Hostel

roomNumber1 = int(input("Enter starting room number range: "))
roomNumber2 = int(input("Enter ending room number range: "))
hostelName = input("Enter hostel name: ")
availableSeats = int(input("Enter number of seats for those rooms: "))
roomType = input("Enter type of room (AC/NONAC): ")



try:
    validHostelName = False
    hostelRecord = Hostel.objects.get(name=hostelName)
    validHostelName = True
    for roomNumber in range(roomNumber1, roomNumber2+1):
        room = Room(
            roomNumber = roomNumber,
            hostelName = hostelName,
            occupancy = 0,
            availableSeats = availableSeats,
            roomType = roomType
        )
        room.save()
except:
    print("Error")
    print("Hostel name validity:",validHostelName)



