"""
# HVAC Design Objects
"""
"""
DesignSpecification:OutdoorAir
This object is used to describe general outdoor air requirements which are referenced by other objects.

Fields

outdoor_air_method [string] (Default: Flow/Person)
outdoor_air_flow_per_person [number] (Default: 0.00944)
outdoor_air_flow_per_zone_floor_area [number] (Default: 0.0)
outdoor_air_flow_per_zone [number] (Default: 0.0)
outdoor_air_flow_air_changes_per_hour [number] (Default: 0.0)
outdoor_air_schedule_name [string]
proportional_control_minimum_outdoor_air_flow_rate_schedule_name [string]
DesignSpecification:OutdoorAir:SpaceList
Defines a list of DesignSpecification:OutdoorAir names which can be referenced as a group. The DesignSpecification:OutdoorAir:SpaceList name may be used in Sizing:Zone and Controller:MechanicalVentilation to specify space-by-space OA requirements and anywhere else that accepts a DesignSpecification:OutdoorAir object name.

Fields

space_specs [Array of {space_name, space_design_specification_outdoor_air_object_name}]
DesignSpecification:ZoneAirDistribution
This object is used to describe zone air distribution in terms of air distribution effectiveness and secondary recirculation fraction. It is referenced by Sizing:Zone and Controller:MechanicalVentilation objects

Fields

zone_air_distribution_effectiveness_in_cooling_mode [number] (Default: 1.0)
zone_air_distribution_effectiveness_in_heating_mode [number] (Default: 1.0)
zone_air_distribution_effectiveness_schedule_name [string]
zone_secondary_recirculation_fraction [number] (Default: 0.0)
minimum_zone_ventilation_efficiency [number] (Default: 0.0)
Sizing:Parameters
Specifies global heating and cooling sizing factors/ratios. These ratios are applied at the zone level to all of the zone heating and cooling loads and air flow rates. Then these new loads and air flow rates are used to calculate the system level flow rates and capacities and are used in all component sizing calculations. Specifies the width (in load timesteps) of a moving average window which is used to smooth the peak load across more than one timestep.

Fields

heating_sizing_factor [number] (Default: 1.0)
cooling_sizing_factor [number] (Default: 1.0)
timesteps_in_averaging_window [number]
Sizing:Zone
Specifies the data needed to perform a zone design air flow calculation. The calculation is done for every sizing period included in the input. The maximum cooling and heating load and cooling, heating, and ventilation air flows are then saved for system level and zone component design calculations.

Fields

zone_or_zonelist_name [string]
zone_cooling_design_supply_air_temperature_input_method [string] (Default: SupplyAirTemperature)
zone_cooling_design_supply_air_temperature [number]
zone_cooling_design_supply_air_temperature_difference [number]
zone_heating_design_supply_air_temperature_input_method [string] (Default: SupplyAirTemperature)
zone_heating_design_supply_air_temperature [number]
zone_heating_design_supply_air_temperature_difference [number]
zone_cooling_design_supply_air_humidity_ratio [number]
zone_heating_design_supply_air_humidity_ratio [number]
design_specification_outdoor_air_object_name [string]
zone_heating_sizing_factor [number]
zone_cooling_sizing_factor [number]
cooling_design_air_flow_method [string] (Default: DesignDay)
cooling_design_air_flow_rate [number] (Default: 0.0)
cooling_minimum_air_flow_per_zone_floor_area [number] (Default: 0.000762)
cooling_minimum_air_flow [number] (Default: 0.0)
cooling_minimum_air_flow_fraction [number] (Default: 0.2)
heating_design_air_flow_method [string] (Default: DesignDay)
heating_design_air_flow_rate [number] (Default: 0.0)
heating_maximum_air_flow_per_zone_floor_area [number] (Default: 0.002032)
heating_maximum_air_flow [number] (Default: 0.1415762)
heating_maximum_air_flow_fraction [number] (Default: 0.3)
design_specification_zone_air_distribution_object_name [string]
account_for_dedicated_outdoor_air_system [string] (Default: No)
dedicated_outdoor_air_system_control_strategy [string] (Default: NeutralSupplyAir)
dedicated_outdoor_air_low_setpoint_temperature_for_design [unknown field type] (Default: Autosize)
dedicated_outdoor_air_high_setpoint_temperature_for_design [unknown field type] (Default: Autosize)
DesignSpecification:ZoneHVAC:Sizing
This object is used to describe general scalable zone HVAC equipment sizing which are referenced by other objects.

Fields

cooling_supply_air_flow_rate_method [string] (Default: SupplyAirFlowRate)
cooling_supply_air_flow_rate [unknown field type]
cooling_supply_air_flow_rate_per_floor_area [number]
cooling_fraction_of_autosized_cooling_supply_air_flow_rate [number]
cooling_supply_air_flow_rate_per_unit_cooling_capacity [number]
no_load_supply_air_flow_rate_method [string] (Default: SupplyAirFlowRate)
no_load_supply_air_flow_rate [unknown field type]
no_load_supply_air_flow_rate_per_floor_area [number]
no_load_fraction_of_cooling_supply_air_flow_rate [number]
no_load_fraction_of_heating_supply_air_flow_rate [number]
heating_supply_air_flow_rate_method [string] (Default: SupplyAirFlowRate)
heating_supply_air_flow_rate [unknown field type]
heating_supply_air_flow_rate_per_floor_area [number]
heating_fraction_of_heating_supply_air_flow_rate [number]
heating_supply_air_flow_rate_per_unit_heating_capacity [number]
cooling_design_capacity_method [string] (Default: None)
cooling_design_capacity [unknown field type]
cooling_design_capacity_per_floor_area [number]
fraction_of_autosized_cooling_design_capacity [number]
heating_design_capacity_method [string] (Default: None)
heating_design_capacity [unknown field type]
heating_design_capacity_per_floor_area [number]
fraction_of_autosized_heating_design_capacity [number]
DesignSpecification:AirTerminal:Sizing
This object is used to scale the sizing of air terminal units.

Fields

fraction_of_design_cooling_load [number] (Default: 1.0)
cooling_design_supply_air_temperature_difference_ratio [number] (Default: 1.0)
fraction_of_design_heating_load [number] (Default: 1.0)
heating_design_supply_air_temperature_difference_ratio [number] (Default: 1.0)
fraction_of_minimum_outdoor_air_flow [number] (Default: 1.0)
Sizing:System
Specifies the input needed to perform sizing calculations for a central forced air system. System design air flow, heating capacity, and cooling capacity will be calculated using this input data.

Fields

airloop_name [string]
type_of_load_to_size_on [string] (Default: Sensible)
design_outdoor_air_flow_rate [unknown field type] (Default: Autosize)
central_heating_maximum_system_air_flow_ratio [unknown field type] (Default: Autosize)
preheat_design_temperature [number]
preheat_design_humidity_ratio [number]
precool_design_temperature [number]
precool_design_humidity_ratio [number]
central_cooling_design_supply_air_temperature [number]
central_heating_design_supply_air_temperature [number]
type_of_zone_sum_to_use [string] (Default: NonCoincident)
100_outdoor_air_in_cooling [string] (Default: No)
100_outdoor_air_in_heating [string] (Default: No)
central_cooling_design_supply_air_humidity_ratio [number] (Default: 0.008)
central_heating_design_supply_air_humidity_ratio [number] (Default: 0.008)
cooling_supply_air_flow_rate_method [string] (Default: DesignDay)
cooling_supply_air_flow_rate [number] (Default: 0.0)
cooling_supply_air_flow_rate_per_floor_area [number]
cooling_fraction_of_autosized_cooling_supply_air_flow_rate [number]
cooling_supply_air_flow_rate_per_unit_cooling_capacity [number]
heating_supply_air_flow_rate_method [string] (Default: DesignDay)
heating_supply_air_flow_rate [number] (Default: 0.0)
heating_supply_air_flow_rate_per_floor_area [number]
heating_fraction_of_autosized_heating_supply_air_flow_rate [number]
heating_fraction_of_autosized_cooling_supply_air_flow_rate [number]
heating_supply_air_flow_rate_per_unit_heating_capacity [number]
system_outdoor_air_method [string] (Default: ZoneSum)
zone_maximum_outdoor_air_fraction [number] (Default: 1.0)
cooling_design_capacity_method [string] (Default: CoolingDesignCapacity)
cooling_design_capacity [unknown field type] (Default: Autosize)
cooling_design_capacity_per_floor_area [number]
fraction_of_autosized_cooling_design_capacity [number]
heating_design_capacity_method [string] (Default: HeatingDesignCapacity)
heating_design_capacity [unknown field type] (Default: Autosize)
heating_design_capacity_per_floor_area [number]
fraction_of_autosized_heating_design_capacity [number]
central_cooling_capacity_control_method [string] (Default: OnOff)
occupant_diversity [unknown field type] (Default: Autosize)
Sizing:Plant
Specifies the input needed to autosize plant loop flow rates and equipment capacities. This information is initially used by components that use water for heating or cooling such as hot or chilled water coils to calculate their maximum water flow rates. These flow rates are then summed for use in calculating the Plant Loop flow rates.

Fields

plant_or_condenser_loop_name [string]
loop_type [string]
design_loop_exit_temperature [number]
loop_design_temperature_difference [number]
sizing_option [string] (Default: NonCoincident)
zone_timesteps_in_averaging_window [number] (Default: 1.0)
coincident_sizing_factor_mode [string]
OutputControl:Sizing:Style
Default style for the Sizing output files is comma – this works well for importing into spreadsheet programs such as Excel(tm) but not so well for word processing programs – there tab may be a better choice. Fixed puts spaces between the “columns”

Fields

column_separator [string]
"""