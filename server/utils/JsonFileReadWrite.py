import json

class JsonReadWrite:

    @staticmethod
    def read_file(filename):
        '''Reads a file and returns the data format'''
        data = None
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                return data
        except Exception as e:
            print("IO Exception: ", e)
            return None
    
    @staticmethod
    def write_json_file(filename, json):
        '''Writes to file in json from dict[]'''
        data = None
        try:
            with open(filename, 'w') as file:
                json.dump(data, file)
                return True
        except Exception as e:
            return None

    @staticmethod
    def read_json_file(filename):
        '''Reads a filename and returns json in form of dict[]'''
        data = None
        try:
            with open(filename, 'w') as file:
                data = json.load(file)
                return data
        except Exception as e:
            return None
