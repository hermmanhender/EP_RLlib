"""
# Zone HVAC Radiative/Convective Units
"""
"""
ZoneHVAC:Baseboard:RadiantConvective:Water:Design
Fields

heating_design_capacity_method [string] (Default: HeatingDesignCapacity)
heating_design_capacity_per_floor_area [number]
fraction_of_autosized_heating_design_capacity [number] (Default: 1.0)
convergence_tolerance [number] (Default: 0.001)
fraction_radiant [number]
fraction_of_radiant_energy_incident_on_people [number]
ZoneHVAC:Baseboard:RadiantConvective:Water
The number of surfaces can be expanded beyond 100, if necessary, by adding more groups to the end of the list

Fields

design_object [string]
availability_schedule_name [string]
inlet_node_name [string]
outlet_node_name [string]
rated_average_water_temperature [number] (Default: 87.78)
rated_water_mass_flow_rate [number] (Default: 0.063)
heating_design_capacity [unknown field type] (Default: Autosize)
maximum_water_flow_rate [unknown field type]
surface_fractions [Array of {surface_name, fraction_of_radiant_energy_to_surface}]
ZoneHVAC:Baseboard:RadiantConvective:Steam:Design
Fields

heating_design_capacity_method [string] (Default: HeatingDesignCapacity)
heating_design_capacity_per_floor_area [number]
fraction_of_autosized_heating_design_capacity [number] (Default: 1.0)
convergence_tolerance [number] (Default: 0.001)
fraction_radiant [number]
fraction_of_radiant_energy_incident_on_people [number]
ZoneHVAC:Baseboard:RadiantConvective:Steam
The number of surfaces can be expanded beyond 100, if necessary, by adding more groups to the end of the list.

Fields

design_object [string]
availability_schedule_name [string]
inlet_node_name [string]
outlet_node_name [string]
heating_design_capacity [unknown field type] (Default: Autosize)
degree_of_subcooling [number] (Default: 5.0)
maximum_steam_flow_rate [unknown field type]
surface_fractions [Array of {surface_name, fraction_of_radiant_energy_to_surface}]
ZoneHVAC:Baseboard:RadiantConvective:Electric
The number of surfaces can be expanded beyond 100, if necessary, by adding more groups to the end of the list

Fields

availability_schedule_name [string]
heating_design_capacity_method [string] (Default: HeatingDesignCapacity)
heating_design_capacity [unknown field type] (Default: Autosize)
heating_design_capacity_per_floor_area [number]
fraction_of_autosized_heating_design_capacity [number] (Default: 1.0)
efficiency [number] (Default: 1.0)
fraction_radiant [number]
fraction_of_radiant_energy_incident_on_people [number]
surface_fractions [Array of {surface_name, fraction_of_radiant_energy_to_surface}]
ZoneHVAC:CoolingPanel:RadiantConvective:Water
The number of surfaces can be expanded beyond 100, if necessary, by adding more groups to the end of the list

Fields

availability_schedule_name [string]
water_inlet_node_name [string]
water_outlet_node_name [string]
rated_inlet_water_temperature [number] (Default: 5.0)
rated_inlet_space_temperature [number] (Default: 24.0)
rated_water_mass_flow_rate [number] (Default: 0.063)
cooling_design_capacity_method [string] (Default: CoolingDesignCapacity)
cooling_design_capacity [unknown field type]
cooling_design_capacity_per_floor_area [number]
fraction_of_autosized_cooling_design_capacity [number]
maximum_chilled_water_flow_rate [unknown field type]
control_type [string] (Default: MeanAirTemperature)
cooling_control_throttling_range [number] (Default: 0.5)
cooling_control_temperature_schedule_name [string]
condensation_control_type [string] (Default: SimpleOff)
condensation_control_dewpoint_offset [number] (Default: 1.0)
fraction_radiant [number]
fraction_of_radiant_energy_incident_on_people [number]
surface_fractions [Array of {surface_name, fraction_of_radiant_energy_to_surface}]
ZoneHVAC:Baseboard:Convective:Water
Hot water baseboard heater, convection-only. Natural convection hydronic heating unit.

Fields

availability_schedule_name [string]
inlet_node_name [string]
outlet_node_name [string]
heating_design_capacity_method [string] (Default: HeatingDesignCapacity)
heating_design_capacity [unknown field type] (Default: Autosize)
heating_design_capacity_per_floor_area [number]
fraction_of_autosized_heating_design_capacity [number] (Default: 1.0)
u_factor_times_area_value [unknown field type]
maximum_water_flow_rate [unknown field type]
convergence_tolerance [number] (Default: 0.001)
ZoneHVAC:Baseboard:Convective:Electric
Electric baseboard heater, convection-only. Natural convection electric heating unit.

Fields

availability_schedule_name [string]
heating_design_capacity_method [string] (Default: HeatingDesignCapacity)
heating_design_capacity [unknown field type] (Default: Autosize)
heating_design_capacity_per_floor_area [number]
fraction_of_autosized_heating_design_capacity [number] (Default: 1.0)
efficiency [number] (Default: 1.0)
ZoneHVAC:LowTemperatureRadiant:VariableFlow
Low temperature hydronic radiant heating and/or cooling system embedded in a building surface (wall, ceiling, or floor). Controlled by varying the hot or chilled water flow to the unit.

Fields

design_object [string]
availability_schedule_name [string]
zone_name [string]
surface_name_or_radiant_surface_group_name [string]
hydronic_tubing_length [unknown field type] (Default: Autosize)
heating_design_capacity [unknown field type] (Default: Autosize)
maximum_hot_water_flow [unknown field type]
heating_water_inlet_node_name [string]
heating_water_outlet_node_name [string]
cooling_design_capacity [unknown field type]
maximum_cold_water_flow [unknown field type]
cooling_water_inlet_node_name [string]
cooling_water_outlet_node_name [string]
number_of_circuits [string] (Default: OnePerSurface)
circuit_length [number] (Default: 106.7)
ZoneHVAC:LowTemperatureRadiant:VariableFlow:Design
Fields

fluid_to_radiant_surface_heat_transfer_model [string] (Default: ConvectionOnly)
hydronic_tubing_inside_diameter [number] (Default: 0.013)
hydronic_tubing_outside_diameter [number] (Default: 0.016)
hydronic_tubing_conductivity [number] (Default: 0.35)
temperature_control_type [string] (Default: MeanAirTemperature)
setpoint_control_type [string] (Default: HalfFlowPower)
heating_design_capacity_method [string] (Default: HeatingDesignCapacity)
heating_design_capacity_per_floor_area [number]
fraction_of_autosized_heating_design_capacity [number] (Default: 1.0)
heating_control_throttling_range [number] (Default: 0.5)
heating_control_temperature_schedule_name [string]
cooling_design_capacity_method [string] (Default: CoolingDesignCapacity)
cooling_design_capacity_per_floor_area [number]
fraction_of_autosized_cooling_design_capacity [number]
cooling_control_throttling_range [number] (Default: 0.5)
cooling_control_temperature_schedule_name [string]
condensation_control_type [string] (Default: SimpleOff)
condensation_control_dewpoint_offset [number] (Default: 1.0)
changeover_delay_time_period_schedule [string]
ZoneHVAC:LowTemperatureRadiant:ConstantFlow
Low temperature hydronic radiant heating and/or cooling system embedded in a building surface (wall, ceiling, or floor). Controlled by varying the hot or chilled water temperature circulating through the unit.

Fields

design_object [string]
availability_schedule_name [string]
zone_name [string]
surface_name_or_radiant_surface_group_name [string]
hydronic_tubing_length [unknown field type] (Default: Autosize)
rated_flow_rate [unknown field type]
pump_flow_rate_schedule_name [string]
rated_pump_head [number] (Default: 179352.0)
rated_power_consumption [number]
heating_water_inlet_node_name [string]
heating_water_outlet_node_name [string]
heating_high_water_temperature_schedule_name [string]
heating_low_water_temperature_schedule_name [string]
heating_high_control_temperature_schedule_name [string]
heating_low_control_temperature_schedule_name [string]
cooling_water_inlet_node_name [string]
cooling_water_outlet_node_name [string]
cooling_high_water_temperature_schedule_name [string]
cooling_low_water_temperature_schedule_name [string]
cooling_high_control_temperature_schedule_name [string]
cooling_low_control_temperature_schedule_name [string]
number_of_circuits [string] (Default: OnePerSurface)
circuit_length [number] (Default: 106.7)
ZoneHVAC:LowTemperatureRadiant:ConstantFlow:Design
Fields

fluid_to_radiant_surface_heat_transfer_model [string] (Default: ConvectionOnly)
hydronic_tubing_inside_diameter [number] (Default: 0.013)
hydronic_tubing_outside_diameter [number] (Default: 0.016)
hydronic_tubing_conductivity [number] (Default: 0.35)
temperature_control_type [string] (Default: MeanAirTemperature)
running_mean_outdoor_dry_bulb_temperature_weighting_factor [number] (Default: 0.8)
motor_efficiency [number] (Default: 0.9)
fraction_of_motor_inefficiencies_to_fluid_stream [number] (Default: 0.0)
condensation_control_type [string] (Default: SimpleOff)
condensation_control_dewpoint_offset [number] (Default: 1.0)
changeover_delay_time_period_schedule [string]
ZoneHVAC:LowTemperatureRadiant:Electric
Electric resistance low temperature radiant system

Fields

availability_schedule_name [string]
zone_name [string]
surface_name_or_radiant_surface_group_name [string]
heating_design_capacity_method [string] (Default: HeatingDesignCapacity)
heating_design_capacity [unknown field type] (Default: Autosize)
heating_design_capacity_per_floor_area [number]
fraction_of_autosized_heating_design_capacity [number] (Default: 1.0)
temperature_control_type [string] (Default: MeanAirTemperature)
setpoint_control_type [string] (Default: HalfFlowPower)
heating_throttling_range [number] (Default: 0.0)
heating_setpoint_temperature_schedule_name [string]
ZoneHVAC:LowTemperatureRadiant:SurfaceGroup
This is used to allow the coordinate control of several radiant system surfaces. Note that the following flow fractions must sum up to 1.0 The number of surfaces can be expanded beyond 100, if necessary, by adding more groups to the end of the list

Fields

surface_fractions [Array of {surface_name, flow_fraction_for_surface}]
ZoneHVAC:HighTemperatureRadiant
The number of surfaces can be expanded beyond 100, if necessary, by adding more groups to the end of the list

Fields

availability_schedule_name [string]
zone_name [string]
heating_design_capacity_method [string] (Default: HeatingDesignCapacity)
heating_design_capacity [unknown field type] (Default: Autosize)
heating_design_capacity_per_floor_area [number]
fraction_of_autosized_heating_design_capacity [number] (Default: 1.0)
fuel_type [string]
combustion_efficiency [number] (Default: 0.9)
fraction_of_input_converted_to_radiant_energy [number] (Default: 0.7)
fraction_of_input_converted_to_latent_energy [number] (Default: 0.0)
fraction_of_input_that_is_lost [number] (Default: 0.0)
temperature_control_type [string] (Default: OperativeTemperature)
heating_throttling_range [number] (Default: 2.0)
heating_setpoint_temperature_schedule_name [string]
fraction_of_radiant_energy_incident_on_people [number]
surface_fractions [Array of {surface_name, fraction_of_radiant_energy_to_surface}]
ZoneHVAC:VentilatedSlab
Ventilated slab system where outdoor air flows through hollow cores in a building surface (wall, ceiling, or floor).

Fields

availability_schedule_name [string]
zone_name [string]
surface_name_or_radiant_surface_group_name [string]
maximum_air_flow_rate [unknown field type]
outdoor_air_control_type [string]
minimum_outdoor_air_flow_rate [unknown field type]
minimum_outdoor_air_schedule_name [string]
maximum_outdoor_air_flow_rate [unknown field type]
maximum_outdoor_air_fraction_or_temperature_schedule_name [string]
system_configuration_type [string] (Default: SlabOnly)
hollow_core_inside_diameter [number] (Default: 0.05)
hollow_core_length [number]
number_of_cores [number]
temperature_control_type [string] (Default: OutdoorDryBulbTemperature)
heating_high_air_temperature_schedule_name [string]
heating_low_air_temperature_schedule_name [string]
heating_high_control_temperature_schedule_name [string]
heating_low_control_temperature_schedule_name [string]
cooling_high_air_temperature_schedule_name [string]
cooling_low_air_temperature_schedule_name [string]
cooling_high_control_temperature_schedule_name [string]
cooling_low_control_temperature_schedule_name [string]
return_air_node_name [string]
slab_in_node_name [string]
zone_supply_air_node_name [string]
outdoor_air_node_name [string]
relief_air_node_name [string]
outdoor_air_mixer_outlet_node_name [string]
fan_outlet_node_name [string]
fan_name [string]
coil_option_type [string]
heating_coil_object_type [string]
heating_coil_name [string]
hot_water_or_steam_inlet_node_name [string]
cooling_coil_object_type [string]
cooling_coil_name [string]
cold_water_inlet_node_name [string]
availability_manager_list_name [string]
design_specification_zonehvac_sizing_object_name [string]
ZoneHVAC:VentilatedSlab:SlabGroup
This is used to allow the coordinate control of several ventilated slab system surfaces. Note that the flow fractions must sum up to 1.0. The number of surfaces can be expanded beyond 10, if necessary, by adding more groups to the end of the list

Fields

data [Array of {zone_name, surface_name, core_diameter_for_surface, core_length_for_surface, core_numbers_for_surface, slab_inlet_node_name_for_surface, slab_outlet_node_name_for_surface}]

"""