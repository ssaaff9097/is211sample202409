import argparse
import urllib.request
import logging
import datetime

def downloadData(url):
    """
    Reads data from a URL and returns the data as a string

    :param url:
    :return: the content of the URL
    """
    # read the URL
    with urllib.request.urlopen(url) as response:
        response = response.read().decode('utf-8')

    # return the data
    return response


def processData(file_content):
    """
    Takes the contents of the file as the first parameter, processes the file line by line, 
    and returns a dictionary that maps a persons ID to a tuple of the form (name, birthday).
    """
    result_dict = {}
    header = True
    for i, line in enumerate(file_content.split("\n")):
        if i > 5:
            break 
        
        if header:
            header = False
            continue

        id_str, name, birthday_str = line.split(",")
        id = int(id_str)

        # make sure you handle bad dates...

        birthday = datetime.datetime.strptime(birthday_str, "%d/%m/%Y")
        result_dict[id] = (name, birthday)

    # parse data using datetime.datetime.strptime(s, "%d/%m/%Y")
    return result_dict


def displayPerson(id, personData):
    """
    The purpose of this function is to print the name and birthday 
    of a given user identified by the input id. 
    """
    if id in personData:
        print("Found ...")
    else:
        print("No user found with that id")


def main(url):
    print(f"Running main with URL = {url}...")
    # Part II - Download Data
    file_data = downloadData(url)

    print(file_data)

    # Part III Process Data
    person_dict = processData(file_data)

    # Make sure to ask the User for an id
    # but as an example, let's try 1
    user_id = 1
    #displayPerson(user_id, person_dict)
    print("Here are the test result:")
    print(person_dict[user_id])
    print(person_dict[2])
    #displayPerson(user_id, person_dict)


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
