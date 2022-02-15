"""
# Main Functions
"""
import json

class MainFunctions():
    def read_epjson(path):
        """
        # Read a epJSON file
        This function allows the opening of an epJSON file, which is necessary to later dynamically modify the content of the file.

        The 'path' is the address where the epJSON file to be read is located.
        """
        with open(path) as file:
            epJSON = json.load(file)
        return epJSON
            
    def write_epjson(path, epJSON):
        """
        # Write a epJSON file

        This function writes the modified epJSON file (or not). It is used at the end, after making all the modifications in the read file with the 'read' function.

        The 'path' is the place where the modified epJSON file will be saved and 'epJSON' the information to be saved.
        """
        with open(path, 'w') as fp:
            json.dump(epJSON, fp, sort_keys=False, indent=4)

    
