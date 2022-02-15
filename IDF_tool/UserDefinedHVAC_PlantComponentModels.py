"""
# User Defined HVAC and Plant Component Models
"""
"""
ZoneHVAC:ForcedAir:UserDefined
Defines a generic zone air unit for custom modeling using Energy Management System or External Interface

Fields

overall_model_simulation_program_calling_manager_name [string]
model_setup_and_sizing_program_calling_manager_name [string]
primary_air_inlet_node_name [string]
primary_air_outlet_node_name [string]
secondary_air_inlet_node_name [string]
secondary_air_outlet_node_name [string]
number_of_plant_loop_connections [number]
plant_connection_1_inlet_node_name [string]
plant_connection_1_outlet_node_name [string]
plant_connection_2_inlet_node_name [string]
plant_connection_2_outlet_node_name [string]
plant_connection_3_inlet_node_name [string]
plant_connection_3_outlet_node_name [string]
supply_inlet_water_storage_tank_name [string]
collection_outlet_water_storage_tank_name [string]
ambient_zone_name [string]
AirTerminal:SingleDuct:UserDefined
Defines a generic single duct air terminal unit for custom modeling using Energy Management System or External Interface

Fields

overall_model_simulation_program_calling_manager_name [string]
model_setup_and_sizing_program_calling_manager_name [string]
primary_air_inlet_node_name [string]
primary_air_outlet_node_name [string]
secondary_air_inlet_node_name [string]
secondary_air_outlet_node_name [string]
number_of_plant_loop_connections [number]
plant_connection_1_inlet_node_name [string]
plant_connection_1_outlet_node_name [string]
plant_connection_2_inlet_node_name [string]
plant_connection_2_outlet_node_name [string]
supply_inlet_water_storage_tank_name [string]
collection_outlet_water_storage_tank_name [string]
ambient_zone_name [string]
Coil:UserDefined
Defines a generic air system component for custom modeling using Energy Management System or External Interface

Fields

overall_model_simulation_program_calling_manager_name [string]
model_setup_and_sizing_program_calling_manager_name [string]
number_of_air_connections [number]
air_connection_1_inlet_node_name [string]
air_connection_1_outlet_node_name [string]
air_connection_2_inlet_node_name [string]
air_connection_2_outlet_node_name [string]
plant_connection_is_used [string]
plant_connection_inlet_node_name [string]
plant_connection_outlet_node_name [string]
supply_inlet_water_storage_tank_name [string]
collection_outlet_water_storage_tank_name [string]
ambient_zone_name [string]
PlantComponent:UserDefined
Defines a generic plant component for custom modeling using Energy Management System or External Interface

Fields

main_model_program_calling_manager_name [string]
number_of_plant_loop_connections [number]
plant_connection_1_inlet_node_name [string]
plant_connection_1_outlet_node_name [string]
plant_connection_1_loading_mode [string]
plant_connection_1_loop_flow_request_mode [string]
plant_connection_1_initialization_program_calling_manager_name [string]
plant_connection_1_simulation_program_calling_manager_name [string]
plant_connection_2_inlet_node_name [string]
plant_connection_2_outlet_node_name [string]
plant_connection_2_loading_mode [string]
plant_connection_2_loop_flow_request_mode [string]
plant_connection_2_initialization_program_calling_manager_name [string]
plant_connection_2_simulation_program_calling_manager_name [string]
plant_connection_3_inlet_node_name [string]
plant_connection_3_outlet_node_name [string]
plant_connection_3_loading_mode [string]
plant_connection_3_loop_flow_request_mode [string]
plant_connection_3_initialization_program_calling_manager_name [string]
plant_connection_3_simulation_program_calling_manager_name [string]
plant_connection_4_inlet_node_name [string]
plant_connection_4_outlet_node_name [string]
plant_connection_4_loading_mode [string]
plant_connection_4_loop_flow_request_mode [string]
plant_connection_4_initialization_program_calling_manager_name [string]
plant_connection_4_simulation_program_calling_manager_name [string]
air_connection_inlet_node_name [string]
air_connection_outlet_node_name [string]
supply_inlet_water_storage_tank_name [string]
collection_outlet_water_storage_tank_name [string]
ambient_zone_name [string]
PlantEquipmentOperation:UserDefined
Defines a generic plant operation scheme for custom supervisory control using Energy Management System or External Interface to dispatch loads

Fields

main_model_program_calling_manager_name [string]
initialization_program_calling_manager_name [string]
equipment_1_object_type [string]
equipment_1_name [string]
equipment_2_object_type [string]
equipment_2_name [string]
equipment_3_object_type [string]
equipment_3_name [string]
equipment_4_object_type [string]
equipment_4_name [string]
equipment_5_object_type [string]
equipment_5_name [string]
equipment_6_object_type [string]
equipment_6_name [string]
equipment_7_object_type [string]
equipment_7_name [string]
equipment_8_object_type [string]
equipment_8_name [string]
equipment_9_object_type [string]
equipment_9_name [string]
equipment_10_object_type [string]
equipment_10_name [string]
"""