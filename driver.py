import logging
from parkinglot import ParkingLot
from vehicle import Vehicle
from constants import (
    CREATE,
    PARK,
    SLOTS_BY_DRIVER_AGE,
    SLOT_BY_CAR,
    VACATE,
    REG_NO_BY_DRIVER_AGE,
    OUT_CREATE,
    OUT_PARK_SUCCESS,
    OUT_PARK_FAIL,
    OUT_LEAVE_SUCCESS,
    OUT_LEAVE_FAIL1,
    OUT_LEAVE_FAIL2,
    OUT_QUERY_NO_RESULT, OUT_INVALID_COMMAND)

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
                out = OUT_CREATE.format(slots)

            elif command == PARK:
                reg_no = split[1]
                age = split[3]
                vehicle = Vehicle(reg_no, age)
                slot = self.parking_lot.park_vehicle(vehicle)
                if slot:
                    out = OUT_PARK_SUCCESS.format(reg_no, slot)
                else:
                    out = OUT_PARK_FAIL

            elif command == VACATE:
                slot = split[1]
                vehicle = self.parking_lot.vacate_slot(int(slot))
                if vehicle:
                    out = OUT_LEAVE_SUCCESS.format(slot, vehicle.reg_no, vehicle.age)
                else:
                    if int(slot) <= self.parking_lot.max_available_slots:
                        out = OUT_LEAVE_FAIL1
                    else:
                        out = OUT_LEAVE_FAIL2

            elif command == SLOT_BY_CAR:
                reg_no = split[1]
                vehicle = self.parking_lot.get_vehicle(reg_no)
                if vehicle:
                    out = vehicle.slot
                else:
                    out = OUT_QUERY_NO_RESULT

            elif command == SLOTS_BY_DRIVER_AGE or command == REG_NO_BY_DRIVER_AGE:
                age = split[1]
                vehicles = self.parking_lot.get_vehicles_by_driver_age(age)
                out_list = []
                if vehicles:

                    for vehicle in vehicles:
                        if command == SLOTS_BY_DRIVER_AGE:
                            out_list.append(str(vehicle.slot))
                        else:
                            out_list.append(vehicle.reg_no)

                if out_list:
                    out = ",".join(out_list)
                else:
                    out = OUT_QUERY_NO_RESULT

            else:
                out = OUT_INVALID_COMMAND

            self.output.append(out)

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

