def find_max_units_on_truck(box_types, truck_size):
    box_types.sort(key=lambda a: -a[1])
    current_truck_size = truck_size
    max_units_on_truck = 0
    boxes_to_load = 0
    for boxt, units in box_types:
        if current_truck_size > 0:
            boxes_to_load = min(boxt, current_truck_size)
            max_units_on_truck += boxes_to_load * units
            current_truck_size -= boxes_to_load
        else:
            return max_units_on_truck
    return max_units_on_truck

boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4
print(find_max_units_on_truck(boxTypes, truckSize))
