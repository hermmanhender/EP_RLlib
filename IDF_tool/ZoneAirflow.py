"""
# Zone Airflow
"""
"""
ZoneInfiltration:DesignFlowRate
Infiltration is specified as a design level which is modified by a Schedule fraction, temperature difference and wind speed: Infiltration=Idesign * FSchedule * (A + B*|(Tzone-Todb)| + C*WindSpd + D * WindSpd**2) If you use a ZoneList in the Zone or ZoneList name field then this definition applies to all the zones in the ZoneList.

Fields

zone_or_zonelist_name [string]
schedule_name [string]
design_flow_rate_calculation_method [string] (Default: Flow/Zone)
design_flow_rate [number]
flow_per_zone_floor_area [number]
flow_per_exterior_surface_area [number]
air_changes_per_hour [number]
constant_term_coefficient [number] (Default: 1.0)
temperature_term_coefficient [number] (Default: 0.0)
velocity_term_coefficient [number] (Default: 0.0)
velocity_squared_term_coefficient [number] (Default: 0.0)
ZoneInfiltration:EffectiveLeakageArea
Infiltration is specified as effective leakage area at 4 Pa, schedule fraction, stack and wind coefficients, and is a function of temperature difference and wind speed: Infiltration=FSchedule * (AL /1000) SQRT(Cs*|(Tzone-Todb)| + Cw*WindSpd**2 )

Fields

zone_name [string]
schedule_name [string]
effective_air_leakage_area [number]
stack_coefficient [number]
wind_coefficient [number]
ZoneInfiltration:FlowCoefficient
Infiltration is specified as flow coefficient, schedule fraction, stack and wind coefficients, and is a function of temperature difference and wind speed: Infiltration=FSchedule * SQRT( (c * Cs*|(Tzone-Todb)|**n)**2 + (c* Cw*(s * WindSpd)**2n)**2 )

Fields

zone_name [string]
schedule_name [string]
flow_coefficient [number]
stack_coefficient [number]
pressure_exponent [number] (Default: 0.67)
wind_coefficient [number]
shelter_factor [number]
ZoneVentilation:DesignFlowRate
Ventilation is specified as a design level which is modified by a schedule fraction, temperature difference and wind speed: Ventilation=Vdesign * Fschedule * (A + B*|(Tzone-Todb)| + C*WindSpd + D * WindSpd**2) If you use a ZoneList in the Zone or ZoneList name field then this definition applies to all the zones in the ZoneList.

Fields

zone_or_zonelist_name [string]
schedule_name [string]
design_flow_rate_calculation_method [string] (Default: Flow/Zone)
design_flow_rate [number]
flow_rate_per_zone_floor_area [number]
flow_rate_per_person [number]
air_changes_per_hour [number]
ventilation_type [string] (Default: Natural)
fan_pressure_rise [number] (Default: 0.0)
fan_total_efficiency [number] (Default: 1.0)
constant_term_coefficient [number] (Default: 1.0)
temperature_term_coefficient [number] (Default: 0.0)
velocity_term_coefficient [number] (Default: 0.0)
velocity_squared_term_coefficient [number] (Default: 0.0)
minimum_indoor_temperature [number] (Default: -100.0)
minimum_indoor_temperature_schedule_name [string]
maximum_indoor_temperature [number] (Default: 100.0)
maximum_indoor_temperature_schedule_name [string]
delta_temperature [number] (Default: -100.0)
delta_temperature_schedule_name [string]
minimum_outdoor_temperature [number] (Default: -100.0)
minimum_outdoor_temperature_schedule_name [string]
maximum_outdoor_temperature [number] (Default: 100.0)
maximum_outdoor_temperature_schedule_name [string]
maximum_wind_speed [number] (Default: 40.0)
ZoneVentilation:WindandStackOpenArea
This object is specified as natural ventilation driven by wind and stack effect only: Ventilation Wind = Cw * Opening Area * Schedule * WindSpd Ventilation Stack = Cd * Opening Area * Schedule * SQRT(2*g*DH*(|(Tzone-Todb)|/Tzone)) Total Ventilation = SQRT((Ventilation Wind)^2 + (Ventilation Stack)^2)

Fields

zone_name [string]
opening_area [number] (Default: 0.0)
opening_area_fraction_schedule_name [string]
opening_effectiveness [unknown field type] (Default: Autocalculate)
effective_angle [number] (Default: 0.0)
height_difference [number] (Default: 0.0)
discharge_coefficient_for_opening [unknown field type] (Default: Autocalculate)
minimum_indoor_temperature [number] (Default: -100.0)
minimum_indoor_temperature_schedule_name [string]
maximum_indoor_temperature [number] (Default: 100.0)
maximum_indoor_temperature_schedule_name [string]
delta_temperature [number] (Default: -100.0)
delta_temperature_schedule_name [string]
minimum_outdoor_temperature [number] (Default: -100.0)
minimum_outdoor_temperature_schedule_name [string]
maximum_outdoor_temperature [number] (Default: 100.0)
maximum_outdoor_temperature_schedule_name [string]
maximum_wind_speed [number] (Default: 40.0)
ZoneAirBalance:OutdoorAir
Provide a combined zone outdoor air flow by including interactions between mechanical ventilation, infiltration and duct leakage. This object will combine outdoor flows from all ZoneInfiltration and ZoneVentilation objects in the same zone. Balanced flows will be summed, while unbalanced flows will be added in quadrature.

Fields

zone_name [string]
air_balance_method [string] (Default: Quadrature)
induced_outdoor_air_due_to_unbalanced_duct_leakage [number] (Default: 0.0)
induced_outdoor_air_schedule_name [string]
ZoneMixing
ZoneMixing is a simple air exchange from one zone to another. Note that this statement only affects the energy balance of the “receiving” zone and will not produce any effect on the “source” zone. Mixing statements can be complementary and include multiple zones, but the balancing of flows between zones is left to the user’s discretion.

Fields

zone_name [string]
schedule_name [string]
design_flow_rate_calculation_method [string] (Default: Flow/Zone)
design_flow_rate [number]
flow_rate_per_zone_floor_area [number]
flow_rate_per_person [number]
air_changes_per_hour [number]
source_zone_name [string]
delta_temperature [number] (Default: 0.0)
delta_temperature_schedule_name [string]
minimum_zone_temperature_schedule_name [string]
maximum_zone_temperature_schedule_name [string]
minimum_source_zone_temperature_schedule_name [string]
maximum_source_zone_temperature_schedule_name [string]
minimum_outdoor_temperature_schedule_name [string]
maximum_outdoor_temperature_schedule_name [string]
ZoneCrossMixing
ZoneCrossMixing exchanges an equal amount of air between two zones. Note that this statement affects the energy balance of both zones.

Fields

zone_name [string]
schedule_name [string]
design_flow_rate_calculation_method [string] (Default: Flow/Zone)
design_flow_rate [number]
flow_rate_per_zone_floor_area [number]
flow_rate_per_person [number]
air_changes_per_hour [number]
source_zone_name [string]
delta_temperature [number] (Default: 0.0)
delta_temperature_schedule_name [string]
minimum_zone_temperature_schedule_name [string]
maximum_zone_temperature_schedule_name [string]
minimum_source_zone_temperature_schedule_name [string]
maximum_source_zone_temperature_schedule_name [string]
minimum_outdoor_temperature_schedule_name [string]
maximum_outdoor_temperature_schedule_name [string]
ZoneRefrigerationDoorMixing
Refrigeration Door Mixing is used for an opening between two zones that are at the same elevation but have different air temperatures. In this case, the mixing air flow between the two zones is determined by the density difference between the two zones. This would typically be used between two zones in a refrigerated warehouse that are controlled at different temperatures. It could also be used to model a door to a walk-in refrigerated space if that space were modeled as a zone instead of using the object Refrigeration:WalkIn.

Fields

zone_1_name [string]
zone_2_name [string]
schedule_name [string]
door_height [number] (Default: 3.0)
door_area [number] (Default: 9.0)
door_protection_type [string] (Default: None)
ZoneEarthtube
Earth Tube is specified as a design level which is modified by a Schedule fraction, temperature difference and wind speed: Earthtube=Edesign * Fschedule * (A + B*|(Tzone-Todb)| + C*WindSpd + D * WindSpd**2)

Fields

zone_name [string]
schedule_name [string]
design_flow_rate [number]
minimum_zone_temperature_when_cooling [number]
maximum_zone_temperature_when_heating [number]
delta_temperature [number]
earthtube_type [string] (Default: Natural)
fan_pressure_rise [number] (Default: 0.0)
fan_total_efficiency [number] (Default: 1.0)
pipe_radius [number] (Default: 1.0)
pipe_thickness [number] (Default: 0.2)
pipe_length [number] (Default: 15.0)
pipe_thermal_conductivity [number] (Default: 200.0)
pipe_depth_under_ground_surface [number] (Default: 3.0)
soil_condition [string] (Default: HeavyAndDamp)
average_soil_surface_temperature [number]
amplitude_of_soil_surface_temperature [number]
phase_constant_of_soil_surface_temperature [number]
constant_term_flow_coefficient [number] (Default: 1.0)
temperature_term_flow_coefficient [number] (Default: 0.0)
velocity_term_flow_coefficient [number] (Default: 0.0)
velocity_squared_term_flow_coefficient [number] (Default: 0.0)
ZoneCoolTower:Shower
A cooltower (sometimes referred to as a wind tower or a shower cooling tower) models passive downdraught evaporative cooling (PDEC) that is designed to capture the wind at the top of a tower and cool the outdoor air using water evaporation before delivering it to a space.

Fields

availability_schedule_name [string]
zone_name [string]
water_supply_storage_tank_name [string]
flow_control_type [string] (Default: WindDrivenFlow)
pump_flow_rate_schedule_name [string]
maximum_water_flow_rate [number]
effective_tower_height [number]
airflow_outlet_area [number]
maximum_air_flow_rate [number]
minimum_indoor_temperature [number]
fraction_of_water_loss [number]
fraction_of_flow_schedule [number]
rated_power_consumption [number]
ZoneThermalChimney
A thermal chimney is a vertical shaft utilizing solar radiation to enhance natural ventilation. It consists of an absorber wall, air gap and glass cover with high solar transmissivity.

Fields

zone_name [string]
availability_schedule_name [string]
width_of_the_absorber_wall [number]
cross_sectional_area_of_air_channel_outlet [number]
discharge_coefficient [number] (Default: 0.8)
zone_1_name [string]
distance_from_top_of_thermal_chimney_to_inlet_1 [number]
relative_ratios_of_air_flow_rates_passing_through_zone_1 [number] (Default: 1.0)
cross_sectional_areas_of_air_channel_inlet_1 [number]
zone_2_name [string]
distance_from_top_of_thermal_chimney_to_inlet_2 [number]
relative_ratios_of_air_flow_rates_passing_through_zone_2 [number]
cross_sectional_areas_of_air_channel_inlet_2 [number]
zone_3_name [string]
distance_from_top_of_thermal_chimney_to_inlet_3 [number]
relative_ratios_of_air_flow_rates_passing_through_zone_3 [number]
cross_sectional_areas_of_air_channel_inlet_3 [number]
zone_4_name [string]
distance_from_top_of_thermal_chimney_to_inlet_4 [number]
relative_ratios_of_air_flow_rates_passing_through_zone_4 [number]
cross_sectional_areas_of_air_channel_inlet_4 [number]
zone_5_name [string]
distance_from_top_of_thermal_chimney_to_inlet_5 [number]
relative_ratios_of_air_flow_rates_passing_through_zone_5 [number]
cross_sectional_areas_of_air_channel_inlet_5 [number]
zone_6_name [string]
distance_from_top_of_thermal_chimney_to_inlet_6 [number]
relative_ratios_of_air_flow_rates_passing_through_zone_6 [number]
cross_sectional_areas_of_air_channel_inlet_6 [number]
zone_7_name [string]
distance_from_top_of_thermal_chimney_to_inlet_7 [number]
relative_ratios_of_air_flow_rates_passing_through_zone_7 [number]
cross_sectional_areas_of_air_channel_inlet_7 [number]
zone_8_name [string]
distance_from_top_of_thermal_chimney_to_inlet_8 [number]
relative_ratios_of_air_flow_rates_passing_through_zone_8 [number]
cross_sectional_areas_of_air_channel_inlet_8 [number]
zone_9_name [string]
distance_from_top_of_thermal_chimney_to_inlet_9 [number]
relative_ratios_of_air_flow_rates_passing_through_zone_9 [number]
cross_sectional_areas_of_air_channel_inlet_9 [number]
zone_10_name [string]
distance_from_top_of_thermal_chimney_to_inlet_10 [number]
relative_ratios_of_air_flow_rates_passing_through_zone_10 [number]
cross_sectional_areas_of_air_channel_inlet_10 [number]
zone_11_name [string]
distance_from_top_of_thermal_chimney_to_inlet_11 [number]
relative_ratios_of_air_flow_rates_passing_through_zone_11 [number]
cross_sectional_areas_of_air_channel_inlet_11 [number]
zone_12_name [string]
distance_from_top_of_thermal_chimney_to_inlet_12 [number]
relative_ratios_of_air_flow_rates_passing_through_zone_12 [number]
cross_sectional_areas_of_air_channel_inlet_12 [number]
zone_13_name [string]
distance_from_top_of_thermal_chimney_to_inlet_13 [number]
relative_ratios_of_air_flow_rates_passing_through_zone_13 [number]
cross_sectional_areas_of_air_channel_inlet_13 [number]
zone_14_name [string]
distance_from_top_of_thermal_chimney_to_inlet_14 [number]
relative_ratios_of_air_flow_rates_passing_through_zone_14 [number]
cross_sectional_areas_of_air_channel_inlet_14 [number]
zone_15_name [string]
distance_from_top_of_thermal_chimney_to_inlet_15 [number]
relative_ratios_of_air_flow_rates_passing_through_zone_15 [number]
cross_sectional_areas_of_air_channel_inlet_15 [number]
zone_16_name [string]
distance_from_top_of_thermal_chimney_to_inlet_16 [number]
relative_ratios_of_air_flow_rates_passing_through_zone_16 [number]
cross_sectional_areas_of_air_channel_inlet_16 [number]
zone_17_name [string]
distance_from_top_of_thermal_chimney_to_inlet_17 [number]
relative_ratios_of_air_flow_rates_passing_through_zone_17 [number]
cross_sectional_areas_of_air_channel_inlet_17 [number]
zone_18_name [string]
distance_from_top_of_thermal_chimney_to_inlet_18 [number]
relative_ratios_of_air_flow_rates_passing_through_zone_18 [number]
cross_sectional_areas_of_air_channel_inlet_18 [number]
zone_19_name [string]
distance_from_top_of_thermal_chimney_to_inlet_19 [number]
relative_ratios_of_air_flow_rates_passing_through_zone_19 [number]
cross_sectional_areas_of_air_channel_inlet_19 [number]
zone_20_name [string]
distance_from_top_of_thermal_chimney_to_inlet_20 [number]
relative_ratios_of_air_flow_rates_passing_through_zone_20 [number]
cross_sectional_areas_of_air_channel_inlet_20 [number]
"""