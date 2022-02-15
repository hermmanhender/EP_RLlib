"""
Solar Collectors
"""
"""
SolarCollectorPerformance:FlatPlate
Thermal and optical performance parameters for a single flat plate solar collector module. These parameters are based on the testing methodologies described in ASHRAE Standards 93 and 96 which are used Solar Rating and Certification Corporation (SRCC) Directory of SRCC Certified Solar Collector Ratings. See EnergyPlus DataSets file SolarCollectors.idf.

Fields

gross_area [number]
test_fluid [string] (Default: Water)
test_flow_rate [number]
test_correlation_type [string]
coefficient_1_of_efficiency_equation [number]
coefficient_2_of_efficiency_equation [number]
coefficient_3_of_efficiency_equation [number]
coefficient_2_of_incident_angle_modifier [number]
coefficient_3_of_incident_angle_modifier [number]
SolarCollector:FlatPlate:Water
Flat plate water solar collector (single glazed, unglazed, or evacuated tube). Thermal and optical properties are taken from the referenced SolarCollectorPerformance:FlatPlate object. Collector tilt, azimuth, and gross area are taken from the referenced building surface or shading surface. The collector surface participates normally in all shading calculations.

Fields

solarcollectorperformance_name [string]
surface_name [string]
inlet_node_name [string]
outlet_node_name [string]
maximum_flow_rate [number]
SolarCollector:FlatPlate:PhotovoltaicThermal
Models hybrid photovoltaic-thermal (PVT) solar collectors that convert incident solar energy into both electricity and useful thermal energy by heating air or water.

Fields

surface_name [string]
photovoltaic_thermal_model_performance_name [string]
photovoltaic_name [string]
thermal_working_fluid_type [string]
water_inlet_node_name [string]
water_outlet_node_name [string]
air_inlet_node_name [string]
air_outlet_node_name [string]
design_flow_rate [unknown field type]
SolarCollectorPerformance:PhotovoltaicThermal:Simple
Thermal performance parameters for a hybrid photovoltaic-thermal (PVT) solar collector.

Fields

fraction_of_surface_area_with_active_thermal_collector [number]
thermal_conversion_efficiency_input_mode_type [string]
value_for_thermal_conversion_efficiency_if_fixed [number]
thermal_conversion_efficiency_schedule_name [string]
front_surface_emittance [number] (Default: 0.84)
SolarCollector:IntegralCollectorStorage
Glazed solar collector with integral storage unit. Thermal and optical properties are taken from the referenced SolarCollectorPerformance:IntegralCollectorStorage object. Collector tilt, azimuth, and gross area are taken from the referenced building surface or shading surface. The collector surface participates normally in all shading calculations.

Fields

integralcollectorstorageparameters_name [string]
surface_name [string]
bottom_surface_boundary_conditions_type [string] (Default: AmbientAir)
boundary_condition_model_name [string]
inlet_node_name [string]
outlet_node_name [string]
maximum_flow_rate [number]
SolarCollectorPerformance:IntegralCollectorStorage
Thermal and optical performance parameters for a single glazed solar collector with integral storage unit.

Fields

ics_collector_type [string] (Default: RectangularTank)
gross_area [number]
collector_water_volume [number]
bottom_heat_loss_conductance [number] (Default: 0.4)
side_heat_loss_conductance [number] (Default: 0.6)
aspect_ratio [number] (Default: 0.8)
collector_side_height [number] (Default: 0.2)
thermal_mass_of_absorber_plate [number] (Default: 0.0)
number_of_covers [number] (Default: 2.0)
cover_spacing [number] (Default: 0.05)
refractive_index_of_outer_cover [number] (Default: 1.526)
extinction_coefficient_times_thickness_of_outer_cover [number] (Default: 0.045)
emissivity_of_outer_cover [number] (Default: 0.88)
refractive_index_of_inner_cover [number] (Default: 1.37)
extinction_coefficient_times_thickness_of_the_inner_cover [number] (Default: 0.008)
emissivity_of_inner_cover [number] (Default: 0.88)
absorptance_of_absorber_plate [number] (Default: 0.96)
emissivity_of_absorber_plate [number] (Default: 0.3)
SolarCollector:UnglazedTranspired
Unglazed transpired solar collector (UTSC) used to condition outdoor air. This type of collector is generally used to heat air drawn through perforated absorbers and also recover heat conducted out through the underlying surface. This object represents a single collector attached to one or more building or shading surfaces and to one or more outdoor air systems.

Fields

boundary_conditions_model_name [string]
availability_schedule_name [string]
inlet_node_name [string]
outlet_node_name [string]
setpoint_node_name [string]
zone_node_name [string]
free_heating_setpoint_schedule_name [string]
diameter_of_perforations_in_collector [number]
distance_between_perforations_in_collector [number]
thermal_emissivity_of_collector_surface [number]
solar_absorbtivity_of_collector_surface [number]
effective_overall_height_of_collector [number]
effective_gap_thickness_of_plenum_behind_collector [number]
effective_cross_section_area_of_plenum_behind_collector [number]
hole_layout_pattern_for_pitch [string] (Default: Square)
heat_exchange_effectiveness_correlation [string] (Default: Kutscher1994)
ratio_of_actual_collector_surface_area_to_projected_surface_area [number] (Default: 1.0)
roughness_of_collector [string]
collector_thickness [number]
effectiveness_for_perforations_with_respect_to_wind [number] (Default: 0.25)
discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow [number] (Default: 0.65)
surfaces [Array of {surface_name}]
SolarCollector:UnglazedTranspired:Multisystem
quad-tuples of inlet, outlet, control, and zone nodes for multiple different outdoor air systems attached to same collector

Fields

solar_collector_name [string]
systems [Array of {outdoor_air_system_collector_inlet_node, outdoor_air_system_collector_outlet_node, outdoor_air_system_mixed_air_node, outdoor_air_system_zone_node}]

"""