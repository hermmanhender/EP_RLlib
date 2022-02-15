"""
# Zone HVAC Controls and Thermostats
"""
"""
ZoneControl:Humidistat
Specifies zone relative humidity setpoint schedules for humidifying and dehumidifying.

Fields

zone_name [string]
humidifying_relative_humidity_setpoint_schedule_name [string]
dehumidifying_relative_humidity_setpoint_schedule_name [string]
ZoneControl:Thermostat
Define the Thermostat settings for a zone or list of zones. If you use a ZoneList in the Zone or ZoneList name field then this definition applies to all the zones in the ZoneList.

Fields

zone_or_zonelist_name [string]
control_type_schedule_name [string]
control_1_object_type [string]
control_1_name [string]
control_2_object_type [string]
control_2_name [string]
control_3_object_type [string]
control_3_name [string]
control_4_object_type [string]
control_4_name [string]
temperature_difference_between_cutout_and_setpoint [number] (Default: 0.0)
ZoneControl:Thermostat:OperativeTemperature
This object can be used with the ZoneList option on a thermostat or with one of the zones on that list (but you won’t be able to use the object list to pick only one of those zones. Thermostat names are <Zone Name> <global Thermostat name> internally.

Fields

thermostat_name [string]
radiative_fraction_input_mode [string]
fixed_radiative_fraction [number]
radiative_fraction_schedule_name [string]
adaptive_comfort_model_type [string] (Default: None)
ZoneControl:Thermostat:ThermalComfort
If you use a ZoneList in the Zone or ZoneList name field then this definition applies to all the zones in the ZoneList.

Fields

zone_or_zonelist_name [string]
averaging_method [string] (Default: PeopleAverage)
specific_people_name [string]
minimum_dry_bulb_temperature_setpoint [number] (Default: 0.0)
maximum_dry_bulb_temperature_setpoint [number] (Default: 50.0)
thermal_comfort_control_type_schedule_name [string]
thermal_comfort_control_1_object_type [string]
thermal_comfort_control_1_name [string]
thermal_comfort_control_2_object_type [string]
thermal_comfort_control_2_name [string]
thermal_comfort_control_3_object_type [string]
thermal_comfort_control_3_name [string]
thermal_comfort_control_4_object_type [string]
thermal_comfort_control_4_name [string]
ZoneControl:Thermostat:TemperatureAndHumidity
This object modifies a ZoneControl:Thermostat object to effect temperature control based on zone air humidity conditions.

Fields

thermostat_name [string]
dehumidifying_relative_humidity_setpoint_schedule_name [string]
dehumidification_control_type [string] (Default: Overcool)
overcool_range_input_method [string] (Default: Constant)
overcool_constant_range [number] (Default: 1.7)
overcool_range_schedule_name [string]
overcool_control_ratio [number] (Default: 3.6)
ThermostatSetpoint:SingleHeating
Used for a heating only thermostat. The setpoint can be scheduled and varied throughout the simulation but only heating is allowed with this control type.

Fields

setpoint_temperature_schedule_name [string]
ThermostatSetpoint:SingleCooling
Used for a cooling only thermostat. The setpoint can be scheduled and varied throughout the simulation but only cooling is allowed.

Fields

setpoint_temperature_schedule_name [string]
ThermostatSetpoint:SingleHeatingOrCooling
Used for a heating and cooling thermostat with a single setpoint. The setpoint can be scheduled and varied throughout the simulation for both heating and cooling.

Fields

setpoint_temperature_schedule_name [string]
ThermostatSetpoint:DualSetpoint
Used for a heating and cooling thermostat with dual setpoints. The setpoints can be scheduled and varied throughout the simulation for both heating and cooling.

Fields

heating_setpoint_temperature_schedule_name [string]
cooling_setpoint_temperature_schedule_name [string]
ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating
Used for heating only thermal comfort control. The PMV setpoint can be scheduled and varied throughout the simulation but only heating is allowed with this control type.

Fields

fanger_thermal_comfort_schedule_name [string]
ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling
Used for cooling only thermal comfort control. The PMV setpoint can be scheduled and varied throughout the simulation but only cooling is allowed with this control type.

Fields

fanger_thermal_comfort_schedule_name [string]
ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling
Used for heating and cooling thermal comfort control with a single setpoint. The PMV setpoint can be scheduled and varied throughout the simulation for both heating and cooling.

Fields

fanger_thermal_comfort_schedule_name [string]
ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint
Used for heating and cooling thermal comfort control with dual setpoints. The PMV setpoints can be scheduled and varied throughout the simulation for both heating and cooling.

Fields

fanger_thermal_comfort_heating_schedule_name [string]
fanger_thermal_comfort_cooling_schedule_name [string]
ZoneControl:Thermostat:StagedDualSetpoint
Define the Thermostat StagedDualSetpoint settings for a zone or list of zones. If you use a ZoneList in the Zone or ZoneList name field then this definition applies to all the zones in the ZoneList.

Fields

zone_or_zonelist_name [string]
number_of_heating_stages [number]
heating_temperature_setpoint_schedule_name [string]
heating_throttling_temperature_range [number] (Default: 1.1)
stage_1_heating_temperature_offset [number]
stage_2_heating_temperature_offset [number]
stage_3_heating_temperature_offset [number]
stage_4_heating_temperature_offset [number]
number_of_cooling_stages [number]
cooling_temperature_setpoint_base_schedule_name [string]
cooling_throttling_temperature_range [number] (Default: 1.1)
stage_1_cooling_temperature_offset [number]
stage_2_cooling_temperature_offset [number]
stage_3_cooling_temperature_offset [number]
stage_4_cooling_temperature_offset [number]
ZoneControl:ContaminantController
Used to control a zone to a specified indoor level of CO2 or generic contaminants, or to specify minimum CO2 concentration schedule name for a zone.

Fields

zone_name [string]
carbon_dioxide_control_availability_schedule_name [string]
carbon_dioxide_setpoint_schedule_name [string]
minimum_carbon_dioxide_concentration_schedule_name [string]
maximum_carbon_dioxide_concentration_schedule_name [string]
generic_contaminant_control_availability_schedule_name [string]
generic_contaminant_setpoint_schedule_name [string]
"""