"""
# HVAC Templates
"""
"""
HVACTemplate:Thermostat
Zone thermostat control. Referenced schedules must be defined elsewhere in the idf. Thermostat control type is dual setpoint with deadband. It is not necessary to create a thermostat object for every zone, only for each unique set of setpoint schedules. For example, an office building may have two thermostat objects, one for “Office” and one for “Storage”.

Fields

heating_setpoint_schedule_name [string]
constant_heating_setpoint [number]
cooling_setpoint_schedule_name [string]
constant_cooling_setpoint [number]
HVACTemplate:Zone:IdealLoadsAirSystem
Zone with ideal air system that meets heating or cooling loads

Fields

zone_name [string]
template_thermostat_name [string]
system_availability_schedule_name [string]
maximum_heating_supply_air_temperature [number] (Default: 50.0)
minimum_cooling_supply_air_temperature [number] (Default: 13.0)
maximum_heating_supply_air_humidity_ratio [number] (Default: 0.0156)
minimum_cooling_supply_air_humidity_ratio [number] (Default: 0.0077)
heating_limit [string] (Default: NoLimit)
maximum_heating_air_flow_rate [unknown field type]
maximum_sensible_heating_capacity [unknown field type]
cooling_limit [string] (Default: NoLimit)
maximum_cooling_air_flow_rate [unknown field type]
maximum_total_cooling_capacity [unknown field type]
heating_availability_schedule_name [string]
cooling_availability_schedule_name [string]
dehumidification_control_type [string] (Default: ConstantSensibleHeatRatio)
cooling_sensible_heat_ratio [number] (Default: 0.7)
dehumidification_setpoint [number] (Default: 60.0)
humidification_control_type [string] (Default: None)
humidification_setpoint [number] (Default: 30.0)
outdoor_air_method [string] (Default: None)
outdoor_air_flow_rate_per_person [number] (Default: 0.00944)
outdoor_air_flow_rate_per_zone_floor_area [number] (Default: 0.0)
outdoor_air_flow_rate_per_zone [number] (Default: 0.0)
design_specification_outdoor_air_object_name [string]
demand_controlled_ventilation_type [string] (Default: None)
outdoor_air_economizer_type [string] (Default: NoEconomizer)
heat_recovery_type [string] (Default: None)
sensible_heat_recovery_effectiveness [number] (Default: 0.7)
latent_heat_recovery_effectiveness [number] (Default: 0.65)
HVACTemplate:Zone:BaseboardHeat
Zone baseboard heating system.

Fields

zone_name [string]
template_thermostat_name [string]
zone_heating_sizing_factor [number]
baseboard_heating_type [string] (Default: HotWater)
baseboard_heating_availability_schedule_name [string]
baseboard_heating_capacity [unknown field type] (Default: Autosize)
dedicated_outdoor_air_system_name [string]
outdoor_air_method [string] (Default: Flow/Person)
outdoor_air_flow_rate_per_person [number] (Default: 0.00944)
outdoor_air_flow_rate_per_zone_floor_area [number] (Default: 0.0)
outdoor_air_flow_rate_per_zone [number] (Default: 0.0)
design_specification_outdoor_air_object_name [string]
design_specification_zone_air_distribution_object_name [string]
HVACTemplate:Zone:FanCoil
4 pipe fan coil unit with optional outdoor air.

Fields

zone_name [string]
template_thermostat_name [string]
supply_air_maximum_flow_rate [unknown field type] (Default: Autosize)
zone_heating_sizing_factor [number]
zone_cooling_sizing_factor [number]
outdoor_air_method [string] (Default: Flow/Person)
outdoor_air_flow_rate_per_person [number] (Default: 0.00944)
outdoor_air_flow_rate_per_zone_floor_area [number] (Default: 0.0)
outdoor_air_flow_rate_per_zone [number] (Default: 0.0)
system_availability_schedule_name [string]
supply_fan_total_efficiency [number] (Default: 0.7)
supply_fan_delta_pressure [number] (Default: 75.0)
supply_fan_motor_efficiency [number] (Default: 0.9)
supply_fan_motor_in_air_stream_fraction [number] (Default: 1.0)
cooling_coil_type [string] (Default: ChilledWater)
cooling_coil_availability_schedule_name [string]
cooling_coil_design_setpoint [number] (Default: 14.0)
heating_coil_type [string] (Default: HotWater)
heating_coil_availability_schedule_name [string]
heating_coil_design_setpoint [number] (Default: 50.0)
dedicated_outdoor_air_system_name [string]
zone_cooling_design_supply_air_temperature_input_method [string] (Default: SupplyAirTemperature)
zone_cooling_design_supply_air_temperature_difference [number] (Default: 11.11)
zone_heating_design_supply_air_temperature_input_method [string] (Default: SupplyAirTemperature)
zone_heating_design_supply_air_temperature_difference [number] (Default: 30.0)
design_specification_outdoor_air_object_name [string]
design_specification_zone_air_distribution_object_name [string]
capacity_control_method [string]
low_speed_supply_air_flow_ratio [number] (Default: 0.33)
medium_speed_supply_air_flow_ratio [number] (Default: 0.66)
outdoor_air_schedule_name [string]
baseboard_heating_type [string] (Default: None)
baseboard_heating_availability_schedule_name [string]
baseboard_heating_capacity [unknown field type] (Default: Autosize)
HVACTemplate:Zone:PTAC
Packaged Terminal Air Conditioner

Fields

zone_name [string]
template_thermostat_name [string]
cooling_supply_air_flow_rate [unknown field type] (Default: Autosize)
heating_supply_air_flow_rate [unknown field type] (Default: Autosize)
no_load_supply_air_flow_rate [unknown field type]
zone_heating_sizing_factor [number]
zone_cooling_sizing_factor [number]
outdoor_air_method [string] (Default: Flow/Person)
outdoor_air_flow_rate_per_person [number] (Default: 0.00944)
outdoor_air_flow_rate_per_zone_floor_area [number] (Default: 0.0)
outdoor_air_flow_rate_per_zone [number] (Default: 0.0)
system_availability_schedule_name [string]
supply_fan_operating_mode_schedule_name [string]
supply_fan_placement [string] (Default: DrawThrough)
supply_fan_total_efficiency [number] (Default: 0.7)
supply_fan_delta_pressure [number] (Default: 75.0)
supply_fan_motor_efficiency [number] (Default: 0.9)
cooling_coil_type [string] (Default: SingleSpeedDX)
cooling_coil_availability_schedule_name [string]
cooling_coil_gross_rated_total_capacity [unknown field type] (Default: Autosize)
cooling_coil_gross_rated_sensible_heat_ratio [unknown field type] (Default: Autosize)
cooling_coil_gross_rated_cooling_cop [number] (Default: 3.0)
heating_coil_type [string] (Default: Electric)
heating_coil_availability_schedule_name [string]
heating_coil_capacity [unknown field type] (Default: Autosize)
gas_heating_coil_efficiency [number] (Default: 0.8)
gas_heating_coil_parasitic_electric_load [number] (Default: 0.0)
dedicated_outdoor_air_system_name [string]
zone_cooling_design_supply_air_temperature_input_method [string] (Default: SupplyAirTemperature)
zone_cooling_design_supply_air_temperature [number] (Default: 14.0)
zone_cooling_design_supply_air_temperature_difference [number] (Default: 11.11)
zone_heating_design_supply_air_temperature_input_method [string] (Default: SupplyAirTemperature)
zone_heating_design_supply_air_temperature [number] (Default: 50.0)
zone_heating_design_supply_air_temperature_difference [number] (Default: 30.0)
design_specification_outdoor_air_object_name [string]
design_specification_zone_air_distribution_object_name [string]
baseboard_heating_type [string] (Default: None)
baseboard_heating_availability_schedule_name [string]
baseboard_heating_capacity [unknown field type] (Default: Autosize)
capacity_control_method [string] (Default: None)
HVACTemplate:Zone:PTHP
Packaged Terminal Heat Pump

Fields

zone_name [string]
template_thermostat_name [string]
cooling_supply_air_flow_rate [unknown field type] (Default: Autosize)
heating_supply_air_flow_rate [unknown field type] (Default: Autosize)
no_load_supply_air_flow_rate [unknown field type]
zone_heating_sizing_factor [number]
zone_cooling_sizing_factor [number]
outdoor_air_method [string] (Default: Flow/Person)
outdoor_air_flow_rate_per_person [number] (Default: 0.00944)
outdoor_air_flow_rate_per_zone_floor_area [number] (Default: 0.0)
outdoor_air_flow_rate_per_zone [number] (Default: 0.0)
system_availability_schedule_name [string]
supply_fan_operating_mode_schedule_name [string]
supply_fan_placement [string] (Default: DrawThrough)
supply_fan_total_efficiency [number] (Default: 0.7)
supply_fan_delta_pressure [number] (Default: 75.0)
supply_fan_motor_efficiency [number] (Default: 0.9)
cooling_coil_type [string] (Default: SingleSpeedDX)
cooling_coil_availability_schedule_name [string]
cooling_coil_gross_rated_total_capacity [unknown field type] (Default: Autosize)
cooling_coil_gross_rated_sensible_heat_ratio [unknown field type] (Default: Autosize)
cooling_coil_gross_rated_cop [number] (Default: 3.0)
heat_pump_heating_coil_type [string] (Default: SingleSpeedDXHeatPump)
heat_pump_heating_coil_availability_schedule_name [string]
heat_pump_heating_coil_gross_rated_capacity [unknown field type] (Default: Autosize)
heat_pump_heating_coil_gross_rated_cop [number] (Default: 2.75)
heat_pump_heating_minimum_outdoor_dry_bulb_temperature [number] (Default: -8.0)
heat_pump_defrost_maximum_outdoor_dry_bulb_temperature [number] (Default: 5.0)
heat_pump_defrost_strategy [string] (Default: ReverseCycle)
heat_pump_defrost_control [string] (Default: Timed)
heat_pump_defrost_time_period_fraction [number] (Default: 0.058333)
supplemental_heating_coil_type [string] (Default: Electric)
supplemental_heating_coil_availability_schedule_name [string]
supplemental_heating_coil_capacity [unknown field type] (Default: Autosize)
supplemental_heating_coil_maximum_outdoor_dry_bulb_temperature [number] (Default: 21.0)
supplemental_gas_heating_coil_efficiency [number] (Default: 0.8)
supplemental_gas_heating_coil_parasitic_electric_load [number] (Default: 0.0)
dedicated_outdoor_air_system_name [string]
zone_cooling_design_supply_air_temperature_input_method [string] (Default: SupplyAirTemperature)
zone_cooling_design_supply_air_temperature [number] (Default: 14.0)
zone_cooling_design_supply_air_temperature_difference [number] (Default: 11.11)
zone_heating_design_supply_air_temperature_input_method [string] (Default: SupplyAirTemperature)
zone_heating_design_supply_air_temperature [number] (Default: 50.0)
zone_heating_design_supply_air_temperature_difference [number] (Default: 30.0)
design_specification_outdoor_air_object_name [string]
design_specification_zone_air_distribution_object_name [string]
baseboard_heating_type [string] (Default: None)
baseboard_heating_availability_schedule_name [string]
baseboard_heating_capacity [unknown field type] (Default: Autosize)
capacity_control_method [string] (Default: None)
HVACTemplate:Zone:WaterToAirHeatPump
Water to Air Heat Pump to be used with HVACTemplate:Plant:MixedWaterLoop

Fields

zone_name [string]
template_thermostat_name [string]
cooling_supply_air_flow_rate [unknown field type] (Default: Autosize)
heating_supply_air_flow_rate [unknown field type] (Default: Autosize)
no_load_supply_air_flow_rate [unknown field type]
zone_heating_sizing_factor [number]
zone_cooling_sizing_factor [number]
outdoor_air_method [string] (Default: Flow/Person)
outdoor_air_flow_rate_per_person [number] (Default: 0.00944)
outdoor_air_flow_rate_per_zone_floor_area [number] (Default: 0.0)
outdoor_air_flow_rate_per_zone [number] (Default: 0.0)
system_availability_schedule_name [string]
supply_fan_operating_mode_schedule_name [string]
supply_fan_placement [string] (Default: DrawThrough)
supply_fan_total_efficiency [number] (Default: 0.7)
supply_fan_delta_pressure [number] (Default: 75.0)
supply_fan_motor_efficiency [number] (Default: 0.9)
cooling_coil_type [string] (Default: Coil:Cooling:WaterToAirHeatPump:EquationFit)
cooling_coil_gross_rated_total_capacity [unknown field type] (Default: Autosize)
cooling_coil_gross_rated_sensible_heat_ratio [unknown field type] (Default: Autosize)
cooling_coil_gross_rated_cop [number] (Default: 3.5)
heat_pump_heating_coil_type [string] (Default: Coil:Heating:WaterToAirHeatPump:EquationFit)
heat_pump_heating_coil_gross_rated_capacity [unknown field type] (Default: Autosize)
heat_pump_heating_coil_gross_rated_cop [number] (Default: 4.2)
supplemental_heating_coil_availability_schedule_name [string]
supplemental_heating_coil_capacity [unknown field type] (Default: Autosize)
maximum_cycling_rate [number] (Default: 2.5)
heat_pump_time_constant [number] (Default: 60.0)
fraction_of_on_cycle_power_use [number] (Default: 0.01)
heat_pump_fan_delay_time [number] (Default: 60.0)
dedicated_outdoor_air_system_name [string]
supplemental_heating_coil_type [string] (Default: Electric)
zone_cooling_design_supply_air_temperature_input_method [string] (Default: SupplyAirTemperature)
zone_cooling_design_supply_air_temperature [number] (Default: 14.0)
zone_cooling_design_supply_air_temperature_difference [number] (Default: 11.11)
zone_heating_design_supply_air_temperature_input_method [string] (Default: SupplyAirTemperature)
zone_heating_design_supply_air_temperature [number] (Default: 50.0)
zone_heating_design_supply_air_temperature_difference [number] (Default: 30.0)
heat_pump_coil_water_flow_mode [string] (Default: Cycling)
design_specification_outdoor_air_object_name [string]
design_specification_zone_air_distribution_object_name [string]
baseboard_heating_type [string] (Default: None)
baseboard_heating_availability_schedule_name [string]
baseboard_heating_capacity [unknown field type] (Default: Autosize)
HVACTemplate:Zone:VRF
Zone terminal unit with variable refrigerant flow (VRF) DX cooling and heating coils (air-to-air or water-to-air heat pump). The VRF terminal units are served by an HVACTemplate:System:VRF system.

Fields

zone_name [string]
template_vrf_system_name [string]
template_thermostat_name [string]
zone_heating_sizing_factor [number]
zone_cooling_sizing_factor [number]
rated_total_heating_capacity_sizing_ratio [number] (Default: 1.0)
cooling_supply_air_flow_rate [unknown field type] (Default: Autosize)
no_cooling_supply_air_flow_rate [unknown field type] (Default: Autosize)
heating_supply_air_flow_rate [unknown field type] (Default: Autosize)
no_heating_supply_air_flow_rate [unknown field type] (Default: Autosize)
cooling_outdoor_air_flow_rate [unknown field type] (Default: Autosize)
heating_outdoor_air_flow_rate [unknown field type] (Default: Autosize)
no_load_outdoor_air_flow_rate [unknown field type] (Default: Autosize)
outdoor_air_method [string] (Default: Flow/Person)
outdoor_air_flow_rate_per_person [number] (Default: 0.00944)
outdoor_air_flow_rate_per_zone_floor_area [number] (Default: 0.0)
outdoor_air_flow_rate_per_zone [number] (Default: 0.0)
design_specification_outdoor_air_object_name [string]
design_specification_zone_air_distribution_object_name [string]
system_availability_schedule_name [string]
supply_fan_operating_mode_schedule_name [string]
supply_air_fan_placement [string] (Default: BlowThrough)
supply_fan_total_efficiency [number] (Default: 0.7)
supply_fan_delta_pressure [number] (Default: 75.0)
supply_fan_motor_efficiency [number] (Default: 0.9)
cooling_coil_type [string] (Default: VariableRefrigerantFlowDX)
cooling_coil_availability_schedule_name [string]
cooling_coil_gross_rated_total_capacity [unknown field type] (Default: Autosize)
cooling_coil_gross_rated_sensible_heat_ratio [unknown field type] (Default: Autosize)
heat_pump_heating_coil_type [string] (Default: VariableRefrigerantFlowDX)
heat_pump_heating_coil_availability_schedule_name [string]
heat_pump_heating_coil_gross_rated_capacity [unknown field type] (Default: Autosize)
zone_terminal_unit_on_parasitic_electric_energy_use [number] (Default: 0.0)
zone_terminal_unit_off_parasitic_electric_energy_use [number] (Default: 0.0)
dedicated_outdoor_air_system_name [string]
zone_cooling_design_supply_air_temperature_input_method [string] (Default: SupplyAirTemperature)
zone_cooling_design_supply_air_temperature [number] (Default: 14.0)
zone_cooling_design_supply_air_temperature_difference [number] (Default: 11.11)
zone_heating_design_supply_air_temperature_input_method [string] (Default: SupplyAirTemperature)
zone_heating_design_supply_air_temperature [number] (Default: 50.0)
zone_heating_design_supply_air_temperature_difference [number] (Default: 30.0)
baseboard_heating_type [string] (Default: None)
baseboard_heating_availability_schedule_name [string]
baseboard_heating_capacity [unknown field type] (Default: Autosize)
HVACTemplate:Zone:Unitary
Zone terminal unit, constant volume, no controls.

Fields

zone_name [string]
template_unitary_system_name [string]
template_thermostat_name [string]
supply_air_maximum_flow_rate [unknown field type] (Default: Autosize)
zone_heating_sizing_factor [number]
zone_cooling_sizing_factor [number]
outdoor_air_method [string] (Default: Flow/Person)
outdoor_air_flow_rate_per_person [number] (Default: 0.00944)
outdoor_air_flow_rate_per_zone_floor_area [number] (Default: 0.0)
outdoor_air_flow_rate_per_zone [number] (Default: 0.0)
supply_plenum_name [string]
return_plenum_name [string]
baseboard_heating_type [string] (Default: None)
baseboard_heating_availability_schedule_name [string]
baseboard_heating_capacity [unknown field type] (Default: Autosize)
zone_cooling_design_supply_air_temperature_input_method [string] (Default: SystemSupplyAirTemperature)
zone_cooling_design_supply_air_temperature [number] (Default: 12.8)
zone_cooling_design_supply_air_temperature_difference [number] (Default: 11.11)
zone_heating_design_supply_air_temperature_input_method [string] (Default: SystemSupplyAirTemperature)
zone_heating_design_supply_air_temperature [number] (Default: 50.0)
zone_heating_design_supply_air_temperature_difference [number] (Default: 30.0)
design_specification_outdoor_air_object_name [string]
design_specification_zone_air_distribution_object_name [string]
HVACTemplate:Zone:VAV
Zone terminal unit, variable volume, reheat optional. For heating, this unit activates reheat coil first, then increases airflow (if reverse action specified).

Fields

zone_name [string]
template_vav_system_name [string]
template_thermostat_name [string]
supply_air_maximum_flow_rate [unknown field type] (Default: Autosize)
zone_heating_sizing_factor [number]
zone_cooling_sizing_factor [number]
zone_minimum_air_flow_input_method [string] (Default: Constant)
constant_minimum_air_flow_fraction [number] (Default: 0.2)
fixed_minimum_air_flow_rate [number]
minimum_air_flow_fraction_schedule_name [string]
outdoor_air_method [string] (Default: Flow/Person)
outdoor_air_flow_rate_per_person [number] (Default: 0.00944)
outdoor_air_flow_rate_per_zone_floor_area [number] (Default: 0.0)
outdoor_air_flow_rate_per_zone [number] (Default: 0.0)
reheat_coil_type [string] (Default: None)
reheat_coil_availability_schedule_name [string]
damper_heating_action [string] (Default: Reverse)
maximum_flow_per_zone_floor_area_during_reheat [unknown field type]
maximum_flow_fraction_during_reheat [unknown field type]
maximum_reheat_air_temperature [number]
design_specification_outdoor_air_object_name_for_control [string]
supply_plenum_name [string]
return_plenum_name [string]
baseboard_heating_type [string] (Default: None)
baseboard_heating_availability_schedule_name [string]
baseboard_heating_capacity [unknown field type] (Default: Autosize)
zone_cooling_design_supply_air_temperature_input_method [string] (Default: SystemSupplyAirTemperature)
zone_cooling_design_supply_air_temperature [number] (Default: 12.8)
zone_cooling_design_supply_air_temperature_difference [number] (Default: 11.11)
zone_heating_design_supply_air_temperature_input_method [string] (Default: SupplyAirTemperature)
zone_heating_design_supply_air_temperature [number] (Default: 50.0)
zone_heating_design_supply_air_temperature_difference [number] (Default: 30.0)
design_specification_outdoor_air_object_name_for_sizing [string]
design_specification_zone_air_distribution_object_name [string]
HVACTemplate:Zone:VAV:FanPowered
Zone terminal unit, fan powered variable volume, reheat optional. Referenced schedules must be defined elsewhere in the idf.

Fields

zone_name [string]
template_vav_system_name [string]
template_thermostat_name [string]
primary_supply_air_maximum_flow_rate [unknown field type] (Default: Autosize)
zone_heating_sizing_factor [number]
zone_cooling_sizing_factor [number]
primary_supply_air_minimum_flow_fraction [unknown field type] (Default: Autosize)
secondary_supply_air_maximum_flow_rate [unknown field type] (Default: Autosize)
flow_type [string] (Default: Parallel)
parallel_fan_on_flow_fraction [unknown field type] (Default: Autosize)
outdoor_air_method [string] (Default: Flow/Person)
outdoor_air_flow_rate_per_person [number] (Default: 0.00944)
outdoor_air_flow_rate_per_zone_floor_area [number] (Default: 0.0)
outdoor_air_flow_rate_per_zone [number] (Default: 0.0)
reheat_coil_type [string] (Default: Electric)
reheat_coil_availability_schedule_name [string]
fan_total_efficiency [number] (Default: 0.7)
fan_delta_pressure [number] (Default: 1000.0)
fan_motor_efficiency [number] (Default: 0.9)
supply_plenum_name [string]
return_plenum_name [string]
baseboard_heating_type [string] (Default: None)
baseboard_heating_availability_schedule_name [string]
baseboard_heating_capacity [unknown field type] (Default: Autosize)
zone_cooling_design_supply_air_temperature_input_method [string] (Default: SystemSupplyAirTemperature)
zone_cooling_design_supply_air_temperature [number] (Default: 12.8)
zone_cooling_design_supply_air_temperature_difference [number] (Default: 11.11)
zone_heating_design_supply_air_temperature_input_method [string] (Default: SupplyAirTemperature)
zone_heating_design_supply_air_temperature [number] (Default: 50.0)
zone_heating_design_supply_air_temperature_difference [number] (Default: 30.0)
zone_piu_fan_schedule_name [string]
design_specification_outdoor_air_object_name [string]
design_specification_zone_air_distribution_object_name [string]
HVACTemplate:Zone:VAV:HeatAndCool
VAV system with VAV for both heating and cooling and optional reheat coil. For heating, this unit increases airflow first, then activates reheat coil.

Fields

zone_name [string]
template_vav_system_name [string]
template_thermostat_name [string]
supply_air_maximum_flow_rate [unknown field type] (Default: Autosize)
zone_heating_sizing_factor [number]
zone_cooling_sizing_factor [number]
constant_minimum_air_flow_fraction [number] (Default: 0.2)
outdoor_air_method [string] (Default: Flow/Person)
outdoor_air_flow_rate_per_person [number] (Default: 0.00944)
outdoor_air_flow_rate_per_zone_floor_area [number] (Default: 0.0)
outdoor_air_flow_rate_per_zone [number] (Default: 0.0)
design_specification_outdoor_air_object_name_for_sizing [string]
design_specification_zone_air_distribution_object_name [string]
reheat_coil_type [string] (Default: None)
reheat_coil_availability_schedule_name [string]
maximum_reheat_air_temperature [number]
supply_plenum_name [string]
return_plenum_name [string]
baseboard_heating_type [string] (Default: None)
baseboard_heating_availability_schedule_name [string]
baseboard_heating_capacity [unknown field type] (Default: Autosize)
zone_cooling_design_supply_air_temperature_input_method [string] (Default: SystemSupplyAirTemperature)
zone_cooling_design_supply_air_temperature [number] (Default: 12.8)
zone_cooling_design_supply_air_temperature_difference [number] (Default: 11.11)
zone_heating_design_supply_air_temperature_input_method [string] (Default: SupplyAirTemperature)
zone_heating_design_supply_air_temperature [number] (Default: 50.0)
zone_heating_design_supply_air_temperature_difference [number] (Default: 30.0)
HVACTemplate:Zone:ConstantVolume
Zone terminal unit, constant volume, reheat optional. Referenced schedules must be defined elsewhere in the idf.

Fields

zone_name [string]
template_constant_volume_system_name [string]
template_thermostat_name [string]
supply_air_maximum_flow_rate [unknown field type] (Default: Autosize)
zone_heating_sizing_factor [number]
zone_cooling_sizing_factor [number]
outdoor_air_method [string] (Default: Flow/Person)
outdoor_air_flow_rate_per_person [number] (Default: 0.00944)
outdoor_air_flow_rate_per_zone_floor_area [number] (Default: 0.0)
outdoor_air_flow_rate_per_zone [number] (Default: 0.0)
design_specification_outdoor_air_object_name [string]
design_specification_zone_air_distribution_object_name [string]
reheat_coil_type [string] (Default: None)
reheat_coil_availability_schedule_name [string]
maximum_reheat_air_temperature [number]
supply_plenum_name [string]
return_plenum_name [string]
baseboard_heating_type [string] (Default: None)
baseboard_heating_availability_schedule_name [string]
baseboard_heating_capacity [unknown field type] (Default: Autosize)
zone_cooling_design_supply_air_temperature_input_method [string] (Default: SystemSupplyAirTemperature)
zone_cooling_design_supply_air_temperature [number] (Default: 12.8)
zone_cooling_design_supply_air_temperature_difference [number] (Default: 11.11)
zone_heating_design_supply_air_temperature_input_method [string] (Default: SupplyAirTemperature)
zone_heating_design_supply_air_temperature [number] (Default: 50.0)
zone_heating_design_supply_air_temperature_difference [number] (Default: 30.0)
HVACTemplate:Zone:DualDuct
Zone terminal unit, dual-duct, constant or variable volume.

Fields

zone_name [string]
template_dual_duct_system_name [string]
template_thermostat_name [string]
supply_air_maximum_flow_rate [unknown field type] (Default: Autosize)
zone_heating_sizing_factor [number]
zone_cooling_sizing_factor [number]
zone_minimum_air_flow_fraction [number] (Default: 0.2)
outdoor_air_method [string] (Default: Flow/Person)
outdoor_air_flow_rate_per_person [number] (Default: 0.00944)
outdoor_air_flow_rate_per_zone_floor_area [number] (Default: 0.0)
outdoor_air_flow_rate_per_zone [number] (Default: 0.0)
design_specification_outdoor_air_object_name_for_sizing [string]
design_specification_zone_air_distribution_object_name [string]
design_specification_outdoor_air_object_name_for_control [string]
cold_supply_plenum_name [string]
hot_supply_plenum_name [string]
return_plenum_name [string]
baseboard_heating_type [string] (Default: None)
baseboard_heating_availability_schedule_name [string]
baseboard_heating_capacity [unknown field type] (Default: Autosize)
zone_cooling_design_supply_air_temperature_input_method [string] (Default: SystemSupplyAirTemperature)
zone_cooling_design_supply_air_temperature [number] (Default: 12.8)
zone_cooling_design_supply_air_temperature_difference [number] (Default: 11.11)
zone_heating_design_supply_air_temperature_input_method [string] (Default: SystemSupplyAirTemperature)
zone_heating_design_supply_air_temperature [number] (Default: 50.0)
zone_heating_design_supply_air_temperature_difference [number] (Default: 30.0)
HVACTemplate:System:VRF
Variable refrigerant flow (VRF) heat pump condensing unit. Serves one or more VRF zone terminal units (HVACTemplate:Zone:VRF).

Fields

system_availability_schedule_name [string]
gross_rated_total_cooling_capacity [unknown field type] (Default: Autosize)
gross_rated_cooling_cop [number] (Default: 3.3)
minimum_outdoor_temperature_in_cooling_mode [number] (Default: -6.0)
maximum_outdoor_temperature_in_cooling_mode [number] (Default: 43.0)
gross_rated_heating_capacity [unknown field type] (Default: Autosize)
rated_heating_capacity_sizing_ratio [number] (Default: 1.0)
gross_rated_heating_cop [number] (Default: 3.4)
minimum_outdoor_temperature_in_heating_mode [number] (Default: -20.0)
maximum_outdoor_temperature_in_heating_mode [number] (Default: 16.0)
minimum_heat_pump_part_load_ratio [number] (Default: 0.15)
zone_name_for_master_thermostat_location [string]
master_thermostat_priority_control_type [string] (Default: MasterThermostatPriority)
thermostat_priority_schedule_name [string]
heat_pump_waste_heat_recovery [string] (Default: No)
equivalent_piping_length_used_for_piping_correction_factor_in_cooling_mode [number] (Default: 30.0)
vertical_height_used_for_piping_correction_factor [number] (Default: 10.0)
equivalent_piping_length_used_for_piping_correction_factor_in_heating_mode [number] (Default: 30.0)
crankcase_heater_power_per_compressor [number] (Default: 33.0)
number_of_compressors [number] (Default: 2.0)
ratio_of_compressor_size_to_total_compressor_capacity [number] (Default: 0.5)
maximum_outdoor_dry_bulb_temperature_for_crankcase_heater [number] (Default: 5.0)
defrost_strategy [string] (Default: Resistive)
defrost_control [string] (Default: Timed)
defrost_time_period_fraction [number] (Default: 0.058333)
resistive_defrost_heater_capacity [unknown field type] (Default: Autosize)
maximum_outdoor_dry_bulb_temperature_for_defrost_operation [number] (Default: 5.0)
condenser_type [string] (Default: AirCooled)
water_condenser_volume_flow_rate [unknown field type] (Default: Autosize)
evaporative_condenser_effectiveness [number] (Default: 0.9)
evaporative_condenser_air_flow_rate [unknown field type] (Default: Autosize)
evaporative_condenser_pump_rated_power_consumption [unknown field type] (Default: 0.0)
basin_heater_capacity [number] (Default: 0.0)
basin_heater_setpoint_temperature [number] (Default: 2.0)
basin_heater_operating_schedule_name [string]
fuel_type [string] (Default: Electricity)
minimum_outdoor_temperature_in_heat_recovery_mode [number] (Default: -15.0)
maximum_outdoor_temperature_in_heat_recovery_mode [number] (Default: 45.0)
HVACTemplate:System:Unitary
Unitary furnace with air conditioner

Fields

system_availability_schedule_name [string]
control_zone_or_thermostat_location_name [string]
supply_fan_maximum_flow_rate [unknown field type] (Default: Autosize)
supply_fan_operating_mode_schedule_name [string]
supply_fan_total_efficiency [number] (Default: 0.7)
supply_fan_delta_pressure [number] (Default: 600.0)
supply_fan_motor_efficiency [number] (Default: 0.9)
supply_fan_motor_in_air_stream_fraction [number] (Default: 1.0)
cooling_coil_type [string] (Default: SingleSpeedDX)
cooling_coil_availability_schedule_name [string]
cooling_design_supply_air_temperature [number] (Default: 12.8)
cooling_coil_gross_rated_total_capacity [unknown field type] (Default: Autosize)
cooling_coil_gross_rated_sensible_heat_ratio [unknown field type] (Default: Autosize)
cooling_coil_gross_rated_cop [number] (Default: 3.0)
heating_coil_type [string]
heating_coil_availability_schedule_name [string]
heating_design_supply_air_temperature [number] (Default: 50.0)
heating_coil_capacity [unknown field type] (Default: Autosize)
gas_heating_coil_efficiency [number] (Default: 0.8)
gas_heating_coil_parasitic_electric_load [number] (Default: 0.0)
maximum_outdoor_air_flow_rate [unknown field type] (Default: Autosize)
minimum_outdoor_air_flow_rate [unknown field type] (Default: Autosize)
minimum_outdoor_air_schedule_name [string]
economizer_type [string] (Default: NoEconomizer)
economizer_lockout [string] (Default: NoLockout)
economizer_upper_temperature_limit [number]
economizer_lower_temperature_limit [number]
economizer_upper_enthalpy_limit [number]
economizer_maximum_limit_dewpoint_temperature [number]
supply_plenum_name [string]
return_plenum_name [string]
supply_fan_placement [string] (Default: BlowThrough)
night_cycle_control [string] (Default: StayOff)
night_cycle_control_zone_name [string]
heat_recovery_type [string] (Default: None)
sensible_heat_recovery_effectiveness [number] (Default: 0.7)
latent_heat_recovery_effectiveness [number] (Default: 0.65)
dehumidification_control_type [string] (Default: None)
dehumidification_setpoint [number] (Default: 60.0)
humidifier_type [string] (Default: None)
humidifier_availability_schedule_name [string]
humidifier_rated_capacity [number] (Default: 1e-06)
humidifier_rated_electric_power [unknown field type] (Default: Autosize)
humidifier_control_zone_name [string]
humidifier_setpoint [number] (Default: 30.0)
return_fan [string] (Default: No)
return_fan_total_efficiency [number] (Default: 0.7)
return_fan_delta_pressure [number] (Default: 500.0)
return_fan_motor_efficiency [number] (Default: 0.9)
return_fan_motor_in_air_stream_fraction [number] (Default: 1.0)
HVACTemplate:System:UnitaryHeatPump:AirToAir
Unitary furnace with electric air-to-air heat pump

Fields

system_availability_schedule_name [string]
control_zone_or_thermostat_location_name [string]
cooling_supply_air_flow_rate [unknown field type] (Default: Autosize)
heating_supply_air_flow_rate [unknown field type] (Default: Autosize)
no_load_supply_air_flow_rate [unknown field type] (Default: Autosize)
supply_fan_operating_mode_schedule_name [string]
supply_fan_placement [string] (Default: BlowThrough)
supply_fan_total_efficiency [number] (Default: 0.7)
supply_fan_delta_pressure [number] (Default: 600.0)
supply_fan_motor_efficiency [number] (Default: 0.9)
supply_fan_motor_in_air_stream_fraction [number] (Default: 1.0)
cooling_coil_type [string] (Default: SingleSpeedDX)
cooling_coil_availability_schedule_name [string]
cooling_design_supply_air_temperature [number] (Default: 12.8)
cooling_coil_gross_rated_total_capacity [unknown field type] (Default: Autosize)
cooling_coil_gross_rated_sensible_heat_ratio [unknown field type] (Default: Autosize)
cooling_coil_gross_rated_cop [number] (Default: 3.0)
heat_pump_heating_coil_type [string] (Default: SingleSpeedDXHeatPump)
heat_pump_heating_coil_availability_schedule_name [string]
heating_design_supply_air_temperature [number] (Default: 50.0)
heat_pump_heating_coil_gross_rated_capacity [unknown field type] (Default: Autosize)
heat_pump_heating_coil_rated_cop [number] (Default: 2.75)
heat_pump_heating_minimum_outdoor_dry_bulb_temperature [number] (Default: -8.0)
heat_pump_defrost_maximum_outdoor_dry_bulb_temperature [number] (Default: 5.0)
heat_pump_defrost_strategy [string] (Default: ReverseCycle)
heat_pump_defrost_control [string] (Default: Timed)
heat_pump_defrost_time_period_fraction [number] (Default: 0.058333)
supplemental_heating_coil_type [string] (Default: Electric)
supplemental_heating_coil_availability_schedule_name [string]
supplemental_heating_coil_capacity [unknown field type] (Default: Autosize)
supplemental_heating_coil_maximum_outdoor_dry_bulb_temperature [number] (Default: 21.0)
supplemental_gas_heating_coil_efficiency [number] (Default: 0.8)
supplemental_gas_heating_coil_parasitic_electric_load [number] (Default: 0.0)
maximum_outdoor_air_flow_rate [unknown field type] (Default: Autosize)
minimum_outdoor_air_flow_rate [unknown field type] (Default: Autosize)
minimum_outdoor_air_schedule_name [string]
economizer_type [string] (Default: NoEconomizer)
economizer_lockout [string] (Default: NoLockout)
economizer_maximum_limit_dry_bulb_temperature [number]
economizer_maximum_limit_enthalpy [number]
economizer_maximum_limit_dewpoint_temperature [number]
economizer_minimum_limit_dry_bulb_temperature [number]
supply_plenum_name [string]
return_plenum_name [string]
night_cycle_control [string] (Default: StayOff)
night_cycle_control_zone_name [string]
heat_recovery_type [string] (Default: None)
sensible_heat_recovery_effectiveness [number] (Default: 0.7)
latent_heat_recovery_effectiveness [number] (Default: 0.65)
humidifier_type [string] (Default: None)
humidifier_availability_schedule_name [string]
humidifier_rated_capacity [number] (Default: 1e-06)
humidifier_rated_electric_power [unknown field type] (Default: Autosize)
humidifier_control_zone_name [string]
humidifier_setpoint [number] (Default: 30.0)
return_fan [string] (Default: No)
return_fan_total_efficiency [number] (Default: 0.7)
return_fan_delta_pressure [number] (Default: 500.0)
return_fan_motor_efficiency [number] (Default: 0.9)
return_fan_motor_in_air_stream_fraction [number] (Default: 1.0)
HVACTemplate:System:UnitarySystem
Unitary HVAC system with optional cooling and heating. Supports DX and chilled water, cooling, gas, electric, and hot water heating, air-to-air and water-to-air heat pumps.

Fields

system_availability_schedule_name [string]
control_type [string] (Default: Load)
control_zone_or_thermostat_location_name [string]
cooling_supply_air_flow_rate [unknown field type] (Default: Autosize)
heating_supply_air_flow_rate [unknown field type] (Default: Autosize)
no_load_supply_air_flow_rate [unknown field type] (Default: Autosize)
supply_fan_operating_mode_schedule_name [string]
supply_fan_placement [string] (Default: BlowThrough)
supply_fan_total_efficiency [number] (Default: 0.7)
supply_fan_delta_pressure [number] (Default: 600.0)
supply_fan_motor_efficiency [number] (Default: 0.9)
supply_fan_motor_in_air_stream_fraction [number] (Default: 1.0)
cooling_coil_type [string] (Default: SingleSpeedDX)
number_of_speeds_for_cooling [number] (Default: 1.0)
cooling_coil_availability_schedule_name [string]
cooling_design_supply_air_temperature [number] (Default: 12.8)
dx_cooling_coil_gross_rated_total_capacity [unknown field type] (Default: Autosize)
dx_cooling_coil_gross_rated_sensible_heat_ratio [unknown field type] (Default: Autosize)
dx_cooling_coil_gross_rated_cop [number] (Default: 3.0)
heating_coil_type [string] (Default: Gas)
number_of_speeds_or_stages_for_heating [number] (Default: 1.0)
heating_coil_availability_schedule_name [string]
heating_design_supply_air_temperature [number] (Default: 50.0)
heating_coil_gross_rated_capacity [unknown field type] (Default: Autosize)
gas_heating_coil_efficiency [number] (Default: 0.8)
gas_heating_coil_parasitic_electric_load [number] (Default: 0.0)
heat_pump_heating_coil_gross_rated_cop [number] (Default: 2.75)
heat_pump_heating_minimum_outdoor_dry_bulb_temperature [number] (Default: -8.0)
heat_pump_defrost_maximum_outdoor_dry_bulb_temperature [number] (Default: 5.0)
heat_pump_defrost_strategy [string] (Default: ReverseCycle)
heat_pump_defrost_control [string] (Default: Timed)
heat_pump_defrost_time_period_fraction [number] (Default: 0.058333)
supplemental_heating_or_reheat_coil_type [string] (Default: None)
supplemental_heating_or_reheat_coil_availability_schedule_name [string]
supplemental_heating_or_reheat_coil_capacity [unknown field type] (Default: Autosize)
supplemental_heating_or_reheat_coil_maximum_outdoor_dry_bulb_temperature [number] (Default: 21.0)
supplemental_gas_heating_or_reheat_coil_efficiency [number] (Default: 0.8)
supplemental_gas_heating_or_reheat_coil_parasitic_electric_load [number] (Default: 0.0)
maximum_outdoor_air_flow_rate [unknown field type] (Default: Autosize)
minimum_outdoor_air_flow_rate [unknown field type] (Default: Autosize)
minimum_outdoor_air_schedule_name [string]
economizer_type [string] (Default: NoEconomizer)
economizer_lockout [string] (Default: NoLockout)
economizer_maximum_limit_dry_bulb_temperature [number]
economizer_maximum_limit_enthalpy [number]
economizer_maximum_limit_dewpoint_temperature [number]
economizer_minimum_limit_dry_bulb_temperature [number]
supply_plenum_name [string]
return_plenum_name [string]
heat_recovery_type [string] (Default: None)
sensible_heat_recovery_effectiveness [number] (Default: 0.7)
latent_heat_recovery_effectiveness [number] (Default: 0.65)
heat_recovery_heat_exchanger_type [string] (Default: Plate)
heat_recovery_frost_control_type [string] (Default: None)
dehumidification_control_type [string] (Default: None)
dehumidification_relative_humidity_setpoint [number] (Default: 60.0)
dehumidification_relative_humidity_setpoint_schedule_name [string]
humidifier_type [string] (Default: None)
humidifier_availability_schedule_name [string]
humidifier_rated_capacity [number] (Default: 1e-06)
humidifier_rated_electric_power [unknown field type] (Default: Autosize)
humidifier_control_zone_name [string]
humidifier_relative_humidity_setpoint [number] (Default: 30.0)
humidifier_relative_humidity_setpoint_schedule_name [string]
sizing_option [string] (Default: NonCoincident)
return_fan [string] (Default: No)
return_fan_total_efficiency [number] (Default: 0.7)
return_fan_delta_pressure [number] (Default: 300.0)
return_fan_motor_efficiency [number] (Default: 0.9)
return_fan_motor_in_air_stream_fraction [number] (Default: 1.0)
HVACTemplate:System:VAV
Variable Air Volume (VAV) air loop with optional heating coil and optional preheat.

Fields

system_availability_schedule_name [string]
supply_fan_maximum_flow_rate [unknown field type] (Default: Autosize)
supply_fan_minimum_flow_rate [unknown field type] (Default: Autosize)
supply_fan_total_efficiency [number] (Default: 0.7)
supply_fan_delta_pressure [number] (Default: 1000.0)
supply_fan_motor_efficiency [number] (Default: 0.9)
supply_fan_motor_in_air_stream_fraction [number] (Default: 1.0)
cooling_coil_type [string] (Default: ChilledWater)
cooling_coil_availability_schedule_name [string]
cooling_coil_setpoint_schedule_name [string]
cooling_coil_design_setpoint [number] (Default: 12.8)
heating_coil_type [string] (Default: None)
heating_coil_availability_schedule_name [string]
heating_coil_setpoint_schedule_name [string]
heating_coil_design_setpoint [number] (Default: 10.0)
gas_heating_coil_efficiency [number] (Default: 0.8)
gas_heating_coil_parasitic_electric_load [number] (Default: 0.0)
preheat_coil_type [string] (Default: None)
preheat_coil_availability_schedule_name [string]
preheat_coil_setpoint_schedule_name [string]
preheat_coil_design_setpoint [number] (Default: 7.2)
gas_preheat_coil_efficiency [number] (Default: 0.8)
gas_preheat_coil_parasitic_electric_load [number] (Default: 0.0)
maximum_outdoor_air_flow_rate [unknown field type] (Default: Autosize)
minimum_outdoor_air_flow_rate [unknown field type] (Default: Autosize)
minimum_outdoor_air_control_type [string] (Default: ProportionalMinimum)
minimum_outdoor_air_schedule_name [string]
economizer_type [string] (Default: NoEconomizer)
economizer_lockout [string] (Default: NoLockout)
economizer_upper_temperature_limit [number]
economizer_lower_temperature_limit [number]
economizer_upper_enthalpy_limit [number]
economizer_maximum_limit_dewpoint_temperature [number]
supply_plenum_name [string]
return_plenum_name [string]
supply_fan_placement [string] (Default: DrawThrough)
supply_fan_part_load_power_coefficients [string] (Default: InletVaneDampers)
night_cycle_control [string] (Default: StayOff)
night_cycle_control_zone_name [string]
heat_recovery_type [string] (Default: None)
sensible_heat_recovery_effectiveness [number] (Default: 0.7)
latent_heat_recovery_effectiveness [number] (Default: 0.65)
cooling_coil_setpoint_reset_type [string] (Default: None)
heating_coil_setpoint_reset_type [string] (Default: None)
dehumidification_control_type [string] (Default: None)
dehumidification_control_zone_name [string]
dehumidification_setpoint [number] (Default: 60.0)
humidifier_type [string] (Default: None)
humidifier_availability_schedule_name [string]
humidifier_rated_capacity [number] (Default: 1e-06)
humidifier_rated_electric_power [unknown field type] (Default: Autosize)
humidifier_control_zone_name [string]
humidifier_setpoint [number] (Default: 30.0)
sizing_option [string] (Default: NonCoincident)
return_fan [string] (Default: No)
return_fan_total_efficiency [number] (Default: 0.7)
return_fan_delta_pressure [number] (Default: 500.0)
return_fan_motor_efficiency [number] (Default: 0.9)
return_fan_motor_in_air_stream_fraction [number] (Default: 1.0)
return_fan_part_load_power_coefficients [string] (Default: InletVaneDampers)
HVACTemplate:System:PackagedVAV
Packaged Variable Air Volume (PVAV) air loop with optional heating coil and optional preheat.

Fields

system_availability_schedule_name [string]
supply_fan_maximum_flow_rate [unknown field type] (Default: Autosize)
supply_fan_minimum_flow_rate [unknown field type] (Default: Autosize)
supply_fan_placement [string] (Default: DrawThrough)
supply_fan_total_efficiency [number] (Default: 0.7)
supply_fan_delta_pressure [number] (Default: 1000.0)
supply_fan_motor_efficiency [number] (Default: 0.9)
supply_fan_motor_in_air_stream_fraction [number] (Default: 1.0)
cooling_coil_type [string] (Default: TwoSpeedDX)
cooling_coil_availability_schedule_name [string]
cooling_coil_setpoint_schedule_name [string]
cooling_coil_design_setpoint [number] (Default: 12.8)
cooling_coil_gross_rated_total_capacity [unknown field type] (Default: Autosize)
cooling_coil_gross_rated_sensible_heat_ratio [unknown field type] (Default: Autosize)
cooling_coil_gross_rated_cop [number] (Default: 3.0)
heating_coil_type [string] (Default: None)
heating_coil_availability_schedule_name [string]
heating_coil_setpoint_schedule_name [string]
heating_coil_design_setpoint [number] (Default: 10.0)
heating_coil_capacity [unknown field type] (Default: Autosize)
gas_heating_coil_efficiency [number] (Default: 0.8)
gas_heating_coil_parasitic_electric_load [number] (Default: 0.0)
maximum_outdoor_air_flow_rate [unknown field type] (Default: Autosize)
minimum_outdoor_air_flow_rate [unknown field type] (Default: Autosize)
minimum_outdoor_air_control_type [string] (Default: ProportionalMinimum)
minimum_outdoor_air_schedule_name [string]
economizer_type [string] (Default: NoEconomizer)
economizer_lockout [string] (Default: NoLockout)
economizer_maximum_limit_dry_bulb_temperature [number]
economizer_maximum_limit_enthalpy [number]
economizer_maximum_limit_dewpoint_temperature [number]
economizer_minimum_limit_dry_bulb_temperature [number]
supply_plenum_name [string]
return_plenum_name [string]
supply_fan_part_load_power_coefficients [string] (Default: InletVaneDampers)
night_cycle_control [string] (Default: StayOff)
night_cycle_control_zone_name [string]
heat_recovery_type [string] (Default: None)
sensible_heat_recovery_effectiveness [number] (Default: 0.7)
latent_heat_recovery_effectiveness [number] (Default: 0.65)
cooling_coil_setpoint_reset_type [string] (Default: None)
heating_coil_setpoint_reset_type [string] (Default: None)
dehumidification_control_type [string] (Default: None)
dehumidification_control_zone_name [string]
dehumidification_setpoint [number] (Default: 60.0)
humidifier_type [string] (Default: None)
humidifier_availability_schedule_name [string]
humidifier_rated_capacity [number] (Default: 1e-06)
humidifier_rated_electric_power [unknown field type] (Default: Autosize)
humidifier_control_zone_name [string]
humidifier_setpoint [number] (Default: 30.0)
sizing_option [string] (Default: NonCoincident)
return_fan [string] (Default: No)
return_fan_total_efficiency [number] (Default: 0.7)
return_fan_delta_pressure [number] (Default: 500.0)
return_fan_motor_efficiency [number] (Default: 0.9)
return_fan_motor_in_air_stream_fraction [number] (Default: 1.0)
return_fan_part_load_power_coefficients [string] (Default: InletVaneDampers)
HVACTemplate:System:ConstantVolume
Constant Air Volume air loop with optional chilled water cooling coil, optional heating coil and optional preheat.

Fields

system_availability_schedule_name [string]
supply_fan_maximum_flow_rate [unknown field type] (Default: Autosize)
supply_fan_total_efficiency [number] (Default: 0.7)
supply_fan_delta_pressure [number] (Default: 600.0)
supply_fan_motor_efficiency [number] (Default: 0.9)
supply_fan_motor_in_air_stream_fraction [number] (Default: 1.0)
supply_fan_placement [string] (Default: DrawThrough)
cooling_coil_type [string] (Default: ChilledWater)
cooling_coil_availability_schedule_name [string]
cooling_coil_setpoint_control_type [string] (Default: FixedSetpoint)
cooling_coil_control_zone_name [string]
cooling_coil_design_setpoint_temperature [number] (Default: 12.8)
cooling_coil_setpoint_schedule_name [string]
cooling_coil_setpoint_at_outdoor_dry_bulb_low [number] (Default: 15.6)
cooling_coil_reset_outdoor_dry_bulb_low [number] (Default: 15.6)
cooling_coil_setpoint_at_outdoor_dry_bulb_high [number] (Default: 12.8)
cooling_coil_reset_outdoor_dry_bulb_high [number] (Default: 23.3)
heating_coil_type [string] (Default: HotWater)
heating_coil_availability_schedule_name [string]
heating_coil_setpoint_control_type [string] (Default: FixedSetpoint)
heating_coil_control_zone_name [string]
heating_coil_design_setpoint [number] (Default: 10.0)
heating_coil_setpoint_schedule_name [string]
heating_coil_setpoint_at_outdoor_dry_bulb_low [number] (Default: 15.0)
heating_coil_reset_outdoor_dry_bulb_low [number] (Default: 7.8)
heating_coil_setpoint_at_outdoor_dry_bulb_high [number] (Default: 12.2)
heating_coil_reset_outdoor_dry_bulb_high [number] (Default: 12.2)
heating_coil_capacity [unknown field type] (Default: Autosize)
gas_heating_coil_efficiency [number] (Default: 0.8)
gas_heating_coil_parasitic_electric_load [number] (Default: 0.0)
preheat_coil_type [string] (Default: None)
preheat_coil_availability_schedule_name [string]
preheat_coil_design_setpoint [number] (Default: 7.2)
preheat_coil_setpoint_schedule_name [string]
gas_preheat_coil_efficiency [number] (Default: 0.8)
gas_preheat_coil_parasitic_electric_load [number] (Default: 0.0)
maximum_outdoor_air_flow_rate [unknown field type] (Default: Autosize)
minimum_outdoor_air_flow_rate [unknown field type] (Default: Autosize)
minimum_outdoor_air_schedule_name [string]
economizer_type [string] (Default: NoEconomizer)
economizer_upper_temperature_limit [number]
economizer_lower_temperature_limit [number]
economizer_upper_enthalpy_limit [number]
economizer_maximum_limit_dewpoint_temperature [number]
supply_plenum_name [string]
return_plenum_name [string]
night_cycle_control [string] (Default: StayOff)
night_cycle_control_zone_name [string]
heat_recovery_type [string] (Default: None)
sensible_heat_recovery_effectiveness [number] (Default: 0.7)
latent_heat_recovery_effectiveness [number] (Default: 0.65)
heat_recovery_heat_exchanger_type [string] (Default: Plate)
heat_recovery_frost_control_type [string] (Default: None)
dehumidification_control_type [string] (Default: None)
dehumidification_control_zone_name [string]
dehumidification_relative_humidity_setpoint [number] (Default: 60.0)
dehumidification_relative_humidity_setpoint_schedule_name [string]
humidifier_type [string] (Default: None)
humidifier_availability_schedule_name [string]
humidifier_rated_capacity [number] (Default: 1e-06)
humidifier_rated_electric_power [unknown field type] (Default: Autosize)
humidifier_control_zone_name [string]
humidifier_relative_humidity_setpoint [number] (Default: 30.0)
humidifier_relative_humidity_setpoint_schedule_name [string]
return_fan [string] (Default: No)
return_fan_total_efficiency [number] (Default: 0.7)
return_fan_delta_pressure [number] (Default: 300.0)
return_fan_motor_efficiency [number] (Default: 0.9)
return_fan_motor_in_air_stream_fraction [number] (Default: 1.0)
HVACTemplate:System:DualDuct
Dual-duct constant volume or variable volume air loop

Fields

system_availability_schedule_name [string]
system_configuration_type [string] (Default: SingleFanConstantVolume)
main_supply_fan_maximum_flow_rate [unknown field type] (Default: Autosize)
main_supply_fan_minimum_flow_fraction [number] (Default: 0.2)
main_supply_fan_total_efficiency [number] (Default: 0.7)
main_supply_fan_delta_pressure [number] (Default: 1000.0)
main_supply_fan_motor_efficiency [number] (Default: 0.9)
main_supply_fan_motor_in_air_stream_fraction [number] (Default: 1.0)
main_supply_fan_part_load_power_coefficients [string] (Default: InletVaneDampers)
cold_duct_supply_fan_maximum_flow_rate [unknown field type] (Default: Autosize)
cold_duct_supply_fan_minimum_flow_fraction [number] (Default: 0.2)
cold_duct_supply_fan_total_efficiency [number] (Default: 0.7)
cold_duct_supply_fan_delta_pressure [number] (Default: 1000.0)
cold_duct_supply_fan_motor_efficiency [number] (Default: 0.9)
cold_duct_supply_fan_motor_in_air_stream_fraction [number] (Default: 1.0)
cold_duct_supply_fan_part_load_power_coefficients [string] (Default: InletVaneDampers)
cold_duct_supply_fan_placement [string] (Default: DrawThrough)
hot_duct_supply_fan_maximum_flow_rate [unknown field type] (Default: Autosize)
hot_duct_supply_fan_minimum_flow_fraction [number] (Default: 0.2)
hot_duct_supply_fan_total_efficiency [number] (Default: 0.7)
hot_duct_supply_fan_delta_pressure [number] (Default: 1000.0)
hot_duct_supply_fan_motor_efficiency [number] (Default: 0.9)
hot_duct_supply_fan_motor_in_air_stream_fraction [number] (Default: 1.0)
hot_duct_supply_fan_part_load_power_coefficients [string] (Default: InletVaneDampers)
hot_duct_supply_fan_placement [string] (Default: DrawThrough)
cooling_coil_type [string] (Default: ChilledWater)
cooling_coil_availability_schedule_name [string]
cooling_coil_setpoint_control_type [string] (Default: FixedSetpoint)
cooling_coil_design_setpoint_temperature [number] (Default: 12.8)
cooling_coil_setpoint_schedule_name [string]
cooling_coil_setpoint_at_outdoor_dry_bulb_low [number] (Default: 15.6)
cooling_coil_reset_outdoor_dry_bulb_low [number] (Default: 15.6)
cooling_coil_setpoint_at_outdoor_dry_bulb_high [number] (Default: 12.8)
cooling_coil_reset_outdoor_dry_bulb_high [number] (Default: 23.3)
heating_coil_type [string] (Default: HotWater)
heating_coil_availability_schedule_name [string]
heating_coil_setpoint_control_type [string] (Default: FixedSetpoint)
heating_coil_design_setpoint [number] (Default: 50.0)
heating_coil_setpoint_schedule_name [string]
heating_coil_setpoint_at_outdoor_dry_bulb_low [number] (Default: 50.0)
heating_coil_reset_outdoor_dry_bulb_low [number] (Default: 7.8)
heating_coil_setpoint_at_outdoor_dry_bulb_high [number] (Default: 20.0)
heating_coil_reset_outdoor_dry_bulb_high [number] (Default: 12.2)
heating_coil_capacity [unknown field type] (Default: Autosize)
gas_heating_coil_efficiency [number] (Default: 0.8)
gas_heating_coil_parasitic_electric_load [number] (Default: 0.0)
preheat_coil_type [string] (Default: None)
preheat_coil_availability_schedule_name [string]
preheat_coil_design_setpoint [number] (Default: 7.2)
preheat_coil_setpoint_schedule_name [string]
gas_preheat_coil_efficiency [number] (Default: 0.8)
gas_preheat_coil_parasitic_electric_load [number] (Default: 0.0)
maximum_outdoor_air_flow_rate [unknown field type] (Default: Autosize)
minimum_outdoor_air_flow_rate [unknown field type] (Default: Autosize)
minimum_outdoor_air_control_type [string] (Default: ProportionalMinimum)
minimum_outdoor_air_schedule_name [string]
economizer_type [string] (Default: NoEconomizer)
economizer_lockout [string] (Default: NoLockout)
economizer_upper_temperature_limit [number]
economizer_lower_temperature_limit [number]
economizer_upper_enthalpy_limit [number]
economizer_maximum_limit_dewpoint_temperature [number]
cold_supply_plenum_name [string]
hot_supply_plenum_name [string]
return_plenum_name [string]
night_cycle_control [string] (Default: StayOff)
night_cycle_control_zone_name [string]
heat_recovery_type [string] (Default: None)
sensible_heat_recovery_effectiveness [number] (Default: 0.7)
latent_heat_recovery_effectiveness [number] (Default: 0.65)
heat_recovery_heat_exchanger_type [string] (Default: Plate)
heat_recovery_frost_control_type [string] (Default: None)
dehumidification_control_type [string] (Default: None)
dehumidification_control_zone_name [string]
dehumidification_relative_humidity_setpoint [number] (Default: 60.0)
dehumidification_relative_humidity_setpoint_schedule_name [string]
humidifier_type [string] (Default: None)
humidifier_availability_schedule_name [string]
humidifier_rated_capacity [number] (Default: 1e-06)
humidifier_rated_electric_power [unknown field type] (Default: Autosize)
humidifier_control_zone_name [string]
humidifier_relative_humidity_setpoint [number] (Default: 30.0)
humidifier_relative_humidity_setpoint_schedule_name [string]
sizing_option [string] (Default: NonCoincident)
return_fan [string] (Default: No)
return_fan_total_efficiency [number] (Default: 0.7)
return_fan_delta_pressure [number] (Default: 500.0)
return_fan_motor_efficiency [number] (Default: 0.9)
return_fan_motor_in_air_stream_fraction [number] (Default: 1.0)
return_fan_part_load_power_coefficients [string] (Default: InletVaneDampers)
HVACTemplate:System:DedicatedOutdoorAir
This object creates a dedicated outdoor air system that must be used with HVACTemplate:Zone:* objects for BaseboardHeat FanCoil PTAC PTHP WaterToAirHeatPump and VRF. Does not support HVACTemplate:Zone:VAV or other central multizone systems

Fields

system_availability_schedule_name [string]
air_outlet_type [string] (Default: DirectIntoZone)
supply_fan_flow_rate [unknown field type] (Default: Autosize)
supply_fan_total_efficiency [number] (Default: 0.7)
supply_fan_delta_pressure [number] (Default: 1000.0)
supply_fan_motor_efficiency [number] (Default: 0.9)
supply_fan_motor_in_air_stream_fraction [number] (Default: 1.0)
supply_fan_placement [string] (Default: DrawThrough)
cooling_coil_type [string] (Default: ChilledWater)
cooling_coil_availability_schedule_name [string]
cooling_coil_setpoint_control_type [string] (Default: FixedSetpoint)
cooling_coil_design_setpoint [number] (Default: 12.8)
cooling_coil_setpoint_schedule_name [string]
cooling_coil_setpoint_at_outdoor_dry_bulb_low [number] (Default: 15.6)
cooling_coil_reset_outdoor_dry_bulb_low [number] (Default: 15.6)
cooling_coil_setpoint_at_outdoor_dry_bulb_high [number] (Default: 12.8)
cooling_coil_reset_outdoor_dry_bulb_high [number] (Default: 23.3)
dx_cooling_coil_gross_rated_total_capacity [unknown field type] (Default: Autosize)
dx_cooling_coil_gross_rated_sensible_heat_ratio [unknown field type] (Default: Autosize)
dx_cooling_coil_gross_rated_cop [number] (Default: 3.0)
heating_coil_type [string] (Default: HotWater)
heating_coil_availability_schedule_name [string]
heating_coil_setpoint_control_type [string] (Default: FixedSetpoint)
heating_coil_design_setpoint [number] (Default: 12.2)
heating_coil_setpoint_schedule_name [string]
heating_coil_setpoint_at_outdoor_dry_bulb_low [number] (Default: 15.0)
heating_coil_reset_outdoor_dry_bulb_low [number] (Default: 7.8)
heating_coil_setpoint_at_outdoor_dry_bulb_high [number] (Default: 12.2)
heating_coil_reset_outdoor_dry_bulb_high [number] (Default: 12.2)
gas_heating_coil_efficiency [number] (Default: 0.8)
gas_heating_coil_parasitic_electric_load [number] (Default: 0.0)
heat_recovery_type [string] (Default: None)
heat_recovery_sensible_effectiveness [number] (Default: 0.7)
heat_recovery_latent_effectiveness [number] (Default: 0.65)
heat_recovery_heat_exchanger_type [string] (Default: Plate)
heat_recovery_frost_control_type [string] (Default: None)
dehumidification_control_type [string] (Default: None)
dehumidification_setpoint [number] (Default: 0.00924)
humidifier_type [string] (Default: None)
humidifier_availability_schedule_name [string]
humidifier_rated_capacity [number] (Default: 1e-06)
humidifier_rated_electric_power [unknown field type] (Default: Autosize)
humidifier_constant_setpoint [number] (Default: 0.003)
dehumidification_setpoint_schedule_name [string]
humidifier_setpoint_schedule_name [string]
HVACTemplate:Plant:ChilledWaterLoop
Plant and condenser loops to serve all HVACTemplate chilled water coils, chillers, and towers.

Fields

pump_schedule_name [string]
pump_control_type [string] (Default: Intermittent)
chiller_plant_operation_scheme_type [string] (Default: Default)
chiller_plant_equipment_operation_schemes_name [string]
chilled_water_setpoint_schedule_name [string]
chilled_water_design_setpoint [number] (Default: 7.22)
chilled_water_pump_configuration [string] (Default: ConstantPrimaryNoSecondary)
primary_chilled_water_pump_rated_head [number] (Default: 179352.0)
secondary_chilled_water_pump_rated_head [number] (Default: 179352.0)
condenser_plant_operation_scheme_type [string] (Default: Default)
condenser_equipment_operation_schemes_name [string]
condenser_water_temperature_control_type [string]
condenser_water_setpoint_schedule_name [string]
condenser_water_design_setpoint [number] (Default: 29.4)
condenser_water_pump_rated_head [number] (Default: 179352.0)
chilled_water_setpoint_reset_type [string] (Default: None)
chilled_water_setpoint_at_outdoor_dry_bulb_low [number] (Default: 12.2)
chilled_water_reset_outdoor_dry_bulb_low [number] (Default: 15.6)
chilled_water_setpoint_at_outdoor_dry_bulb_high [number] (Default: 6.7)
chilled_water_reset_outdoor_dry_bulb_high [number] (Default: 26.7)
chilled_water_primary_pump_type [string] (Default: SinglePump)
chilled_water_secondary_pump_type [string] (Default: SinglePump)
condenser_water_pump_type [string] (Default: SinglePump)
chilled_water_supply_side_bypass_pipe [string] (Default: Yes)
chilled_water_demand_side_bypass_pipe [string] (Default: Yes)
condenser_water_supply_side_bypass_pipe [string] (Default: Yes)
condenser_water_demand_side_bypass_pipe [string] (Default: Yes)
fluid_type [string] (Default: Water)
loop_design_delta_temperature [number] (Default: 6.67)
minimum_outdoor_dry_bulb_temperature [number]
chilled_water_load_distribution_scheme [string] (Default: SequentialLoad)
condenser_water_load_distribution_scheme [string] (Default: SequentialLoad)
HVACTemplate:Plant:Chiller
This object adds a chiller to an HVACTemplate:Plant:ChilledWaterLoop.

Fields

chiller_type [string]
capacity [unknown field type] (Default: Autosize)
nominal_cop [number]
condenser_type [string] (Default: WaterCooled)
priority [string]
sizing_factor [number] (Default: 1.0)
minimum_part_load_ratio [number] (Default: 0.0)
maximum_part_load_ratio [number] (Default: 1.0)
optimum_part_load_ratio [number] (Default: 1.0)
minimum_unloading_ratio [number] (Default: 0.25)
leaving_chilled_water_lower_temperature_limit [number] (Default: 5.0)
HVACTemplate:Plant:Chiller:ObjectReference
This object references a detailed chiller object and adds it to an HVACTemplate:Plant:ChilledWaterLoop. The user must create a complete detailed chiller object with all required curve or performance objects.

Fields

chiller_object_type [string] (Default: Chiller:Electric:EIR)
chiller_name [string]
priority [number]
HVACTemplate:Plant:Tower
This object adds a cooling tower to an HVACTemplate:Plant:ChilledWaterLoop or MixedWaterLoop.

Fields

tower_type [string]
high_speed_nominal_capacity [unknown field type] (Default: Autosize)
high_speed_fan_power [unknown field type] (Default: Autosize)
low_speed_nominal_capacity [unknown field type] (Default: Autosize)
low_speed_fan_power [unknown field type] (Default: Autosize)
free_convection_capacity [unknown field type] (Default: Autosize)
priority [string]
sizing_factor [number] (Default: 1.0)
template_plant_loop_type [string]
HVACTemplate:Plant:Tower:ObjectReference
This object references a detailed cooling tower object and adds it to an HVACTemplate:Plant:ChilledWaterLoop or MixedWaterLoop. The user must create a complete detailed cooling tower object with all required curve or performance objects.

Fields

cooling_tower_object_type [string] (Default: CoolingTower:SingleSpeed)
cooling_tower_name [string]
priority [number]
template_plant_loop_type [string]
HVACTemplate:Plant:HotWaterLoop
Plant loop to serve all HVACTemplate hot water coils and boilers.

Fields

pump_schedule_name [string]
pump_control_type [string] (Default: Intermittent)
hot_water_plant_operation_scheme_type [string] (Default: Default)
hot_water_plant_equipment_operation_schemes_name [string]
hot_water_setpoint_schedule_name [string]
hot_water_design_setpoint [number] (Default: 82.0)
hot_water_pump_configuration [string] (Default: ConstantFlow)
hot_water_pump_rated_head [number] (Default: 179352.0)
hot_water_setpoint_reset_type [string] (Default: None)
hot_water_setpoint_at_outdoor_dry_bulb_low [number] (Default: 82.2)
hot_water_reset_outdoor_dry_bulb_low [number] (Default: -6.7)
hot_water_setpoint_at_outdoor_dry_bulb_high [number] (Default: 65.6)
hot_water_reset_outdoor_dry_bulb_high [number] (Default: 10.0)
hot_water_pump_type [string] (Default: SinglePump)
supply_side_bypass_pipe [string] (Default: Yes)
demand_side_bypass_pipe [string] (Default: Yes)
fluid_type [string] (Default: Water)
loop_design_delta_temperature [number] (Default: 11.0)
maximum_outdoor_dry_bulb_temperature [number]
load_distribution_scheme [string] (Default: SequentialLoad)
HVACTemplate:Plant:Boiler
This object adds a boiler to an HVACTemplate:Plant:HotWaterLoop or MixedWaterLoop.

Fields

boiler_type [string]
capacity [unknown field type] (Default: Autosize)
efficiency [number] (Default: 0.8)
fuel_type [string]
priority [string]
sizing_factor [number] (Default: 1.0)
minimum_part_load_ratio [number] (Default: 0.0)
maximum_part_load_ratio [number] (Default: 1.1)
optimum_part_load_ratio [number] (Default: 1.0)
water_outlet_upper_temperature_limit [number] (Default: 100.0)
template_plant_loop_type [string]
HVACTemplate:Plant:Boiler:ObjectReference
This object references a detailed boiler object and adds it to an HVACTemplate:Plant:HotWaterLoop or MixedWaterLoop. The user must create a complete detailed boiler object with all required curve or performance objects.

Fields

boiler_object_type [string] (Default: Boiler:HotWater)
boiler_name [string]
priority [number]
template_plant_loop_type [string]
HVACTemplate:Plant:MixedWaterLoop
Central plant loop portion of a water source heat pump system.

Fields

pump_schedule_name [string]
pump_control_type [string] (Default: Intermittent)
operation_scheme_type [string] (Default: Default)
equipment_operation_schemes_name [string]
high_temperature_setpoint_schedule_name [string]
high_temperature_design_setpoint [number] (Default: 33.0)
low_temperature_setpoint_schedule_name [string]
low_temperature_design_setpoint [number] (Default: 20.0)
water_pump_configuration [string] (Default: ConstantFlow)
water_pump_rated_head [number] (Default: 179352.0)
water_pump_type [string] (Default: SinglePump)
supply_side_bypass_pipe [string] (Default: Yes)
demand_side_bypass_pipe [string] (Default: Yes)
fluid_type [string] (Default: Water)
loop_design_delta_temperature [number] (Default: 5.6)
load_distribution_scheme [string] (Default: SequentialLoad)
"""