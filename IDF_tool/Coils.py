"""
Coils
"""
"""
Coil:Cooling:Water
Chilled water cooling coil, NTU-effectiveness model, with inputs for design entering and leaving conditions.

Fields

availability_schedule_name [string]
design_water_flow_rate [unknown field type] (Default: Autosize)
design_air_flow_rate [unknown field type] (Default: Autosize)
design_inlet_water_temperature [unknown field type] (Default: Autosize)
design_inlet_air_temperature [unknown field type] (Default: Autosize)
design_outlet_air_temperature [unknown field type] (Default: Autosize)
design_inlet_air_humidity_ratio [unknown field type] (Default: Autosize)
design_outlet_air_humidity_ratio [unknown field type] (Default: Autosize)
water_inlet_node_name [string]
water_outlet_node_name [string]
air_inlet_node_name [string]
air_outlet_node_name [string]
type_of_analysis [string] (Default: SimpleAnalysis)
heat_exchanger_configuration [string] (Default: CounterFlow)
condensate_collection_water_storage_tank_name [string]
design_water_temperature_difference [number]
Coil:Cooling:Water:DetailedGeometry
Chilled water cooling coil, detailed flat fin coil model for continuous plate fins, with inputs for detailed coil geometry specifications.

Fields

availability_schedule_name [string]
maximum_water_flow_rate [unknown field type] (Default: Autosize)
tube_outside_surface_area [unknown field type] (Default: Autosize)
total_tube_inside_area [unknown field type] (Default: Autosize)
fin_surface_area [unknown field type] (Default: Autosize)
minimum_airflow_area [unknown field type] (Default: Autosize)
coil_depth [unknown field type] (Default: Autosize)
fin_diameter [unknown field type] (Default: Autosize)
fin_thickness [number] (Default: 0.0015)
tube_inside_diameter [number] (Default: 0.01445)
tube_outside_diameter [number] (Default: 0.0159)
tube_thermal_conductivity [number] (Default: 386.0)
fin_thermal_conductivity [number] (Default: 204.0)
fin_spacing [number] (Default: 0.0018)
tube_depth_spacing [number] (Default: 0.026)
number_of_tube_rows [number] (Default: 4.0)
number_of_tubes_per_row [unknown field type] (Default: Autosize)
water_inlet_node_name [string]
water_outlet_node_name [string]
air_inlet_node_name [string]
air_outlet_node_name [string]
condensate_collection_water_storage_tank_name [string]
design_water_temperature_difference [number]
design_inlet_water_temperature [unknown field type] (Default: Autosize)
CoilSystem:Cooling:Water
Virtual container component that consists of a water cooling coil and its associated controls. This control object supports the available water coil types and may be placed directly on an air loop branch or in an outdoor air equipment list.

Fields

air_inlet_node_name [string]
air_outlet_node_name [string]
availability_schedule_name [string]
cooling_coil_object_type [string]
cooling_coil_name [string]
dehumidification_control_type [string] (Default: None)
run_on_sensible_load [string] (Default: Yes)
run_on_latent_load [string] (Default: No)
minimum_air_to_water_temperature_offset [number] (Default: 0.0)
economizer_lockout [string] (Default: Yes)
minimum_water_loop_temperature_for_heat_recovery [number] (Default: 0.0)
companion_coil_used_for_heat_recovery [string]
Coil:Cooling:DX
New general DX cooling coil supporting on or more speeds and one or or operating modes. Includes DX evaporator coil, compressor, and condenser. Object is currently only supported by the AIRLOOPHVAC:UNITARYSYSTEM object. Remaining Coil:Cooling:DX* objects will be deprecated at a future date, after which, this object will replace all other Coil:Cooling:DX* objects.

Fields

evaporator_inlet_node_name [string]
evaporator_outlet_node_name [string]
availability_schedule_name [string]
condenser_zone_name [string]
condenser_inlet_node_name [string]
condenser_outlet_node_name [string]
performance_object_name [string]
condensate_collection_water_storage_tank_name [string]
evaporative_condenser_supply_water_storage_tank_name [string]
Coil:Cooling:DX:CurveFit:Performance
DX cooling coil performance specification referencing one or more operating modes. Mode 1 is always the base design operating mode. Additional modes are optional states such as subcool reheat for humidity control.

Fields

crankcase_heater_capacity [number] (Default: 0.0)
minimum_outdoor_dry_bulb_temperature_for_compressor_operation [number] (Default: -25.0)
maximum_outdoor_dry_bulb_temperature_for_crankcase_heater_operation [number] (Default: 10.0)
unit_internal_static_air_pressure [number]
capacity_control_method [string] (Default: Discrete)
evaporative_condenser_basin_heater_capacity [number] (Default: 0.0)
evaporative_condenser_basin_heater_setpoint_temperature [number] (Default: 2.0)
evaporative_condenser_basin_heater_operating_schedule_name [string]
compressor_fuel_type [string] (Default: Electricity)
base_operating_mode [string]
alternative_operating_mode_1 [string]
alternative_operating_mode_2 [string]
Coil:Cooling:DX:CurveFit:OperatingMode
DX cooling coil performance for a single operating mode which may have one or more speeds.

Fields

rated_gross_total_cooling_capacity [unknown field type] (Default: Autosize)
rated_evaporator_air_flow_rate [unknown field type]
rated_condenser_air_flow_rate [unknown field type]
maximum_cycling_rate [number] (Default: 0.0)
ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity [number] (Default: 0.0)
latent_capacity_time_constant [number] (Default: 0.0)
nominal_time_for_condensate_removal_to_begin [number] (Default: 0.0)
apply_latent_degradation_to_speeds_greater_than_1 [string] (Default: No)
condenser_type [string] (Default: AirCooled)
nominal_evaporative_condenser_pump_power [unknown field type] (Default: 0.0)
nominal_speed_number [number]
speed_1_name [string]
speed_2_name [string]
speed_3_name [string]
speed_4_name [string]
speed_5_name [string]
speed_6_name [string]
speed_7_name [string]
speed_8_name [string]
speed_9_name [string]
speed_10_name [string]
Coil:Cooling:DX:CurveFit:Speed
DX cooling coil performance for a single speed within a single operating mode.

Fields

gross_total_cooling_capacity_fraction [number]
evaporator_air_flow_rate_fraction [number]
condenser_air_flow_rate_fraction [number]
gross_sensible_heat_ratio [unknown field type] (Default: Autosize)
gross_cooling_cop [number] (Default: 3.0)
active_fraction_of_coil_face_area [number] (Default: 1.0)
rated_evaporator_fan_power_per_volume_flow_rate [number] (Default: 773.3)
evaporative_condenser_pump_power_fraction [number] (Default: 1.0)
evaporative_condenser_effectiveness [number] (Default: 0.9)
total_cooling_capacity_modifier_function_of_temperature_curve_name [string]
total_cooling_capacity_modifier_function_of_air_flow_fraction_curve_name [string]
energy_input_ratio_modifier_function_of_temperature_curve_name [string]
energy_input_ratio_modifier_function_of_air_flow_fraction_curve_name [string]
part_load_fraction_correlation_curve_name [string]
rated_waste_heat_fraction_of_power_input [number] (Default: 0.2)
waste_heat_modifier_function_of_temperature_curve_name [string]
sensible_heat_ratio_modifier_function_of_temperature_curve_name [string]
sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name [string]
Coil:Cooling:DX:SingleSpeed
Direct expansion (DX) cooling coil and condensing unit (includes electric compressor and condenser fan), single-speed. Optional inputs for moisture evaporation from wet coil when compressor cycles off with continuous fan operation.

Fields

availability_schedule_name [string]
gross_rated_total_cooling_capacity [unknown field type]
gross_rated_sensible_heat_ratio [unknown field type]
gross_rated_cooling_cop [number] (Default: 3.0)
rated_air_flow_rate [unknown field type]
rated_evaporator_fan_power_per_volume_flow_rate [number] (Default: 773.3)
air_inlet_node_name [string]
air_outlet_node_name [string]
total_cooling_capacity_function_of_temperature_curve_name [string]
total_cooling_capacity_function_of_flow_fraction_curve_name [string]
energy_input_ratio_function_of_temperature_curve_name [string]
energy_input_ratio_function_of_flow_fraction_curve_name [string]
part_load_fraction_correlation_curve_name [string]
minimum_outdoor_dry_bulb_temperature_for_compressor_operation [number] (Default: -25.0)
nominal_time_for_condensate_removal_to_begin [number] (Default: 0.0)
ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity [number] (Default: 0.0)
maximum_cycling_rate [number] (Default: 0.0)
latent_capacity_time_constant [number] (Default: 0.0)
condenser_air_inlet_node_name [string]
condenser_type [string] (Default: AirCooled)
evaporative_condenser_effectiveness [number] (Default: 0.9)
evaporative_condenser_air_flow_rate [unknown field type]
evaporative_condenser_pump_rated_power_consumption [unknown field type] (Default: 0.0)
crankcase_heater_capacity [number] (Default: 0.0)
maximum_outdoor_dry_bulb_temperature_for_crankcase_heater_operation [number] (Default: 10.0)
supply_water_storage_tank_name [string]
condensate_collection_water_storage_tank_name [string]
basin_heater_capacity [number] (Default: 0.0)
basin_heater_setpoint_temperature [number] (Default: 2.0)
basin_heater_operating_schedule_name [string]
sensible_heat_ratio_function_of_temperature_curve_name [string]
sensible_heat_ratio_function_of_flow_fraction_curve_name [string]
report_ashrae_standard_127_performance_ratings [string] (Default: No)
zone_name_for_condenser_placement [string]
Coil:Cooling:DX:TwoSpeed
Direct expansion (DX) cooling coil and condensing unit (includes electric compressor and condenser fan), two-speed (or variable-speed). Requires two sets of performance data and will interpolate between speeds. Modeled as a single coil (multi-speed compressor or multiple compressors with row split or intertwined coil).

Fields

availability_schedule_name [string]
high_speed_gross_rated_total_cooling_capacity [unknown field type]
high_speed_rated_sensible_heat_ratio [unknown field type]
high_speed_gross_rated_cooling_cop [number] (Default: 3.0)
high_speed_rated_air_flow_rate [unknown field type]
unit_internal_static_air_pressure [number]
air_inlet_node_name [string]
air_outlet_node_name [string]
total_cooling_capacity_function_of_temperature_curve_name [string]
total_cooling_capacity_function_of_flow_fraction_curve_name [string]
energy_input_ratio_function_of_temperature_curve_name [string]
energy_input_ratio_function_of_flow_fraction_curve_name [string]
part_load_fraction_correlation_curve_name [string]
low_speed_gross_rated_total_cooling_capacity [unknown field type]
low_speed_gross_rated_sensible_heat_ratio [unknown field type]
low_speed_gross_rated_cooling_cop [number] (Default: 3.0)
low_speed_rated_air_flow_rate [unknown field type]
low_speed_total_cooling_capacity_function_of_temperature_curve_name [string]
low_speed_energy_input_ratio_function_of_temperature_curve_name [string]
condenser_air_inlet_node_name [string]
condenser_type [string] (Default: AirCooled)
minimum_outdoor_dry_bulb_temperature_for_compressor_operation [number] (Default: -25.0)
high_speed_evaporative_condenser_effectiveness [number] (Default: 0.9)
high_speed_evaporative_condenser_air_flow_rate [unknown field type]
high_speed_evaporative_condenser_pump_rated_power_consumption [unknown field type]
low_speed_evaporative_condenser_effectiveness [number] (Default: 0.9)
low_speed_evaporative_condenser_air_flow_rate [unknown field type]
low_speed_evaporative_condenser_pump_rated_power_consumption [unknown field type]
supply_water_storage_tank_name [string]
condensate_collection_water_storage_tank_name [string]
basin_heater_capacity [number] (Default: 0.0)
basin_heater_setpoint_temperature [number] (Default: 2.0)
basin_heater_operating_schedule_name [string]
sensible_heat_ratio_function_of_temperature_curve_name [string]
sensible_heat_ratio_function_of_flow_fraction_curve_name [string]
low_speed_sensible_heat_ratio_function_of_temperature_curve_name [string]
low_speed_sensible_heat_ratio_function_of_flow_fraction_curve_name [string]
zone_name_for_condenser_placement [string]
Coil:Cooling:DX:MultiSpeed
Direct expansion (DX) cooling coil and condensing unit (includes electric or engine-driven compressor and condenser fan), multi-speed (or variable-speed). Optional moisture evaporation from wet coil when compressor cycles off with continuous fan operation. Requires two to four sets of performance data and will interpolate between speeds. Modeled as a single coil (multi-speed compressor or multiple compressors with row split or intertwined coil).

Fields

availability_schedule_name [string]
air_inlet_node_name [string]
air_outlet_node_name [string]
condenser_air_inlet_node_name [string]
condenser_type [string] (Default: AirCooled)
minimum_outdoor_dry_bulb_temperature_for_compressor_operation [number] (Default: -25.0)
supply_water_storage_tank_name [string]
condensate_collection_water_storage_tank_name [string]
apply_part_load_fraction_to_speeds_greater_than_1 [string] (Default: No)
apply_latent_degradation_to_speeds_greater_than_1 [string] (Default: No)
crankcase_heater_capacity [number] (Default: 0.0)
maximum_outdoor_dry_bulb_temperature_for_crankcase_heater_operation [number] (Default: 10.0)
basin_heater_capacity [number] (Default: 0.0)
basin_heater_setpoint_temperature [number] (Default: 2.0)
basin_heater_operating_schedule_name [string]
fuel_type [string]
number_of_speeds [number]
speed_1_gross_rated_total_cooling_capacity [unknown field type]
speed_1_gross_rated_sensible_heat_ratio [unknown field type]
speed_1_gross_rated_cooling_cop [number] (Default: 3.0)
speed_1_rated_air_flow_rate [unknown field type]
speed_1_rated_evaporator_fan_power_per_volume_flow_rate [number] (Default: 773.3)
speed_1_total_cooling_capacity_function_of_temperature_curve_name [string]
speed_1_total_cooling_capacity_function_of_flow_fraction_curve_name [string]
speed_1_energy_input_ratio_function_of_temperature_curve_name [string]
speed_1_energy_input_ratio_function_of_flow_fraction_curve_name [string]
speed_1_part_load_fraction_correlation_curve_name [string]
speed_1_nominal_time_for_condensate_removal_to_begin [number] (Default: 0.0)
speed_1_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity [number] (Default: 0.0)
speed_1_maximum_cycling_rate [number] (Default: 0.0)
speed_1_latent_capacity_time_constant [number] (Default: 0.0)
speed_1_rated_waste_heat_fraction_of_power_input [number] (Default: 0.2)
speed_1_waste_heat_function_of_temperature_curve_name [string]
speed_1_evaporative_condenser_effectiveness [number] (Default: 0.9)
speed_1_evaporative_condenser_air_flow_rate [unknown field type]
speed_1_rated_evaporative_condenser_pump_power_consumption [unknown field type]
speed_2_gross_rated_total_cooling_capacity [unknown field type]
speed_2_gross_rated_sensible_heat_ratio [unknown field type]
speed_2_gross_rated_cooling_cop [number] (Default: 3.0)
speed_2_rated_air_flow_rate [unknown field type]
speed_2_rated_evaporator_fan_power_per_volume_flow_rate [number] (Default: 773.3)
speed_2_total_cooling_capacity_function_of_temperature_curve_name [string]
speed_2_total_cooling_capacity_function_of_flow_fraction_curve_name [string]
speed_2_energy_input_ratio_function_of_temperature_curve_name [string]
speed_2_energy_input_ratio_function_of_flow_fraction_curve_name [string]
speed_2_part_load_fraction_correlation_curve_name [string]
speed_2_nominal_time_for_condensate_removal_to_begin [number] (Default: 0.0)
speed_2_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity [number] (Default: 0.0)
speed_2_maximum_cycling_rate [number] (Default: 0.0)
speed_2_latent_capacity_time_constant [number] (Default: 0.0)
speed_2_rated_waste_heat_fraction_of_power_input [number] (Default: 0.2)
speed_2_waste_heat_function_of_temperature_curve_name [string]
speed_2_evaporative_condenser_effectiveness [number] (Default: 0.9)
speed_2_evaporative_condenser_air_flow_rate [unknown field type]
speed_2_rated_evaporative_condenser_pump_power_consumption [unknown field type]
speed_3_gross_rated_total_cooling_capacity [unknown field type]
speed_3_gross_rated_sensible_heat_ratio [unknown field type]
speed_3_gross_rated_cooling_cop [number] (Default: 3.0)
speed_3_rated_air_flow_rate [unknown field type]
speed_3_rated_evaporator_fan_power_per_volume_flow_rate [number] (Default: 773.3)
speed_3_total_cooling_capacity_function_of_temperature_curve_name [string]
speed_3_total_cooling_capacity_function_of_flow_fraction_curve_name [string]
speed_3_energy_input_ratio_function_of_temperature_curve_name [string]
speed_3_energy_input_ratio_function_of_flow_fraction_curve_name [string]
speed_3_part_load_fraction_correlation_curve_name [string]
speed_3_nominal_time_for_condensate_removal_to_begin [number] (Default: 0.0)
speed_3_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity [number] (Default: 0.0)
speed_3_maximum_cycling_rate [number] (Default: 0.0)
speed_3_latent_capacity_time_constant [number] (Default: 0.0)
speed_3_rated_waste_heat_fraction_of_power_input [number] (Default: 0.2)
speed_3_waste_heat_function_of_temperature_curve_name [string]
speed_3_evaporative_condenser_effectiveness [number] (Default: 0.9)
speed_3_evaporative_condenser_air_flow_rate [unknown field type]
speed_3_rated_evaporative_condenser_pump_power_consumption [unknown field type]
speed_4_gross_rated_total_cooling_capacity [unknown field type]
speed_4_gross_rated_sensible_heat_ratio [unknown field type]
speed_4_gross_rated_cooling_cop [number] (Default: 3.0)
speed_4_rated_air_flow_rate [unknown field type]
speed_4_rated_evaporator_fan_power_per_volume_flow_rate [number] (Default: 773.3)
speed_4_total_cooling_capacity_function_of_temperature_curve_name [string]
speed_4_total_cooling_capacity_function_of_flow_fraction_curve_name [string]
speed_4_energy_input_ratio_function_of_temperature_curve_name [string]
speed_4_energy_input_ratio_function_of_flow_fraction_curve_name [string]
speed_4_part_load_fraction_correlation_curve_name [string]
speed_4_nominal_time_for_condensate_removal_to_begin [number] (Default: 0.0)
speed_4_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity [number] (Default: 0.0)
speed_4_maximum_cycling_rate [number] (Default: 0.0)
speed_4_latent_capacity_time_constant [number] (Default: 0.0)
speed_4_rated_waste_heat_fraction_of_power_input [number] (Default: 0.2)
speed_4_waste_heat_function_of_temperature_curve_name [string]
speed_4_evaporative_condenser_effectiveness [number] (Default: 0.9)
speed_4_evaporative_condenser_air_flow_rate [unknown field type]
speed_4_rated_evaporative_condenser_pump_power_consumption [unknown field type]
zone_name_for_condenser_placement [string]
Coil:Cooling:DX:VariableSpeed
Direct expansion (DX) cooling coil and condensing unit (includes electric compressor and condenser fan), variable-speed. Optional inputs for moisture evaporation from wet coil when compressor cycles off with continuous fan operation. Requires two to ten sets of performance data and will interpolate between speeds. Modeled as a single coil with variable-speed compressor.

Fields

indoor_air_inlet_node_name [string]
indoor_air_outlet_node_name [string]
number_of_speeds [number] (Default: 2.0)
nominal_speed_level [number] (Default: 2.0)
gross_rated_total_cooling_capacity_at_selected_nominal_speed_level [unknown field type] (Default: Autosize)
rated_air_flow_rate_at_selected_nominal_speed_level [unknown field type] (Default: Autosize)
nominal_time_for_condensate_to_begin_leaving_the_coil [number] (Default: 0.0)
initial_moisture_evaporation_rate_divided_by_steady_state_ac_latent_capacity [number] (Default: 0.0)
energy_part_load_fraction_curve_name [string]
condenser_air_inlet_node_name [string]
condenser_type [string] (Default: AirCooled)
evaporative_condenser_pump_rated_power_consumption [unknown field type] (Default: 0.0)
crankcase_heater_capacity [number] (Default: 0.0)
maximum_outdoor_dry_bulb_temperature_for_crankcase_heater_operation [number] (Default: 10.0)
minimum_outdoor_dry_bulb_temperature_for_compressor_operation [number] (Default: -25.0)
supply_water_storage_tank_name [string]
condensate_collection_water_storage_tank_name [string]
basin_heater_capacity [number] (Default: 0.0)
basin_heater_setpoint_temperature [number] (Default: 2.0)
basin_heater_operating_schedule_name [string]
speed_1_reference_unit_gross_rated_total_cooling_capacity [number]
speed_1_reference_unit_gross_rated_sensible_heat_ratio [number]
speed_1_reference_unit_gross_rated_cooling_cop [number]
speed_1_reference_unit_rated_air_flow_rate [number]
speed_1_reference_unit_rated_condenser_air_flow_rate [number]
speed_1_reference_unit_rated_pad_effectiveness_of_evap_precooling [number]
speed_1_total_cooling_capacity_function_of_temperature_curve_name [string]
speed_1_total_cooling_capacity_function_of_air_flow_fraction_curve_name [string]
speed_1_energy_input_ratio_function_of_temperature_curve_name [string]
speed_1_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_2_reference_unit_gross_rated_total_cooling_capacity [number]
speed_2_reference_unit_gross_rated_sensible_heat_ratio [number]
speed_2_reference_unit_gross_rated_cooling_cop [number]
speed_2_reference_unit_rated_air_flow_rate [number]
speed_2_reference_unit_rated_condenser_air_flow_rate [number]
speed_2_reference_unit_rated_pad_effectiveness_of_evap_precooling [number]
speed_2_total_cooling_capacity_function_of_temperature_curve_name [string]
speed_2_total_cooling_capacity_function_of_air_flow_fraction_curve_name [string]
speed_2_energy_input_ratio_function_of_temperature_curve_name [string]
speed_2_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_3_reference_unit_gross_rated_total_cooling_capacity [number]
speed_3_reference_unit_gross_rated_sensible_heat_ratio [number]
speed_3_reference_unit_gross_rated_cooling_cop [number]
speed_3_reference_unit_rated_air_flow_rate [number]
speed_3_reference_unit_rated_condenser_air_flow_rate [number]
speed_3_reference_unit_rated_pad_effectiveness_of_evap_precooling [number]
speed_3_total_cooling_capacity_function_of_temperature_curve_name [string]
speed_3_total_cooling_capacity_function_of_air_flow_fraction_curve_name [string]
speed_3_energy_input_ratio_function_of_temperature_curve_name [string]
speed_3_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_4_reference_unit_gross_rated_total_cooling_capacity [number]
speed_4_reference_unit_gross_rated_sensible_heat_ratio [number]
speed_4_reference_unit_gross_rated_cooling_cop [number]
speed_4_reference_unit_rated_air_flow_rate [number]
speed_4_reference_unit_rated_condenser_air_flow_rate [number]
speed_4_reference_unit_rated_pad_effectiveness_of_evap_precooling [number]
speed_4_total_cooling_capacity_function_of_temperature_curve_name [string]
speed_4_total_cooling_capacity_function_of_air_flow_fraction_curve_name [string]
speed_4_energy_input_ratio_function_of_temperature_curve_name [string]
speed_4_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_5_reference_unit_gross_rated_total_cooling_capacity [number]
speed_5_reference_unit_gross_rated_sensible_heat_ratio [number]
speed_5_reference_unit_gross_rated_cooling_cop [number]
speed_5_reference_unit_rated_air_flow_rate [number]
speed_5_reference_unit_rated_condenser_air_flow_rate [number]
speed_5_reference_unit_rated_pad_effectiveness_of_evap_precooling [number]
speed_5_total_cooling_capacity_function_of_temperature_curve_name [string]
speed_5_total_cooling_capacity_function_of_air_flow_fraction_curve_name [string]
speed_5_energy_input_ratio_function_of_temperature_curve_name [string]
speed_5_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_6_reference_unit_gross_rated_total_cooling_capacity [number]
speed_6_reference_unit_gross_rated_sensible_heat_ratio [number]
speed_6_reference_unit_gross_rated_cooling_cop [number]
speed_6_reference_unit_rated_air_flow_rate [number]
speed_6_reference_unit_condenser_air_flow_rate [number]
speed_6_reference_unit_rated_pad_effectiveness_of_evap_precooling [number]
speed_6_total_cooling_capacity_function_of_temperature_curve_name [string]
speed_6_total_cooling_capacity_function_of_air_flow_fraction_curve_name [string]
speed_6_energy_input_ratio_function_of_temperature_curve_name [string]
speed_6_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_7_reference_unit_gross_rated_total_cooling_capacity [number]
speed_7_reference_unit_gross_rated_sensible_heat_ratio [number]
speed_7_reference_unit_gross_rated_cooling_cop [number]
speed_7_reference_unit_rated_air_flow_rate [number]
speed_7_reference_unit_condenser_flow_rate [number]
speed_7_reference_unit_rated_pad_effectiveness_of_evap_precooling [number]
speed_7_total_cooling_capacity_function_of_temperature_curve_name [string]
speed_7_total_cooling_capacity_function_of_air_flow_fraction_curve_name [string]
speed_7_energy_input_ratio_function_of_temperature_curve_name [string]
speed_7_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_8_reference_unit_gross_rated_total_cooling_capacity [number]
speed_8_reference_unit_gross_rated_sensible_heat_ratio [number]
speed_8_reference_unit_gross_rated_cooling_cop [number]
speed_8_reference_unit_rated_air_flow_rate [number]
speed_8_reference_unit_condenser_air_flow_rate [number]
speed_8_reference_unit_rated_pad_effectiveness_of_evap_precooling [number]
speed_8_total_cooling_capacity_function_of_temperature_curve_name [string]
speed_8_total_cooling_capacity_function_of_air_flow_fraction_curve_name [string]
speed_8_energy_input_ratio_function_of_temperature_curve_name [string]
speed_8_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_9_reference_unit_gross_rated_total_cooling_capacity [number]
speed_9_reference_unit_gross_rated_sensible_heat_ratio [number]
speed_9_reference_unit_gross_rated_cooling_cop [number]
speed_9_reference_unit_rated_air_flow_rate [number]
speed_9_reference_unit_condenser_air_flow_rate [number]
speed_9_reference_unit_rated_pad_effectiveness_of_evap_precooling [number]
speed_9_total_cooling_capacity_function_of_temperature_curve_name [string]
speed_9_total_cooling_capacity_function_of_air_flow_fraction_curve_name [string]
speed_9_energy_input_ratio_function_of_temperature_curve_name [string]
speed_9_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_10_reference_unit_gross_rated_total_cooling_capacity [number]
speed_10_reference_unit_gross_rated_sensible_heat_ratio [number]
speed_10_reference_unit_gross_rated_cooling_cop [number]
speed_10_reference_unit_rated_air_flow_rate [number]
speed_10_reference_unit_condenser_air_flow_rate [number]
speed_10_reference_unit_rated_pad_effectiveness_of_evap_precooling [number]
speed_10_total_cooling_capacity_function_of_temperature_curve_name [string]
speed_10_total_cooling_capacity_function_of_air_flow_fraction_curve_name [string]
speed_10_energy_input_ratio_function_of_temperature_curve_name [string]
speed_10_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
Coil:Cooling:DX:TwoStageWithHumidityControlMode
Direct expansion (DX) cooling coil and condensing unit (includes electric compressor and condenser fan), two-stage with humidity control mode (e.g. sub-cool or hot gas reheat). Optional inputs for moisture evaporation from wet coil when compressor cycles off with continuous fan operation. Requires two to four sets of performance data, see CoilPerformance:DX:Cooling. Stages are modeled as a face-split coil.

Fields

availability_schedule_name [string]
air_inlet_node_name [string]
air_outlet_node_name [string]
crankcase_heater_capacity [number] (Default: 0.0)
maximum_outdoor_dry_bulb_temperature_for_crankcase_heater_operation [number] (Default: 10.0)
number_of_capacity_stages [number] (Default: 1.0)
number_of_enhanced_dehumidification_modes [number] (Default: 0.0)
normal_mode_stage_1_coil_performance_object_type [string]
normal_mode_stage_1_coil_performance_name [string]
normal_mode_stage_1_2_coil_performance_object_type [string]
normal_mode_stage_1_2_coil_performance_name [string]
dehumidification_mode_1_stage_1_coil_performance_object_type [string]
dehumidification_mode_1_stage_1_coil_performance_name [string]
dehumidification_mode_1_stage_1_2_coil_performance_object_type [string]
dehumidification_mode_1_stage_1_2_coil_performance_name [string]
supply_water_storage_tank_name [string]
condensate_collection_water_storage_tank_name [string]
minimum_outdoor_dry_bulb_temperature_for_compressor_operation [number] (Default: -25.0)
basin_heater_capacity [number] (Default: 0.0)
basin_heater_setpoint_temperature [number] (Default: 2.0)
basin_heater_operating_schedule_name [string]
CoilPerformance:DX:Cooling
Used to specify DX cooling coil performance for one mode of operation for a Coil:Cooling:DX:TwoStageWithHumidityControlMode object which may reference one to four CoilPerformance:DX:Cooling objects depending on the specified number of stages and dehumidification modes. In nearly all cases, the Rated Air Flow Rate will be the same for all performance objects associated with a given coil. If bypass is specified, the Rated Air Flow Rate includes both the bypassed flow and the flow through the active part of the coil.

Fields

gross_rated_total_cooling_capacity [unknown field type]
gross_rated_sensible_heat_ratio [unknown field type]
gross_rated_cooling_cop [number] (Default: 3.0)
rated_air_flow_rate [unknown field type]
fraction_of_air_flow_bypassed_around_coil [number] (Default: 0.0)
total_cooling_capacity_function_of_temperature_curve_name [string]
total_cooling_capacity_function_of_flow_fraction_curve_name [string]
energy_input_ratio_function_of_temperature_curve_name [string]
energy_input_ratio_function_of_flow_fraction_curve_name [string]
part_load_fraction_correlation_curve_name [string]
nominal_time_for_condensate_removal_to_begin [number] (Default: 0.0)
ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity [number] (Default: 0.0)
maximum_cycling_rate [number] (Default: 0.0)
latent_capacity_time_constant [number] (Default: 0.0)
condenser_air_inlet_node_name [string]
condenser_type [string] (Default: AirCooled)
evaporative_condenser_effectiveness [number] (Default: 0.9)
evaporative_condenser_air_flow_rate [unknown field type]
evaporative_condenser_pump_rated_power_consumption [unknown field type] (Default: 0.0)
sensible_heat_ratio_function_of_temperature_curve_name [string]
sensible_heat_ratio_function_of_flow_fraction_curve_name [string]
Coil:Cooling:DX:VariableRefrigerantFlow
Variable refrigerant flow (VRF) direct expansion (DX) cooling coil. Used with ZoneHVAC:TerminalUnit:VariableRefrigerantFlow. Condensing unit is modeled separately, see AirConditioner:VariableRefrigerantFlow.

Fields

availability_schedule_name [string]
gross_rated_total_cooling_capacity [unknown field type]
gross_rated_sensible_heat_ratio [unknown field type]
rated_air_flow_rate [unknown field type]
cooling_capacity_ratio_modifier_function_of_temperature_curve_name [string]
cooling_capacity_modifier_curve_function_of_flow_fraction_name [string]
coil_air_inlet_node [string]
coil_air_outlet_node [string]
name_of_water_storage_tank_for_condensate_collection [string]
Coil:Heating:DX:VariableRefrigerantFlow
Variable refrigerant flow (VRF) direct expansion (DX) heating coil (air-to-air heat pump). Used with ZoneHVAC:TerminalUnit:VariableRefrigerantFlow. Condensing unit is modeled separately, see AirConditioner:VariableRefrigerantFlow.

Fields

availability_schedule [string]
gross_rated_heating_capacity [unknown field type]
rated_air_flow_rate [unknown field type]
coil_air_inlet_node [string]
coil_air_outlet_node [string]
heating_capacity_ratio_modifier_function_of_temperature_curve_name [string]
heating_capacity_modifier_function_of_flow_fraction_curve_name [string]
Coil:Cooling:DX:VariableRefrigerantFlow:FluidTemperatureControl
This is a key object in the new physics based VRF model applicable for Fluid Temperature Control. It describes the the indoor unit coil of the system at cooling mode. Used with ZoneHVAC:TerminalUnit:VariableRefrigerantFlow. Outdoor unit is modeled separately, see AirConditioner:VariableRefrigerantFlow:FluidTemperatureControl or AirConditioner:VariableRefrigerantFlow:FluidTemperatureControl:HR

Fields

availability_schedule_name [string]
coil_air_inlet_node [string]
coil_air_outlet_node [string]
rated_total_cooling_capacity [unknown field type]
rated_sensible_heat_ratio [unknown field type]
indoor_unit_reference_superheating [number] (Default: 5.0)
indoor_unit_evaporating_temperature_function_of_superheating_curve_name [string]
name_of_water_storage_tank_for_condensate_collection [string]
Coil:Heating:DX:VariableRefrigerantFlow:FluidTemperatureControl
This is a key object in the new physics based VRF model applicable for Fluid Temperature Control. It describes the the indoor unit coil of the system at heating mode. Used with ZoneHVAC:TerminalUnit:VariableRefrigerantFlow. Outdoor unit is modeled separately, see AirConditioner:VariableRefrigerantFlow:FluidTemperatureControl or AirConditioner:VariableRefrigerantFlow:FluidTemperatureControl:HR

Fields

availability_schedule [string]
coil_air_inlet_node [string]
coil_air_outlet_node [string]
rated_total_heating_capacity [unknown field type]
indoor_unit_reference_subcooling [number] (Default: 5.0)
indoor_unit_condensing_temperature_function_of_subcooling_curve_name [string]
Coil:Heating:Water
Hot water heating coil, NTU-effectiveness model, assumes a cross-flow heat exchanger. Two options for capacity inputs: UA and water flow rate or capacity and design temperatures.

Fields

availability_schedule_name [string]
u_factor_times_area_value [unknown field type] (Default: Autosize)
maximum_water_flow_rate [unknown field type] (Default: Autosize)
water_inlet_node_name [string]
water_outlet_node_name [string]
air_inlet_node_name [string]
air_outlet_node_name [string]
performance_input_method [string] (Default: UFactorTimesAreaAndDesignWaterFlowRate)
rated_capacity [unknown field type] (Default: Autosize)
rated_inlet_water_temperature [number] (Default: 82.2)
rated_inlet_air_temperature [number] (Default: 16.6)
rated_outlet_water_temperature [number] (Default: 71.1)
rated_outlet_air_temperature [number] (Default: 32.2)
rated_ratio_for_air_and_water_convection [number] (Default: 0.5)
design_water_temperature_difference [number]
Coil:Heating:Steam
Steam heating coil. Condenses and sub-cools steam at loop pressure and discharges condensate through steam traps to low pressure condensate line.

Fields

availability_schedule_name [string]
maximum_steam_flow_rate [unknown field type]
degree_of_subcooling [number]
degree_of_loop_subcooling [number] (Default: 20.0)
water_inlet_node_name [string]
water_outlet_node_name [string]
air_inlet_node_name [string]
air_outlet_node_name [string]
coil_control_type [string]
temperature_setpoint_node_name [string]
Coil:Heating:Electric
Electric heating coil. If the coil is located directly in an air loop branch or outdoor air equipment list, then it is controlled on leaving air temperature and the Temperature Setpoint Node Name must be specified. If the coil is contained within another component such as an air terminal unit, zone HVAC equipment, or unitary system, then the coil is controlled by the parent component and the setpoint node name is not entered.

Fields

availability_schedule_name [string]
efficiency [number] (Default: 1.0)
nominal_capacity [unknown field type]
air_inlet_node_name [string]
air_outlet_node_name [string]
temperature_setpoint_node_name [string]
Coil:Heating:Electric:MultiStage
Electric heating coil, multi-stage. If the coil is located directly in an air loop branch or outdoor air equipment list, then it is controlled on leaving air temperature and the Temperature Setpoint Node Name must be specified. If the coil is contained within another component such as an air terminal unit, zone HVAC equipment, or unitary system, then the coil is controlled by the parent component and the setpoint node name is not entered.

Fields

availability_schedule_name [string]
air_inlet_node_name [string]
air_outlet_node_name [string]
temperature_setpoint_node_name [string]
number_of_stages [number]
stage_1_efficiency [number]
stage_1_nominal_capacity [unknown field type]
stage_2_efficiency [number]
stage_2_nominal_capacity [unknown field type]
stage_3_efficiency [number]
stage_3_nominal_capacity [unknown field type]
stage_4_efficiency [number]
stage_4_nominal_capacity [unknown field type]
Coil:Heating:Fuel
Gas or other fuel heating coil. If the coil is located directly in an air loop branch or outdoor air equipment list, then it is controlled on leaving air temperature and the Temperature Setpoint Node Name must be specified. If the coil is contained within another component such as an air terminal unit, zone HVAC equipment, or unitary system, then the coil is controlled by the parent component and the setpoint node name is not entered.

Fields

availability_schedule_name [string]
fuel_type [string] (Default: NaturalGas)
burner_efficiency [number] (Default: 0.8)
nominal_capacity [unknown field type]
air_inlet_node_name [string]
air_outlet_node_name [string]
temperature_setpoint_node_name [string]
parasitic_electric_load [number]
part_load_fraction_correlation_curve_name [string]
parasitic_fuel_load [number]
Coil:Heating:Gas:MultiStage
Gas heating coil, multi-stage. If the coil is located directly in an air loop branch or outdoor air equipment list, then it is controlled on leaving air temperature and the Temperature Setpoint Node Name must be specified. If the coil is contained within another component such as an air terminal unit, zone HVAC equipment, or unitary system, then the coil is controlled by the parent component and the setpoint node name is not entered.

Fields

availability_schedule_name [string]
air_inlet_node_name [string]
air_outlet_node_name [string]
temperature_setpoint_node_name [string]
part_load_fraction_correlation_curve_name [string]
parasitic_gas_load [number]
number_of_stages [number]
stage_1_gas_burner_efficiency [number]
stage_1_nominal_capacity [unknown field type]
stage_1_parasitic_electric_load [number]
stage_2_gas_burner_efficiency [number]
stage_2_nominal_capacity [unknown field type]
stage_2_parasitic_electric_load [number]
stage_3_gas_burner_efficiency [number]
stage_3_nominal_capacity [unknown field type]
stage_3_parasitic_electric_load [number]
stage_4_gas_burner_efficiency [number]
stage_4_nominal_capacity [unknown field type]
stage_4_parasitic_electric_load [number]
Coil:Heating:Desuperheater
Desuperheater air heating coil. The heating energy provided by this coil is reclaimed from the superheated refrigerant gas leaving a compressor and does not impact the performance of the compressor. If the coil is located directly in an air loop branch or outdoor air equipment list, then it is controlled on leaving air temperature and the Temperature Setpoint Node Name must be specified. If the coil is contained within another component such as a unitary system, then the coil is controlled by the parent component and the setpoint node name is not entered.

Fields

availability_schedule_name [string]
heat_reclaim_recovery_efficiency [number]
air_inlet_node_name [string]
air_outlet_node_name [string]
heating_source_object_type [string]
heating_source_name [string]
temperature_setpoint_node_name [string]
parasitic_electric_load [number]
Coil:Heating:DX:SingleSpeed
Direct expansion (DX) heating coil (air-to-air heat pump) and compressor unit (includes electric compressor and outdoor fan), single-speed, with defrost controls.

Fields

availability_schedule_name [string]
gross_rated_heating_capacity [unknown field type]
gross_rated_heating_cop [number]
rated_air_flow_rate [unknown field type]
rated_supply_fan_power_per_volume_flow_rate [number] (Default: 773.3)
air_inlet_node_name [string]
air_outlet_node_name [string]
heating_capacity_function_of_temperature_curve_name [string]
heating_capacity_function_of_flow_fraction_curve_name [string]
energy_input_ratio_function_of_temperature_curve_name [string]
energy_input_ratio_function_of_flow_fraction_curve_name [string]
part_load_fraction_correlation_curve_name [string]
defrost_energy_input_ratio_function_of_temperature_curve_name [string]
minimum_outdoor_dry_bulb_temperature_for_compressor_operation [number] (Default: -8.0)
outdoor_dry_bulb_temperature_to_turn_on_compressor [number]
maximum_outdoor_dry_bulb_temperature_for_defrost_operation [number] (Default: 5.0)
crankcase_heater_capacity [number] (Default: 0.0)
maximum_outdoor_dry_bulb_temperature_for_crankcase_heater_operation [number] (Default: 10.0)
defrost_strategy [string] (Default: ReverseCycle)
defrost_control [string] (Default: Timed)
defrost_time_period_fraction [number] (Default: 0.058333)
resistive_defrost_heater_capacity [unknown field type] (Default: 0.0)
region_number_for_calculating_hspf [number] (Default: 4.0)
evaporator_air_inlet_node_name [string]
zone_name_for_evaporator_placement [string]
secondary_coil_air_flow_rate [unknown field type]
secondary_coil_fan_flow_scaling_factor [number] (Default: 1.25)
nominal_sensible_heat_ratio_of_secondary_coil [number]
sensible_heat_ratio_modifier_function_of_temperature_curve_name [string]
sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name [string]
Coil:Heating:DX:MultiSpeed
Direct expansion (DX) heating coil (air-to-air heat pump) and compressor unit (includes electric or engine-driven compressor and outdoor fan), multi-speed (or variable-speed), with defrost controls. Requires two to four sets of performance data and will interpolate between speeds.

Fields

availability_schedule_name [string]
air_inlet_node_name [string]
air_outlet_node_name [string]
minimum_outdoor_dry_bulb_temperature_for_compressor_operation [number] (Default: -8.0)
outdoor_dry_bulb_temperature_to_turn_on_compressor [number]
crankcase_heater_capacity [number] (Default: 0.0)
maximum_outdoor_dry_bulb_temperature_for_crankcase_heater_operation [number] (Default: 10.0)
defrost_energy_input_ratio_function_of_temperature_curve_name [string]
maximum_outdoor_dry_bulb_temperature_for_defrost_operation [number] (Default: 5.0)
defrost_strategy [string] (Default: ReverseCycle)
defrost_control [string] (Default: Timed)
defrost_time_period_fraction [number] (Default: 0.058333)
resistive_defrost_heater_capacity [unknown field type] (Default: 0.0)
apply_part_load_fraction_to_speeds_greater_than_1 [string] (Default: No)
fuel_type [string]
region_number_for_calculating_hspf [number] (Default: 4.0)
number_of_speeds [number]
speed_1_gross_rated_heating_capacity [unknown field type]
speed_1_gross_rated_heating_cop [number]
speed_1_rated_air_flow_rate [unknown field type]
speed_1_rated_supply_air_fan_power_per_volume_flow_rate [number] (Default: 773.3)
speed_1_heating_capacity_function_of_temperature_curve_name [string]
speed_1_heating_capacity_function_of_flow_fraction_curve_name [string]
speed_1_energy_input_ratio_function_of_temperature_curve_name [string]
speed_1_energy_input_ratio_function_of_flow_fraction_curve_name [string]
speed_1_part_load_fraction_correlation_curve_name [string]
speed_1_rated_waste_heat_fraction_of_power_input [number] (Default: 0.2)
speed_1_waste_heat_function_of_temperature_curve_name [string]
speed_2_gross_rated_heating_capacity [unknown field type]
speed_2_gross_rated_heating_cop [number]
speed_2_rated_air_flow_rate [unknown field type]
speed_2_rated_supply_air_fan_power_per_volume_flow_rate [number] (Default: 773.3)
speed_2_heating_capacity_function_of_temperature_curve_name [string]
speed_2_heating_capacity_function_of_flow_fraction_curve_name [string]
speed_2_energy_input_ratio_function_of_temperature_curve_name [string]
speed_2_energy_input_ratio_function_of_flow_fraction_curve_name [string]
speed_2_part_load_fraction_correlation_curve_name [string]
speed_2_rated_waste_heat_fraction_of_power_input [number] (Default: 0.2)
speed_2_waste_heat_function_of_temperature_curve_name [string]
speed_3_gross_rated_heating_capacity [unknown field type]
speed_3_gross_rated_heating_cop [number]
speed_3_rated_air_flow_rate [unknown field type]
speed_3_rated_supply_air_fan_power_per_volume_flow_rate [number] (Default: 773.3)
speed_3_heating_capacity_function_of_temperature_curve_name [string]
speed_3_heating_capacity_function_of_flow_fraction_curve_name [string]
speed_3_energy_input_ratio_function_of_temperature_curve_name [string]
speed_3_energy_input_ratio_function_of_flow_fraction_curve_name [string]
speed_3_part_load_fraction_correlation_curve_name [string]
speed_3_rated_waste_heat_fraction_of_power_input [number] (Default: 0.2)
speed_3_waste_heat_function_of_temperature_curve_name [string]
speed_4_gross_rated_heating_capacity [unknown field type]
speed_4_gross_rated_heating_cop [number]
speed_4_rated_air_flow_rate [unknown field type]
speed_4_rated_supply_air_fan_power_per_volume_flow_rate [number] (Default: 773.3)
speed_4_heating_capacity_function_of_temperature_curve_name [string]
speed_4_heating_capacity_function_of_flow_fraction_curve_name [string]
speed_4_energy_input_ratio_function_of_temperature_curve_name [string]
speed_4_energy_input_ratio_function_of_flow_fraction_curve_name [string]
speed_4_part_load_fraction_correlation_curve_name [string]
speed_4_rated_waste_heat_fraction_of_power_input [number] (Default: 0.2)
speed_4_waste_heat_function_of_temperature_curve_name [string]
zone_name_for_evaporator_placement [string]
speed_1_secondary_coil_air_flow_rate [unknown field type]
speed_1_secondary_coil_fan_flow_scaling_factor [number] (Default: 1.25)
speed_1_nominal_sensible_heat_ratio_of_secondary_coil [number]
speed_1_sensible_heat_ratio_modifier_function_of_temperature_curve_name [string]
speed_1_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name [string]
speed_2_secondary_coil_air_flow_rate [unknown field type]
speed_2_secondary_coil_fan_flow_scaling_factor [number] (Default: 1.25)
speed_2_nominal_sensible_heat_ratio_of_secondary_coil [number]
speed_2_sensible_heat_ratio_modifier_function_of_temperature_curve_name [string]
speed_2_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name [string]
speed_3_secondary_coil_air_flow_rate [unknown field type]
speed_3_secondary_coil_fan_flow_scaling_factor [number] (Default: 1.25)
speed_3_nominal_sensible_heat_ratio_of_secondary_coil [number]
speed_3_sensible_heat_ratio_modifier_function_of_temperature_curve_name [string]
speed_3_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name [string]
speed_4_secondary_coil_air_flow_rate [unknown field type]
speed_4_secondary_coil_fan_flow_scaling_factor [number] (Default: 1.25)
speed_4_nominal_sensible_heat_ratio_of_secondary_coil [number]
speed_4_sensible_heat_ratio_modifier_function_of_temperature_curve_name [string]
speed_4_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name [string]
Coil:Heating:DX:VariableSpeed
Direct expansion (DX) heating coil (air-to-air heat pump) and compressor unit (includes electric compressor and outdoor fan), variable-speed, with defrost controls. Requires two to ten sets of performance data and will interpolate between speeds.

Fields

indoor_air_inlet_node_name [string]
indoor_air_outlet_node_name [string]
number_of_speeds [number] (Default: 2.0)
nominal_speed_level [number] (Default: 2.0)
rated_heating_capacity_at_selected_nominal_speed_level [unknown field type] (Default: Autosize)
rated_air_flow_rate_at_selected_nominal_speed_level [unknown field type] (Default: Autosize)
energy_part_load_fraction_curve_name [string]
defrost_energy_input_ratio_function_of_temperature_curve_name [string]
minimum_outdoor_dry_bulb_temperature_for_compressor_operation [number] (Default: -8.0)
outdoor_dry_bulb_temperature_to_turn_on_compressor [number]
maximum_outdoor_dry_bulb_temperature_for_defrost_operation [number] (Default: 5.0)
crankcase_heater_capacity [number] (Default: 0.0)
maximum_outdoor_dry_bulb_temperature_for_crankcase_heater_operation [number] (Default: 10.0)
defrost_strategy [string] (Default: ReverseCycle)
defrost_control [string] (Default: Timed)
defrost_time_period_fraction [number] (Default: 0.058333)
resistive_defrost_heater_capacity [unknown field type] (Default: 0.0)
speed_1_reference_unit_gross_rated_heating_capacity [number]
speed_1_reference_unit_gross_rated_heating_cop [number]
speed_1_reference_unit_rated_air_flow_rate [number]
speed_1_heating_capacity_function_of_temperature_curve_name [string]
speed_1_total_heating_capacity_function_of_air_flow_fraction_curve_name [string]
speed_1_energy_input_ratio_function_of_temperature_curve_name [string]
speed_1_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_2_reference_unit_gross_rated_heating_capacity [number]
speed_2_reference_unit_gross_rated_heating_cop [number]
speed_2_reference_unit_rated_air_flow_rate [number]
speed_2_heating_capacity_function_of_temperature_curve_name [string]
speed_2_total_heating_capacity_function_of_air_flow_fraction_curve_name [string]
speed_2_energy_input_ratio_function_of_temperature_curve_name [string]
speed_2_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_3_reference_unit_gross_rated_heating_capacity [number]
speed_3_reference_unit_gross_rated_heating_cop [number]
speed_3_reference_unit_rated_air_flow_rate [number]
speed_3_heating_capacity_function_of_temperature_curve_name [string]
speed_3_total_heating_capacity_function_of_air_flow_fraction_curve_name [string]
speed_3_energy_input_ratio_function_of_temperature_curve_name [string]
speed_3_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_4_reference_unit_gross_rated_heating_capacity [number]
speed_4_reference_unit_gross_rated_heating_cop [number]
speed_4_reference_unit_rated_air_flow_rate [number]
speed_4_heating_capacity_function_of_temperature_curve_name [string]
speed_4_heating_capacity_function_of_air_flow_fraction_curve_name [string]
speed_4_energy_input_ratio_function_of_temperature_curve_name [string]
speed_4_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_5_reference_unit_gross_rated_heating_capacity [number]
speed_5_reference_unit_gross_rated_heating_cop [number]
speed_5_reference_unit_rated_air_flow_rate [number]
speed_5_heating_capacity_function_of_temperature_curve_name [string]
speed_5_heating_capacity_function_of_air_flow_fraction_curve_name [string]
speed_5_energy_input_ratio_function_of_temperature_curve_name [string]
speed_5_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_6_reference_unit_gross_rated_heating_capacity [number]
speed_6_reference_unit_gross_rated_heating_cop [number]
speed_6_reference_unit_rated_air_flow_rate [number]
speed_6_heating_capacity_function_of_temperature_curve_name [string]
speed_6_heating_capacity_function_of_air_flow_fraction_curve_name [string]
speed_6_energy_input_ratio_function_of_temperature_curve_name [string]
speed_6_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_7_reference_unit_gross_rated_heating_capacity [number]
speed_7_reference_unit_gross_rated_heating_cop [number]
speed_7_reference_unit_rated_air_flow_rate [number]
speed_7_heating_capacity_function_of_temperature_curve_name [string]
speed_7_heating_capacity_function_of_air_flow_fraction_curve_name [string]
speed_7_energy_input_ratio_function_of_temperature_curve_name [string]
speed_7_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_8_reference_unit_gross_rated_heating_capacity [number]
speed_8_reference_unit_gross_rated_heating_cop [number]
speed_8_reference_unit_rated_air_flow_rate [number]
speed_8_heating_capacity_function_of_temperature_curve_name [string]
speed_8_heating_capacity_function_of_air_flow_fraction_curve_name [string]
speed_8_energy_input_ratio_function_of_temperature_curve_name [string]
speed_8_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_9_reference_unit_gross_rated_heating_capacity [number]
speed_9_reference_unit_gross_rated_heating_cop [number]
speed_9_reference_unit_rated_air_flow_rate [number]
speed_9_heating_capacity_function_of_temperature_curve_name [string]
speed_9_heating_capacity_function_of_air_flow_fraction_curve_name [string]
speed_9_energy_input_ratio_function_of_temperature_curve_name [string]
speed_9_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_10_reference_unit_gross_rated_heating_capacity [number]
speed_10_reference_unit_gross_rated_heating_cop [number]
speed_10_reference_unit_rated_air_flow_rate [number]
speed_10_heating_capacity_function_of_temperature_curve_name [string]
speed_10_heating_capacity_function_of_air_flow_fraction_curve_name [string]
speed_10_energy_input_ratio_function_of_temperature_curve_name [string]
speed_10_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
Coil:Cooling:WaterToAirHeatPump:ParameterEstimation
Direct expansion (DX) cooling coil for water-to-air heat pump (includes electric compressor), single-speed, parameter estimation model. Optional inputs for moisture evaporation from wet coil when compressor cycles off with continuous fan operation. Parameter estimation model is a deterministic model that requires a consistent set of parameters to describe the operating conditions of the heat pump components.

Fields

compressor_type [string]
refrigerant_type [string] (Default: R22)
design_source_side_flow_rate [number]
nominal_cooling_coil_capacity [number]
nominal_time_for_condensate_removal_to_begin [number] (Default: 0.0)
ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity [number] (Default: 0.0)
high_pressure_cutoff [number]
low_pressure_cutoff [number]
water_inlet_node_name [string]
water_outlet_node_name [string]
air_inlet_node_name [string]
air_outlet_node_name [string]
load_side_total_heat_transfer_coefficient [number]
load_side_outside_surface_heat_transfer_coefficient [number]
superheat_temperature_at_the_evaporator_outlet [number]
compressor_power_losses [number]
compressor_efficiency [number]
compressor_piston_displacement [number]
compressor_suction_discharge_pressure_drop [number]
compressor_clearance_factor [number]
refrigerant_volume_flow_rate [number]
volume_ratio [number]
leak_rate_coefficient [number]
source_side_heat_transfer_coefficient [number]
source_side_heat_transfer_resistance1 [number]
source_side_heat_transfer_resistance2 [number]
Coil:Heating:WaterToAirHeatPump:ParameterEstimation
Direct expansion (DX) heating coil for water-to-air heat pump (includes electric compressor), single-speed, parameter estimation model. Parameter estimation model is a deterministic model that requires a consistent set of parameters to describe the operating conditions of the heat pump components.

Fields

compressor_type [string]
refrigerant_type [string] (Default: R22)
design_source_side_flow_rate [number]
gross_rated_heating_capacity [number]
high_pressure_cutoff [number]
low_pressure_cutoff [number]
water_inlet_node_name [string]
water_outlet_node_name [string]
air_inlet_node_name [string]
air_outlet_node_name [string]
load_side_total_heat_transfer_coefficient [number]
superheat_temperature_at_the_evaporator_outlet [number]
compressor_power_losses [number]
compressor_efficiency [number]
compressor_piston_displacement [number]
compressor_suction_discharge_pressure_drop [number]
compressor_clearance_factor [number]
refrigerant_volume_flow_rate [number]
volume_ratio [number]
leak_rate_coefficient [number]
source_side_heat_transfer_coefficient [number]
source_side_heat_transfer_resistance1 [number]
source_side_heat_transfer_resistance2 [number]
Coil:Cooling:WaterToAirHeatPump:EquationFit
Direct expansion (DX) cooling coil for water-to-air heat pump (includes electric compressor), single-speed, equation-fit model. Optional inputs for moisture evaporation from wet coil when compressor cycles off with continuous fan operation. Equation-fit model uses normalized curves to describe the heat pump performance.

Fields

water_inlet_node_name [string]
water_outlet_node_name [string]
air_inlet_node_name [string]
air_outlet_node_name [string]
rated_air_flow_rate [unknown field type]
rated_water_flow_rate [unknown field type]
gross_rated_total_cooling_capacity [unknown field type]
gross_rated_sensible_cooling_capacity [unknown field type]
gross_rated_cooling_cop [number]
total_cooling_capacity_curve_name [string]
sensible_cooling_capacity_curve_name [string]
cooling_power_consumption_curve_name [string]
nominal_time_for_condensate_removal_to_begin [number] (Default: 0.0)
ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity [number] (Default: 0.0)
Coil:Cooling:WaterToAirHeatPump:VariableSpeedEquationFit
Direct expansion (DX) cooling coil for water-to-air heat pump (includes electric compressor), variable-speed, equation-fit model. Optional inputs for moisture evaporation from wet coil when compressor cycles off with continuous fan operation. Equation-fit model uses normalized curves to describe the heat pump performance. Requires two to ten sets of performance data and will interpolate between speeds. Modeled as a single coil with variable-speed compressor.

Fields

water_to_refrigerant_hx_water_inlet_node_name [string]
water_to_refrigerant_hx_water_outlet_node_name [string]
indoor_air_inlet_node_name [string]
indoor_air_outlet_node_name [string]
number_of_speeds [number] (Default: 2.0)
nominal_speed_level [number] (Default: 2.0)
gross_rated_total_cooling_capacity_at_selected_nominal_speed_level [unknown field type] (Default: Autosize)
rated_air_flow_rate_at_selected_nominal_speed_level [unknown field type] (Default: Autosize)
rated_water_flow_rate_at_selected_nominal_speed_level [unknown field type] (Default: Autosize)
nominal_time_for_condensate_to_begin_leaving_the_coil [number] (Default: 0.0)
initial_moisture_evaporation_rate_divided_by_steady_state_ac_latent_capacity [number] (Default: 0.0)
flag_for_using_hot_gas_reheat_0_or_1 [number] (Default: 0.0)
energy_part_load_fraction_curve_name [string]
speed_1_reference_unit_gross_rated_total_cooling_capacity [number]
speed_1_reference_unit_gross_rated_sensible_heat_ratio [number]
speed_1_reference_unit_gross_rated_cooling_cop [number]
speed_1_reference_unit_rated_air_flow_rate [number]
speed_1_reference_unit_rated_water_flow_rate [number]
speed_1_total_cooling_capacity_function_of_temperature_curve_name [string]
speed_1_total_cooling_capacity_function_of_air_flow_fraction_curve_name [string]
speed_1_total_cooling_capacity_function_of_water_flow_fraction_curve_name [string]
speed_1_energy_input_ratio_function_of_temperature_curve_name [string]
speed_1_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_1_energy_input_ratio_function_of_water_flow_fraction_curve_name [string]
speed_1_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions [number]
speed_1_waste_heat_function_of_temperature_curve_name [string]
speed_2_reference_unit_gross_rated_total_cooling_capacity [number]
speed_2_reference_unit_gross_rated_sensible_heat_ratio [number]
speed_2_reference_unit_gross_rated_cooling_cop [number]
speed_2_reference_unit_rated_air_flow_rate [number]
speed_2_reference_unit_rated_water_flow_rate [number]
speed_2_total_cooling_capacity_function_of_temperature_curve_name [string]
speed_2_total_cooling_capacity_function_of_air_flow_fraction_curve_name [string]
speed_2_total_cooling_capacity_function_of_water_flow_fraction_curve_name [string]
speed_2_energy_input_ratio_function_of_temperature_curve_name [string]
speed_2_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_2_energy_input_ratio_function_of_water_flow_fraction_curve_name [string]
speed_2_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions [number]
speed_2_waste_heat_function_of_temperature_curve_name [string]
speed_3_reference_unit_gross_rated_total_cooling_capacity [number]
speed_3_reference_unit_gross_rated_sensible_heat_ratio [number]
speed_3_reference_unit_gross_rated_cooling_cop [number]
speed_3_reference_unit_rated_air_flow_rate [number]
speed_3_reference_unit_rated_water_flow_rate [number]
speed_3_total_cooling_capacity_function_of_temperature_curve_name [string]
speed_3_total_cooling_capacity_function_of_air_flow_fraction_curve_name [string]
speed_3_total_cooling_capacity_function_of_water_flow_fraction_curve_name [string]
speed_3_energy_input_ratio_function_of_temperature_curve_name [string]
speed_3_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_3_energy_input_ratio_function_of_water_flow_fraction_curve_name [string]
speed_3_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions [number]
speed_3_waste_heat_function_of_temperature_curve_name [string]
speed_4_reference_unit_gross_rated_total_cooling_capacity [number]
speed_4_reference_unit_gross_rated_sensible_heat_ratio [number]
speed_4_reference_unit_gross_rated_cooling_cop [number]
speed_4_reference_unit_rated_air_flow_rate [number]
speed_4_reference_unit_rated_water_flow_rate [number]
speed_4_total_cooling_capacity_function_of_temperature_curve_name [string]
speed_4_total_cooling_capacity_function_of_air_flow_fraction_curve_name [string]
speed_4_total_cooling_capacity_function_of_water_flow_fraction_curve_name [string]
speed_4_energy_input_ratio_function_of_temperature_curve_name [string]
speed_4_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_4_energy_input_ratio_function_of_water_flow_fraction_curve_name [string]
speed_4_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions [number]
speed_4_waste_heat_function_of_temperature_curve_name [string]
speed_5_reference_unit_gross_rated_total_cooling_capacity [number]
speed_5_reference_unit_gross_rated_sensible_heat_ratio [number]
speed_5_reference_unit_gross_rated_cooling_cop [number]
speed_5_reference_unit_rated_air_flow_rate [number]
speed_5_reference_unit_rated_water_flow_rate [number]
speed_5_total_cooling_capacity_function_of_temperature_curve_name [string]
speed_5_total_cooling_capacity_function_of_air_flow_fraction_curve_name [string]
speed_5_total_cooling_capacity_function_of_water_flow_fraction_curve_name [string]
speed_5_energy_input_ratio_function_of_temperature_curve_name [string]
speed_5_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_5_energy_input_ratio_function_of_water_flow_fraction_curve_name [string]
speed_5_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions [number]
speed_5_waste_heat_function_of_temperature_curve_name [string]
speed_6_reference_unit_gross_rated_total_cooling_capacity [number]
speed_6_reference_unit_gross_rated_sensible_heat_ratio [number]
speed_6_reference_unit_gross_rated_cooling_cop [number]
speed_6_reference_unit_rated_air_flow_rate [number]
speed_6_reference_unit_rated_water_flow_rate [number]
speed_6_total_cooling_capacity_function_of_temperature_curve_name [string]
speed_6_total_cooling_capacity_function_of_air_flow_fraction_curve_name [string]
speed_6_total_cooling_capacity_function_of_water_flow_fraction_curve_name [string]
speed_6_energy_input_ratio_function_of_temperature_curve_name [string]
speed_6_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_6_energy_input_ratio_function_of_water_flow_fraction_curve_name [string]
speed_6_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions [number]
speed_6_waste_heat_function_of_temperature_curve_name [string]
speed_7_reference_unit_gross_rated_total_cooling_capacity [number]
speed_7_reference_unit_gross_rated_sensible_heat_ratio [number]
speed_7_reference_unit_gross_rated_cooling_cop [number]
speed_7_reference_unit_rated_air_flow_rate [number]
speed_7_reference_unit_rated_water_flow_rate [number]
speed_7_total_cooling_capacity_function_of_temperature_curve_name [string]
speed_7_total_cooling_capacity_function_of_air_flow_fraction_curve_name [string]
speed_7_total_cooling_capacity_function_of_water_flow_fraction_curve_name [string]
speed_7_energy_input_ratio_function_of_temperature_curve_name [string]
speed_7_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_7_energy_input_ratio_function_of_water_flow_fraction_curve_name [string]
speed_7_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions [number]
speed_7_waste_heat_function_of_temperature_curve_name [string]
speed_8_reference_unit_gross_rated_total_cooling_capacity [number]
speed_8_reference_unit_gross_rated_sensible_heat_ratio [number]
speed_8_reference_unit_gross_rated_cooling_cop [number]
speed_8_reference_unit_rated_air_flow_rate [number]
speed_8_reference_unit_rated_water_flow_rate [number]
speed_8_total_cooling_capacity_function_of_temperature_curve_name [string]
speed_8_total_cooling_capacity_function_of_air_flow_fraction_curve_name [string]
speed_8_total_cooling_capacity_function_of_water_flow_fraction_curve_name [string]
speed_8_energy_input_ratio_function_of_temperature_curve_name [string]
speed_8_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_8_energy_input_ratio_function_of_water_flow_fraction_curve_name [string]
speed_8_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions [number]
speed_8_waste_heat_function_of_temperature_curve_name [string]
speed_9_reference_unit_gross_rated_total_cooling_capacity [number]
speed_9_reference_unit_gross_rated_sensible_heat_ratio [number]
speed_9_reference_unit_gross_rated_cooling_cop [number]
speed_9_reference_unit_rated_air_flow_rate [number]
speed_9_reference_unit_rated_water_flow_rate [number]
speed_9_total_cooling_capacity_function_of_temperature_curve_name [string]
speed_9_total_cooling_capacity_function_of_air_flow_fraction_curve_name [string]
speed_9_total_cooling_capacity_function_of_water_flow_fraction_curve_name [string]
speed_9_energy_input_ratio_function_of_temperature_curve_name [string]
speed_9_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_9_energy_input_ratio_function_of_water_flow_fraction_curve_name [string]
speed_9_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions [number]
speed_9_waste_heat_function_of_temperature_curve_name [string]
speed_10_reference_unit_gross_rated_total_cooling_capacity [number]
speed_10_reference_unit_gross_rated_sensible_heat_ratio [number]
speed_10_reference_unit_gross_rated_cooling_cop [number]
speed_10_reference_unit_rated_air_flow_rate [number]
speed_10_reference_unit_rated_water_flow_rate [number]
speed_10_total_cooling_capacity_function_of_temperature_curve_name [string]
speed_10_total_cooling_capacity_function_of_air_flow_fraction_curve_name [string]
speed_10_total_cooling_capacity_function_of_water_flow_fraction_curve_name [string]
speed_10_energy_input_ratio_function_of_temperature_curve_name [string]
speed_10_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_10_energy_input_ratio_function_of_water_flow_fraction_curve_name [string]
speed_10_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions [number]
speed_10_waste_heat_function_of_temperature_curve_name [string]
Coil:Heating:WaterToAirHeatPump:EquationFit
Direct expansion (DX) heating coil for water-to-air heat pump (includes electric compressor), single-speed, equation-fit model. Equation-fit model uses normalized curves to describe the heat pump performance.

Fields

water_inlet_node_name [string]
water_outlet_node_name [string]
air_inlet_node_name [string]
air_outlet_node_name [string]
rated_air_flow_rate [unknown field type]
rated_water_flow_rate [unknown field type]
gross_rated_heating_capacity [unknown field type]
gross_rated_heating_cop [number]
heating_capacity_curve_name [string]
heating_power_consumption_curve_name [string]
Coil:Heating:WaterToAirHeatPump:VariableSpeedEquationFit
Direct expansion (DX) heating coil for water-to-air heat pump (includes electric compressor), variable-speed, equation-fit model. Equation-fit model uses normalized curves to describe the heat pump performance. Requires two to ten sets of performance data and will interpolate between speeds.

Fields

water_to_refrigerant_hx_water_inlet_node_name [string]
water_to_refrigerant_hx_water_outlet_node_name [string]
indoor_air_inlet_node_name [string]
indoor_air_outlet_node_name [string]
number_of_speeds [number] (Default: 2.0)
nominal_speed_level [number] (Default: 2.0)
rated_heating_capacity_at_selected_nominal_speed_level [unknown field type] (Default: Autosize)
rated_air_flow_rate_at_selected_nominal_speed_level [unknown field type] (Default: Autosize)
rated_water_flow_rate_at_selected_nominal_speed_level [unknown field type] (Default: Autosize)
energy_part_load_fraction_curve_name [string]
speed_1_reference_unit_gross_rated_heating_capacity [number]
speed_1_reference_unit_gross_rated_heating_cop [number]
speed_1_reference_unit_rated_air_flow [number]
speed_1_reference_unit_rated_water_flow_rate [number]
speed_1_heating_capacity_function_of_temperature_curve_name [string]
speed_1_total_heating_capacity_function_of_air_flow_fraction_curve_name [string]
speed_1_heating_capacity_function_of_water_flow_fraction_curve_name [string]
speed_1_energy_input_ratio_function_of_temperature_curve_name [string]
speed_1_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_1_energy_input_ratio_function_of_water_flow_fraction_curve_name [string]
speed_1_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions [number]
speed_1_waste_heat_function_of_temperature_curve_name [string]
speed_2_reference_unit_gross_rated_heating_capacity [number]
speed_2_reference_unit_gross_rated_heating_cop [number]
speed_2_reference_unit_rated_air_flow_rate [number]
speed_2_reference_unit_rated_water_flow_rate [number]
speed_2_heating_capacity_function_of_temperature_curve_name [string]
speed_2_total_heating_capacity_function_of_air_flow_fraction_curve_name [string]
speed_2_heating_capacity_function_of_water_flow_fraction_curve_name [string]
speed_2_energy_input_ratio_function_of_temperature_curve_name [string]
speed_2_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_2_energy_input_ratio_function_of_water_flow_fraction_curve_name [string]
speed_2_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions [number]
speed_2_waste_heat_function_of_temperature_curve_name [string]
speed_3_reference_unit_gross_rated_heating_capacity [number]
speed_3_reference_unit_gross_rated_heating_cop [number]
speed_3_reference_unit_rated_air_flow_rate [number]
speed_3_reference_unit_rated_water_flow_rate [number]
speed_3_heating_capacity_function_of_temperature_curve_name [string]
speed_3_total_heating_capacity_function_of_air_flow_fraction_curve_name [string]
speed_3_heating_capacity_function_of_water_flow_fraction_curve_name [string]
speed_3_energy_input_ratio_function_of_temperature_curve_name [string]
speed_3_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_3_energy_input_ratio_function_of_water_flow_fraction_curve_name [string]
speed_3_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions [number]
speed_3_waste_heat_function_of_temperature_curve_name [string]
speed_4_reference_unit_gross_rated_heating_capacity [number]
speed_4_reference_unit_gross_rated_heating_cop [number]
speed_4_reference_unit_rated_air_flow_rate [number]
speed_4_reference_unit_rated_water_flow_rate [number]
speed_4_heating_capacity_function_of_temperature_curve_name [string]
speed_4_total_heating_capacity_function_of_air_flow_fraction_curve_name [string]
speed_4_heating_capacity_function_of_water_flow_fraction_curve_name [string]
speed_4_energy_input_ratio_function_of_temperature_curve_name [string]
speed_4_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_4_energy_input_ratio_function_of_water_flow_fraction_curve_name [string]
speed_4_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions [number]
speed_4_waste_heat_function_of_temperature_curve_name [string]
speed_5_reference_unit_gross_rated_heating_capacity [number]
speed_5_reference_unit_gross_rated_heating_cop [number]
speed_5_reference_unit_rated_air_flow_rate [number]
speed_5_reference_unit_rated_water_flow_rate [number]
speed_5_heating_capacity_function_of_temperature_curve_name [string]
speed_5_total_heating_capacity_function_of_air_flow_fraction_curve_name [string]
speed_5_heating_capacity_function_of_water_flow_fraction_curve_name [string]
speed_5_energy_input_ratio_function_of_temperature_curve_name [string]
speed_5_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_5_energy_input_ratio_function_of_water_flow_fraction_curve_name [string]
speed_5_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions [number]
speed_5_waste_heat_function_of_temperature_curve_name [string]
speed_6_reference_unit_gross_rated_heating_capacity [number]
speed_6_reference_unit_gross_rated_heating_cop [number]
speed_6_reference_unit_rated_air_flow_rate [number]
speed_6_reference_unit_rated_water_flow_rate [number]
speed_6_heating_capacity_function_of_temperature_curve_name [string]
speed_6_total_heating_capacity_function_of_air_flow_fraction_curve_name [string]
speed_6_heating_capacity_function_of_water_flow_fraction_curve_name [string]
speed_6_energy_input_ratio_function_of_temperature_curve_name [string]
speed_6_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_6_energy_input_ratio_function_of_water_flow_fraction_curve_name [string]
speed_6_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions [number]
speed_6_waste_heat_function_of_temperature_curve_name [string]
speed_7_reference_unit_gross_rated_heating_capacity [number]
speed_7_reference_unit_gross_rated_heating_cop [number]
speed_7_reference_unit_rated_air_flow_rate [number]
speed_7_reference_unit_rated_water_flow_rate [number]
speed_7_heating_capacity_function_of_temperature_curve_name [string]
speed_7_total_heating_capacity_function_of_air_flow_fraction_curve_name [string]
speed_7_heating_capacity_function_of_water_flow_fraction_curve_name [string]
speed_7_energy_input_ratio_function_of_temperature_curve_name [string]
speed_7_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_7_energy_input_ratio_function_of_water_flow_fraction_curve_name [string]
speed_7_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions [number]
speed_7_waste_heat_function_of_temperature_curve_name [string]
speed_8_reference_unit_gross_rated_heating_capacity [number]
speed_8_reference_unit_gross_rated_heating_cop [number]
speed_8_reference_unit_rated_air_flow_rate [number]
speed_8_reference_unit_rated_water_flow_rate [number]
speed_8_heating_capacity_function_of_temperature_curve_name [string]
speed_8_total_heating_capacity_function_of_air_flow_fraction_curve_name [string]
speed_8_heating_capacity_function_of_water_flow_fraction_curve_name [string]
speed_8_energy_input_ratio_function_of_temperature_curve_name [string]
speed_8_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_8_energy_input_ratio_function_of_water_flow_fraction_curve_name [string]
speed_8_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions [number]
speed_8_waste_heat_function_of_temperature_curve_name [string]
speed_9_reference_unit_gross_rated_heating_capacity [number]
speed_9_reference_unit_gross_rated_heating_cop [number]
speed_9_reference_unit_rated_air_flow_rate [number]
speed_9_reference_unit_rated_water_flow_rate [number]
speed_9_heating_capacity_function_of_temperature_curve_name [string]
speed_9_total_heating_capacity_function_of_air_flow_fraction_curve_name [string]
speed_9_heating_capacity_function_of_water_flow_fraction_curve_name [string]
speed_9_energy_input_ratio_function_of_temperature_curve_name [string]
speed_9_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_9_energy_input_ratio_function_of_water_flow_fraction_curve_name [string]
speed_9_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions [number]
speed_9_waste_heat_function_of_temperature_curve_name [string]
speed_10_reference_unit_gross_rated_heating_capacity [number]
speed_10_reference_unit_gross_rated_heating_cop [number]
speed_10_reference_unit_rated_air_flow_rate [number]
speed_10_reference_unit_rated_water_flow_rate [number]
speed_10_heating_capacity_function_of_temperature_curve_name [string]
speed_10_total_heating_capacity_function_of_air_flow_fraction_curve_name [string]
speed_10_heating_capacity_function_of_water_flow_fraction_curve_name [string]
speed_10_energy_input_ratio_function_of_temperature_curve_name [string]
speed_10_energy_input_ratio_function_of_air_flow_fraction_curve_name [string]
speed_10_energy_input_ratio_function_of_water_flow_fraction_curve_name [string]
speed_10_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions [number]
speed_10_waste_heat_function_of_temperature_curve_name [string]
Coil:WaterHeating:AirToWaterHeatPump:Pumped
Heat pump water heater (HPWH) heating coil, air-to-water direct-expansion (DX) system which includes a water heating coil, evaporator air coil, evaporator fan, electric compressor, and water pump. Part of a WaterHeater:HeatPump:PumpedCondenser system.

Fields

rated_heating_capacity [number]
rated_cop [number] (Default: 3.2)
rated_sensible_heat_ratio [number] (Default: 0.85)
rated_evaporator_inlet_air_dry_bulb_temperature [number] (Default: 19.7)
rated_evaporator_inlet_air_wet_bulb_temperature [number] (Default: 13.5)
rated_condenser_inlet_water_temperature [number] (Default: 57.5)
rated_evaporator_air_flow_rate [unknown field type]
rated_condenser_water_flow_rate [unknown field type]
evaporator_fan_power_included_in_rated_cop [string] (Default: Yes)
condenser_pump_power_included_in_rated_cop [string] (Default: No)
condenser_pump_heat_included_in_rated_heating_capacity_and_rated_cop [string] (Default: No)
condenser_water_pump_power [number] (Default: 0.0)
fraction_of_condenser_pump_heat_to_water [number] (Default: 0.2)
evaporator_air_inlet_node_name [string]
evaporator_air_outlet_node_name [string]
condenser_water_inlet_node_name [string]
condenser_water_outlet_node_name [string]
crankcase_heater_capacity [number] (Default: 0.0)
maximum_ambient_temperature_for_crankcase_heater_operation [number] (Default: 10.0)
evaporator_air_temperature_type_for_curve_objects [string] (Default: WetBulbTemperature)
heating_capacity_function_of_temperature_curve_name [string]
heating_capacity_function_of_air_flow_fraction_curve_name [string]
heating_capacity_function_of_water_flow_fraction_curve_name [string]
heating_cop_function_of_temperature_curve_name [string]
heating_cop_function_of_air_flow_fraction_curve_name [string]
heating_cop_function_of_water_flow_fraction_curve_name [string]
part_load_fraction_correlation_curve_name [string]
Coil:WaterHeating:AirToWaterHeatPump:Wrapped
Heat pump water heater (HPWH) heating coil, air-to-water direct-expansion (DX) system which includes a water heating coil, evaporator air coil, evaporator fan, electric compressor, and water pump. Part of a WaterHeater:HeatPump:WrappedCondenser system.

Fields

rated_heating_capacity [number]
rated_cop [number] (Default: 3.2)
rated_sensible_heat_ratio [number] (Default: 0.85)
rated_evaporator_inlet_air_dry_bulb_temperature [number] (Default: 19.7)
rated_evaporator_inlet_air_wet_bulb_temperature [number] (Default: 13.5)
rated_condenser_water_temperature [number] (Default: 57.5)
rated_evaporator_air_flow_rate [unknown field type]
evaporator_fan_power_included_in_rated_cop [string] (Default: Yes)
evaporator_air_inlet_node_name [string]
evaporator_air_outlet_node_name [string]
crankcase_heater_capacity [number] (Default: 0.0)
maximum_ambient_temperature_for_crankcase_heater_operation [number] (Default: 10.0)
evaporator_air_temperature_type_for_curve_objects [string] (Default: WetBulbTemperature)
heating_capacity_function_of_temperature_curve_name [string]
heating_capacity_function_of_air_flow_fraction_curve_name [string]
heating_cop_function_of_temperature_curve_name [string]
heating_cop_function_of_air_flow_fraction_curve_name [string]
part_load_fraction_correlation_curve_name [string]
Coil:WaterHeating:AirToWaterHeatPump:VariableSpeed
vairlable-speed Heat pump water heater (VSHPWH) heating coil, air-to-water direct-expansion (DX) system which includes a variable-speed water heating coil, evaporator air coil, evaporator fan, electric compressor, and water pump. Part of a WaterHeater:HeatPump system.

Fields

number_of_speeds [number] (Default: 1.0)
nominal_speed_level [number] (Default: 1.0)
rated_water_heating_capacity [number]
rated_evaporator_inlet_air_dry_bulb_temperature [number] (Default: 19.7)
rated_evaporator_inlet_air_wet_bulb_temperature [number] (Default: 13.5)
rated_condenser_inlet_water_temperature [number] (Default: 57.5)
rated_evaporator_air_flow_rate [unknown field type]
rated_condenser_water_flow_rate [unknown field type]
evaporator_fan_power_included_in_rated_cop [string] (Default: Yes)
condenser_pump_power_included_in_rated_cop [string] (Default: No)
condenser_pump_heat_included_in_rated_heating_capacity_and_rated_cop [string] (Default: No)
fraction_of_condenser_pump_heat_to_water [number] (Default: 0.2)
evaporator_air_inlet_node_name [string]
evaporator_air_outlet_node_name [string]
condenser_water_inlet_node_name [string]
condenser_water_outlet_node_name [string]
crankcase_heater_capacity [number] (Default: 0.0)
maximum_ambient_temperature_for_crankcase_heater_operation [number] (Default: 10.0)
evaporator_air_temperature_type_for_curve_objects [string] (Default: WetBulbTemperature)
part_load_fraction_correlation_curve_name [string]
rated_water_heating_capacity_at_speed_1 [number]
rated_water_heating_cop_at_speed_1 [number] (Default: 3.2)
rated_sensible_heat_ratio_at_speed_1 [number] (Default: 0.85)
speed_1_reference_unit_rated_air_flow_rate [number]
speed_1_reference_unit_rated_water_flow_rate [number]
speed_1_reference_unit_water_pump_input_power_at_rated_conditions [number]
speed_1_total_wh_capacity_function_of_temperature_curve_name [string]
speed_1_total_wh_capacity_function_of_air_flow_fraction_curve_name [string]
speed_1_total_wh_capacity_function_of_water_flow_fraction_curve_name [string]
speed_1_cop_function_of_temperature_curve_name [string]
speed_1_cop_function_of_air_flow_fraction_curve_name [string]
speed_1_cop_function_of_water_flow_fraction_curve_name [string]
rated_water_heating_capacity_at_speed_2 [number]
rated_water_heating_cop_at_speed_2 [number] (Default: 3.2)
rated_sensible_heat_ratio_at_speed_2 [number] (Default: 0.85)
speed_2_reference_unit_rated_air_flow_rate [number]
speed_2_reference_unit_rated_water_flow_rate [number]
speed_2_reference_unit_water_pump_input_power_at_rated_conditions [number]
speed_2_total_wh_capacity_function_of_temperature_curve_name [string]
speed_2_total_wh_capacity_function_of_air_flow_fraction_curve_name [string]
speed_2_total_wh_capacity_function_of_water_flow_fraction_curve_name [string]
speed_2_cop_function_of_temperature_curve_name [string]
speed_2_cop_function_of_air_flow_fraction_curve_name [string]
speed_2_cop_function_of_water_flow_fraction_curve_name [string]
rated_water_heating_capacity_at_speed_3 [number]
rated_water_heating_cop_at_speed_3 [number] (Default: 3.2)
rated_sensible_heat_ratio_at_speed_3 [number] (Default: 0.85)
speed_3_reference_unit_rated_air_flow_rate [number]
speed_3_reference_unit_rated_water_flow_rate [number]
speed_3_reference_unit_water_pump_input_power_at_rated_conditions [number]
speed_3_total_wh_capacity_function_of_temperature_curve_name [string]
speed_3_total_wh_capacity_function_of_air_flow_fraction_curve_name [string]
speed_3_total_wh_capacity_function_of_water_flow_fraction_curve_name [string]
speed_3_cop_function_of_temperature_curve_name [string]
speed_3_cop_function_of_air_flow_fraction_curve_name [string]
speed_3_cop_function_of_water_flow_fraction_curve_name [string]
rated_water_heating_capacity_at_speed_4 [number]
rated_water_heating_cop_at_speed_4 [number] (Default: 3.2)
rated_sensible_heat_ratio_at_speed_4 [number] (Default: 0.85)
speed_4_reference_unit_rated_air_flow_rate [number]
speed_4_reference_unit_rated_water_flow_rate [number]
speed_4_reference_unit_water_pump_input_power_at_rated_conditions [number]
speed_4_total_wh_capacity_function_of_temperature_curve_name [string]
speed_4_total_wh_capacity_function_of_air_flow_fraction_curve_name [string]
speed_4_total_wh_capacity_function_of_water_flow_fraction_curve_name [string]
speed_4_cop_function_of_temperature_curve_name [string]
speed_4_cop_function_of_air_flow_fraction_curve_name [string]
speed_4_cop_function_of_water_flow_fraction_curve_name [string]
rated_water_heating_capacity_at_speed_5 [number]
rated_water_heating_cop_at_speed_5 [number] (Default: 3.2)
rated_sensible_heat_ratio_at_speed_5 [number] (Default: 0.85)
speed_5_reference_unit_rated_air_flow_rate [number]
speed_5_reference_unit_rated_water_flow_rate [number]
speed_5_reference_unit_water_pump_input_power_at_rated_conditions [number]
speed_5_total_wh_capacity_function_of_temperature_curve_name [string]
speed_5_total_wh_capacity_function_of_air_flow_fraction_curve_name [string]
speed_5_total_wh_capacity_function_of_water_flow_fraction_curve_name [string]
speed_5_cop_function_of_temperature_curve_name [string]
speed_5_cop_function_of_air_flow_fraction_curve_name [string]
speed_5_cop_function_of_water_flow_fraction_curve_name [string]
rated_water_heating_capacity_at_speed_6 [number]
rated_water_heating_cop_at_speed_6 [number] (Default: 3.2)
rated_sensible_heat_ratio_at_speed_6 [number] (Default: 0.85)
speed_6_reference_unit_rated_air_flow_rate [number]
speed_6_reference_unit_rated_water_flow_rate [number]
speed_6_reference_unit_water_pump_input_power_at_rated_conditions [number]
speed_6_total_wh_capacity_function_of_temperature_curve_name [string]
speed_6_total_wh_capacity_function_of_air_flow_fraction_curve_name [string]
speed_6_total_wh_capacity_function_of_water_flow_fraction_curve_name [string]
speed_6_cop_function_of_temperature_curve_name [string]
speed_6_cop_function_of_air_flow_fraction_curve_name [string]
speed_6_cop_function_of_water_flow_fraction_curve_name [string]
rated_water_heating_capacity_at_speed_7 [number]
rated_water_heating_cop_at_speed_7 [number] (Default: 3.2)
rated_sensible_heat_ratio_at_speed_7 [number] (Default: 0.85)
speed_7_reference_unit_rated_air_flow_rate [number]
speed_7_reference_unit_rated_water_flow_rate [number]
speed_7_reference_unit_water_pump_input_power_at_rated_conditions [number]
speed_7_total_wh_capacity_function_of_temperature_curve_name [string]
speed_7_total_wh_capacity_function_of_air_flow_fraction_curve_name [string]
speed_7_total_wh_capacity_function_of_water_flow_fraction_curve_name [string]
speed_7_cop_function_of_temperature_curve_name [string]
speed_7_cop_function_of_air_flow_fraction_curve_name [string]
speed_7_cop_function_of_water_flow_fraction_curve_name [string]
rated_water_heating_capacity_at_speed_8 [number]
rated_water_heating_cop_at_speed_8 [number] (Default: 3.2)
rated_sensible_heat_ratio_at_speed_8 [number] (Default: 0.85)
speed_8_reference_unit_rated_air_flow_rate [number]
speed_8_reference_unit_rated_water_flow_rate [number]
speed_8_reference_unit_water_pump_input_power_at_rated_conditions [number]
speed_8_total_wh_capacity_function_of_temperature_curve_name [string]
speed_8_total_wh_capacity_function_of_air_flow_fraction_curve_name [string]
speed_8_total_wh_capacity_function_of_water_flow_fraction_curve_name [string]
speed_8_cop_function_of_temperature_curve_name [string]
speed_8_cop_function_of_air_flow_fraction_curve_name [string]
speed_8_cop_function_of_water_flow_fraction_curve_name [string]
rated_water_heating_capacity_at_speed_9 [number]
rated_water_heating_cop_at_speed_9 [number] (Default: 3.2)
rated_sensible_heat_ratio_at_speed_9 [number] (Default: 0.85)
speed_9_reference_unit_rated_air_flow_rate [number]
speed_9_reference_unit_rated_water_flow_rate [number]
speed_9_reference_unit_water_pump_input_power_at_rated_conditions [number]
speed_9_total_wh_capacity_function_of_temperature_curve_name [string]
speed_9_total_wh_capacity_function_of_air_flow_fraction_curve_name [string]
speed_9_total_wh_capacity_function_of_water_flow_fraction_curve_name [string]
speed_9_cop_function_of_temperature_curve_name [string]
speed_9_cop_function_of_air_flow_fraction_curve_name [string]
speed_9_cop_function_of_water_flow_fraction_curve_name [string]
rated_water_heating_capacity_at_speed_10 [number]
rated_water_heating_cop_at_speed_10 [number] (Default: 3.2)
rated_sensible_heat_ratio_at_speed_10 [number] (Default: 0.85)
speed_10_reference_unit_rated_air_flow_rate [number]
speed_10_reference_unit_rated_water_flow_rate [number]
speed_10_reference_unit_water_pump_input_power_at_rated_conditions [number]
speed_10_total_wh_capacity_function_of_temperature_curve_name [string]
speed_10_total_wh_capacity_function_of_air_flow_fraction_curve_name [string]
speed_10_total_wh_capacity_function_of_water_flow_fraction_curve_name [string]
speed_10_cop_function_of_temperature_curve_name [string]
speed_10_cop_function_of_air_flow_fraction_curve_name [string]
speed_10_cop_function_of_water_flow_fraction_curve_name [string]
Coil:WaterHeating:Desuperheater
Desuperheater air heating coil. The heating energy provided by this coil is reclaimed from the superheated refrigerant gas leaving a compressor and does not impact the performance of the compressor. This coil must be used with a water heater tank, see Water Heater:Mixed.

Fields

availability_schedule_name [string]
setpoint_temperature_schedule_name [string]
dead_band_temperature_difference [number] (Default: 5.0)
rated_heat_reclaim_recovery_efficiency [number]
rated_inlet_water_temperature [number]
rated_outdoor_air_temperature [number]
maximum_inlet_water_temperature_for_heat_reclaim [number]
heat_reclaim_efficiency_function_of_temperature_curve_name [string]
water_inlet_node_name [string]
water_outlet_node_name [string]
tank_object_type [string] (Default: WaterHeater:Mixed)
tank_name [string]
heating_source_object_type [string]
heating_source_name [string]
water_flow_rate [number]
water_pump_power [number] (Default: 0.0)
fraction_of_pump_heat_to_water [number] (Default: 0.2)
on_cycle_parasitic_electric_load [number] (Default: 0.0)
off_cycle_parasitic_electric_load [number] (Default: 0.0)
CoilSystem:Cooling:DX
Virtual container component that consists of a DX cooling coil and its associated controls. This control object supports several different types of DX cooling coils and may be placed directly in an air loop branch or outdoor air equipment list.

Fields

availability_schedule_name [string]
dx_cooling_coil_system_inlet_node_name [string]
dx_cooling_coil_system_outlet_node_name [string]
dx_cooling_coil_system_sensor_node_name [string]
cooling_coil_object_type [string]
cooling_coil_name [string]
dehumidification_control_type [string] (Default: None)
run_on_sensible_load [string] (Default: Yes)
run_on_latent_load [string] (Default: No)
use_outdoor_air_dx_cooling_coil [string] (Default: No)
outdoor_air_dx_cooling_coil_leaving_minimum_air_temperature [number] (Default: 2.0)
CoilSystem:Heating:DX
Virtual container component that consists of a DX heating coil (heat pump) and its associated controls. This control object supports two different types of DX heating coils and may be placed directly in an air loop branch or outdoor air equipment list.

Fields

availability_schedule_name [string]
heating_coil_object_type [string]
heating_coil_name [string]
CoilSystem:Cooling:Water:HeatExchangerAssisted
Virtual component consisting of a chilled-water cooling coil and an air-to-air heat exchanger. The air-to-air heat exchanger precools the air entering the cooling coil and reuses this energy to reheat the supply air leaving the cooling coil. This heat exchange process improves the latent removal performance of the cooling coil (lower sensible heat ratio).

Fields

heat_exchanger_object_type [string]
heat_exchanger_name [string]
cooling_coil_object_type [string]
cooling_coil_name [string]
CoilSystem:Cooling:DX:HeatExchangerAssisted
Virtual component consisting of a direct expansion (DX) cooling coil and an air-to-air heat exchanger. The air-to-air heat exchanger precools the air entering the cooling coil and reuses this energy to reheat the supply air leaving the cooling coil. This heat exchange process improves the latent removal performance of the cooling coil (lower sensible heat ratio).

Fields

heat_exchanger_object_type [string]
heat_exchanger_name [string]
cooling_coil_object_type [string]
cooling_coil_name [string]
CoilSystem:IntegratedHeatPump:AirSource
This object is used for air-source integrated heat pump, a collection of its working modes.

Fields

supply_hot_water_flow_sensor_node_name [string]
space_cooling_coil_name [string]
space_heating_coil_name [string]
dedicated_water_heating_coil_name [string]
scwh_coil_name [string]
scdwh_cooling_coil_name [string]
scdwh_water_heating_coil_name [string]
shdwh_heating_coil_name [string]
shdwh_water_heating_coil_name [string]
indoor_temperature_limit_for_scwh_mode [number] (Default: 20.0)
ambient_temperature_limit_for_scwh_mode [number] (Default: 27.0)
indoor_temperature_above_which_wh_has_higher_priority [number] (Default: 20.0)
ambient_temperature_above_which_wh_has_higher_priority [number] (Default: 20.0)
flag_to_indicate_load_control_in_scwh_mode [number] (Default: 0.0)
minimum_speed_level_for_scwh_mode [number] (Default: 1.0)
maximum_water_flow_volume_before_switching_from_scdwh_to_scwh_mode [number] (Default: 0.0)
minimum_speed_level_for_scdwh_mode [number] (Default: 1.0)
maximum_running_time_before_allowing_electric_resistance_heat_use_during_shdwh_mode [number] (Default: 360.0)
minimum_speed_level_for_shdwh_mode [number] (Default: 1.0)
Coil:Cooling:DX:SingleSpeed:ThermalStorage
Direct expansion (DX) cooling coil and condensing unit (includes electric compressor and condenser fan), single-speed with packaged integrated thermal storage for cooling.

Fields

availability_schedule_name [string]
operating_mode_control_method [string]
operation_mode_control_schedule_name [string]
storage_type [string]
user_defined_fluid_type [string]
fluid_storage_volume [unknown field type]
ice_storage_capacity [unknown field type]
storage_capacity_sizing_factor [number]
storage_tank_ambient_temperature_node_name [string]
storage_tank_to_ambient_u_value_times_area_heat_transfer_coefficient [number]
fluid_storage_tank_rating_temperature [number]
rated_evaporator_air_flow_rate [unknown field type]
evaporator_air_inlet_node_name [string]
evaporator_air_outlet_node_name [string]
cooling_only_mode_available [string]
cooling_only_mode_rated_total_evaporator_cooling_capacity [unknown field type]
cooling_only_mode_rated_sensible_heat_ratio [number] (Default: 0.7)
cooling_only_mode_rated_cop [number] (Default: 3.0)
cooling_only_mode_total_evaporator_cooling_capacity_function_of_temperature_curve_name [string]
cooling_only_mode_total_evaporator_cooling_capacity_function_of_flow_fraction_curve_name [string]
cooling_only_mode_energy_input_ratio_function_of_temperature_curve_name [string]
cooling_only_mode_energy_input_ratio_function_of_flow_fraction_curve_name [string]
cooling_only_mode_part_load_fraction_correlation_curve_name [string]
cooling_only_mode_sensible_heat_ratio_function_of_temperature_curve_name [string]
cooling_only_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name [string]
cooling_and_charge_mode_available [string]
cooling_and_charge_mode_rated_total_evaporator_cooling_capacity [unknown field type]
cooling_and_charge_mode_capacity_sizing_factor [number] (Default: 0.5)
cooling_and_charge_mode_rated_storage_charging_capacity [unknown field type]
cooling_and_charge_mode_storage_capacity_sizing_factor [number] (Default: 0.5)
cooling_and_charge_mode_rated_sensible_heat_ratio [number] (Default: 0.7)
cooling_and_charge_mode_cooling_rated_cop [number] (Default: 3.0)
cooling_and_charge_mode_charging_rated_cop [number] (Default: 3.0)
cooling_and_charge_mode_total_evaporator_cooling_capacity_function_of_temperature_curve_name [string]
cooling_and_charge_mode_total_evaporator_cooling_capacity_function_of_flow_fraction_curve_name [string]
cooling_and_charge_mode_evaporator_energy_input_ratio_function_of_temperature_curve_name [string]
cooling_and_charge_mode_evaporator_energy_input_ratio_function_of_flow_fraction_curve_name [string]
cooling_and_charge_mode_evaporator_part_load_fraction_correlation_curve_name [string]
cooling_and_charge_mode_storage_charge_capacity_function_of_temperature_curve_name [string]
cooling_and_charge_mode_storage_charge_capacity_function_of_total_evaporator_plr_curve_name [string]
cooling_and_charge_mode_storage_energy_input_ratio_function_of_temperature_curve_name [string]
cooling_and_charge_mode_storage_energy_input_ratio_function_of_flow_fraction_curve_name [string]
cooling_and_charge_mode_storage_energy_part_load_fraction_correlation_curve_name [string]
cooling_and_charge_mode_sensible_heat_ratio_function_of_temperature_curve_name [string]
cooling_and_charge_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name [string]
cooling_and_discharge_mode_available [string]
cooling_and_discharge_mode_rated_total_evaporator_cooling_capacity [unknown field type]
cooling_and_discharge_mode_evaporator_capacity_sizing_factor [number] (Default: 1.0)
cooling_and_discharge_mode_rated_storage_discharging_capacity [unknown field type]
cooling_and_discharge_mode_storage_discharge_capacity_sizing_factor [number] (Default: 1.0)
cooling_and_discharge_mode_rated_sensible_heat_ratio [number] (Default: 0.7)
cooling_and_discharge_mode_cooling_rated_cop [number] (Default: 3.0)
cooling_and_discharge_mode_discharging_rated_cop [number] (Default: 3.0)
cooling_and_discharge_mode_total_evaporator_cooling_capacity_function_of_temperature_curve_name [string]
cooling_and_discharge_mode_total_evaporator_cooling_capacity_function_of_flow_fraction_curve_name [string]
cooling_and_discharge_mode_evaporator_energy_input_ratio_function_of_temperature_curve_name [string]
cooling_and_discharge_mode_evaporator_energy_input_ratio_function_of_flow_fraction_curve_name [string]
cooling_and_discharge_mode_evaporator_part_load_fraction_correlation_curve_name [string]
cooling_and_discharge_mode_storage_discharge_capacity_function_of_temperature_curve_name [string]
cooling_and_discharge_mode_storage_discharge_capacity_function_of_flow_fraction_curve_name [string]
cooling_and_discharge_mode_storage_discharge_capacity_function_of_total_evaporator_plr_curve_name [string]
cooling_and_discharge_mode_storage_energy_input_ratio_function_of_temperature_curve_name [string]
cooling_and_discharge_mode_storage_energy_input_ratio_function_of_flow_fraction_curve_name [string]
cooling_and_discharge_mode_storage_energy_part_load_fraction_correlation_curve_name [string]
cooling_and_discharge_mode_sensible_heat_ratio_function_of_temperature_curve_name [string]
cooling_and_discharge_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name [string]
charge_only_mode_available [string]
charge_only_mode_rated_storage_charging_capacity [unknown field type]
charge_only_mode_capacity_sizing_factor [number] (Default: 1.0)
charge_only_mode_charging_rated_cop [number] (Default: 3.0)
charge_only_mode_storage_charge_capacity_function_of_temperature_curve_name [string]
charge_only_mode_storage_energy_input_ratio_function_of_temperature_curve_name [string]
discharge_only_mode_available [string]
discharge_only_mode_rated_storage_discharging_capacity [unknown field type]
discharge_only_mode_capacity_sizing_factor [number] (Default: 1.0)
discharge_only_mode_rated_sensible_heat_ratio [number]
discharge_only_mode_rated_cop [number] (Default: 3.0)
discharge_only_mode_storage_discharge_capacity_function_of_temperature_curve_name [string]
discharge_only_mode_storage_discharge_capacity_function_of_flow_fraction_curve_name [string]
discharge_only_mode_energy_input_ratio_function_of_temperature_curve_name [string]
discharge_only_mode_energy_input_ratio_function_of_flow_fraction_curve_name [string]
discharge_only_mode_part_load_fraction_correlation_curve_name [string]
discharge_only_mode_sensible_heat_ratio_function_of_temperature_curve_name [string]
discharge_only_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name [string]
ancillary_electric_power [number]
cold_weather_operation_minimum_outdoor_air_temperature [number]
cold_weather_operation_ancillary_power [number]
condenser_air_inlet_node_name [string]
condenser_air_outlet_node_name [string]
condenser_design_air_flow_rate [unknown field type]
condenser_air_flow_sizing_factor [number] (Default: 1.0)
condenser_type [string] (Default: AirCooled)
evaporative_condenser_effectiveness [number] (Default: 0.7)
evaporative_condenser_pump_rated_power_consumption [unknown field type] (Default: 0.0)
basin_heater_capacity [number] (Default: 0.0)
basin_heater_setpoint_temperature [number] (Default: 2.0)
basin_heater_availability_schedule_name [string]
supply_water_storage_tank_name [string]
condensate_collection_water_storage_tank_name [string]
storage_tank_plant_connection_inlet_node_name [string]
storage_tank_plant_connection_outlet_node_name [string]
storage_tank_plant_connection_design_flow_rate [number]
storage_tank_plant_connection_heat_transfer_effectiveness [number] (Default: 0.7)
storage_tank_minimum_operating_limit_fluid_temperature [number]
storage_tank_maximum_operating_limit_fluid_temperature [number]
"""