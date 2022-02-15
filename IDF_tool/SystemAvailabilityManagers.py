"""
# System Availability Managers
"""
"""
AvailabilityManager:Scheduled
Determines the availability of a loop or system: whether it is on or off. Schedule overrides fan/pump schedule.

Fields

schedule_name [string]
AvailabilityManager:ScheduledOn
Determines the availability of a loop or system: only controls the turn on action. Schedule overrides fan/pump schedule.

Fields

schedule_name [string]
AvailabilityManager:ScheduledOff
Determines the availability of a loop or system: only controls the turn off action. Schedule overrides fan/pump schedule.

Fields

schedule_name [string]
AvailabilityManager:OptimumStart
Determines the optimal start of HVAC systems before occupancy.

Fields

applicability_schedule_name [string]
fan_schedule_name [string]
control_type [string] (Default: ControlZone)
control_zone_name [string]
zone_list_name [string]
maximum_value_for_optimum_start_time [number] (Default: 6.0)
control_algorithm [string] (Default: AdaptiveASHRAE)
constant_temperature_gradient_during_cooling [number]
constant_temperature_gradient_during_heating [number]
initial_temperature_gradient_during_cooling [number]
initial_temperature_gradient_during_heating [number]
constant_start_time [number]
number_of_previous_days [number] (Default: 2.0)
AvailabilityManager:NightCycle
Determines the availability of a loop or system: whether it is on or off. Depending on zone temperatures, overrides Schedules and forces system Fans on.

Fields

applicability_schedule_name [string]
fan_schedule_name [string]
control_type [string] (Default: StayOff)
thermostat_tolerance [number] (Default: 1.0)
cycling_run_time_control_type [string] (Default: FixedRunTime)
cycling_run_time [number] (Default: 3600.0)
control_zone_or_zone_list_name [string]
cooling_control_zone_or_zone_list_name [string]
heating_control_zone_or_zone_list_name [string]
heating_zone_fans_only_zone_or_zone_list_name [string]
AvailabilityManager:DifferentialThermostat
Overrides fan/pump schedules depending on temperature difference between two nodes.

Fields

hot_node_name [string]
cold_node_name [string]
temperature_difference_on_limit [number]
temperature_difference_off_limit [number]
AvailabilityManager:HighTemperatureTurnOff
Overrides fan/pump schedules depending on temperature at sensor node.

Fields

sensor_node_name [string]
temperature [number]
AvailabilityManager:HighTemperatureTurnOn
Overrides fan/pump schedules depending on temperature at sensor node.

Fields

sensor_node_name [string]
temperature [number]
AvailabilityManager:LowTemperatureTurnOff
Overrides fan/pump schedules depending on temperature at sensor node.

Fields

sensor_node_name [string]
temperature [number]
applicability_schedule_name [string]
AvailabilityManager:LowTemperatureTurnOn
Overrides fan/pump schedules depending on temperature at sensor node.

Fields

sensor_node_name [string]
temperature [number]
AvailabilityManager:NightVentilation
depending on zone and outdoor conditions overrides fan schedule to do precooling with outdoor air

Fields

applicability_schedule_name [string]
fan_schedule_name [string]
ventilation_temperature_schedule_name [string]
ventilation_temperature_difference [number] (Default: 2.0)
ventilation_temperature_low_limit [number] (Default: 15.0)
night_venting_flow_fraction [number] (Default: 1.0)
control_zone_name [string]
AvailabilityManager:HybridVentilation
Depending on zone and outdoor conditions overrides window/door opening controls to maximize natural ventilation and turn off an HVAC system when ventilation control conditions are met. This object (zone ventilation object name) has not been instrumented to work with global Zone or Zone List names option for Ventilation:DesignFlowRate. In order to use, you must enter the single <Ventilation:DesignFlowRate> name in that field. If it is a part of a global ventilation assignment the name will be <Zone Name> <global Ventilation:DesignFlowRate> name. Currently, hybrid ventilation manager is restricted to one per zone. It can either be applied through the air loop or directly to the zone. If hybrid ventilation manager is applied to an air loop and one of the zones served by that air loop also has hybrid ventilation manager, then zone hybrid ventilation manager is disabled.

Fields

hvac_air_loop_name [string]
control_zone_name [string]
ventilation_control_mode_schedule_name [string]
use_weather_file_rain_indicators [string] (Default: Yes)
maximum_wind_speed [number] (Default: 40.0)
minimum_outdoor_temperature [number] (Default: -100.0)
maximum_outdoor_temperature [number] (Default: 100.0)
minimum_outdoor_enthalpy [number]
maximum_outdoor_enthalpy [number]
minimum_outdoor_dewpoint [number] (Default: -100.0)
maximum_outdoor_dewpoint [number] (Default: 100.0)
minimum_outdoor_ventilation_air_schedule_name [string]
opening_factor_function_of_wind_speed_curve_name [string]
airflownetwork_control_type_schedule_name [string]
simple_airflow_control_type_schedule_name [string]
zoneventilation_object_name [string]
minimum_hvac_operation_time [number] (Default: 0.0)
minimum_ventilation_time [number] (Default: 0.0)
AvailabilityManagerAssignmentList
Defines the applicable managers used for an AirLoopHVAC or PlantLoop. The priority of availability managers is based on a set of rules and are specific to the type of loop. The output from each availability manager is an availability status flag: NoAction, ForceOff, CycleOn, or CycleOnZoneFansOnly (used only for air loops).

Fields

managers [Array of {availability_manager_object_type, availability_manager_name}]
"""