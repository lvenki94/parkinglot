CREATE = "Create_parking_lot"
PARK = "Park"
VACATE = "Leave"
SLOT_BY_CAR = "Slot_number_for_car_with_number"
SLOTS_BY_DRIVER_AGE = "Slot_numbers_for_driver_of_age"
REG_NO_BY_DRIVER_AGE = "Vehicle_registration_number_for_driver_of_age"


OUT_CREATE = "Created parking of {} slots"
OUT_PARK_SUCCESS = "Car with vehicle registration number \"{}\" has been parked at slot number {}"
OUT_PARK_FAIL = "Parking Lot is Full or car already parked."
OUT_LEAVE_SUCCESS = "Slot number {} vacated, the car with vehicle registration number \"{}\" left the space," \
                    " the driver of the car was of age {}"
OUT_LEAVE_FAIL1 = "Slot is Empty"
OUT_LEAVE_FAIL2 = "Slot Does not Exist"
OUT_QUERY_NO_RESULT = "No parked car matches the query"
OUT_INVALID_COMMAND = "Invalid Command."
