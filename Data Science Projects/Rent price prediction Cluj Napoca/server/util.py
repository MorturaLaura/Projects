import json
import pickle
import numpy as np

__neighborhoods = None
__new_building = None
__partitioning = None
__rooms = None
__floor = None
__data_columns = None
__model = None


def get_estimated_rent_price(neighborhood, partitioning, new_building, space, floor, rooms):
    try:
        loc_index = __data_columns.index(neighborhood)
    except:
        loc_index = -1

    try:
        loc_index1 = __data_columns.index(partitioning)
    except:
        loc_index1 = -1

    try:
        loc_index2 = __data_columns.index(new_building)
    except:
        loc_index2 = -1

    try:
        loc_index3 = __data_columns.index(floor)
    except:
        loc_index3 = -1

    try:
        loc_index4 = __data_columns.index(rooms)
    except:
        loc_index4 = -1

    x = np.zeros(len(__data_columns))
    x[0] = space
    if loc_index >= 0 and loc_index1 >= 0 and loc_index2 >= 0 and loc_index3 >= 0 and loc_index4 >= 0:
        x[loc_index] = 1
        x[loc_index1] = 1
        x[loc_index2] = 1
        x[loc_index3] = 1
        x[loc_index4] = 1

    return round(__model.predict([x])[0], 2)


def get_neighborhood_names():
    return __neighborhoods


def get_new_building_names():
    return __new_building


def get_partitioning_names():
    return __partitioning


def get_rooms_names():
    return __rooms


def get_floor_names():
    return __floor


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __neighborhoods
    global __new_building
    global __partitioning
    global __rooms
    global __floor
    global __data_columns

    with open("D:\\GitHub\\Projects\\Data Science Projects\\Rent price prediction Cluj Napoca\\server\\artifacts\\columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __neighborhoods = __data_columns[1:26]
        __new_building = __data_columns[26:28]
        __partitioning = __data_columns[28:33]
        __rooms = __data_columns[33:41]
        __floor = __data_columns[41:]

    global __model
    with open("D:\\GitHub\\Projects\\Data Science Projects\\Rent price prediction Cluj Napoca\\server\\artifacts\\cluj_napoca_rent_price_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts...end")


if __name__ == "__main__":
    load_saved_artifacts()
    print(get_neighborhood_names())
    print(get_new_building_names())
    print(get_partitioning_names())
    print(get_rooms_names())
    print(get_floor_names())
    print(get_estimated_rent_price('Marasti', 'Semidecomandat', 'Imobil vechi', 28, 'Etaj 2', '1 camera'))
    print(get_estimated_rent_price('Andrei Muresanu', 'Circular', 'Imobil vechi', 250, 'Parter', '4 camere'))
    print(get_estimated_rent_price('Central', 'Semidecomandat', 'Imobil vechi', 50, 'Etaj 5', '2 camere'))
    print(get_estimated_rent_price('Manastur', 'Semidecomandat', 'Imobil vechi', 45, 'Etaj 8', '2 camere'))
    print(get_estimated_rent_price('Marasti', 'Semidecomandat', 'Imobil vechi', 40, 'Etaj 2', '2 camere'))
    print(get_estimated_rent_price('Central', 'Decomandat', 'Imobil nou', 50, 'Etaj 2', '2 camere'))
