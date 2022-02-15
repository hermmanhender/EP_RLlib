"""
# Humidifiers and Dehumidifiers
"""
"""
Humidifier:Steam:Electric
Electrically heated steam humidifier with fan.

Fields

availability_schedule_name [string]
rated_capacity [unknown field type]
rated_power [unknown field type]
rated_fan_power [number]
standby_power [number]
air_inlet_node_name [string]
air_outlet_node_name [string]
water_storage_tank_name [string]
Humidifier:Steam:Gas
Natural gas fired steam humidifier with optional blower fan.

Fields

availability_schedule_name [string]
rated_capacity [unknown field type]
rated_gas_use_rate [unknown field type]
thermal_efficiency [number] (Default: 0.8)
thermal_efficiency_modifier_curve_name [string]
rated_fan_power [number]
auxiliary_electric_power [number] (Default: 0.0)
air_inlet_node_name [string]
air_outlet_node_name [string]
water_storage_tank_name [string]
inlet_water_temperature_option [string] (Default: FixedInletWaterTemperature)
Dehumidifier:Desiccant:NoFans
This object models a solid desiccant dehumidifier. The process air stream is the air which is dehumidified. The regeneration air stream is the air which is heated to regenerate the desiccant. This object determines the process air outlet conditions, the load on the regeneration heating coil, the electric power consumption for the wheel rotor motor, and the regeneration air fan mass flow rate. All other heat exchangers are modeled as separate objects connected to the inlet and outlet nodes of the dehumidifier. The solid desiccant dehumidifier is typically used in an AirLoopHVAC:OutdoorAirSystem, but can also be specified in any AirLoopHVAC.

Fields

availability_schedule_name [string]
process_air_inlet_node_name [string]
process_air_outlet_node_name [string]
regeneration_air_inlet_node_name [string]
regeneration_fan_inlet_node_name [string]
control_type [string]
leaving_maximum_humidity_ratio_setpoint [number]
nominal_process_air_flow_rate [number]
nominal_process_air_velocity [number]
rotor_power [number]
regeneration_coil_object_type [string]
regeneration_coil_name [string]
regeneration_fan_object_type [string]
regeneration_fan_name [string]
performance_model_type [string]
leaving_dry_bulb_function_of_entering_dry_bulb_and_humidity_ratio_curve_name [string]
leaving_dry_bulb_function_of_air_velocity_curve_name [string]
leaving_humidity_ratio_function_of_entering_dry_bulb_and_humidity_ratio_curve_name [string]
leaving_humidity_ratio_function_of_air_velocity_curve_name [string]
regeneration_energy_function_of_entering_dry_bulb_and_humidity_ratio_curve_name [string]
regeneration_energy_function_of_air_velocity_curve_name [string]
regeneration_velocity_function_of_entering_dry_bulb_and_humidity_ratio_curve_name [string]
regeneration_velocity_function_of_air_velocity_curve_name [string]
nominal_regeneration_temperature [number]
Dehumidifier:Desiccant:System
This compound object models a desiccant heat exchanger, an optional heater, and associated fans. The process air stream is the air which is dehumidified. The regeneration air stream is the air which is heated to regenerate the desiccant. The desiccant heat exchanger transfers both sensible and latent energy between the process and regeneration air streams. The desiccant dehumidifier is typically used in an AirLoopHVAC:OutdoorAirSystem, but can also be specified in any AirLoopHVAC.

Fields

availability_schedule_name [string]
desiccant_heat_exchanger_object_type [string]
desiccant_heat_exchanger_name [string]
sensor_node_name [string]
regeneration_air_fan_object_type [string]
regeneration_air_fan_name [string]
regeneration_air_fan_placement [string] (Default: DrawThrough)
regeneration_air_heater_object_type [string]
regeneration_air_heater_name [string]
regeneration_inlet_air_setpoint_temperature [number] (Default: 46.0)
companion_cooling_coil_object_type [string]
companion_cooling_coil_name [string]
companion_cooling_coil_upstream_of_dehumidifier_process_inlet [string] (Default: No)
companion_coil_regeneration_air_heating [string] (Default: No)
exhaust_fan_maximum_flow_rate [number]
exhaust_fan_maximum_power [number]
exhaust_fan_power_curve_name [string]
"""