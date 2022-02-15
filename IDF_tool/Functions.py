
def modify_variable(jsonFile, ClassName, ObjectName, FunctionName, value):
    jsonFile[ClassName][ObjectName][FunctionName] = value
    return jsonFile

def read_variable(jsonFile, ClassName, ObjectName, FunctionName):
        """
        Specifies the EnergyPlus version of the IDF file.
        """
        value = jsonFile[ClassName][ObjectName][FunctionName]
        return value