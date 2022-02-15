"""
# Plant-Condenser Control
"""
"""
PlantEquipmentList
List plant equipment in order of operating priority, 1st in list will be used 1st, etc Use only plant equipment in this list. If no equipment object types and equipment names are specified, then the corresponding PlantEquipmentOperation:* object will assume all available plant equipment for the loop should be OFF (not operate) within the specified lower/upper limit.

Fields

equipment [Array of {equipment_object_type, equipment_name}]
CondenserEquipmentList
List condenser equipment in order of operating priority, 1st in list will be used 1st, etc Use only condenser equipment in this list. If no equipment object types and equipment names are specified, then the corresponding PlantEquipmentOperation:* object will assume all available condenser equipment for the loop should be OFF (not operate) within the specified lower/upper limit.

Fields

equipment [Array of {equipment_object_type, equipment_name}]
PlantEquipmentOperation:Uncontrolled
Plant equipment operation scheme for uncontrolled operation. Specifies a group of equipment that runs if the loop is active, unless turned off by the loop flow resolver to maintain continuity in the fluid loop.

Fields

equipment_list_name [string]
PlantEquipmentOperation:CoolingLoad
Plant equipment operation scheme for cooling load range operation. Specifies one or more groups of equipment which are available to operate for successive cooling load ranges.

Fields

load_range_1_lower_limit [number]
load_range_1_upper_limit [number]
range_1_equipment_list_name [string]
load_range_2_lower_limit [number]
load_range_2_upper_limit [number]
range_2_equipment_list_name [string]
load_range_3_lower_limit [number]
load_range_3_upper_limit [number]
range_3_equipment_list_name [string]
load_range_4_lower_limit [number]
load_range_4_upper_limit [number]
range_4_equipment_list_name [string]
load_range_5_lower_limit [number]
load_range_5_upper_limit [number]
range_5_equipment_list_name [string]
load_range_6_lower_limit [number]
load_range_6_upper_limit [number]
range_6_equipment_list_name [string]
load_range_7_lower_limit [number]
load_range_7_upper_limit [number]
range_7_equipment_list_name [string]
load_range_8_lower_limit [number]
load_range_8_upper_limit [number]
range_8_equipment_list_name [string]
load_range_9_lower_limit [number]
load_range_9_upper_limit [number]
range_9_equipment_list_name [string]
load_range_10_lower_limit [number]
load_range_10_upper_limit [number]
range_10_equipment_list_name [string]
PlantEquipmentOperation:HeatingLoad
Plant equipment operation scheme for heating load range operation. Specifies one or more groups of equipment which are available to operate for successive heating load ranges.

Fields

load_range_1_lower_limit [number]
load_range_1_upper_limit [number]
range_1_equipment_list_name [string]
load_range_2_lower_limit [number]
load_range_2_upper_limit [number]
range_2_equipment_list_name [string]
load_range_3_lower_limit [number]
load_range_3_upper_limit [number]
range_3_equipment_list_name [string]
load_range_4_lower_limit [number]
load_range_4_upper_limit [number]
range_4_equipment_list_name [string]
load_range_5_lower_limit [number]
load_range_5_upper_limit [number]
range_5_equipment_list_name [string]
load_range_6_lower_limit [number]
load_range_6_upper_limit [number]
range_6_equipment_list_name [string]
load_range_7_lower_limit [number]
load_range_7_upper_limit [number]
range_7_equipment_list_name [string]
load_range_8_lower_limit [number]
load_range_8_upper_limit [number]
range_8_equipment_list_name [string]
load_range_9_lower_limit [number]
load_range_9_upper_limit [number]
range_9_equipment_list_name [string]
load_range_10_lower_limit [number]
load_range_10_upper_limit [number]
range_10_equipment_list_name [string]
PlantEquipmentOperation:OutdoorDryBulb
Plant equipment operation scheme for outdoor dry-bulb temperature range operation. Specifies one or more groups of equipment which are available to operate for successive outdoor dry-bulb temperature ranges.

Fields

dry_bulb_temperature_range_1_lower_limit [number]
dry_bulb_temperature_range_1_upper_limit [number]
range_1_equipment_list_name [string]
dry_bulb_temperature_range_2_lower_limit [number]
dry_bulb_temperature_range_2_upper_limit [number]
range_2_equipment_list_name [string]
dry_bulb_temperature_range_3_lower_limit [number]
dry_bulb_temperature_range_3_upper_limit [number]
range_3_equipment_list_name [string]
dry_bulb_temperature_range_4_lower_limit [number]
dry_bulb_temperature_range_4_upper_limit [number]
range_4_equipment_list_name [string]
dry_bulb_temperature_range_5_lower_limit [number]
dry_bulb_temperature_range_5_upper_limit [number]
range_5_equipment_list_name [string]
dry_bulb_temperature_range_6_lower_limit [number]
dry_bulb_temperature_range_6_upper_limit [number]
range_6_equipment_list_name [string]
dry_bulb_temperature_range_7_lower_limit [number]
dry_bulb_temperature_range_7_upper_limit [number]
range_7_equipment_list_name [string]
dry_bulb_temperature_range_8_lower_limit [number]
dry_bulb_temperature_range_8_upper_limit [number]
range_8_equipment_list_name [string]
dry_bulb_temperature_range_9_lower_limit [number]
dry_bulb_temperature_range_9_upper_limit [number]
range_9_equipment_list_name [string]
dry_bulb_temperature_range_10_lower_limit [number]
dry_bulb_temperature_range_10_upper_limit [number]
range_10_equipment_list_name [string]
PlantEquipmentOperation:OutdoorWetBulb
Plant equipment operation scheme for outdoor wet-bulb temperature range operation. Specifies one or more groups of equipment which are available to operate for successive outdoor wet-bulb temperature ranges.

Fields

wet_bulb_temperature_range_1_lower_limit [number]
wet_bulb_temperature_range_1_upper_limit [number]
range_1_equipment_list_name [string]
wet_bulb_temperature_range_2_lower_limit [number]
wet_bulb_temperature_range_2_upper_limit [number]
range_2_equipment_list_name [string]
wet_bulb_temperature_range_3_lower_limit [number]
wet_bulb_temperature_range_3_upper_limit [number]
range_3_equipment_list_name [string]
wet_bulb_temperature_range_4_lower_limit [number]
wet_bulb_temperature_range_4_upper_limit [number]
range_4_equipment_list_name [string]
wet_bulb_temperature_range_5_lower_limit [number]
wet_bulb_temperature_range_5_upper_limit [number]
range_5_equipment_list_name [string]
wet_bulb_temperature_range_6_lower_limit [number]
wet_bulb_temperature_range_6_upper_limit [number]
range_6_equipment_list_name [string]
wet_bulb_temperature_range_7_lower_limit [number]
wet_bulb_temperature_range_7_upper_limit [number]
range_7_equipment_list_name [string]
wet_bulb_temperature_range_8_lower_limit [number]
wet_bulb_temperature_range_8_upper_limit [number]
range_8_equipment_list_name [string]
wet_bulb_temperature_range_9_lower_limit [number]
wet_bulb_temperature_range_9_upper_limit [number]
range_9_equipment_list_name [string]
wet_bulb_temperature_range_10_lower_limit [number]
wet_bulb_temperature_range_10_upper_limit [number]
range_10_equipment_list_name [string]
PlantEquipmentOperation:OutdoorRelativeHumidity
Plant equipment operation scheme for outdoor relative humidity range operation. Specifies one or more groups of equipment which are available to operate for successive outdoor relative humidity ranges.

Fields

relative_humidity_range_1_lower_limit [number]
relative_humidity_range_1_upper_limit [number]
range_1_equipment_list_name [string]
relative_humidity_range_2_lower_limit [number]
relative_humidity_range_2_upper_limit [number]
range_2_equipment_list_name [string]
relative_humidity_range_3_lower_limit [number]
relative_humidity_range_3_upper_limit [number]
range_3_equipment_list_name [string]
relative_humidity_range_4_lower_limit [number]
relative_humidity_range_4_upper_limit [number]
range_4_equipment_list_name [string]
relative_humidity_range_5_lower_limit [number]
relative_humidity_range_5_upper_limit [number]
range_5_equipment_list_name [string]
relative_humidity_range_6_lower_limit [number]
relative_humidity_range_6_upper_limit [number]
range_6_equipment_list_name [string]
relative_humidity_range_7_lower_limit [number]
relative_humidity_range_7_upper_limit [number]
range_7_equipment_list_name [string]
relative_humidity_range_8_lower_limit [number]
relative_humidity_range_8_upper_limit [number]
range_8_equipment_list_name [string]
relative_humidity_range_9_lower_limit [number]
relative_humidity_range_9_upper_limit [number]
range_9_equipment_list_name [string]
relative_humidity_range_10_lower_limit [number]
relative_humidity_range_10_upper_limit [number]
range_10_equipment_list_name [string]
PlantEquipmentOperation:OutdoorDewpoint
Plant equipment operation scheme for outdoor dewpoint temperature range operation. Specifies one or more groups of equipment which are available to operate for successive outdoor dewpoint temperature ranges.

Fields

dewpoint_temperature_range_1_lower_limit [number]
dewpoint_temperature_range_1_upper_limit [number]
range_1_equipment_list_name [string]
dewpoint_temperature_range_2_lower_limit [number]
dewpoint_temperature_range_2_upper_limit [number]
range_2_equipment_list_name [string]
dewpoint_temperature_range_3_lower_limit [number]
dewpoint_temperature_range_3_upper_limit [number]
range_3_equipment_list_name [string]
dewpoint_temperature_range_4_lower_limit [number]
dewpoint_temperature_range_4_upper_limit [number]
range_4_equipment_list_name [string]
dewpoint_temperature_range_5_lower_limit [number]
dewpoint_temperature_range_5_upper_limit [number]
range_5_equipment_list_name [string]
dewpoint_temperature_range_6_lower_limit [number]
dewpoint_temperature_range_6_upper_limit [number]
range_6_equipment_list_name [string]
dewpoint_temperature_range_7_lower_limit [number]
dewpoint_temperature_range_7_upper_limit [number]
range_7_equipment_list_name [string]
dewpoint_temperature_range_8_lower_limit [number]
dewpoint_temperature_range_8_upper_limit [number]
range_8_equipment_list_name [string]
dewpoint_temperature_range_9_lower_limit [number]
dewpoint_temperature_range_9_upper_limit [number]
range_9_equipment_list_name [string]
dewpoint_temperature_range_10_lower_limit [number]
dewpoint_temperature_range_10_upper_limit [number]
range_10_equipment_list_name [string]
PlantEquipmentOperation:ComponentSetpoint
Plant equipment operation scheme for component setpoint operation. Specifies one or pieces of equipment which are controlled to meet the temperature setpoint at the component outlet node.

Fields

equipment_1_object_type [string]
equipment_1_name [string]
demand_calculation_1_node_name [string]
setpoint_1_node_name [string]
component_1_flow_rate [unknown field type]
operation_1_type [string]
equipment_2_object_type [string]
equipment_2_name [string]
demand_calculation_2_node_name [string]
setpoint_2_node_name [string]
component_2_flow_rate [unknown field type]
operation_2_type [string]
equipment_3_object_type [string]
equipment_3_name [string]
demand_calculation_3_node_name [string]
setpoint_3_node_name [string]
component_3_flow_rate [unknown field type]
operation_3_type [string]
equipment_4_object_type [string]
equipment_4_name [string]
demand_calculation_4_node_name [string]
setpoint_4_node_name [string]
component_4_flow_rate [unknown field type]
operation_4_type [string]
equipment_5_object_type [string]
equipment_5_name [string]
demand_calculation_5_node_name [string]
setpoint_5_node_name [string]
component_5_flow_rate [unknown field type]
operation_5_type [string]
equipment_6_object_type [string]
equipment_6_name [string]
demand_calculation_6_node_name [string]
setpoint_6_node_name [string]
component_6_flow_rate [unknown field type]
operation_6_type [string]
equipment_7_object_type [string]
equipment_7_name [string]
demand_calculation_7_node_name [string]
setpoint_7_node_name [string]
component_7_flow_rate [unknown field type]
operation_7_type [string]
equipment_8_object_type [string]
equipment_8_name [string]
demand_calculation_8_node_name [string]
setpoint_8_node_name [string]
component_8_flow_rate [unknown field type]
operation_8_type [string]
equipment_9_object_type [string]
equipment_9_name [string]
demand_calculation_9_node_name [string]
setpoint_9_node_name [string]
component_9_flow_rate [unknown field type]
operation_9_type [string]
equipment_10_object_type [string]
equipment_10_name [string]
demand_calculation_10_node_name [string]
setpoint_10_node_name [string]
component_10_flow_rate [unknown field type]
operation_10_type [string]
PlantEquipmentOperation:ThermalEnergyStorage
Plant equipment operation scheme for simpler input to control thermal (ice) energy storage systems. It replaces a host of setpoint managers with simple, single input values. For more complex controls, use the ComponentSetpoint scheme.

Fields

on_peak_schedule [string]
charging_availability_schedule [string]
non_charging_chilled_water_temperature [number]
charging_chilled_water_temperature [number]
component_1_object_type [string]
component_1_name [string]
component_1_demand_calculation_node_name [string]
component_1_setpoint_node_name [string]
component_1_flow_rate [unknown field type]
component_1_operation_type [string]
component_2_object_type [string]
component_2_name [string]
component_2_demand_calculation_node_name [string]
component_2_setpoint_node_name [string]
component_2_flow_rate [unknown field type]
component_2_operation_type [string]
component_3_object_type [string]
component_3_name [string]
component_3_demand_calculation_node_name [string]
component_3_setpoint_node_name [string]
component_3_flow_rate [unknown field type]
component_3_operation_type [string]
component_4_object_type [string]
component_4_name [string]
component_4_demand_calculation_node_name [string]
component_4_setpoint_node_name [string]
component_4_flow_rate [unknown field type]
component_4_operation_type [string]
component_5_object_type [string]
component_5_name [string]
component_5_demand_calculation_node_name [string]
component_5_setpoint_node_name [string]
component_5_flow_rate [unknown field type]
component_5_operation_type [string]
component_6_object_type [string]
component_6_name [string]
component_6_demand_calculation_node_name [string]
component_6_setpoint_node_name [string]
component_6_flow_rate [unknown field type]
component_6_operation_type [string]
component_7_object_type [string]
component_7_name [string]
component_7_demand_calculation_node_name [string]
component_7_setpoint_node_name [string]
component_7_flow_rate [unknown field type]
component_7_operation_type [string]
component_8_object_type [string]
component_8_name [string]
component_8_demand_calculation_node_name [string]
component_8_setpoint_node_name [string]
component_8_flow_rate [unknown field type]
component_8_operation_type [string]
component_9_object_type [string]
component_9_name [string]
component_9_demand_calculation_node_name [string]
component_9_setpoint_node_name [string]
component_9_flow_rate [unknown field type]
component_9_operation_type [string]
component_10_object_type [string]
component_10_name [string]
component_10_demand_calculation_node_name [string]
component_10_setpoint_node_name [string]
component_10_flow_rate [unknown field type]
component_10_operation_type [string]
PlantEquipmentOperation:OutdoorDryBulbDifference
Plant equipment operation scheme for outdoor dry-bulb temperature difference operation. Specifies one or more groups of equipment which are available to operate for successive ranges based the difference between a reference node temperature and the outdoor dry-bulb temperature.

Fields

reference_temperature_node_name [string]
dry_bulb_temperature_difference_range_1_lower_limit [number]
dry_bulb_temperature_difference_range_1_upper_limit [number]
range_1_equipment_list_name [string]
dry_bulb_temperature_difference_range_2_lower_limit [number]
dry_bulb_temperature_difference_range_2_upper_limit [number]
range_2_equipment_list_name [string]
dry_bulb_temperature_difference_range_3_lower_limit [number]
dry_bulb_temperature_difference_range_3_upper_limit [number]
range_3_equipment_list_name [string]
dry_bulb_temperature_difference_range_4_lower_limit [number]
dry_bulb_temperature_difference_range_4_upper_limit [number]
range_4_equipment_list_name [string]
dry_bulb_temperature_difference_range_5_lower_limit [number]
dry_bulb_temperature_difference_range_5_upper_limit [number]
range_5_equipment_list_name [string]
dry_bulb_temperature_difference_range_6_lower_limit [number]
dry_bulb_temperature_difference_range_6_upper_limit [number]
range_6_equipment_list_name [string]
dry_bulb_temperature_difference_range_7_lower_limit [number]
dry_bulb_temperature_difference_range_7_upper_limit [number]
range_7_equipment_list_name [string]
dry_bulb_temperature_difference_range_8_lower_limit [number]
dry_bulb_temperature_difference_range_8_upper_limit [number]
range_8_equipment_list_name [string]
dry_bulb_temperature_difference_range_9_lower_limit [number]
dry_bulb_temperature_difference_range_9_upper_limit [number]
range_9_equipment_list_name [string]
dry_bulb_temperature_difference_range_10_lower_limit [number]
dry_bulb_temperature_difference_range_10_upper_limit [number]
range_10_equipment_list_name [string]
PlantEquipmentOperation:OutdoorWetBulbDifference
Plant equipment operation scheme for outdoor wet-bulb temperature difference operation. Specifies one or more groups of equipment which are available to operate for successive ranges based the difference between a reference node temperature and the outdoor wet-bulb temperature.

Fields

reference_temperature_node_name [string]
wet_bulb_temperature_difference_range_1_lower_limit [number]
wet_bulb_temperature_difference_range_1_upper_limit [number]
range_1_equipment_list_name [string]
wet_bulb_temperature_difference_range_2_lower_limit [number]
wet_bulb_temperature_difference_range_2_upper_limit [number]
range_2_equipment_list_name [string]
wet_bulb_temperature_difference_range_3_lower_limit [number]
wet_bulb_temperature_difference_range_3_upper_limit [number]
range_3_equipment_list_name [string]
wet_bulb_temperature_difference_range_4_lower_limit [number]
wet_bulb_temperature_difference_range_4_upper_limit [number]
range_4_equipment_list_name [string]
wet_bulb_temperature_difference_range_5_lower_limit [number]
wet_bulb_temperature_difference_range_5_upper_limit [number]
range_5_equipment_list_name [string]
wet_bulb_temperature_difference_range_6_lower_limit [number]
wet_bulb_temperature_difference_range_6_upper_limit [number]
range_6_equipment_list_name [string]
wet_bulb_temperature_difference_range_7_lower_limit [number]
wet_bulb_temperature_difference_range_7_upper_limit [number]
range_7_equipment_list_name [string]
wet_bulb_temperature_difference_range_8_lower_limit [number]
wet_bulb_temperature_difference_range_8_upper_limit [number]
range_8_equipment_list_name [string]
wet_bulb_temperature_difference_range_9_lower_limit [number]
wet_bulb_temperature_difference_range_9_upper_limit [number]
range_9_equipment_list_name [string]
wet_bulb_temperature_difference_range_10_lower_limit [number]
wet_bulb_temperature_difference_range_10_upper_limit [number]
range_10_equipment_list_name [string]
PlantEquipmentOperation:OutdoorDewpointDifference
Plant equipment operation scheme for outdoor dewpoint temperature difference operation. Specifies one or more groups of equipment which are available to operate for successive ranges based the difference between a reference node temperature and the outdoor dewpoint temperature.

Fields

reference_temperature_node_name [string]
dewpoint_temperature_difference_range_1_lower_limit [number]
dewpoint_temperature_difference_range_1_upper_limit [number]
range_1_equipment_list_name [string]
dewpoint_temperature_difference_range_2_lower_limit [number]
dewpoint_temperature_difference_range_2_upper_limit [number]
range_2_equipment_list_name [string]
dewpoint_temperature_difference_range_3_lower_limit [number]
dewpoint_temperature_difference_range_3_upper_limit [number]
range_3_equipment_list_name [string]
dewpoint_temperature_difference_range_4_lower_limit [number]
dewpoint_temperature_difference_range_4_upper_limit [number]
range_4_equipment_list_name [string]
dewpoint_temperature_difference_range_5_lower_limit [number]
dewpoint_temperature_difference_range_5_upper_limit [number]
range_5_equipment_list_name [string]
dewpoint_temperature_difference_range_6_lower_limit [number]
dewpoint_temperature_difference_range_6_upper_limit [number]
range_6_equipment_list_name [string]
dewpoint_temperature_difference_range_7_lower_limit [number]
dewpoint_temperature_difference_range_7_upper_limit [number]
range_7_equipment_list_name [string]
dewpoint_temperature_difference_range_8_lower_limit [number]
dewpoint_temperature_difference_range_8_upper_limit [number]
range_8_equipment_list_name [string]
dewpoint_temperature_difference_range_9_lower_limit [number]
dewpoint_temperature_difference_range_9_upper_limit [number]
range_9_equipment_list_name [string]
dewpoint_temperature_difference_range_10_lower_limit [number]
dewpoint_temperature_difference_range_10_upper_limit [number]
range_10_equipment_list_name [string]
PlantEquipmentOperationSchemes
Operation schemes are listed in “priority” order. Note that each scheme must address the entire load and/or condition ranges for the simulation. The actual one selected for use will be the first that is “Scheduled” on. That is, if control scheme 1 is not “on” and control scheme 2 is – then control scheme 2 is selected. Only plant equipment should be listed on a Control Scheme for this item.

Fields

control_scheme_1_object_type [string]
control_scheme_1_name [string]
control_scheme_1_schedule_name [string]
control_scheme_2_object_type [string]
control_scheme_2_name [string]
control_scheme_2_schedule_name [string]
control_scheme_3_object_type [string]
control_scheme_3_name [string]
control_scheme_3_schedule_name [string]
control_scheme_4_object_type [string]
control_scheme_4_name [string]
control_scheme_4_schedule_name [string]
control_scheme_5_object_type [string]
control_scheme_5_name [string]
control_scheme_5_schedule_name [string]
control_scheme_6_object_type [string]
control_scheme_6_name [string]
control_scheme_6_schedule_name [string]
control_scheme_7_object_type [string]
control_scheme_7_name [string]
control_scheme_7_schedule_name [string]
control_scheme_8_object_type [string]
control_scheme_8_name [string]
control_scheme_8_schedule_name [string]
CondenserEquipmentOperationSchemes
Operation schemes are listed in “priority” order. Note that each scheme must address the entire load and/or condition ranges for the simulation. The actual one selected for use will be the first that is “Scheduled” on. That is, if control scheme 1 is not “on” and control scheme 2 is – then control scheme 2 is selected. Only condenser equipment should be listed on a Control Scheme for this item.

Fields

control_scheme_1_object_type [string]
control_scheme_1_name [string]
control_scheme_1_schedule_name [string]
control_scheme_2_object_type [string]
control_scheme_2_name [string]
control_scheme_2_schedule_name [string]
control_scheme_3_object_type [string]
control_scheme_3_name [string]
control_scheme_3_schedule_name [string]
control_scheme_4_object_type [string]
control_scheme_4_name [string]
control_scheme_4_schedule_name [string]
control_scheme_5_object_type [string]
control_scheme_5_name [string]
control_scheme_5_schedule_name [string]
control_scheme_6_object_type [string]
control_scheme_6_name [string]
control_scheme_6_schedule_name [string]
control_scheme_7_object_type [string]
control_scheme_7_name [string]
control_scheme_7_schedule_name [string]
control_scheme_8_object_type [string]
control_scheme_8_name [string]
control_scheme_8_schedule_name [string]
"""