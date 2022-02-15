"""
# Heat Recovery
"""
"""
HeatExchanger:AirToAir:FlatPlate
Flat plate air-to-air heat exchanger, typically used for exhaust or relief air heat recovery.

Fields

availability_schedule_name [string]
flow_arrangement_type [string]
economizer_lockout [string] (Default: Yes)
ratio_of_supply_to_secondary_ha_values [number]
nominal_supply_air_flow_rate [unknown field type] (Default: Autosize)
nominal_supply_air_inlet_temperature [number]
nominal_supply_air_outlet_temperature [number]
nominal_secondary_air_flow_rate [unknown field type]
nominal_secondary_air_inlet_temperature [number]
nominal_electric_power [number]
supply_air_inlet_node_name [string]
supply_air_outlet_node_name [string]
secondary_air_inlet_node_name [string]
secondary_air_outlet_node_name [string]
HeatExchanger:AirToAir:SensibleAndLatent
This object models an air-to-air heat exchanger using effectiveness relationships. The heat exchanger can transfer sensible energy, latent energy, or both between the supply (primary) and exhaust (secondary) air streams.

Fields

availability_schedule_name [string]
nominal_supply_air_flow_rate [unknown field type]
sensible_effectiveness_at_100_heating_air_flow [number] (Default: 0.0)
latent_effectiveness_at_100_heating_air_flow [number] (Default: 0.0)
sensible_effectiveness_at_75_heating_air_flow [number] (Default: 0.0)
latent_effectiveness_at_75_heating_air_flow [number] (Default: 0.0)
sensible_effectiveness_at_100_cooling_air_flow [number] (Default: 0.0)
latent_effectiveness_at_100_cooling_air_flow [number] (Default: 0.0)
sensible_effectiveness_at_75_cooling_air_flow [number] (Default: 0.0)
latent_effectiveness_at_75_cooling_air_flow [number] (Default: 0.0)
supply_air_inlet_node_name [string]
supply_air_outlet_node_name [string]
exhaust_air_inlet_node_name [string]
exhaust_air_outlet_node_name [string]
nominal_electric_power [number] (Default: 0.0)
supply_air_outlet_temperature_control [string] (Default: No)
heat_exchanger_type [string] (Default: Plate)
frost_control_type [string] (Default: None)
threshold_temperature [number] (Default: 1.7)
initial_defrost_time_fraction [number] (Default: 0.083)
rate_of_defrost_time_fraction_increase [number] (Default: 0.012)
economizer_lockout [string] (Default: Yes)
HeatExchanger:Desiccant:BalancedFlow
This object models a balanced desiccant heat exchanger. The heat exchanger transfers both sensible and latent energy between the process and regeneration air streams. The air flow rate and face velocity are assumed to be the same on both the process and regeneration sides of the heat exchanger.

Fields

availability_schedule_name [string]
regeneration_air_inlet_node_name [string]
regeneration_air_outlet_node_name [string]
process_air_inlet_node_name [string]
process_air_outlet_node_name [string]
heat_exchanger_performance_object_type [string] (Default: HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1)
heat_exchanger_performance_name [string]
economizer_lockout [string] (Default: No)
HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1
RTO = B1 + B2*RWI + B3*RTI + B4*(RWI/RTI) + B5*PWI + B6*PTI + B7*(PWI/PTI) + B8*RFV RWO = C1 + C2*RWI + C3*RTI + C4*(RWI/RTI) + C5*PWI + C6*PTI + C7*(PWI/PTI) + C8*RFV where, RTO = Dry-bulb temperature of the regeneration outlet air (C) RWO = Humidity ratio of the regeneration outlet air (kgWater/kgDryAir) RWI = Humidity ratio of the regeneration inlet air (kgWater/kgDryAir) RTI = Dry-bulb temperature of the regeneration inlet air (C) PWI = Humidity ratio of the process inlet air (kgWater/kgDryAir) PTI = Dry-bulb temperature of the process inlet air (C) RFV = Regeneration Face Velocity (m/s)

Fields

nominal_air_flow_rate [unknown field type]
nominal_air_face_velocity [unknown field type]
nominal_electric_power [number] (Default: 0.0)
temperature_equation_coefficient_1 [number]
temperature_equation_coefficient_2 [number]
temperature_equation_coefficient_3 [number]
temperature_equation_coefficient_4 [number]
temperature_equation_coefficient_5 [number]
temperature_equation_coefficient_6 [number]
temperature_equation_coefficient_7 [number]
temperature_equation_coefficient_8 [number]
minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation [number]
maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation [number]
minimum_regeneration_inlet_air_temperature_for_temperature_equation [number]
maximum_regeneration_inlet_air_temperature_for_temperature_equation [number]
minimum_process_inlet_air_humidity_ratio_for_temperature_equation [number]
maximum_process_inlet_air_humidity_ratio_for_temperature_equation [number]
minimum_process_inlet_air_temperature_for_temperature_equation [number]
maximum_process_inlet_air_temperature_for_temperature_equation [number]
minimum_regeneration_air_velocity_for_temperature_equation [number]
maximum_regeneration_air_velocity_for_temperature_equation [number]
minimum_regeneration_outlet_air_temperature_for_temperature_equation [number]
maximum_regeneration_outlet_air_temperature_for_temperature_equation [number]
minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation [number]
maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation [number]
minimum_process_inlet_air_relative_humidity_for_temperature_equation [number]
maximum_process_inlet_air_relative_humidity_for_temperature_equation [number]
humidity_ratio_equation_coefficient_1 [number]
humidity_ratio_equation_coefficient_2 [number]
humidity_ratio_equation_coefficient_3 [number]
humidity_ratio_equation_coefficient_4 [number]
humidity_ratio_equation_coefficient_5 [number]
humidity_ratio_equation_coefficient_6 [number]
humidity_ratio_equation_coefficient_7 [number]
humidity_ratio_equation_coefficient_8 [number]
minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation [number]
maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation [number]
minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation [number]
maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation [number]
minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation [number]
maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation [number]
minimum_process_inlet_air_temperature_for_humidity_ratio_equation [number]
maximum_process_inlet_air_temperature_for_humidity_ratio_equation [number]
minimum_regeneration_air_velocity_for_humidity_ratio_equation [number]
maximum_regeneration_air_velocity_for_humidity_ratio_equation [number]
minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation [number]
maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation [number]
minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation [number]
maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation [number]
minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation [number]
maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation [number]
"""