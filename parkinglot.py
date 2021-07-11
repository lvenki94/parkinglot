class ParkingLot:
    def __init__(self, slots):
        self.max_available_slots = slots
        self.available_slots = slots
        self.nearest_available_slot = 1
        self.slots = dict()
        self.age = dict()
        self.vehicle = dict()

    def park_vehicle(self, vehicle):
        """
        Parks a vehicle
        :param vehicle:
        :return:
        """
        if self.available_slots:
            parked_slot = self.nearest_available_slot
            vehicle.slot = parked_slot
            self.slots[parked_slot] = vehicle
            if vehicle.age not in self.age:
                self.age[vehicle.age] = {vehicle}
            else:
                self.age[vehicle.age].add(vehicle)

            if vehicle.reg_no not in self.vehicle:
                self.vehicle[vehicle.reg_no] = vehicle

            self.available_slots -= 1
            if not self.available_slots:
                self.nearest_available_slot = None
            else:
                for slot in range(self.nearest_available_slot+1, self.max_available_slots+1):
                    if slot not in self.slots:
                        self.nearest_available_slot = slot
                        break
            return parked_slot
        else:
            return 0

    def vacate_slot(self, slot):
        """
        Vacates an occupied slot.
        :param slot:
        :return:
        """
        if slot in self.slots:
            vehicle = self.slots[slot]

            del self.slots[slot]
            del self.vehicle[vehicle.reg_no]
            self.age[vehicle.age].remove(vehicle)

            self.available_slots += 1
            if self.nearest_available_slot:
                self.nearest_available_slot = min(self.nearest_available_slot, slot)
            else:
                self.nearest_available_slot = slot

            return vehicle
        else:
            return False

    def get_slot_of_vehicle(self, reg_no):
        """
        Gets the slot no. of Vehicle
        :param reg_no:
        :return:
        """

        if reg_no in self.vehicle:
            return self.vehicle[reg_no]
        else:
            return None

    def get_vehicles_by_age(self, age):
        """
        Gets all Vehicles parked by owner of given age.
        :param age:
        :return:
        """

        if age in self.age:
            return self.age[age]
        else:
            return None
