"""
Controllers
"""
"""
Controller:WaterCoil
Controller for a water coil which is located directly in an air loop branch or outdoor air equipment list. Controls the coil water flow to meet the specified leaving air setpoint(s). Used with Coil:Heating:Water, Coil:Cooling:Water, Coil:Cooling:Water:DetailedGeometry, and CoilSystem:Cooling:Water:HeatexchangerAssisted.

Fields

control_variable [string]
action [string]
actuator_variable [string]
sensor_node_name [string]
actuator_node_name [string]
controller_convergence_tolerance [unknown field type] (Default: Autosize)
maximum_actuated_flow [unknown field type] (Default: Autosize)
minimum_actuated_flow [number] (Default: 0.0)
Controller:OutdoorAir
Controller to set the outdoor air flow rate for an air loop. Control options include fixed, proportional, scheduled, economizer, and demand-controlled ventilation.

Fields

relief_air_outlet_node_name [string]
return_air_node_name [string]
mixed_air_node_name [string]
actuator_node_name [string]
minimum_outdoor_air_flow_rate [unknown field type]
maximum_outdoor_air_flow_rate [unknown field type]
economizer_control_type [string] (Default: NoEconomizer)
economizer_control_action_type [string] (Default: ModulateFlow)
economizer_maximum_limit_dry_bulb_temperature [number]
economizer_maximum_limit_enthalpy [number]
economizer_maximum_limit_dewpoint_temperature [number]
electronic_enthalpy_limit_curve_name [string]
economizer_minimum_limit_dry_bulb_temperature [number]
lockout_type [string] (Default: NoLockout)
minimum_limit_type [string] (Default: ProportionalMinimum)
minimum_outdoor_air_schedule_name [string]
minimum_fraction_of_outdoor_air_schedule_name [string]
maximum_fraction_of_outdoor_air_schedule_name [string]
mechanical_ventilation_controller_name [string]
time_of_day_economizer_control_schedule_name [string]
high_humidity_control [string] (Default: No)
humidistat_control_zone_name [string]
high_humidity_outdoor_air_flow_ratio [number] (Default: 1.0)
control_high_indoor_humidity_based_on_outdoor_humidity_ratio [string] (Default: Yes)
heat_recovery_bypass_control_type [string] (Default: BypassWhenWithinEconomizerLimits)
Controller:MechanicalVentilation
This object is used in conjunction with Controller:OutdoorAir to specify outdoor ventilation air based on outdoor air specified in the DesignSpecification:OutdoorAir object The Controller:OutdoorAir object is associated with a specific air loop, so the outdoor air flow rates specified in Controller:MechanicalVentilation correspond to the zones attached to that specific air loop. Duplicate groups of Zone name, Design Specification Outdoor Air Object Name, and Design Specification Zone Air Distribution Object Name to increase allowable number of entries

Fields

availability_schedule_name [string]
demand_controlled_ventilation [string] (Default: No)
system_outdoor_air_method [string] (Default: Standard62.1VentilationRateProcedure)
zone_maximum_outdoor_air_fraction [number] (Default: 1.0)
zone_specifications [Array of {zone_or_zonelist_name, design_specification_outdoor_air_object_name, design_specification_zone_air_distribution_object_name}]
AirLoopHVAC:ControllerList
List controllers in order of control sequence

Fields

controller_1_object_type [string]
controller_1_name [string]
controller_2_object_type [string]
controller_2_name [string]
controller_3_object_type [string]
controller_3_name [string]
controller_4_object_type [string]
controller_4_name [string]
controller_5_object_type [string]
controller_5_name [string]
controller_6_object_type [string]
controller_6_name [string]
controller_7_object_type [string]
controller_7_name [string]
controller_8_object_type [string]
controller_8_name [string]
"""