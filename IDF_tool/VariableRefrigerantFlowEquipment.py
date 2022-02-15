"""
# Variable Refrigerant Flow Equipment
"""
"""
AirConditioner:VariableRefrigerantFlow
Variable refrigerant flow (VRF) air-to-air heat pump condensing unit (includes one or more electric compressors and outdoor fan). Serves one or more VRF zone terminal units. See ZoneHVAC:TerminalUnit:VariableRefrigerantFlow and ZoneTerminalUnitList.

Fields

availability_schedule_name [string]
gross_rated_total_cooling_capacity [unknown field type]
gross_rated_cooling_cop [number] (Default: 3.3)
minimum_condenser_inlet_node_temperature_in_cooling_mode [number] (Default: -6.0)
maximum_condenser_inlet_node_temperature_in_cooling_mode [number] (Default: 43.0)
cooling_capacity_ratio_modifier_function_of_low_temperature_curve_name [string]
cooling_capacity_ratio_boundary_curve_name [string]
cooling_capacity_ratio_modifier_function_of_high_temperature_curve_name [string]
cooling_energy_input_ratio_modifier_function_of_low_temperature_curve_name [string]
cooling_energy_input_ratio_boundary_curve_name [string]
cooling_energy_input_ratio_modifier_function_of_high_temperature_curve_name [string]
cooling_energy_input_ratio_modifier_function_of_low_part_load_ratio_curve_name [string]
cooling_energy_input_ratio_modifier_function_of_high_part_load_ratio_curve_name [string]
cooling_combination_ratio_correction_factor_curve_name [string]
cooling_part_load_fraction_correlation_curve_name [string]
gross_rated_heating_capacity [unknown field type]
rated_heating_capacity_sizing_ratio [number] (Default: 1.0)
gross_rated_heating_cop [number] (Default: 3.4)
minimum_condenser_inlet_node_temperature_in_heating_mode [number] (Default: -20.0)
maximum_condenser_inlet_node_temperature_in_heating_mode [number] (Default: 16.0)
heating_capacity_ratio_modifier_function_of_low_temperature_curve_name [string]
heating_capacity_ratio_boundary_curve_name [string]
heating_capacity_ratio_modifier_function_of_high_temperature_curve_name [string]
heating_energy_input_ratio_modifier_function_of_low_temperature_curve_name [string]
heating_energy_input_ratio_boundary_curve_name [string]
heating_energy_input_ratio_modifier_function_of_high_temperature_curve_name [string]
heating_performance_curve_outdoor_temperature_type [string] (Default: WetBulbTemperature)
heating_energy_input_ratio_modifier_function_of_low_part_load_ratio_curve_name [string]
heating_energy_input_ratio_modifier_function_of_high_part_load_ratio_curve_name [string]
heating_combination_ratio_correction_factor_curve_name [string]
heating_part_load_fraction_correlation_curve_name [string]
minimum_heat_pump_part_load_ratio [number] (Default: 0.15)
zone_name_for_master_thermostat_location [string]
master_thermostat_priority_control_type [string] (Default: MasterThermostatPriority)
thermostat_priority_schedule_name [string]
zone_terminal_unit_list_name [string]
heat_pump_waste_heat_recovery [string] (Default: No)
equivalent_piping_length_used_for_piping_correction_factor_in_cooling_mode [number]
vertical_height_used_for_piping_correction_factor [number]
piping_correction_factor_for_length_in_cooling_mode_curve_name [string]
piping_correction_factor_for_height_in_cooling_mode_coefficient [number] (Default: 0.0)
equivalent_piping_length_used_for_piping_correction_factor_in_heating_mode [number]
piping_correction_factor_for_length_in_heating_mode_curve_name [string]
piping_correction_factor_for_height_in_heating_mode_coefficient [number] (Default: 0.0)
crankcase_heater_power_per_compressor [number] (Default: 33.0)
number_of_compressors [number] (Default: 2.0)
ratio_of_compressor_size_to_total_compressor_capacity [number] (Default: 0.5)
maximum_outdoor_dry_bulb_temperature_for_crankcase_heater [number] (Default: 5.0)
defrost_strategy [string] (Default: Resistive)
defrost_control [string] (Default: Timed)
defrost_energy_input_ratio_modifier_function_of_temperature_curve_name [string]
defrost_time_period_fraction [number] (Default: 0.058333)
resistive_defrost_heater_capacity [unknown field type] (Default: 0.0)
maximum_outdoor_dry_bulb_temperature_for_defrost_operation [number] (Default: 5.0)
condenser_type [string] (Default: AirCooled)
condenser_inlet_node_name [string]
condenser_outlet_node_name [string]
water_condenser_volume_flow_rate [unknown field type]
evaporative_condenser_effectiveness [number] (Default: 0.9)
evaporative_condenser_air_flow_rate [unknown field type]
evaporative_condenser_pump_rated_power_consumption [unknown field type] (Default: 0.0)
supply_water_storage_tank_name [string]
basin_heater_capacity [number] (Default: 0.0)
basin_heater_setpoint_temperature [number] (Default: 2.0)
basin_heater_operating_schedule_name [string]
fuel_type [string] (Default: Electricity)
minimum_condenser_inlet_node_temperature_in_heat_recovery_mode [number]
maximum_condenser_inlet_node_temperature_in_heat_recovery_mode [number]
heat_recovery_cooling_capacity_modifier_curve_name [string]
initial_heat_recovery_cooling_capacity_fraction [number] (Default: 0.5)
heat_recovery_cooling_capacity_time_constant [number] (Default: 0.15)
heat_recovery_cooling_energy_modifier_curve_name [string]
initial_heat_recovery_cooling_energy_fraction [number] (Default: 1.0)
heat_recovery_cooling_energy_time_constant [number] (Default: 0.0)
heat_recovery_heating_capacity_modifier_curve_name [string]
initial_heat_recovery_heating_capacity_fraction [number] (Default: 1.0)
heat_recovery_heating_capacity_time_constant [number] (Default: 0.15)
heat_recovery_heating_energy_modifier_curve_name [string]
initial_heat_recovery_heating_energy_fraction [number] (Default: 1.0)
heat_recovery_heating_energy_time_constant [number] (Default: 0.0)
AirConditioner:VariableRefrigerantFlow:FluidTemperatureControl
This is a key object in the new physics based VRF model applicable for Fluid Temperature Control It describes the Variable Refrigerant Flow system excluding the performance of indoor units Indoor units are modeled separately, see ZoneHVAC:TerminalUnit:VariableRefrigerantFlow

Fields

heat_pump_name [string]
availability_schedule_name [string]
zone_terminal_unit_list_name [string]
refrigerant_type [string] (Default: R410A)
rated_evaporative_capacity [unknown field type] (Default: 40000.0)
rated_compressor_power_per_unit_of_rated_evaporative_capacity [number] (Default: 0.35)
minimum_outdoor_air_temperature_in_cooling_mode [number] (Default: -6.0)
maximum_outdoor_air_temperature_in_cooling_mode [number] (Default: 43.0)
minimum_outdoor_air_temperature_in_heating_mode [number] (Default: -20.0)
maximum_outdoor_air_temperature_in_heating_mode [number] (Default: 16.0)
reference_outdoor_unit_superheating [number] (Default: 3.0)
reference_outdoor_unit_subcooling [number] (Default: 5.0)
refrigerant_temperature_control_algorithm_for_indoor_unit [string] (Default: VariableTemp)
reference_evaporating_temperature_for_indoor_unit [number] (Default: 6.0)
reference_condensing_temperature_for_indoor_unit [number] (Default: 44.0)
variable_evaporating_temperature_minimum_for_indoor_unit [number] (Default: 4.0)
variable_evaporating_temperature_maximum_for_indoor_unit [number] (Default: 13.0)
variable_condensing_temperature_minimum_for_indoor_unit [number] (Default: 42.0)
variable_condensing_temperature_maximum_for_indoor_unit [number] (Default: 46.0)
outdoor_unit_fan_power_per_unit_of_rated_evaporative_capacity [number] (Default: 0.00425)
outdoor_unit_fan_flow_rate_per_unit_of_rated_evaporative_capacity [number] (Default: 7.5e-05)
outdoor_unit_evaporating_temperature_function_of_superheating_curve_name [string]
outdoor_unit_condensing_temperature_function_of_subcooling_curve_name [string]
diameter_of_main_pipe_connecting_outdoor_unit_to_the_first_branch_joint [number] (Default: 0.0762)
length_of_main_pipe_connecting_outdoor_unit_to_the_first_branch_joint [number] (Default: 30.0)
equivalent_length_of_main_pipe_connecting_outdoor_unit_to_the_first_branch_joint [number] (Default: 36.0)
height_difference_between_outdoor_unit_and_indoor_units [number] (Default: 5.0)
main_pipe_insulation_thickness [number] (Default: 0.02)
main_pipe_insulation_thermal_conductivity [number] (Default: 0.032)
crankcase_heater_power_per_compressor [number] (Default: 33.0)
number_of_compressors [number] (Default: 2.0)
ratio_of_compressor_size_to_total_compressor_capacity [number] (Default: 0.5)
maximum_outdoor_dry_bulb_temperature_for_crankcase_heater [number] (Default: 5.0)
defrost_strategy [string] (Default: Resistive)
defrost_control [string] (Default: Timed)
defrost_energy_input_ratio_modifier_function_of_temperature_curve_name [string]
defrost_time_period_fraction [number] (Default: 0.058333)
resistive_defrost_heater_capacity [unknown field type] (Default: 0.0)
maximum_outdoor_dry_bulb_temperature_for_defrost_operation [number] (Default: 5.0)
compressor_maximum_delta_pressure [number] (Default: 4500000.0)
number_of_compressor_loading_index_entries [number] (Default: 2.0)
loading_indices [Array of {compressor_speed_at_loading_index, loading_index_evaporative_capacity_multiplier_function_of_temperature_curve_name, loading_index_compressor_power_multiplier_function_of_temperature_curve_name}]
AirConditioner:VariableRefrigerantFlow:FluidTemperatureControl:HR
This is a key object in the new physics based VRF Heat Recovery (HR) model applicable for Fluid Temperature Control. It describes the VRF HR system excluding the performance of indoor units. Indoor units are modeled separately in the ZoneHVAC:TerminalUnit:VariableRefrigerantFlow object

Fields

availability_schedule_name [string]
zone_terminal_unit_list_name [string]
refrigerant_type [string] (Default: R410A)
rated_evaporative_capacity [unknown field type] (Default: 40000.0)
rated_compressor_power_per_unit_of_rated_evaporative_capacity [number] (Default: 0.35)
minimum_outdoor_air_temperature_in_cooling_only_mode [number] (Default: -6.0)
maximum_outdoor_air_temperature_in_cooling_only_mode [number] (Default: 43.0)
minimum_outdoor_air_temperature_in_heating_only_mode [number] (Default: -20.0)
maximum_outdoor_air_temperature_in_heating_only_mode [number] (Default: 16.0)
minimum_outdoor_temperature_in_heat_recovery_mode [number] (Default: -20.0)
maximum_outdoor_temperature_in_heat_recovery_mode [number] (Default: 43.0)
refrigerant_temperature_control_algorithm_for_indoor_unit [string] (Default: VariableTemp)
reference_evaporating_temperature_for_indoor_unit [number] (Default: 6.0)
reference_condensing_temperature_for_indoor_unit [number] (Default: 44.0)
variable_evaporating_temperature_minimum_for_indoor_unit [number] (Default: 4.0)
variable_evaporating_temperature_maximum_for_indoor_unit [number] (Default: 13.0)
variable_condensing_temperature_minimum_for_indoor_unit [number] (Default: 42.0)
variable_condensing_temperature_maximum_for_indoor_unit [number] (Default: 46.0)
outdoor_unit_evaporator_reference_superheating [number] (Default: 3.0)
outdoor_unit_condenser_reference_subcooling [number] (Default: 5.0)
outdoor_unit_evaporator_rated_bypass_factor [number] (Default: 0.4)
outdoor_unit_condenser_rated_bypass_factor [number] (Default: 0.2)
difference_between_outdoor_unit_evaporating_temperature_and_outdoor_air_temperature_in_heat_recovery_mode [number] (Default: 5.0)
outdoor_unit_heat_exchanger_capacity_ratio [number] (Default: 0.3)
outdoor_unit_fan_power_per_unit_of_rated_evaporative_capacity [number] (Default: 0.00425)
outdoor_unit_fan_flow_rate_per_unit_of_rated_evaporative_capacity [number] (Default: 7.5e-05)
outdoor_unit_evaporating_temperature_function_of_superheating_curve_name [string]
outdoor_unit_condensing_temperature_function_of_subcooling_curve_name [string]
diameter_of_main_pipe_for_suction_gas [number] (Default: 0.0762)
diameter_of_main_pipe_for_discharge_gas [number] (Default: 0.0762)
length_of_main_pipe_connecting_outdoor_unit_to_the_first_branch_joint [number] (Default: 30.0)
equivalent_length_of_main_pipe_connecting_outdoor_unit_to_the_first_branch_joint [number] (Default: 36.0)
height_difference_between_outdoor_unit_and_indoor_units [number] (Default: 5.0)
main_pipe_insulation_thickness [number] (Default: 0.02)
main_pipe_insulation_thermal_conductivity [number] (Default: 0.032)
crankcase_heater_power_per_compressor [number] (Default: 33.0)
number_of_compressors [number] (Default: 2.0)
ratio_of_compressor_size_to_total_compressor_capacity [number] (Default: 0.5)
maximum_outdoor_dry_bulb_temperature_for_crankcase_heater [number] (Default: 5.0)
defrost_strategy [string] (Default: Resistive)
defrost_control [string] (Default: Timed)
defrost_energy_input_ratio_modifier_function_of_temperature_curve_name [string]
defrost_time_period_fraction [number] (Default: 0.058333)
resistive_defrost_heater_capacity [unknown field type] (Default: 0.0)
maximum_outdoor_dry_bulb_temperature_for_defrost_operation [number] (Default: 5.0)
initial_heat_recovery_cooling_capacity_fraction [number] (Default: 1.0)
heat_recovery_cooling_capacity_time_constant [number] (Default: 0.0)
initial_heat_recovery_cooling_energy_fraction [number] (Default: 1.0)
heat_recovery_cooling_energy_time_constant [number] (Default: 0.0)
initial_heat_recovery_heating_capacity_fraction [number] (Default: 1.0)
heat_recovery_heating_capacity_time_constant [number] (Default: 0.0)
initial_heat_recovery_heating_energy_fraction [number] (Default: 1.0)
heat_recovery_heating_energy_time_constant [number] (Default: 0.0)
compressor_maximum_delta_pressure [number] (Default: 4500000.0)
compressor_inverter_efficiency [number] (Default: 0.95)
compressor_evaporative_capacity_correction_factor [number] (Default: 1.0)
number_of_compressor_loading_index_entries [number] (Default: 2.0)
loading_indices [Array of {compressor_speed_at_loading_index, loading_index_evaporative_capacity_multiplier_function_of_temperature_curve_name, loading_index_compressor_power_multiplier_function_of_temperature_curve_name}]
ZoneTerminalUnitList
List of variable refrigerant flow (VRF) terminal units served by a given VRF condensing unit. See ZoneHVAC:TerminalUnit:VariableRefrigerantFlow and AirConditioner:VariableRefrigerantFlow.

Fields

zone_terminal_unit_list_name [string]
terminal_units [Array of {zone_terminal_unit_name}]
"""