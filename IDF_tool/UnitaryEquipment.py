"""
# Unitary Equipment
"""
"""
AirLoopHVAC:UnitarySystem
AirloopHVAC:UnitarySystem is a generic HVAC system type that allows any configuration of coils and/or fan. This object is a replacement of other AirloopHVAC objects. This object can be used in outdoor air systems, outdoor air units, air loops, and as zone equipment if desired.

Fields

control_type [string] (Default: Load)
controlling_zone_or_thermostat_location [string]
dehumidification_control_type [string] (Default: None)
availability_schedule_name [string]
air_inlet_node_name [string]
air_outlet_node_name [string]
supply_fan_object_type [string]
supply_fan_name [string]
fan_placement [string]
supply_air_fan_operating_mode_schedule_name [string]
heating_coil_object_type [string]
heating_coil_name [string]
dx_heating_coil_sizing_ratio [number] (Default: 1.0)
cooling_coil_object_type [string]
cooling_coil_name [string]
use_doas_dx_cooling_coil [string] (Default: No)
minimum_supply_air_temperature [unknown field type] (Default: 2.0)
latent_load_control [string] (Default: SensibleOnlyLoadControl)
supplemental_heating_coil_object_type [string]
supplemental_heating_coil_name [string]
cooling_supply_air_flow_rate_method [string]
cooling_supply_air_flow_rate [unknown field type]
cooling_supply_air_flow_rate_per_floor_area [number]
cooling_fraction_of_autosized_cooling_supply_air_flow_rate [number]
cooling_supply_air_flow_rate_per_unit_of_capacity [number]
heating_supply_air_flow_rate_method [string]
heating_supply_air_flow_rate [unknown field type]
heating_supply_air_flow_rate_per_floor_area [number]
heating_fraction_of_autosized_heating_supply_air_flow_rate [number]
heating_supply_air_flow_rate_per_unit_of_capacity [number]
no_load_supply_air_flow_rate_method [string]
no_load_supply_air_flow_rate [unknown field type]
no_load_supply_air_flow_rate_per_floor_area [number]
no_load_fraction_of_autosized_cooling_supply_air_flow_rate [number]
no_load_fraction_of_autosized_heating_supply_air_flow_rate [number]
no_load_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation [number]
no_load_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation [number]
maximum_supply_air_temperature [unknown field type] (Default: 80.0)
maximum_outdoor_dry_bulb_temperature_for_supplemental_heater_operation [number] (Default: 21.0)
outdoor_dry_bulb_temperature_sensor_node_name [string]
maximum_cycling_rate [number] (Default: 2.5)
heat_pump_time_constant [number] (Default: 60.0)
fraction_of_on_cycle_power_use [number] (Default: 0.01)
heat_pump_fan_delay_time [number] (Default: 60.0)
ancillary_on_cycle_electric_power [number] (Default: 0.0)
ancillary_off_cycle_electric_power [number] (Default: 0.0)
design_heat_recovery_water_flow_rate [number] (Default: 0.0)
maximum_temperature_for_heat_recovery [number] (Default: 80.0)
heat_recovery_water_inlet_node_name [string]
heat_recovery_water_outlet_node_name [string]
design_specification_multispeed_object_type [string]
design_specification_multispeed_object_name [string]
UnitarySystemPerformance:Multispeed
The UnitarySystemPerformance object is used to specify the air flow ratio at each operating speed. This object is primarily used for multispeed DX and water coils to allow operation at alternate flow rates different from those specified in the coil object.

Fields

number_of_speeds_for_heating [number]
number_of_speeds_for_cooling [number]
single_mode_operation [string] (Default: No)
no_load_supply_air_flow_rate_ratio [number] (Default: 1.0)
flow_ratios [Array of {heating_speed_supply_air_flow_ratio, cooling_speed_supply_air_flow_ratio}]
AirLoopHVAC:Unitary:Furnace:HeatOnly
Unitary system, heating-only with constant volume supply fan (continuous or cycling) and heating coil (gas, electric, hot water, or steam). Identical to AirLoopHVAC:UnitaryHeatOnly.

Fields

availability_schedule_name [string]
furnace_air_inlet_node_name [string]
furnace_air_outlet_node_name [string]
supply_air_fan_operating_mode_schedule_name [string]
maximum_supply_air_temperature [unknown field type] (Default: 80.0)
heating_supply_air_flow_rate [unknown field type]
controlling_zone_or_thermostat_location [string]
supply_fan_object_type [string]
supply_fan_name [string]
fan_placement [string] (Default: BlowThrough)
heating_coil_object_type [string]
heating_coil_name [string]
AirLoopHVAC:Unitary:Furnace:HeatCool
Unitary system, heating and cooling with constant volume supply fan (continuous or cycling), direct expansion (DX) cooling coil, heating coil (gas, electric, hot water, or steam), and optional reheat coil for dehumidification control. Identical to AirLoopHVAC:UnitaryHeatCool.

Fields

availability_schedule_name [string]
furnace_air_inlet_node_name [string]
furnace_air_outlet_node_name [string]
supply_air_fan_operating_mode_schedule_name [string]
maximum_supply_air_temperature [unknown field type] (Default: 80.0)
cooling_supply_air_flow_rate [unknown field type]
heating_supply_air_flow_rate [unknown field type]
no_load_supply_air_flow_rate [unknown field type]
controlling_zone_or_thermostat_location [string]
supply_fan_object_type [string]
supply_fan_name [string]
fan_placement [string] (Default: BlowThrough)
heating_coil_object_type [string]
heating_coil_name [string]
cooling_coil_object_type [string]
cooling_coil_name [string]
dehumidification_control_type [string] (Default: None)
reheat_coil_object_type [string]
reheat_coil_name [string]
AirLoopHVAC:UnitaryHeatOnly
Unitary system, heating-only with constant volume supply fan (continuous or cycling) and heating coil (gas, electric, hot water, or steam). Identical to AirLoopHVAC:Unitary:Furnace:HeatOnly.

Fields

availability_schedule_name [string]
unitary_system_air_inlet_node_name [string]
unitary_system_air_outlet_node_name [string]
supply_air_fan_operating_mode_schedule_name [string]
maximum_supply_air_temperature [unknown field type] (Default: 80.0)
heating_supply_air_flow_rate [unknown field type]
controlling_zone_or_thermostat_location [string]
supply_fan_object_type [string]
supply_fan_name [string]
fan_placement [string] (Default: BlowThrough)
heating_coil_object_type [string]
heating_coil_name [string]
AirLoopHVAC:UnitaryHeatCool
Unitary system, heating and cooling with constant volume supply fan (continuous or cycling), direct expansion (DX) cooling coil, heating coil (gas, electric, hot water, or steam), and optional reheat coil for dehumidification control. Identical to AirLoopHVAC:Unitary:Furnace:HeatCool.

Fields

availability_schedule_name [string]
unitary_system_air_inlet_node_name [string]
unitary_system_air_outlet_node_name [string]
supply_air_fan_operating_mode_schedule_name [string]
maximum_supply_air_temperature [unknown field type] (Default: 80.0)
cooling_supply_air_flow_rate [unknown field type]
heating_supply_air_flow_rate [unknown field type]
no_load_supply_air_flow_rate [unknown field type]
controlling_zone_or_thermostat_location [string]
supply_fan_object_type [string]
supply_fan_name [string]
fan_placement [string] (Default: BlowThrough)
heating_coil_object_type [string]
heating_coil_name [string]
cooling_coil_object_type [string]
cooling_coil_name [string]
dehumidification_control_type [string] (Default: None)
reheat_coil_object_type [string]
reheat_coil_name [string]
AirLoopHVAC:UnitaryHeatPump:AirToAir
Unitary heat pump system, heating and cooling, single-speed with supply fan, direct expansion (DX) cooling coil, DX heating coil (air-to-air heat pump), and supplemental heating coil (gas, electric, hot water, or steam).

Fields

availability_schedule_name [string]
air_inlet_node_name [string]
air_outlet_node_name [string]
cooling_supply_air_flow_rate [unknown field type]
heating_supply_air_flow_rate [unknown field type]
no_load_supply_air_flow_rate [unknown field type]
controlling_zone_or_thermostat_location [string]
supply_air_fan_object_type [string]
supply_air_fan_name [string]
heating_coil_object_type [string]
heating_coil_name [string]
cooling_coil_object_type [string]
cooling_coil_name [string]
supplemental_heating_coil_object_type [string]
supplemental_heating_coil_name [string]
maximum_supply_air_temperature_from_supplemental_heater [unknown field type]
maximum_outdoor_dry_bulb_temperature_for_supplemental_heater_operation [number] (Default: 21.0)
fan_placement [string] (Default: BlowThrough)
supply_air_fan_operating_mode_schedule_name [string]
dehumidification_control_type [string] (Default: None)
AirLoopHVAC:UnitaryHeatPump:WaterToAir
Unitary heat pump system, heating and cooling, single-speed with constant volume supply fan (continuous or cycling), direct expansion (DX) cooling coil, DX heating coil (water-to-air heat pump), and supplemental heating coil (gas, electric, hot water, or steam).

Fields

availability_schedule_name [string]
air_inlet_node_name [string]
air_outlet_node_name [string]
supply_air_flow_rate [unknown field type]
controlling_zone_or_thermostat_location [string]
supply_air_fan_object_type [string]
supply_air_fan_name [string]
heating_coil_object_type [string]
heating_coil_name [string]
heating_convergence [number] (Default: 0.001)
cooling_coil_object_type [string]
cooling_coil_name [string]
cooling_convergence [number] (Default: 0.001)
maximum_cycling_rate [number] (Default: 2.5)
heat_pump_time_constant [number] (Default: 60.0)
fraction_of_on_cycle_power_use [number] (Default: 0.01)
heat_pump_fan_delay_time [number] (Default: 60.0)
supplemental_heating_coil_object_type [string]
supplemental_heating_coil_name [string]
maximum_supply_air_temperature_from_supplemental_heater [unknown field type]
maximum_outdoor_dry_bulb_temperature_for_supplemental_heater_operation [number] (Default: 21.0)
outdoor_dry_bulb_temperature_sensor_node_name [string]
fan_placement [string] (Default: BlowThrough)
supply_air_fan_operating_mode_schedule_name [string]
dehumidification_control_type [string] (Default: None)
heat_pump_coil_water_flow_mode [string] (Default: Cycling)
AirLoopHVAC:UnitaryHeatCool:VAVChangeoverBypass
Unitary system, heating and cooling with constant volume supply fan (continuous or cycling), direct expansion (DX) cooling coil, heating coil (gas, electric, hot water, steam, or DX air-to-air heat pump) and bypass damper for variable volume flow to terminal units. Used with AirTerminal:SingleDuct:VAV:HeatAndCool:Reheat or AirTerminal:SingleDuct:VAV:HeatAndCool:NoReheat.

Fields

availability_schedule_name [string]
cooling_supply_air_flow_rate [unknown field type]
heating_supply_air_flow_rate [unknown field type]
no_load_supply_air_flow_rate [unknown field type]
cooling_outdoor_air_flow_rate [unknown field type]
heating_outdoor_air_flow_rate [unknown field type]
no_load_outdoor_air_flow_rate [unknown field type]
outdoor_air_flow_rate_multiplier_schedule_name [string]
air_inlet_node_name [string]
bypass_duct_mixer_node_name [string]
bypass_duct_splitter_node_name [string]
air_outlet_node_name [string]
outdoor_air_mixer_object_type [string]
outdoor_air_mixer_name [string]
supply_air_fan_object_type [string]
supply_air_fan_name [string]
supply_air_fan_placement [string]
supply_air_fan_operating_mode_schedule_name [string]
cooling_coil_object_type [string]
cooling_coil_name [string]
heating_coil_object_type [string]
heating_coil_name [string]
priority_control_mode [string] (Default: ZonePriority)
minimum_outlet_air_temperature_during_cooling_operation [number] (Default: 8.0)
maximum_outlet_air_temperature_during_heating_operation [number] (Default: 50.0)
dehumidification_control_type [string] (Default: None)
plenum_or_mixer_inlet_node_name [string]
minimum_runtime_before_operating_mode_change [number] (Default: 0.25)
AirLoopHVAC:UnitaryHeatPump:AirToAir:MultiSpeed
Unitary system, heating and cooling, multi-speed with constant volume supply fan (continuous or cycling), direct expansion (DX) cooling coil, heating coil (DX air-to-air heat pump, gas, electric, hot water, or steam), and supplemental heating coil (gas, electric, hot water, or steam).

Fields

availability_schedule_name [string]
air_inlet_node_name [string]
air_outlet_node_name [string]
controlling_zone_or_thermostat_location [string]
supply_air_fan_object_type [string]
supply_air_fan_name [string]
supply_air_fan_placement [string]
supply_air_fan_operating_mode_schedule_name [string]
heating_coil_object_type [string]
heating_coil_name [string]
minimum_outdoor_dry_bulb_temperature_for_compressor_operation [number] (Default: -8.0)
cooling_coil_object_type [string]
cooling_coil_name [string]
supplemental_heating_coil_object_type [string]
supplemental_heating_coil_name [string]
maximum_supply_air_temperature_from_supplemental_heater [unknown field type]
maximum_outdoor_dry_bulb_temperature_for_supplemental_heater_operation [number] (Default: 21.0)
auxiliary_on_cycle_electric_power [number] (Default: 0.0)
auxiliary_off_cycle_electric_power [number] (Default: 0.0)
design_heat_recovery_water_flow_rate [number] (Default: 0.0)
maximum_temperature_for_heat_recovery [number] (Default: 80.0)
heat_recovery_water_inlet_node_name [string]
heat_recovery_water_outlet_node_name [string]
no_load_supply_air_flow_rate [unknown field type]
number_of_speeds_for_heating [number]
number_of_speeds_for_cooling [number]
heating_speed_1_supply_air_flow_rate [unknown field type]
heating_speed_2_supply_air_flow_rate [unknown field type]
heating_speed_3_supply_air_flow_rate [unknown field type]
heating_speed_4_supply_air_flow_rate [unknown field type]
cooling_speed_1_supply_air_flow_rate [unknown field type]
cooling_speed_2_supply_air_flow_rate [unknown field type]
cooling_speed_3_supply_air_flow_rate [unknown field type]
cooling_speed_4_supply_air_flow_rate [unknown field type]
"""