class ParkingLot:
    def __init__(self, slots):
        self.max_available_slots = slots
        self.available_slots = slots
        self.nearest_available_slot = 1
        self.slots = dict()
        self.driver_age = dict()
        self.vehicle = dict()

    def park_vehicle(self, vehicle):
        """
        Parks a vehicle if a slot is available.

        :param vehicle: Type <Vehicle>.
        :return: Returns the parked slot no, if no slot was found returns 0. <int>
        """
        if self.available_slots and vehicle.reg_no not in self.vehicle:
            parked_slot = self.nearest_available_slot
            vehicle.slot = parked_slot
            self.slots[parked_slot] = vehicle
            if vehicle.age not in self.driver_age:
                self.driver_age[vehicle.age] = {vehicle}
            else:
                self.driver_age[vehicle.age].add(vehicle)

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
        
        :param slot: Slot Number to vacate.
        :return: Type <Vehicle> or <Boolean> Returns the vacated vehicle.
        """
        if slot in self.slots:
            vehicle = self.slots[slot]

            del self.slots[slot]
            del self.vehicle[vehicle.reg_no]
            self.driver_age[vehicle.age].remove(vehicle)

            self.available_slots += 1
            if self.nearest_available_slot:
                self.nearest_available_slot = min(self.nearest_available_slot, slot)
            else:
                self.nearest_available_slot = slot

            return vehicle
        else:
            return False

    def get_vehicle(self, reg_no):
        """
        Returns a vehicle with reg_no.
        
        :param reg_no: Registration No. of a parked vehicle.
        :return: Type <Vehicle> if vehicle is parked, else <None> type.
        """

        if reg_no in self.vehicle:
            return self.vehicle[reg_no]
        else:
            return None

    def get_vehicles_by_driver_age(self, age):
        """
        Gets all Vehicles parked by owner of given age.
        
        :param age: Driver's Age
        :return: Type set of <Vehicle> of vehicles driven by age.
        """

        if age in self.driver_age:
            return self.driver_age[age]
        else:
            return None
