"""
# Setpoint Managers
"""
"""
SetpointManager:Scheduled
The simplest Setpoint Manager simply uses a schedule to determine one or more setpoints. Values of the nodes are not used as input.

Fields

control_variable [string]
schedule_name [string]
setpoint_node_or_nodelist_name [string]
SetpointManager:Scheduled:DualSetpoint
This setpoint manager places a high and low schedule value on one or more nodes.

Fields

control_variable [string] (Default: Temperature)
high_setpoint_schedule_name [string]
low_setpoint_schedule_name [string]
setpoint_node_or_nodelist_name [string]
SetpointManager:OutdoorAirReset
This Setpoint Manager is used to place a setpoint temperature on system node according to the outdoor air temperature using a reset rule. The outdoor air temperature is obtained from the weather information during the simulation.

Fields

control_variable [string] (Default: Temperature)
setpoint_at_outdoor_low_temperature [number]
outdoor_low_temperature [number]
setpoint_at_outdoor_high_temperature [number]
outdoor_high_temperature [number]
setpoint_node_or_nodelist_name [string]
schedule_name [string]
setpoint_at_outdoor_low_temperature_2 [number]
outdoor_low_temperature_2 [number]
setpoint_at_outdoor_high_temperature_2 [number]
outdoor_high_temperature_2 [number]
SetpointManager:SingleZone:Reheat
This setpoint manager detects the control zone load, zone inlet node flow rate, and zone node temperature and calculates a setpoint temperature for the supply air that will satisfy the zone load (heating or cooling) for the control zone. This setpoint manager is not limited to reheat applications.

Fields

control_variable [string] (Default: Temperature)
minimum_supply_air_temperature [number] (Default: -99.0)
maximum_supply_air_temperature [number] (Default: 99.0)
control_zone_name [string]
zone_node_name [string]
zone_inlet_node_name [string]
setpoint_node_or_nodelist_name [string]
SetpointManager:SingleZone:Heating
This setpoint manager detects the control zone load to meet the current heating setpoint, zone inlet node flow rate, and zone node temperature, and calculates a setpoint temperature for the supply air that will satisfy the zone heating load for the control zone.

Fields

control_variable [string] (Default: Temperature)
minimum_supply_air_temperature [number] (Default: -99.0)
maximum_supply_air_temperature [number] (Default: 99.0)
control_zone_name [string]
zone_node_name [string]
zone_inlet_node_name [string]
setpoint_node_or_nodelist_name [string]
SetpointManager:SingleZone:Cooling
This setpoint manager detects the control zone load to meet the current cooling setpoint, zone inlet node flow rate, and zone node temperature, and calculates a setpoint temperature for the supply air that will satisfy the zone cooling load for the control zone.

Fields

control_variable [string] (Default: Temperature)
minimum_supply_air_temperature [number] (Default: -99.0)
maximum_supply_air_temperature [number] (Default: 99.0)
control_zone_name [string]
zone_node_name [string]
zone_inlet_node_name [string]
setpoint_node_or_nodelist_name [string]
SetpointManager:SingleZone:Humidity:Minimum
The Single Zone Minimum Humidity Setpoint Manager allows the control of a single zone minimum humidity level. This setpoint manager can be used in conjunction with object ZoneControl:Humidistat to detect humidity levels.

Fields

setpoint_node_or_nodelist_name [string]
control_zone_air_node_name [string]
SetpointManager:SingleZone:Humidity:Maximum
The Single Zone Maximum Humidity Setpoint Manager allows the control of a single zone maximum humidity level. This setpoint manager can be used in conjunction with object ZoneControl:Humidistat to detect humidity levels.

Fields

setpoint_node_or_nodelist_name [string]
control_zone_air_node_name [string]
SetpointManager:MixedAir
The Mixed Air Setpoint Manager is meant to be used in conjunction with a Controller:OutdoorAir object. This setpoint manager is used to establish a temperature setpoint at the mixed air node.

Fields

control_variable [string] (Default: Temperature)
reference_setpoint_node_name [string]
fan_inlet_node_name [string]
fan_outlet_node_name [string]
setpoint_node_or_nodelist_name [string]
cooling_coil_inlet_node_name [string]
cooling_coil_outlet_node_name [string]
minimum_temperature_at_cooling_coil_outlet_node [number] (Default: 7.2)
SetpointManager:OutdoorAirPretreat
This setpoint manager determines the required conditions at the outdoor air stream node which will produce the reference setpoint condition at the mixed air node when mixed with the return air stream

Fields

control_variable [string]
minimum_setpoint_temperature [number] (Default: -99.0)
maximum_setpoint_temperature [number] (Default: 99.0)
minimum_setpoint_humidity_ratio [number] (Default: 1e-05)
maximum_setpoint_humidity_ratio [number] (Default: 1.0)
reference_setpoint_node_name [string]
mixed_air_stream_node_name [string]
outdoor_air_stream_node_name [string]
return_air_stream_node_name [string]
setpoint_node_or_nodelist_name [string]
SetpointManager:Warmest
This SetpointManager resets the cooling supply air temperature of a central forced air HVAC system according to the cooling demand of the warmest zone.

Fields

control_variable [string] (Default: Temperature)
hvac_air_loop_name [string]
minimum_setpoint_temperature [number] (Default: 12.0)
maximum_setpoint_temperature [number] (Default: 18.0)
strategy [string] (Default: MaximumTemperature)
setpoint_node_or_nodelist_name [string]
SetpointManager:Coldest
This SetpointManager is used in dual duct systems to reset the setpoint temperature of the air in the heating supply duct. Usually it is used in conjunction with a SetpointManager:Warmest resetting the temperature of the air in the cooling supply duct.

Fields

control_variable [string] (Default: Temperature)
hvac_air_loop_name [string]
minimum_setpoint_temperature [number] (Default: 20.0)
maximum_setpoint_temperature [number] (Default: 50.0)
strategy [string] (Default: MinimumTemperature)
setpoint_node_or_nodelist_name [string]
SetpointManager:ReturnAirBypassFlow
This setpoint manager determines the required mass flow rate through a return air bypass duct to meet the specified temperature setpoint

Fields

control_variable [string] (Default: Flow)
hvac_air_loop_name [string]
temperature_setpoint_schedule_name [string]
SetpointManager:WarmestTemperatureFlow
This setpoint manager sets both the supply air temperature and the supply air flow rate.

Fields

control_variable [string]
hvac_air_loop_name [string]
minimum_setpoint_temperature [number] (Default: 12.0)
maximum_setpoint_temperature [number] (Default: 18.0)
strategy [string] (Default: TemperatureFirst)
setpoint_node_or_nodelist_name [string]
minimum_turndown_ratio [number] (Default: 0.2)
SetpointManager:MultiZone:Heating:Average
This setpoint manager sets the average supply air temperature based on the heating load requirements of all controlled zones in an air loop served by a central air-conditioner.

Fields

hvac_air_loop_name [string]
minimum_setpoint_temperature [number] (Default: 20.0)
maximum_setpoint_temperature [number] (Default: 50.0)
setpoint_node_or_nodelist_name [string]
SetpointManager:MultiZone:Cooling:Average
This setpoint manager sets the average supply air temperature based on the cooling load requirements of all controlled zones in an air loop served by a central air-conditioner.

Fields

hvac_air_loop_name [string]
minimum_setpoint_temperature [number] (Default: 12.0)
maximum_setpoint_temperature [number] (Default: 18.0)
setpoint_node_or_nodelist_name [string]
SetpointManager:MultiZone:MinimumHumidity:Average
This setpoint manager sets the average supply air minimum humidity ratio based on moisture load requirements of all controlled zones in an air loop served by a central air-conditioner.

Fields

hvac_air_loop_name [string]
minimum_setpoint_humidity_ratio [number] (Default: 0.005)
maximum_setpoint_humidity_ratio [number] (Default: 0.012)
setpoint_node_or_nodelist_name [string]
SetpointManager:MultiZone:MaximumHumidity:Average
This setpoint manager sets the average supply air maximum humidity ratio based on moisture load requirements of all controlled zones in an air loop served by a central air-conditioner.

Fields

hvac_air_loop_name [string]
minimum_setpoint_humidity_ratio [number] (Default: 0.008)
maximum_setpoint_humidity_ratio [number] (Default: 0.015)
setpoint_node_or_nodelist_name [string]
SetpointManager:MultiZone:Humidity:Minimum
This setpoint manager sets the minimum supply air humidity ratio based on humidification requirements of a controlled zone with critical humidity ratio setpoint (i.e., a zone with the highest humidity ratio setpoint) in an air loop served by a central air-conditioner.

Fields

hvac_air_loop_name [string]
minimum_setpoint_humidity_ratio [number] (Default: 0.005)
maximum_setpoint_humidity_ratio [number] (Default: 0.012)
setpoint_node_or_nodelist_name [string]
SetpointManager:MultiZone:Humidity:Maximum
This setpoint manager sets the maximum supply air humidity ratio based on dehumidification requirements of a controlled zone with critical humidity ratio setpoint (i.e., a zone with the lowest humidity ratio setpoint) in an air loop served by a central air-conditioner.

Fields

hvac_air_loop_name [string]
minimum_setpoint_humidity_ratio [number] (Default: 0.008)
maximum_setpoint_humidity_ratio [number] (Default: 0.015)
setpoint_node_or_nodelist_name [string]
SetpointManager:FollowOutdoorAirTemperature
This setpoint manager is used to place a temperature setpoint on a system node that is derived from the current outdoor air environmental conditions. The outdoor air conditions are obtained from the weather information during the simulation.

Fields

control_variable [string] (Default: Temperature)
reference_temperature_type [string] (Default: OutdoorAirWetBulb)
offset_temperature_difference [number]
maximum_setpoint_temperature [number]
minimum_setpoint_temperature [number]
setpoint_node_or_nodelist_name [string]
SetpointManager:FollowSystemNodeTemperature
This setpoint manager is used to place a temperature setpoint on a system node that is derived from the current temperatures at a separate system node. The current value of the temperature at a reference node is obtained and used to generate setpoint on a second system node. If the reference node is also designated to be an outdoor air (intake) node, then this setpoint manager can be used to follow outdoor air conditions that are adjusted for altitude.

Fields

control_variable [string] (Default: Temperature)
reference_node_name [string]
reference_temperature_type [string] (Default: NodeDryBulb)
offset_temperature_difference [number]
maximum_limit_setpoint_temperature [number]
minimum_limit_setpoint_temperature [number]
setpoint_node_or_nodelist_name [string]
SetpointManager:FollowGroundTemperature
This setpoint manager is used to place a temperature setpoint on a system node that is derived from a current ground temperature. The ground temperatures are specified in different Site:GroundTemperature:* objects and used during the simulation. This setpoint manager is primarily intended for condenser or plant loops using some type of ground heat exchanger.

Fields

control_variable [string] (Default: Temperature)
reference_ground_temperature_object_type [string]
offset_temperature_difference [number]
maximum_setpoint_temperature [number]
minimum_setpoint_temperature [number]
setpoint_node_or_nodelist_name [string]
SetpointManager:CondenserEnteringReset
This setpoint manager uses one curve to determine the optimum condenser entering water temperature for a given timestep and two other curves to place boundary conditions on the setpoint value.

Fields

control_variable [string] (Default: Temperature)
default_condenser_entering_water_temperature_schedule_name [string]
minimum_design_wetbulb_temperature_curve_name [string]
minimum_outside_air_wetbulb_temperature_curve_name [string]
optimized_cond_entering_water_temperature_curve_name [string]
minimum_lift [number] (Default: 11.1)
maximum_condenser_entering_water_temperature [number] (Default: 32.0)
cooling_tower_design_inlet_air_wet_bulb_temperature [number] (Default: 25.56)
setpoint_node_or_nodelist_name [string]
SetpointManager:CondenserEnteringReset:Ideal
This setpoint manager determine the ideal optimum condenser entering water temperature setpoint for a given timestep.

Fields

control_variable [string] (Default: Temperature)
minimum_lift [number] (Default: 11.1)
maximum_condenser_entering_water_temperature [number] (Default: 32.0)
setpoint_node_or_nodelist_name [string]
SetpointManager:SingleZone:OneStageCooling
This object can be used with CoilSystem:Cooling:DX to model on/off cycling control of single stage air systems. Setpoints are modulated to run coil full on or full off depending on zone conditions. Intended for use with ZoneControl:Thermostat:StagedDualSetpoint

Fields

cooling_stage_on_supply_air_setpoint_temperature [number] (Default: -99.0)
cooling_stage_off_supply_air_setpoint_temperature [number] (Default: 99.0)
control_zone_name [string]
setpoint_node_or_nodelist_name [string]
SetpointManager:SingleZone:OneStageHeating
This object can be used with CoilSystem:Heating:DX, Coil:Heating:Fuel, Coil:Heating:Electric to model on/off cycling control of single stage air systems. Setpoints are modulated to run coil full on or full off depending on zone conditions. Intended for use with ZoneControl:Thermostat:StagedDualSetpoint.

Fields

heating_stage_on_supply_air_setpoint_temperature [number] (Default: 99.0)
heating_stage_off_supply_air_setpoint_temperature [number] (Default: -99.0)
control_zone_name [string]
setpoint_node_or_nodelist_name [string]
SetpointManager:ReturnTemperature:ChilledWater
This setpoint manager is used to place a temperature setpoint on a plant supply outlet node based on a target return water setpoint. The setpoint manager attempts to achieve the desired return water temperature by adjusting the supply temperature setpoint based on the plant conditions at each system time step.

Fields

plant_loop_supply_outlet_node [string]
plant_loop_supply_inlet_node [string]
minimum_supply_temperature_setpoint [number] (Default: 5.0)
maximum_supply_temperature_setpoint [number] (Default: 10.0)
return_temperature_setpoint_input_type [string]
return_temperature_setpoint_constant_value [number] (Default: 13.0)
return_temperature_setpoint_schedule_name [string]
SetpointManager:ReturnTemperature:HotWater
This setpoint manager is used to place a temperature setpoint on a plant supply outlet node based on a target return water setpoint. The setpoint manager attempts to achieve the desired return water temperature by adjusting the supply temperature setpoint based on the plant conditions at each system time step.

Fields

plant_loop_supply_outlet_node [string]
plant_loop_supply_inlet_node [string]
minimum_supply_temperature_setpoint [number] (Default: 77.0)
maximum_supply_temperature_setpoint [number] (Default: 82.0)
return_temperature_setpoint_input_type [string]
return_temperature_setpoint_constant_value [number] (Default: 71.0)
return_temperature_setpoint_schedule_name [string]
"""