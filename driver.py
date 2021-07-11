import logging
from parkinglot import ParkingLot
from vehicle import Vehicle
from constants import (
    CREATE,
    PARK,
    SLOTS_BY_AGE,
    SLOT_BY_CAR,
    VACATE,
    REG_NO_BY_DRIVER_AGE
)

log = logging.getLogger(__name__)


class Driver:
    def __init__(self, file_path):
        self.file_path = file_path
        self.commands = []
        self.output = []
        self.parking_lot = ParkingLot(0)

    def set_input_commands(self):
        """
        Reads the input file and sets the constants.py.
        :return: None
        """

        try:
            with open(self.file_path) as fp:
                self.commands = fp.readlines()
        except Exception as e:
            log.error("Exception Occurred while reading the input file: {}, error: {}".format(self.file_path, e))

    def execute_commands(self):
        """
        Parses and Executes every input command.
        :return: None
        """

        for _input in self.commands:

            split = _input.strip().split(" ")
            command = split[0]

            if command == CREATE:
                slots = int(split[1])
                self.parking_lot = ParkingLot(slots)
                out = "Created parking of {} slots".format(slots)
                self.output.append(out)

            elif command == PARK:
                reg_no = split[1]
                age = split[3]
                vehicle = Vehicle(reg_no, age)
                slot = self.parking_lot.park_vehicle(vehicle)
                if slot:
                    out = "Car with vehicle registration number \"{}\" has been parked at slot number {}"\
                        .format(reg_no, slot)
                else:
                    out = "Parking Lot is Full."
                self.output.append(out)

            elif command == VACATE:
                slot = split[1]
                vehicle = self.parking_lot.vacate_slot(int(slot))
                if vehicle:
                    out = "Slot number {} vacated, the car with vehicle registration number" \
                          " \"{}\" left the space, the driver of the car was of age {}"\
                        .format(
                        slot,
                        vehicle.reg_no,
                        vehicle.age
                    )
                else:
                    out = "Slot is Empty"

                self.output.append(out)

            elif command == SLOT_BY_CAR:
                reg_no = split[1]
                vehicle = self.parking_lot.get_vehicle(reg_no)
                if vehicle:
                    out = vehicle.slot
                else:
                    out = "No parked car matches the query"

                self.output.append(out)

            elif command == SLOTS_BY_AGE or command == REG_NO_BY_DRIVER_AGE:
                age = split[1]
                vehicles = self.parking_lot.get_vehicles_by_driver_age(age)
                out_list = []
                if vehicles:

                    for vehicle in vehicles:
                        if command == SLOTS_BY_AGE:
                            out_list.append(str(vehicle.slot))
                        else:
                            out_list.append(vehicle.reg_no)

                if out_list:
                    out = ",".join(out_list)
                else:
                    out = "No parked car matches the query"

                self.output.append(out)

            else:
                self.output.append("Invalid Command.")

    def print_output(self):
        """
        Prints the Output to Terminal.
        :return: None
        """
        for output in self.output:
            print(output)

    def drive(self):
        """
        Program Driver
        :return: None
        """
        self.set_input_commands()
        self.execute_commands()
        self.print_output()

