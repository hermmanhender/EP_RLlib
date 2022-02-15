"""
# Python Plugin System
"""
"""
PythonPlugin:SearchPaths
Add directories to the search path for Python plugin modules The directory containing the EnergyPlus executable file is automatically added so that the Python interpreter can find the packaged up pyenergyplus Python package. By default, the current working directory and input file directory are also added to the search path. However, this object allows modifying this behavior. With this object, searching these directories can be disabled, and users can add supplemental search paths that point to libraries of plugin scripts.

Fields

add_current_working_directory_to_search_path [string] (Default: Yes)
add_input_file_directory_to_search_path [string] (Default: Yes)
py_search_paths [Array of {search_path}]
PythonPlugin:Instance
A single plugin to be executed during the simulation, which can contain multiple calling points for the same class instance by overriding multiple calling point methods.

Fields

run_during_warmup_days [string] (Default: No)
python_module_name [string]
plugin_class_name [string]
PythonPlugin:Variables
This object defines name identifiers for custom Python Plugin variable data that should be shared among all running Python Plugins.

Fields

global_py_vars [Array of {variable_name}]
"""
class PythonPlugin_TrendVariable():
    """
    This object sets up a Python plugin trend variable from an Python plugin variable A trend variable logs values across timesteps
    """
    def name_of_a_python_plugin_variable(epJSON, string, ObjectName="PythonPlugin:TrendVariable 1"):
        epJSON["PythonPlugin:TrendVariable"][ObjectName]["name_of_a_python_plugin_variable"] = string
        return epJSON
    """
    number_of_timesteps_to_be_logged [number]
    """

class PythonPlugin_OutputVariable():
    """
    This object sets up an EnergyPlus output variable from a Python Plugin variable
    """
    def python_plugin_variable_name(epJSON, string, ObjectName="PythonPlugin:OutputVariable 1"):
        epJSON["PythonPlugin:OutputVariable"][ObjectName]["python_plugin_variable_name"] = string
        return epJSON
    """
    type_of_data_in_variable [string]
    update_frequency [string]
    units [string]
    resource_type [string]
    group_type [string]
    end_use_category [string]
    end_use_subcategory [string]
    """