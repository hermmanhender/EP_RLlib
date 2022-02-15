"""
# Zone HVAC Air Loop Terminal Units
"""
"""
AirTerminal:SingleDuct:ConstantVolume:Reheat
Central air system terminal unit, single duct, constant volume, with reheat coil (hot water, electric, gas, or steam).

Fields

availability_schedule_name [string]
air_outlet_node_name [string]
air_inlet_node_name [string]
maximum_air_flow_rate [unknown field type]
reheat_coil_object_type [string]
reheat_coil_name [string]
maximum_hot_water_or_steam_flow_rate [unknown field type]
minimum_hot_water_or_steam_flow_rate [number] (Default: 0.0)
convergence_tolerance [number] (Default: 0.001)
maximum_reheat_air_temperature [number]
AirTerminal:SingleDuct:ConstantVolume:NoReheat
Central air system terminal unit, single duct, constant volume, without reheat coil

Fields

availability_schedule_name [string]
air_inlet_node_name [string]
air_outlet_node_name [string]
maximum_air_flow_rate [unknown field type]
design_specification_outdoor_air_object_name [string]
per_person_ventilation_rate_mode [string] (Default: CurrentOccupancy)
AirTerminal:SingleDuct:VAV:NoReheat
Central air system terminal unit, single duct, variable volume, with no reheat coil.

Fields

availability_schedule_name [string]
air_outlet_node_name [string]
air_inlet_node_name [string]
maximum_air_flow_rate [unknown field type]
zone_minimum_air_flow_input_method [string] (Default: Constant)
constant_minimum_air_flow_fraction [unknown field type] (Default: Autosize)
fixed_minimum_air_flow_rate [unknown field type] (Default: Autosize)
minimum_air_flow_fraction_schedule_name [string]
design_specification_outdoor_air_object_name [string]
minimum_air_flow_turndown_schedule_name [string]
AirTerminal:SingleDuct:VAV:Reheat
Central air system terminal unit, single duct, variable volume, with reheat coil (hot water, electric, gas, or steam).

Fields

availability_schedule_name [string]
damper_air_outlet_node_name [string]
air_inlet_node_name [string]
maximum_air_flow_rate [unknown field type]
zone_minimum_air_flow_input_method [string] (Default: Constant)
constant_minimum_air_flow_fraction [unknown field type] (Default: Autosize)
fixed_minimum_air_flow_rate [unknown field type] (Default: Autosize)
minimum_air_flow_fraction_schedule_name [string]
reheat_coil_object_type [string]
reheat_coil_name [string]
maximum_hot_water_or_steam_flow_rate [unknown field type]
minimum_hot_water_or_steam_flow_rate [number] (Default: 0.0)
air_outlet_node_name [string]
convergence_tolerance [number] (Default: 0.001)
damper_heating_action [string] (Default: ReverseWithLimits)
maximum_flow_per_zone_floor_area_during_reheat [unknown field type] (Default: Autosize)
maximum_flow_fraction_during_reheat [unknown field type] (Default: Autosize)
maximum_reheat_air_temperature [number]
design_specification_outdoor_air_object_name [string]
minimum_air_flow_turndown_schedule_name [string]
AirTerminal:SingleDuct:VAV:Reheat:VariableSpeedFan
Central air system terminal unit, single duct, variable volume, with reheat coil (hot water, electric, gas, or steam) and variable-speed fan. These units are usually employed in underfloor air distribution (UFAD) systems where the air is supplied at low static pressure through an underfloor plenum. The fan is used to control the flow of conditioned air that enters the space.

Fields

availability_schedule_name [string]
maximum_cooling_air_flow_rate [unknown field type]
maximum_heating_air_flow_rate [unknown field type]
zone_minimum_air_flow_fraction [number]
air_inlet_node_name [string]
air_outlet_node_name [string]
fan_object_type [string]
fan_name [string]
heating_coil_object_type [string]
heating_coil_name [string]
maximum_hot_water_or_steam_flow_rate [unknown field type]
minimum_hot_water_or_steam_flow_rate [number] (Default: 0.0)
heating_convergence_tolerance [number] (Default: 0.001)
minimum_air_flow_turndown_schedule_name [string]
AirTerminal:SingleDuct:VAV:HeatAndCool:NoReheat
Central air system terminal unit, single duct, variable volume for both cooling and heating, with no reheat coil.

Fields

availability_schedule_name [string]
air_outlet_node_name [string]
air_inlet_node_name [string]
maximum_air_flow_rate [unknown field type]
zone_minimum_air_flow_fraction [number]
minimum_air_flow_turndown_schedule_name [string]
AirTerminal:SingleDuct:VAV:HeatAndCool:Reheat
Central air system terminal unit, single duct, variable volume for both cooling and heating, with reheat coil (hot water, electric, gas, or steam).

Fields

availability_schedule_name [string]
damper_air_outlet_node_name [string]
air_inlet_node_name [string]
maximum_air_flow_rate [unknown field type]
zone_minimum_air_flow_fraction [number]
reheat_coil_object_type [string]
reheat_coil_name [string]
maximum_hot_water_or_steam_flow_rate [unknown field type]
minimum_hot_water_or_steam_flow_rate [number] (Default: 0.0)
air_outlet_node_name [string]
convergence_tolerance [number] (Default: 0.001)
maximum_reheat_air_temperature [number]
minimum_air_flow_turndown_schedule_name [string]
AirTerminal:SingleDuct:SeriesPIU:Reheat
Central air system terminal unit, single duct, variable volume, series powered induction unit (PIU), with reheat coil (hot water, electric, gas, or steam).

Fields

availability_schedule_name [string]
maximum_air_flow_rate [unknown field type]
maximum_primary_air_flow_rate [unknown field type]
minimum_primary_air_flow_fraction [unknown field type]
supply_air_inlet_node_name [string]
secondary_air_inlet_node_name [string]
outlet_node_name [string]
reheat_coil_air_inlet_node_name [string]
zone_mixer_name [string]
fan_name [string]
reheat_coil_object_type [string]
reheat_coil_name [string]
maximum_hot_water_or_steam_flow_rate [unknown field type]
minimum_hot_water_or_steam_flow_rate [number] (Default: 0.0)
convergence_tolerance [number] (Default: 0.001)
AirTerminal:SingleDuct:ParallelPIU:Reheat
Central air system terminal unit, single duct, variable volume, parallel powered induction unit (PIU), with reheat coil (hot water, electric, gas, or steam).

Fields

availability_schedule_name [string]
maximum_primary_air_flow_rate [unknown field type]
maximum_secondary_air_flow_rate [unknown field type]
minimum_primary_air_flow_fraction [unknown field type]
fan_on_flow_fraction [unknown field type]
supply_air_inlet_node_name [string]
secondary_air_inlet_node_name [string]
outlet_node_name [string]
reheat_coil_air_inlet_node_name [string]
zone_mixer_name [string]
fan_name [string]
reheat_coil_object_type [string]
reheat_coil_name [string]
maximum_hot_water_or_steam_flow_rate [unknown field type]
minimum_hot_water_or_steam_flow_rate [number] (Default: 0.0)
convergence_tolerance [number] (Default: 0.001)
AirTerminal:SingleDuct:ConstantVolume:FourPipeInduction
Central air system terminal unit, single duct, variable volume, induction unit with hot water reheat coil and chilled water recool coil.

Fields

availability_schedule_name [string]
maximum_total_air_flow_rate [unknown field type]
induction_ratio [number] (Default: 2.5)
supply_air_inlet_node_name [string]
induced_air_inlet_node_name [string]
air_outlet_node_name [string]
heating_coil_object_type [string]
heating_coil_name [string]
maximum_hot_water_flow_rate [unknown field type]
minimum_hot_water_flow_rate [number] (Default: 0.0)
heating_convergence_tolerance [number] (Default: 0.001)
cooling_coil_object_type [string]
cooling_coil_name [string]
maximum_cold_water_flow_rate [unknown field type]
minimum_cold_water_flow_rate [number] (Default: 0.0)
cooling_convergence_tolerance [number] (Default: 0.001)
zone_mixer_name [string]
AirTerminal:SingleDuct:ConstantVolume:FourPipeBeam
Central air system terminal unit, single duct, constant volume, with heating and/or cooling. Operates as two-pipe unit if heating or cooling water is omitted. Heating and/or cooling can be scheduled off for dedicated ventilation.

Fields

primary_air_availability_schedule_name [string]
cooling_availability_schedule_name [string]
heating_availability_schedule_name [string]
primary_air_inlet_node_name [string]
primary_air_outlet_node_name [string]
chilled_water_inlet_node_name [string]
chilled_water_outlet_node_name [string]
hot_water_inlet_node_name [string]
hot_water_outlet_node_name [string]
design_primary_air_volume_flow_rate [unknown field type] (Default: Autosize)
design_chilled_water_volume_flow_rate [unknown field type] (Default: Autosize)
design_hot_water_volume_flow_rate [unknown field type] (Default: Autosize)
zone_total_beam_length [unknown field type] (Default: Autosize)
rated_primary_air_flow_rate_per_beam_length [number] (Default: 0.035)
beam_rated_cooling_capacity_per_beam_length [number] (Default: 600.0)
beam_rated_cooling_room_air_chilled_water_temperature_difference [number] (Default: 10.0)
beam_rated_chilled_water_volume_flow_rate_per_beam_length [number] (Default: 5e-05)
beam_cooling_capacity_temperature_difference_modification_factor_curve_name [string]
beam_cooling_capacity_air_flow_modification_factor_curve_name [string]
beam_cooling_capacity_chilled_water_flow_modification_factor_curve_name [string]
beam_rated_heating_capacity_per_beam_length [number] (Default: 1500.0)
beam_rated_heating_room_air_hot_water_temperature_difference [number] (Default: 27.8)
beam_rated_hot_water_volume_flow_rate_per_beam_length [number] (Default: 5e-05)
beam_heating_capacity_temperature_difference_modification_factor_curve_name [string]
beam_heating_capacity_air_flow_modification_factor_curve_name [string]
beam_heating_capacity_hot_water_flow_modification_factor_curve_name [string]
AirTerminal:SingleDuct:ConstantVolume:CooledBeam
Central air system terminal unit, single duct, constant volume, with cooled beam (active or passive).

Fields

availability_schedule_name [string]
cooled_beam_type [string]
supply_air_inlet_node_name [string]
supply_air_outlet_node_name [string]
chilled_water_inlet_node_name [string]
chilled_water_outlet_node_name [string]
supply_air_volumetric_flow_rate [unknown field type] (Default: Autosize)
maximum_total_chilled_water_volumetric_flow_rate [unknown field type] (Default: Autosize)
number_of_beams [unknown field type] (Default: Autosize)
beam_length [unknown field type] (Default: Autosize)
design_inlet_water_temperature [number] (Default: 15.0)
design_outlet_water_temperature [number] (Default: 17.0)
coil_surface_area_per_coil_length [number] (Default: 5.422)
model_parameter_a [number] (Default: 15.3)
model_parameter_n1 [number] (Default: 0.0)
model_parameter_n2 [number] (Default: 0.84)
model_parameter_n3 [number] (Default: 0.12)
model_parameter_a0 [number] (Default: 0.171)
model_parameter_k1 [number] (Default: 0.0057)
model_parameter_n [number] (Default: 0.4)
coefficient_of_induction_kin [unknown field type] (Default: Autocalculate)
leaving_pipe_inside_diameter [number] (Default: 0.0145)
AirTerminal:SingleDuct:Mixer
The mixer air terminal unit provides a means of supplying central system air to the air inlet or outlet side of a zoneHVAC equipment such as a four pipe fan coil unit. Normally the central air would be ventilation air from a dedicated outdoor air system (DOAS).

Fields

zonehvac_unit_object_type [string]
zonehvac_unit_object_name [string]
mixer_outlet_node_name [string]
mixer_primary_air_inlet_node_name [string]
mixer_secondary_air_inlet_node_name [string]
mixer_connection_type [string]
design_specification_outdoor_air_object_name [string]
per_person_ventilation_rate_mode [string] (Default: CurrentOccupancy)
AirTerminal:DualDuct:ConstantVolume
Central air system terminal unit, dual duct, constant volume.

Fields

availability_schedule_name [string]
air_outlet_node_name [string]
hot_air_inlet_node_name [string]
cold_air_inlet_node_name [string]
maximum_air_flow_rate [unknown field type]
AirTerminal:DualDuct:VAV
Central air system terminal unit, dual duct, variable volume.

Fields

availability_schedule_name [string]
air_outlet_node_name [string]
hot_air_inlet_node_name [string]
cold_air_inlet_node_name [string]
maximum_damper_air_flow_rate [unknown field type]
zone_minimum_air_flow_fraction [number] (Default: 0.2)
design_specification_outdoor_air_object_name [string]
minimum_air_flow_turndown_schedule_name [string]
AirTerminal:DualDuct:VAV:OutdoorAir
Central air system terminal unit, dual duct, variable volume with special controls. One VAV duct is controlled to supply ventilation air and the other VAV duct is controlled to meet the zone cooling load.

Fields

availability_schedule_name [string]
air_outlet_node_name [string]
outdoor_air_inlet_node_name [string]
recirculated_air_inlet_node_name [string]
maximum_terminal_air_flow_rate [unknown field type]
design_specification_outdoor_air_object_name [string]
per_person_ventilation_rate_mode [string]
ZoneHVAC:AirDistributionUnit
Central air system air distribution unit, serves as a wrapper for a specific type of air terminal unit. This object is referenced in a ZoneHVAC:EquipmentList.

Fields

air_distribution_unit_outlet_node_name [string]
air_terminal_object_type [string]
air_terminal_name [string]
nominal_upstream_leakage_fraction [number] (Default: 0.0)
constant_downstream_leakage_fraction [number] (Default: 0.0)
design_specification_air_terminal_sizing_object_name [string]
"""