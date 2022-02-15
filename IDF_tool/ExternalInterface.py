"""
# External Interface
"""
"""
ExternalInterface
This object activates the external interface of EnergyPlus. If the object ExternalInterface is present, then all ExtnernalInterface:* objects will receive their values from the BCVTB interface or from FMUs at each zone time step. If this object is not present, then the values of these objects will be fixed at the value declared in the “initial value” field of the corresponding object, and a warning will be written to the EnergyPlus error file.

Fields

name_of_external_interface [string]
ExternalInterface:Schedule
A ExternalInterface:Schedule contains only one value, which is used during the warm-up period and the system sizing.

Fields

schedule_type_limits_name [string]
initial_value [number]
ExternalInterface:Variable
This input object is similar to EnergyManagementSystem:GlobalVariable. However, at the beginning of each zone time step, its value is set to the value received from the external interface. During the warm-up period and the system sizing, its value is set to the value specified by the field “initial value.” This object can be used to move data into Erl subroutines.

Fields

initial_value [number]
ExternalInterface:Actuator
Hardware portion of EMS used to set up actuators in the model

Fields

actuated_component_unique_name [string]
actuated_component_type [string]
actuated_component_control_type [string]
optional_initial_value [number]
ExternalInterface:FunctionalMockupUnitImport
This object declares an FMU

Fields

fmu_file_name [string]
fmu_timeout [number] (Default: 0.0)
fmu_loggingon [number] (Default: 0.0)
ExternalInterface:FunctionalMockupUnitImport:From:Variable
This object declares an FMU input variable

Fields

output_variable_index_key_name [string]
output_variable_name [string]
fmu_file_name [string]
fmu_instance_name [string]
fmu_variable_name [string]
ExternalInterface:FunctionalMockupUnitImport:To:Schedule
This objects contains only one value, which is used during the first call of EnergyPlus

Fields

schedule_type_limits_names [string]
fmu_file_name [string]
fmu_instance_name [string]
fmu_variable_name [string]
initial_value [number]
ExternalInterface:FunctionalMockupUnitImport:To:Actuator
Hardware portion of EMS used to set up actuators in the model that are dynamically updated from the FMU.

Fields

actuated_component_unique_name [string]
actuated_component_type [string]
actuated_component_control_type [string]
fmu_file_name [string]
fmu_instance_name [string]
fmu_variable_name [string]
initial_value [number]
ExternalInterface:FunctionalMockupUnitImport:To:Variable
Declares Erl variable as having global scope No spaces allowed in names used for Erl variables

Fields

fmu_file_name [string]
fmu_instance_name [string]
fmu_variable_name [string]
initial_value [number]
ExternalInterface:FunctionalMockupUnitExport:From:Variable
This object declares an FMU input variable

Fields

output_variable_index_key_name [string]
output_variable_name [string]
fmu_variable_name [string]
ExternalInterface:FunctionalMockupUnitExport:To:Schedule
This objects contains only one value, which is used during the first call of EnergyPlus

Fields

schedule_name [string]
schedule_type_limits_names [string]
fmu_variable_name [string]
initial_value [number]
ExternalInterface:FunctionalMockupUnitExport:To:Actuator
Hardware portion of EMS used to set up actuators in the model that are dynamically updated from the FMU.

Fields

actuated_component_unique_name [string]
actuated_component_type [string]
actuated_component_control_type [string]
fmu_variable_name [string]
initial_value [number]
ExternalInterface:FunctionalMockupUnitExport:To:Variable
Declares Erl variable as having global scope No spaces allowed in names used for Erl variables

Fields

fmu_variable_name [string]
initial_value [number]
"""