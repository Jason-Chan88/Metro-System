"""
File: metro_lines.py
Author: Jason Chan
Description: Creating your own metro lines
"""


def create_station(station_name, places):
    """"
        create stations
        :param: station name which is your key to your dictionary and your station
        :param: places is your station dictionary
        :return: places the dictionary that hold all your stations and all the info for that
        """""
    if station_name in places:
        print("Station exist")     # can't have duplicate stations

    if station_name not in places:
        places[station_name] = {"connections": [], "lines": [], "visited": False}  # sets up your dictionary for later
        #print(places)

    return places


def connect_stations(first_station, second_station, line_name, places):
    """"
        Connect your stations with a line name
        :param: first station being connect to the second
        :param: second being connected to first
        :param: line name is the line they are all on
        :param: places the dictionary
        :return: places the dictionary that hold all your stations and all the info for that
    """""
    if first_station in places and second_station in places:  # connecting the stations together
        places[first_station]["connections"].append(second_station)
        places[second_station]["connections"].append(first_station)

        if line_name not in places[first_station]["lines"] and first_station in places:
            places[first_station]["lines"].append(line_name)
            # needs to be like this to prevent duplicate but also to stop from having a station not get the line name
        if line_name not in places[second_station]["lines"] and second_station in places:
            places[second_station]["lines"].append(line_name)

    if first_station not in places or second_station not in places:
        print("Stations don't exist")

    #print(places)
    return places


def plan_trip(places, starting_station, ending_station):
    """"
        Planning a trip from one station to another
        :param: starting station is where the trip starts
        :param: ending station is where the trips ends
        :param: places is the dictionary with the info
        :return: the trip planned out  
        """""

    if starting_station == ending_station:  # if the stations equal each other return the ending station
        return [ending_station]

    else:
        # print("Start on the", " ".join(places[starting_station]["lines"]),)
        places[starting_station]["visited"] = True  # prevents error as it wouldn't stop

        for new_destination in places[starting_station]["connections"]:

            if not places[new_destination]["visited"]:

                trip = plan_trip(places, new_destination, ending_station)
                if trip:
                    return [starting_station] + trip   # get you the plan trip from point A to point B

        return []  # happens if the visited is true


def reset(places):
    """"
        This is the reason you can run plan trip more than once as it reset the visited from True to False
        :param: places is the dictionary with the info and this reset the visited so the recursion function works
        :return: nothing
    """""
    for place in places:   # goes through places and makes the visited false again
        places[place]["visited"] = False


def create_train(train_id, line_name, starting_position, train):
    """"
        Creating your train
        :param: train id is your key and your train name
        :param: line name is th eline the train is connected to
        :param: starting positions is where the train starts
        :param: train is where all the train info is
        :return: nothing
    """""
    if line_name not in places[starting_position]["lines"] and starting_position not in places:
        print("Station don't exist")
        # to make sure you can actually make the train
    if line_name in places[starting_position]["lines"] and starting_position in places:
        train[train_id] = {"line": [line_name], "start": [starting_position]}  # putting in the train info
    #print(train)

def display_stations(places):
    """"
    displays your station's name
    :param: places is your station dictionary with all the info
    """""
    for keys in places:   # keys are your stations and gives you all the station
        print(keys)


def display_trains(train):
    """"
    Display all the trains and their info
    :param: train is where all your train info is
    """""
    for keys, value in train.items():  # so you can get all the trains and there info

        print("*** Information for train", keys, "***")

        print("Line:", " ".join(train[keys]["line"]))  # .join to get rid of brackets

        print("Current position:", " ".join(train[keys]["start"]))


def get_station_info(station_name, places):
    """"
    Gets a specific station and all of it's info
    :param: station name is used as a key to get info 
    :param: places is where the info is stored
    """""
    if station_name not in places:  # if station don't exist
        print("Station don't exist")

    if station_name in places:

        print("*** Information for station", station_name, "***")

        print("Line:", " ".join(places[station_name]["lines"]))  # getting the station info

        print("Connection:", " , ".join(places[station_name]["connections"]))


def get_train_info(train_id, train):
    """"
    get a specific station's info
    :param: train id is a key to the info
    :param: train is where the info is stored
    """""
    if train_id not in train:  # if train doesn't exist
        print("Train don't exist")

    if train_id in train:
        print("*** Information for train", train_id, "***")

        print("Line:", " ".join(train[train_id]["line"]))  # gets the train info

        print("Current position:", " ".join(train[train_id]["start"]))


if __name__ == '__main__':
    places = {}  # all the station info

    train = {}  # all the train info

    system = input(">>> ")  # first input to get the type of system

    order = input(f'{system} >>> ')  # the input for all your order

    while order != "exit":  # keeps going until exit

        split_order = order.split()  # split your order, so you can determine what you want through indexes

        if split_order[0] == "create" and split_order[1] == "station" and len(split_order) == 3:
            create_station(split_order[2], places)
            # checking for create station and proper length than having the index for the info they need
        if split_order[0] == "connect" and split_order[1] == "stations" and len(split_order) == 5:
            connect_stations(split_order[2], split_order[3], split_order[4], places)
            # checking for connect station and proper length than having the index for the info they need
        if split_order[0] == "create" and split_order[1] == "train" and len(split_order) == 5:
            create_train(split_order[2], split_order[3], split_order[4], train)
            # checking for create train and proper length than having the index for the info they need
        if split_order[0] == "display" and split_order[1] == "station" and len(split_order) == 2:
            display_stations(places)
            # checking for display station and proper length
        if split_order[0] == "display" and split_order[1] == "train" and len(split_order) == 2:
            display_trains(train)
            # checking for display train and proper length
        if split_order[0] == "get" and split_order[1] == "station" and split_order[2] == "info" and \
                len(split_order) == 4:
            get_station_info(split_order[3], places)
            # checking for get station info and proper length than having the index for the info they need
        if split_order[0] == "get" and split_order[1] == "train" and split_order[2] == "info" and len(split_order) == 4:
            get_train_info(split_order[3], train)
            # checking for get station info and proper length than having the index for the info they need
        if split_order[0] == "plan" and split_order[1] == "trip" and len(split_order) == 4:

            if split_order[2] not in places or split_order[3] not in places:  # if one of the station doesn't exist
                print("Station don't exist")

            if split_order[2] in places and split_order[3] in places:
                print("Start on the", " ".join(places[split_order[2]]["lines"]), "-->", " --> ".join(plan_trip(places,
             split_order[2], split_order[3])))
            # checking for plan trip and proper length than having the index for the info they need
                reset(places)
            # this reset the visit part, so you can run plan trip more than once

        order = input(f'{system} >>> ')  # need this to keep asking after function is used
