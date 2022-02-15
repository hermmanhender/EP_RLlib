"""
# Energy Management System (EMS)
"""
"""
EnergyManagementSystem:Sensor
Declares EMS variable as a sensor a list of output variables and meters that can be reported are available after a run on the report (.rdd) or meter dictionary file (.mdd) if the Output:VariableDictionary has been requested.

Fields

output_variable_or_output_meter_index_key_name [string]
output_variable_or_output_meter_name [string]
EnergyManagementSystem:Actuator
Hardware portion of EMS used to set up actuators in the model

Fields

actuated_component_unique_name [string]
actuated_component_type [string]
actuated_component_control_type [string]
EnergyManagementSystem:ProgramCallingManager
Input EMS program. a program needs a name a description of when it should be called and then lines of program code for EMS Runtime language

Fields

energyplus_model_calling_point [string]
programs [Array of {program_name}]
EnergyManagementSystem:Program
This input defines an Erl program Each field after the name is a line of EMS Runtime Language

Fields

lines [Array of {program_line}]
EnergyManagementSystem:Subroutine
This input defines an Erl program subroutine Each field after the name is a line of EMS Runtime Language

Fields

lines [Array of {program_line}]
EnergyManagementSystem:GlobalVariable
Declares Erl variable as having global scope No spaces allowed in names used for Erl variables

Fields

variables [Array of {erl_variable_name}]
EnergyManagementSystem:OutputVariable
This object sets up an EnergyPlus output variable from an Erl variable

Fields

ems_variable_name [string]
type_of_data_in_variable [string]
update_frequency [string]
ems_program_or_subroutine_name [string]
units [string]
EnergyManagementSystem:MeteredOutputVariable
This object sets up an EnergyPlus output variable from an Erl variable

Fields

ems_variable_name [string]
update_frequency [string]
ems_program_or_subroutine_name [string]
resource_type [string]
group_type [string]
end_use_category [string]
end_use_subcategory [string]
units [string]
EnergyManagementSystem:TrendVariable
This object sets up an EMS trend variable from an Erl variable A trend variable logs values across timesteps

Fields

ems_variable_name [string]
number_of_timesteps_to_be_logged [number]
EnergyManagementSystem:InternalVariable
Declares EMS variable as an internal data variable

Fields

internal_data_index_key_name [string]
internal_data_type [string]
EnergyManagementSystem:CurveOrTableIndexVariable
Declares EMS variable that identifies a curve or table

Fields

curve_or_table_object_name [string]
EnergyManagementSystem:ConstructionIndexVariable
Declares EMS variable that identifies a construction

Fields

construction_object_name [string]
"""