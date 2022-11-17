import json
class JsonData():
    def create_json_file(self):
        try:
            with open("data.json", "w"): pass
        except OSError as e:
            print("Error! Could not create file: {}". format(e))

    # save the retrieved data to data.json
    def save_to_json_file(self, json_dictionary):
        print("Saving data.json to disk. Please, wait...")
        try:
            with open("data.json", "w") as outfile:
                json.dump(json_dictionary, outfile, indent=4)
            print("Done!")
        except Exception as e:
            print("An error has occurred while saving the json file to disk: {}".format(e))

    # Open the data.json file
    def open_json_file(self):
        try:
            with open("data.json", "r") as openfile:
                json_object = json.load(openfile)
                return json_object
        except Exception as e:
            print("An error has occurred while opening the json file: {}".format(e))