"""
# Refrigeration
"""
"""
Refrigeration:Case
The Refrigeration Case object works in conjunction with a compressor rack, a refrigeration system, or a secondary loop to simulate the performance of a refrigerated case system. The object calculates the energy use for lights, fans and anti-sweat heaters and accounts for the sensible and latent heat exchange with the surrounding environment (termed “case credits”) which impacts the temperature and humidity in the zone where the case is located.

Fields

availability_schedule_name [string]
zone_name [string]
rated_ambient_temperature [number] (Default: 23.9)
rated_ambient_relative_humidity [number] (Default: 55.0)
rated_total_cooling_capacity_per_unit_length [number] (Default: 1900.0)
rated_latent_heat_ratio [number] (Default: 0.3)
rated_runtime_fraction [number] (Default: 0.85)
case_length [number] (Default: 3.0)
case_operating_temperature [number] (Default: 1.1)
latent_case_credit_curve_type [string] (Default: CaseTemperatureMethod)
latent_case_credit_curve_name [string]
standard_case_fan_power_per_unit_length [number] (Default: 75.0)
operating_case_fan_power_per_unit_length [number] (Default: 75.0)
standard_case_lighting_power_per_unit_length [number] (Default: 90.0)
installed_case_lighting_power_per_unit_length [number]
case_lighting_schedule_name [string]
fraction_of_lighting_energy_to_case [number] (Default: 1.0)
case_anti_sweat_heater_power_per_unit_length [number] (Default: 0.0)
minimum_anti_sweat_heater_power_per_unit_length [number] (Default: 0.0)
anti_sweat_heater_control_type [string] (Default: None)
humidity_at_zero_anti_sweat_heater_energy [number] (Default: -10.0)
case_height [number] (Default: 1.5)
fraction_of_anti_sweat_heater_energy_to_case [number] (Default: 1.0)
case_defrost_power_per_unit_length [number] (Default: 0.0)
case_defrost_type [string] (Default: OffCycle)
case_defrost_schedule_name [string]
case_defrost_drip_down_schedule_name [string]
defrost_energy_correction_curve_type [string] (Default: None)
defrost_energy_correction_curve_name [string]
under_case_hvac_return_air_fraction [number] (Default: 0.0)
refrigerated_case_restocking_schedule_name [string]
case_credit_fraction_schedule_name [string]
design_evaporator_temperature_or_brine_inlet_temperature [number]
average_refrigerant_charge_inventory [number] (Default: 0.0)
under_case_hvac_return_air_node_name [string]
Refrigeration:CompressorRack
Works in conjunction with the refrigeration case and walk-in objects to simulate the performance of a refrigerated case system. This object models the electric consumption of the rack compressors and the condenser fans. Heat can be rejected either outdoors or to a zone. Compressor rack waste heat can also be reclaimed for use by an optional air- or water-heating coil (Coil:Heating:Desuperheater and Coil:WaterHeating:Desuperheater).

Fields

heat_rejection_location [string] (Default: Outdoors)
design_compressor_rack_cop [number] (Default: 2.0)
compressor_rack_cop_function_of_temperature_curve_name [string]
design_condenser_fan_power [number] (Default: 250.0)
condenser_fan_power_function_of_temperature_curve_name [string]
condenser_type [string] (Default: AirCooled)
water_cooled_condenser_inlet_node_name [string]
water_cooled_condenser_outlet_node_name [string]
water_cooled_loop_flow_type [string] (Default: VariableFlow)
water_cooled_condenser_outlet_temperature_schedule_name [string]
water_cooled_condenser_design_flow_rate [number]
water_cooled_condenser_maximum_flow_rate [number]
water_cooled_condenser_maximum_water_outlet_temperature [number] (Default: 55.0)
water_cooled_condenser_minimum_water_inlet_temperature [number] (Default: 10.0)
evaporative_condenser_availability_schedule_name [string]
evaporative_condenser_effectiveness [number] (Default: 0.9)
evaporative_condenser_air_flow_rate [unknown field type] (Default: Autocalculate)
basin_heater_capacity [number] (Default: 200.0)
basin_heater_setpoint_temperature [number] (Default: 2.0)
design_evaporative_condenser_water_pump_power [unknown field type] (Default: 1000.0)
evaporative_water_supply_tank_name [string]
condenser_air_inlet_node_name [string]
end_use_subcategory [string] (Default: General)
refrigeration_case_name_or_walkin_name_or_caseandwalkinlist_name [string]
heat_rejection_zone_name [string]
Refrigeration:CaseAndWalkInList
Provides a list of all the refrigerated cases, walk in coolers, or air chillers cooled by a single refrigeration system. Note that the names of all cases, walk-ins ,air chillers, and CaseAndWalkInLists must be unique. That is, you cannot give a list the same name as one of list items. This list may contain a combination of case and walk-in names OR a list of air chiller names. Air chillers may not be included in any list that also includes cases or walk-ins.

Fields

cases_and_walkins [Array of {case_or_walkin_name}]
Refrigeration:Condenser:AirCooled
Air cooled condenser for a refrigeration system (Refrigeration:System).

Fields

rated_effective_total_heat_rejection_rate_curve_name [string]
rated_subcooling_temperature_difference [number] (Default: 0.0)
condenser_fan_speed_control_type [string] (Default: Fixed)
rated_fan_power [number] (Default: 250.0)
minimum_fan_air_flow_ratio [number] (Default: 0.2)
air_inlet_node_name_or_zone_name [string]
end_use_subcategory [string] (Default: General)
condenser_refrigerant_operating_charge_inventory [number] (Default: 0.0)
condensate_receiver_refrigerant_inventory [number] (Default: 0.0)
condensate_piping_refrigerant_inventory [number] (Default: 0.0)
Refrigeration:Condenser:EvaporativeCooled
Evaporative-cooled condenser for a refrigeration system (Refrigeration:System).

Fields

rated_effective_total_heat_rejection_rate [number]
rated_subcooling_temperature_difference [number] (Default: 0.0)
fan_speed_control_type [string] (Default: Fixed)
rated_fan_power [number]
minimum_fan_air_flow_ratio [number] (Default: 0.2)
approach_temperature_constant_term [number] (Default: 6.63)
approach_temperature_coefficient_2 [number] (Default: 0.468)
approach_temperature_coefficient_3 [number] (Default: 17.93)
approach_temperature_coefficient_4 [number] (Default: -0.322)
minimum_capacity_factor [number] (Default: 0.5)
maximum_capacity_factor [number] (Default: 5.0)
air_inlet_node_name [string]
rated_air_flow_rate [unknown field type] (Default: Autocalculate)
basin_heater_capacity [number] (Default: 200.0)
basin_heater_setpoint_temperature [number] (Default: 2.0)
rated_water_pump_power [unknown field type] (Default: 1000.0)
evaporative_water_supply_tank_name [string]
evaporative_condenser_availability_schedule_name [string]
end_use_subcategory [string] (Default: General)
condenser_refrigerant_operating_charge_inventory [number] (Default: 0.0)
condensate_receiver_refrigerant_inventory [number] (Default: 0.0)
condensate_piping_refrigerant_inventory [number] (Default: 0.0)
Refrigeration:Condenser:WaterCooled
Water cooled condenser for a refrigeration system (Refrigeration:System).

Fields

rated_effective_total_heat_rejection_rate [number]
rated_condensing_temperature [number]
rated_subcooling_temperature_difference [number] (Default: 0.0)
rated_water_inlet_temperature [number]
water_inlet_node_name [string]
water_outlet_node_name [string]
water_cooled_loop_flow_type [string] (Default: VariableFlow)
water_outlet_temperature_schedule_name [string]
water_design_flow_rate [number]
water_maximum_flow_rate [number]
water_maximum_water_outlet_temperature [number] (Default: 55.0)
water_minimum_water_inlet_temperature [number] (Default: 10.0)
end_use_subcategory [string] (Default: General)
condenser_refrigerant_operating_charge_inventory [number]
condensate_receiver_refrigerant_inventory [number]
condensate_piping_refrigerant_inventory [number]
Refrigeration:Condenser:Cascade
Cascade condenser for a refrigeration system (Refrigeration:System). The cascade condenser is unlike the other condenser options because it rejects heat to another, higher-temperature, refrigeration system. That is, the cascade condenser acts as a heat rejection object for one system, but acts as a refrigeration load for another system.

Fields

rated_condensing_temperature [number]
rated_approach_temperature_difference [number] (Default: 3.0)
rated_effective_total_heat_rejection_rate [number]
condensing_temperature_control_type [string] (Default: Fixed)
condenser_refrigerant_operating_charge_inventory [number]
condensate_receiver_refrigerant_inventory [number]
condensate_piping_refrigerant_inventory [number]
Refrigeration:GasCooler:AirCooled
The transcritical refrigeration system requires a single gas cooler to reject the system heat.

Fields

rated_total_heat_rejection_rate_curve_name [string]
gas_cooler_fan_speed_control_type [string] (Default: Fixed)
rated_fan_power [number] (Default: 5000.0)
minimum_fan_air_flow_ratio [number] (Default: 0.2)
transition_temperature [number] (Default: 27.0)
transcritical_approach_temperature [number] (Default: 3.0)
subcritical_temperature_difference [number] (Default: 10.0)
minimum_condensing_temperature [number] (Default: 10.0)
air_inlet_node_name [string]
end_use_subcategory [string] (Default: General)
gas_cooler_refrigerant_operating_charge_inventory [number] (Default: 0.0)
gas_cooler_receiver_refrigerant_inventory [number] (Default: 0.0)
gas_cooler_outlet_piping_refrigerant_inventory [number] (Default: 0.0)
Refrigeration:TransferLoadList
A refrigeration system may provide cooling to other, secondary, systems through either a secondary loop or a cascade condenser. If multiple transfer loads are served by a single primary system, use this list to group them together for reference by the primary system (see the field “Refrigeration Transfer Load or TransferLoad List Name” in the Refrigeration:System object).

Fields

transfer_loads [Array of {cascade_condenser_name_or_secondary_system_name}]
Refrigeration:Subcooler
Two types of subcoolers are modeled by the detailed refrigeration system. The liquid suction heat exchanger uses cool suction gas to subcool the hot condensate after it leaves the condenser and before it reaches the thermal expansion valve. A mechanical subcooler is used to transfer cooling capacity from one refrigeration system to another.

Fields

subcooler_type [string] (Default: LiquidSuction)
liquid_suction_design_subcooling_temperature_difference [number]
design_liquid_inlet_temperature [number]
design_vapor_inlet_temperature [number]
capacity_providing_system [string]
outlet_control_temperature [number]
Refrigeration:Compressor
Refrigeration system compressor. Data is available for many compressors in the RefrigerationCompressor.idf dataset

Fields

refrigeration_compressor_power_curve_name [string]
refrigeration_compressor_capacity_curve_name [string]
rated_superheat [number]
rated_return_gas_temperature [number]
rated_liquid_temperature [number]
rated_subcooling [number]
end_use_subcategory [string] (Default: General)
mode_of_operation [string] (Default: Subcritical)
transcritical_compressor_power_curve_name [string]
transcritical_compressor_capacity_curve_name [string]
Refrigeration:CompressorList
List of all the compressors included within a single refrigeration system (Refrigeration:System). Each list must contain at least one compressor. The order in which the individual compressors are listed here will be the order in which the compressors are dispatched to meet the system load. IMPORTANT: List compressor names in the order in which the compressors will be loaded Data is available for many compressors in the RefrigerationCompressor.idf dataset

Fields

compressors [Array of {refrigeration_compressor_name}]
Refrigeration:System
Simulates the performance of a supermarket refrigeration system when used along with other objects to define the refrigeration load(s), the compressor(s), and the condenser.

Fields

refrigerated_case_or_walkin_or_caseandwalkinlist_name [string]
refrigeration_transfer_load_or_transferload_list_name [string]
refrigeration_condenser_name [string]
compressor_or_compressorlist_name [string]
minimum_condensing_temperature [number]
refrigeration_system_working_fluid_type [string]
suction_temperature_control_type [string] (Default: ConstantSuctionTemperature)
mechanical_subcooler_name [string]
liquid_suction_heat_exchanger_subcooler_name [string]
sum_ua_suction_piping [number] (Default: 0.0)
suction_piping_zone_name [string]
end_use_subcategory [string] (Default: General)
number_of_compressor_stages [unknown field type] (Default: 1.0)
intercooler_type [string] (Default: None)
shell_and_coil_intercooler_effectiveness [number] (Default: 0.8)
high_stage_compressor_or_compressorlist_name [string]
Refrigeration:TranscriticalSystem
Detailed transcritical carbon dioxide (CO2) booster refrigeration systems used in supermarkets. The object allows for modeling either a single stage system with medium-temperature loads or a two stage system with both medium- and low-temperature loads.

Fields

system_type [string]
medium_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name [string]
low_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name [string]
refrigeration_gas_cooler_name [string]
high_pressure_compressor_or_compressorlist_name [string]
low_pressure_compressor_or_compressorlist_name [string]
receiver_pressure [number] (Default: 4000000.0)
subcooler_effectiveness [number] (Default: 0.4)
refrigeration_system_working_fluid_type [string]
sum_ua_suction_piping_for_medium_temperature_loads [number] (Default: 0.0)
medium_temperature_suction_piping_zone_name [string]
sum_ua_suction_piping_for_low_temperature_loads [number] (Default: 0.0)
low_temperature_suction_piping_zone_name [string]
end_use_subcategory [string] (Default: General)
Refrigeration:SecondarySystem
Works in conjunction with refrigerated cases and walkins to simulate the performance of a secondary loop supermarket refrigeration system. Heat from the refrigeration loads served by the secondary loop is absorbed by a primary refrigeration system (Refrigeration:System). The SecondarySystem object simulates a heat exchanger that is an evaporator, or refrigeration load, on the primary refrigeration system.

Fields

refrigerated_case_or_walkin_or_caseandwalkinlist_name [string]
circulating_fluid_type [string]
circulating_fluid_name [string]
evaporator_capacity [number]
evaporator_flow_rate_for_secondary_fluid [number]
evaporator_evaporating_temperature [number]
evaporator_approach_temperature_difference [number]
evaporator_range_temperature_difference [number]
number_of_pumps_in_loop [number] (Default: 1.0)
total_pump_flow_rate [number]
total_pump_power [number]
total_pump_head [number]
phasechange_circulating_rate [number] (Default: 2.5)
pump_drive_type [string] (Default: Constant)
variable_speed_pump_cubic_curve_name [string]
pump_motor_heat_to_fluid [number] (Default: 0.85)
sum_ua_distribution_piping [number] (Default: 0.0)
distribution_piping_zone_name [string]
sum_ua_receiver_separator_shell [number] (Default: 0.0)
receiver_separator_zone_name [string]
evaporator_refrigerant_inventory [number] (Default: 0.0)
end_use_subcategory [string] (Default: General)
Refrigeration:WalkIn
Works in conjunction with a compressor rack, a refrigeration system, or a refrigeration secondary system to simulate the performance of a walk-in cooler. The walk-in cooler model uses information at rated conditions along with input descriptions for heat transfer surfaces facing multiple zones to determine performance.

Fields

availability_schedule_name [string]
rated_coil_cooling_capacity [number]
operating_temperature [number]
rated_cooling_source_temperature [number]
rated_total_heating_power [number]
heating_power_schedule_name [string]
rated_cooling_coil_fan_power [number] (Default: 375.0)
rated_circulation_fan_power [number] (Default: 0.0)
rated_total_lighting_power [number]
lighting_schedule_name [string]
defrost_type [string] (Default: Electric)
defrost_control_type [string] (Default: TimeSchedule)
defrost_schedule_name [string]
defrost_drip_down_schedule_name [string]
defrost_power [number]
temperature_termination_defrost_fraction_to_ice [number]
restocking_schedule_name [string]
average_refrigerant_charge_inventory [number] (Default: 0.0)
insulated_floor_surface_area [number]
insulated_floor_u_value [number] (Default: 0.3154)
zone_data [Array of {zone_name, total_insulated_surface_area_facing_zone, insulated_surface_u_value_facing_zone, area_of_glass_reach_in_doors_facing_zone, height_of_glass_reach_in_doors_facing_zone, glass_reach_in_door_u_value_facing_zone, glass_reach_in_door_opening_schedule_name_facing_zone, area_of_stocking_doors_facing_zone, height_of_stocking_doors_facing_zone, stocking_door_u_value_facing_zone, stocking_door_opening_schedule_name_facing_zone, stocking_door_opening_protection_type_facing_zone}]
Refrigeration:AirChiller
Works in conjunction with a refrigeration chiller set, compressor rack, a refrigeration system, or a refrigeration secondary system to simulate the performance of an air chiller, similar to one found in a refrigerated warehouse. Energy use for fans and heaters is modeled based on inputs for nominal power, schedules, and control type. The air chiller model accounts for the sensible and latent heat exchange with the surrounding environment.

Fields

availability_schedule_name [string]
capacity_rating_type [string]
rated_unit_load_factor [number]
rated_capacity [number]
rated_relative_humidity [number] (Default: 85.0)
rated_cooling_source_temperature [number]
rated_temperature_difference_dt1 [number]
maximum_temperature_difference_between_inlet_air_and_evaporating_temperature [number]
coil_material_correction_factor [number] (Default: 1.0)
refrigerant_correction_factor [number] (Default: 1.0)
capacity_correction_curve_type [string]
capacity_correction_curve_name [string]
shr60_correction_factor [number] (Default: 1.48)
rated_total_heating_power [number]
heating_power_schedule_name [string]
fan_speed_control_type [string] (Default: Fixed)
rated_fan_power [number] (Default: 375.0)
rated_air_flow [number]
minimum_fan_air_flow_ratio [number] (Default: 0.2)
defrost_type [string] (Default: Electric)
defrost_control_type [string] (Default: TimeSchedule)
defrost_schedule_name [string]
defrost_drip_down_schedule_name [string]
defrost_power [number]
temperature_termination_defrost_fraction_to_ice [number]
vertical_location [string] (Default: Middle)
average_refrigerant_charge_inventory [number] (Default: 0.0)
ZoneHVAC:RefrigerationChillerSet
Works in conjunction with one or multiple air chillers, compressor racks, refrigeration systems, or refrigeration secondary system objects to simulate the performance of a group of air chillers cooling a single zone. The chiller set model passes information about the zone conditions to determine the performance of individual chiller coils within the set, thus providing the sensible and latent heat exchange with the zone environment.

Fields

availability_schedule_name [string]
zone_name [string]
air_inlet_node_name [string]
air_outlet_node_name [string]
chillers [Array of {air_chiller_name}]
"""