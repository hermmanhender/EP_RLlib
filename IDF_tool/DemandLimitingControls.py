"""
# Demand Limiting Controls
"""
"""
DemandManagerAssignmentList
a list of meters that can be reported are available after a run on the meter dictionary file (.mdd) if the Output:VariableDictionary has been requested.

Fields

meter_name [string]
demand_limit_schedule_name [string]
demand_limit_safety_fraction [number]
billing_period_schedule_name [string]
peak_period_schedule_name [string]
demand_window_length [number]
demand_manager_priority [string]
manager_data [Array of {demandmanager_object_type, demandmanager_name}]
DemandManager:ExteriorLights
used for demand limiting Exterior:Lights objects.

Fields

availability_schedule_name [string]
limit_control [string]
minimum_limit_duration [number]
maximum_limit_fraction [number]
limit_step_change [number]
selection_control [string]
rotation_duration [number]
lights [Array of {exterior_lights_name}]
DemandManager:Lights
used for demand limiting Lights objects.

Fields

availability_schedule_name [string]
limit_control [string]
minimum_limit_duration [number]
maximum_limit_fraction [number]
limit_step_change [number]
selection_control [string]
rotation_duration [number]
lights [Array of {lights_name}]
DemandManager:ElectricEquipment
used for demand limiting ElectricEquipment objects.

Fields

availability_schedule_name [string]
limit_control [string]
minimum_limit_duration [number]
maximum_limit_fraction [number]
limit_step_change [number]
selection_control [string]
rotation_duration [number]
equipment [Array of {electric_equipment_name}]
DemandManager:Thermostats
used for demand limiting ZoneControl:Thermostat objects.

Fields

availability_schedule_name [string]
reset_control [string]
minimum_reset_duration [number]
maximum_heating_setpoint_reset [number]
maximum_cooling_setpoint_reset [number]
reset_step_change [number]
selection_control [string]
rotation_duration [number]
thermostats [Array of {thermostat_name}]
DemandManager:Ventilation
used for demand limiting Controller:OutdoorAir objects.

Fields

availability_schedule_name [string]
limit_control [string]
minimum_limit_duration [number]
fixed_rate [number]
reduction_ratio [number]
limit_step_change [number]
selection_control [string] (Default: All)
rotation_duration [number]
controllers [Array of {controller_outdoor_air_name}]
"""