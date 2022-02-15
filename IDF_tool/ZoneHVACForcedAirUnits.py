"""
# Zone HVAC Forced Air Units
"""
class ZoneHVAC_IdealLoadsAirSystem():
    
    def availability_schedule_name(epJSON, ObjectName, data=str):
        epJSON["ZoneHVAC:IdealLoadsAirSystem"][ ObjectName]["availability_schedule_name"] = data
        return epJSON
    
    def cooling_limit(epJSON, ObjectName, data=str):
        epJSON["ZoneHVAC:IdealLoadsAirSystem"][ ObjectName]["cooling_limit"] = data
        return epJSON

    def dehumidification_control_type(epJSON, ObjectName, data=str):
        epJSON["ZoneHVAC:IdealLoadsAirSystem"][ ObjectName]["dehumidification_control_type"] = data
        return epJSON

    def heating_limit(epJSON, ObjectName, data=str):
        epJSON["ZoneHVAC:IdealLoadsAirSystem"][ ObjectName]["heating_limit"] = data
        return epJSON

    def humidification_control_type(epJSON, ObjectName, data=str):
        epJSON["ZoneHVAC:IdealLoadsAirSystem"][ ObjectName]["humidification_control_type"] = data
        return epJSON

    def maximum_heating_supply_air_humidity_ratio(epJSON, ObjectName, data=bool):
        epJSON["ZoneHVAC:IdealLoadsAirSystem"][ ObjectName]["availability_schedule_name"] = data
        return epJSON

    def maximum_heating_supply_air_temperature(epJSON, ObjectName, data=bool):
        epJSON["ZoneHVAC:IdealLoadsAirSystem"][ ObjectName]["maximum_heating_supply_air_temperature"] = data
        return epJSON

    def maximum_sensible_heating_capacity(epJSON, ObjectName, data=bool):
        epJSON["ZoneHVAC:IdealLoadsAirSystem"][ ObjectName]["maximum_sensible_heating_capacity"] = data
        return epJSON

    def maximum_total_cooling_capacity(epJSON, ObjectName, data=bool):
        epJSON["ZoneHVAC:IdealLoadsAirSystem"][ ObjectName]["maximum_total_cooling_capacity"] = data
        return epJSON

    def minimum_cooling_supply_air_humidity_ratio(epJSON, ObjectName, data=bool):
        epJSON["ZoneHVAC:IdealLoadsAirSystem"][ ObjectName]["minimum_cooling_supply_air_humidity_ratio"] = data
        return epJSON

    def minimum_cooling_supply_air_temperature(epJSON, ObjectName, data=bool):
        epJSON["ZoneHVAC:IdealLoadsAirSystem"][ ObjectName]["minimum_cooling_supply_air_temperature"] = data
        return epJSON

    def zone_supply_air_node_name(epJSON, ObjectName, data=str):
        epJSON["ZoneHVAC:IdealLoadsAirSystem"][ ObjectName]["zone_supply_air_node_name"] = data
        return epJSON
    

"""

ZoneHVAC:FourPipeFanCoil
Four pipe fan coil system. Forced-convection hydronic heating-cooling unit with supply fan, hot water heating coil, chilled water cooling coil, and fixed-position outdoor air mixer.

Fields

availability_schedule_name [data]
capacity_control_method [data]
maximum_supply_air_flow_rate [unknown field type]
low_speed_supply_air_flow_ratio [data] (Default: 0.33)
medium_speed_supply_air_flow_ratio [data] (Default: 0.66)
maximum_outdoor_air_flow_rate [unknown field type]
outdoor_air_schedule_name [data]
air_inlet_node_name [data]
air_outlet_node_name [data]
outdoor_air_mixer_object_type [data]
outdoor_air_mixer_name [data]
supply_air_fan_object_type [data]
supply_air_fan_name [data]
cooling_coil_object_type [data]
cooling_coil_name [data]
maximum_cold_water_flow_rate [unknown field type]
minimum_cold_water_flow_rate [data] (Default: 0.0)
cooling_convergence_tolerance [data] (Default: 0.001)
heating_coil_object_type [data]
heating_coil_name [data]
maximum_hot_water_flow_rate [unknown field type]
minimum_hot_water_flow_rate [data] (Default: 0.0)
heating_convergence_tolerance [data] (Default: 0.001)
availability_manager_list_name [data]
design_specification_zonehvac_sizing_object_name [data]
supply_air_fan_operating_mode_schedule_name [data]
minimum_supply_air_temperature_in_cooling_mode [unknown field type] (Default: Autosize)
maximum_supply_air_temperature_in_heating_mode [unknown field type] (Default: Autosize)
ZoneHVAC:WindowAirConditioner
Window air conditioner. Forced-convection cooling-only unit with supply fan, direct expansion (DX) cooling coil, and fixed-position outdoor air mixer.

Fields

availability_schedule_name [data]
maximum_supply_air_flow_rate [unknown field type]
maximum_outdoor_air_flow_rate [unknown field type]
air_inlet_node_name [data]
air_outlet_node_name [data]
outdoor_air_mixer_object_type [data]
outdoor_air_mixer_name [data]
supply_air_fan_object_type [data]
supply_air_fan_name [data]
cooling_coil_object_type [data]
dx_cooling_coil_name [data]
supply_air_fan_operating_mode_schedule_name [data]
fan_placement [data]
cooling_convergence_tolerance [data] (Default: 0.001)
availability_manager_list_name [data]
design_specification_zonehvac_sizing_object_name [data]
ZoneHVAC:PackagedTerminalAirConditioner
Packaged terminal air conditioner (PTAC). Forced-convection heating-cooling unit with supply fan, direct expansion (DX) cooling coil, heating coil (gas, electric, hot water, or steam) and fixed-position outdoor air mixer.

Fields

availability_schedule_name [data]
air_inlet_node_name [data]
air_outlet_node_name [data]
outdoor_air_mixer_object_type [data]
outdoor_air_mixer_name [data]
cooling_supply_air_flow_rate [unknown field type]
heating_supply_air_flow_rate [unknown field type]
no_load_supply_air_flow_rate [unknown field type]
cooling_outdoor_air_flow_rate [unknown field type]
heating_outdoor_air_flow_rate [unknown field type]
no_load_outdoor_air_flow_rate [unknown field type]
supply_air_fan_object_type [data]
supply_air_fan_name [data]
heating_coil_object_type [data]
heating_coil_name [data]
cooling_coil_object_type [data]
cooling_coil_name [data]
fan_placement [data] (Default: DrawThrough)
supply_air_fan_operating_mode_schedule_name [data]
availability_manager_list_name [data]
design_specification_zonehvac_sizing_object_name [data]
capacity_control_method [data] (Default: None)
minimum_supply_air_temperature_in_cooling_mode [unknown field type] (Default: Autosize)
maximum_supply_air_temperature_in_heating_mode [unknown field type] (Default: Autosize)
ZoneHVAC:PackagedTerminalHeatPump
Packaged terminal heat pump (PTHP). Forced-convection heating-cooling unit with supply fan, direct expansion (DX) cooling coil, DX heating coil (air-to-air heat pump), supplemental heating coil (gas, electric, hot water, or steam), and fixed-position outdoor air mixer.

Fields

availability_schedule_name [data]
air_inlet_node_name [data]
air_outlet_node_name [data]
outdoor_air_mixer_object_type [data]
outdoor_air_mixer_name [data]
cooling_supply_air_flow_rate [unknown field type]
heating_supply_air_flow_rate [unknown field type]
no_load_supply_air_flow_rate [unknown field type]
cooling_outdoor_air_flow_rate [unknown field type]
heating_outdoor_air_flow_rate [unknown field type]
no_load_outdoor_air_flow_rate [unknown field type]
supply_air_fan_object_type [data]
supply_air_fan_name [data]
heating_coil_object_type [data]
heating_coil_name [data]
heating_convergence_tolerance [data] (Default: 0.001)
cooling_coil_object_type [data]
cooling_coil_name [data]
cooling_convergence_tolerance [data] (Default: 0.001)
supplemental_heating_coil_object_type [data]
supplemental_heating_coil_name [data]
maximum_supply_air_temperature_from_supplemental_heater [unknown field type]
maximum_outdoor_dry_bulb_temperature_for_supplemental_heater_operation [data] (Default: 21.0)
fan_placement [data] (Default: DrawThrough)
supply_air_fan_operating_mode_schedule_name [data]
availability_manager_list_name [data]
design_specification_zonehvac_sizing_object_name [data]
capacity_control_method [data] (Default: None)
minimum_supply_air_temperature_in_cooling_mode [unknown field type] (Default: Autosize)
maximum_supply_air_temperature_in_heating_mode [unknown field type] (Default: Autosize)
ZoneHVAC:WaterToAirHeatPump
Water-to-air heat pump. Forced-convection heating-cooling unit with supply fan, water-to-air cooling and heating coils, supplemental heating coil (gas, electric, hot water, or steam), and fixed-position outdoor air mixer.

Fields

availability_schedule_name [data]
air_inlet_node_name [data]
air_outlet_node_name [data]
outdoor_air_mixer_object_type [data]
outdoor_air_mixer_name [data]
cooling_supply_air_flow_rate [unknown field type]
heating_supply_air_flow_rate [unknown field type]
no_load_supply_air_flow_rate [unknown field type]
cooling_outdoor_air_flow_rate [unknown field type]
heating_outdoor_air_flow_rate [unknown field type]
no_load_outdoor_air_flow_rate [unknown field type]
supply_air_fan_object_type [data]
supply_air_fan_name [data]
heating_coil_object_type [data]
heating_coil_name [data]
cooling_coil_object_type [data]
cooling_coil_name [data]
maximum_cycling_rate [data] (Default: 2.5)
heat_pump_time_constant [data] (Default: 60.0)
fraction_of_on_cycle_power_use [data] (Default: 0.01)
heat_pump_fan_delay_time [data] (Default: 60.0)
supplemental_heating_coil_object_type [data]
supplemental_heating_coil_name [data]
maximum_supply_air_temperature_from_supplemental_heater [unknown field type] (Default: Autosize)
maximum_outdoor_dry_bulb_temperature_for_supplemental_heater_operation [data] (Default: 21.0)
outdoor_dry_bulb_temperature_sensor_node_name [data]
fan_placement [data] (Default: BlowThrough)
supply_air_fan_operating_mode_schedule_name [data]
availability_manager_list_name [data]
heat_pump_coil_water_flow_mode [data] (Default: Cycling)
design_specification_zonehvac_sizing_object_name [data]
ZoneHVAC:Dehumidifier:DX
This object calculates the performance of zone (room) air dehumidifiers. Meant to model conventional direct expansion (DX) cooling-based room air dehumidifiers (reject 100% of condenser heat to the zone air), but this object might be able to be used to model other room air dehumidifier types.

Fields

availability_schedule_name [data]
air_inlet_node_name [data]
air_outlet_node_name [data]
rated_water_removal [data]
rated_energy_factor [data]
rated_air_flow_rate [data]
water_removal_curve_name [data]
energy_factor_curve_name [data]
part_load_fraction_correlation_curve_name [data]
minimum_dry_bulb_temperature_for_dehumidifier_operation [data] (Default: 10.0)
maximum_dry_bulb_temperature_for_dehumidifier_operation [data] (Default: 35.0)
off_cycle_parasitic_electric_load [data] (Default: 0.0)
condensate_collection_water_storage_tank_name [data]
ZoneHVAC:EnergyRecoveryVentilator
This compound component models a stand-alone energy recovery ventilator (ERV) that conditions outdoor ventilation air and supplies that air directly to a zone. The ERV unit is modeled as a collection of components: air-to-air heat exchanger, supply air fan, exhaust air fan and an optional controller to avoid overheating of the supply air (economizer or free cooling operation).

Fields

availability_schedule_name [data]
heat_exchanger_name [data]
supply_air_flow_rate [unknown field type]
exhaust_air_flow_rate [unknown field type]
supply_air_fan_name [data]
exhaust_air_fan_name [data]
controller_name [data]
ventilation_rate_per_unit_floor_area [data]
ventilation_rate_per_occupant [data]
availability_manager_list_name [data]
ZoneHVAC:EnergyRecoveryVentilator:Controller
This controller is used exclusively by the ZoneHVAC:EnergyRecoveryVentilator object to allow economizer (free cooling) operation when possible.

Fields

temperature_high_limit [data]
temperature_low_limit [data]
enthalpy_high_limit [data]
dewpoint_temperature_limit [data]
electronic_enthalpy_limit_curve_name [data]
exhaust_air_temperature_limit [data] (Default: NoExhaustAirTemperatureLimit)
exhaust_air_enthalpy_limit [data] (Default: NoExhaustAirEnthalpyLimit)
time_of_day_economizer_flow_control_schedule_name [data]
high_humidity_control_flag [data] (Default: No)
humidistat_control_zone_name [data]
high_humidity_outdoor_air_flow_ratio [data] (Default: 1.0)
control_high_indoor_humidity_based_on_outdoor_humidity_ratio [data] (Default: Yes)
ZoneHVAC:UnitVentilator
Unit ventilator. Forced-convection ventilation unit with supply fan (constant-volume or variable-volume), optional chilled water cooling coil, optional heating coil (gas, electric, hot water, or steam) and controllable outdoor air mixer.

Fields

availability_schedule_name [data]
maximum_supply_air_flow_rate [unknown field type]
outdoor_air_control_type [data]
minimum_outdoor_air_flow_rate [unknown field type]
minimum_outdoor_air_schedule_name [data]
maximum_outdoor_air_flow_rate [unknown field type]
maximum_outdoor_air_fraction_or_temperature_schedule_name [data]
air_inlet_node_name [data]
air_outlet_node_name [data]
outdoor_air_node_name [data]
exhaust_air_node_name [data]
mixed_air_node_name [data]
supply_air_fan_object_type [data]
supply_air_fan_name [data]
coil_option [data]
supply_air_fan_operating_mode_schedule_name [data]
heating_coil_object_type [data]
heating_coil_name [data]
heating_convergence_tolerance [data] (Default: 0.001)
cooling_coil_object_type [data]
cooling_coil_name [data]
cooling_convergence_tolerance [data] (Default: 0.001)
availability_manager_list_name [data]
design_specification_zonehvac_sizing_object_name [data]
ZoneHVAC:UnitHeater
Unit heater. Forced-convection heating-only unit with supply fan, heating coil (gas, electric, hot water, or steam) and fixed-position outdoor air mixer.

Fields

availability_schedule_name [data]
air_inlet_node_name [data]
air_outlet_node_name [data]
supply_air_fan_object_type [data]
supply_air_fan_name [data]
maximum_supply_air_flow_rate [unknown field type]
heating_coil_object_type [data]
heating_coil_name [data]
supply_air_fan_operating_mode_schedule_name [data]
supply_air_fan_operation_during_no_heating [data]
maximum_hot_water_or_steam_flow_rate [unknown field type]
minimum_hot_water_or_steam_flow_rate [data] (Default: 0.0)
heating_convergence_tolerance [data] (Default: 0.001)
availability_manager_list_name [data]
design_specification_zonehvac_sizing_object_name [data]
ZoneHVAC:EvaporativeCoolerUnit
Zone evaporative cooler. Forced-convection cooling-only unit with supply fan, 100% outdoor air supply. Optional relief exhaust node

Fields

availability_schedule_name [data]
availability_manager_list_name [data]
outdoor_air_inlet_node_name [data]
cooler_outlet_node_name [data]
zone_relief_air_node_name [data]
supply_air_fan_object_type [data]
supply_air_fan_name [data]
design_supply_air_flow_rate [unknown field type]
fan_placement [data]
cooler_unit_control_method [data]
throttling_range_temperature_difference [data] (Default: 1.0)
cooling_load_control_threshold_heat_transfer_rate [data] (Default: 100.0)
first_evaporative_cooler_object_type [data]
first_evaporative_cooler_object_name [data]
second_evaporative_cooler_object_type [data]
second_evaporative_cooler_name [data]
design_specification_zonehvac_sizing_object_name [data]
ZoneHVAC:HybridUnitaryHVAC
Hybrid Unitary HVAC. A black box model for multi-mode packaged forced air equipment. Independent variables include outdoor air conditions and indoor air conditions. Controlled inputs include operating mode, supply air flow rate, and outdoor air faction. Emperical lookup tables are required to map supply air temperature supply air humidity, electricity use, fuel uses, water use, fan electricity use, and external static pressure as a function of each indpednent varaible and each controlled input. In each timestep the model will choose one or more combinations of settings for mode, supply air flow rate, outdoor air faction, and part runtime fraction so as to satisfy zone requests for sensible cooling, heating, ventilation, and/or dehumidification with the least resource consumption. Equipment in this class may consume electricity, water, and up to two additional fuel types.

Fields

availability_schedule_name [data]
availability_manager_list_name [data]
minimum_supply_air_temperature_schedule_name [data]
maximum_supply_air_temperature_schedule_name [data]
minimum_supply_air_humidity_ratio_schedule_name [data]
maximum_supply_air_humidity_ratio_schedule_name [data]
method_to_choose_controlled_inputs_and_part_runtime_fraction [data] (Default: Automatic)
return_air_node_name [data]
outdoor_air_node_name [data]
supply_air_node_name [data]
relief_node_name [data]
system_maximum_supply_air_flow_rate [data]
external_static_pressure_at_system_maximum_supply_air_flow_rate [data]
fan_heat_included_in_lookup_tables [data] (Default: No)
fan_heat_gain_location [data] (Default: SupplyAirStream)
fan_heat_in_air_stream_fraction [data] (Default: 1.0)
scaling_factor [data] (Default: 1.0)
minimum_time_between_mode_change [data] (Default: 10.0)
first_fuel_type [data] (Default: Electricity)
second_fuel_type [data] (Default: None)
third_fuel_type [data] (Default: None)
objective_function_to_minimize [data] (Default: Electricity Use)
design_specification_outdoor_air_object_name [data]
mode_0_name [data]
mode_0_supply_air_temperature_lookup_table_name [data]
mode_0_supply_air_humidity_ratio_lookup_table_name [data]
mode_0_system_electric_power_lookup_table_name [data]
mode_0_supply_fan_electric_power_lookup_table_name [data]
mode_0_external_static_pressure_lookup_table_name [data]
mode_0_system_second_fuel_consumption_lookup_table_name [data]
mode_0_system_third_fuel_consumption_lookup_table_name [data]
mode_0_system_water_use_lookup_table_name [data]
mode_0_outdoor_air_fraction [data] (Default: 0.0)
mode_0_supply_air_mass_flow_rate_ratio [data] (Default: 0.0)
modes [Array of {mode_name, mode_supply_air_temperature_lookup_table_name, mode_supply_air_humidity_ratio_lookup_table_name, mode_system_electric_power_lookup_table_name, mode_supply_fan_electric_power_lookup_table_name, mode_external_static_pressure_lookup_table_name, mode_system_second_fuel_consumption_lookup_table_name, mode_system_third_fuel_consumption_lookup_table_name, mode_system_water_use_lookup_table_name, mode_minimum_outdoor_air_temperature, mode_maximum_outdoor_air_temperature, mode_minimum_outdoor_air_humidity_ratio, mode_maximum_outdoor_air_humidity_ratio, mode_minimum_outdoor_air_relative_humidity, mode_maximum_outdoor_air_relative_humidity, mode_minimum_return_air_temperature, mode_maximum_return_air_temperature, mode_minimum_return_air_humidity_ratio, mode_maximum_return_air_humidity_ratio, mode_minimum_return_air_relative_humidity, mode_maximum_return_air_relative_humidity, mode_minimum_outdoor_air_fraction, mode_maximum_outdoor_air_fraction, mode_minimum_supply_air_mass_flow_rate_ratio, mode_maximum_supply_air_mass_flow_rate_ratio}]
ZoneHVAC:OutdoorAirUnit
The zone outdoor air unit models a single-zone dedicated outdoor air system (DOAS). Forced-convection 100% outdoor air unit with supply fan and optional equipment including exhaust fan, heating coil, cooling coil, and heat recovery.

Fields

availability_schedule_name [data]
zone_name [data]
outdoor_air_flow_rate [unknown field type]
outdoor_air_schedule_name [data]
supply_fan_name [data]
supply_fan_placement [data] (Default: DrawThrough)
exhaust_fan_name [data]
exhaust_air_flow_rate [unknown field type]
exhaust_air_schedule_name [data]
unit_control_type [data] (Default: NeutralControl)
high_air_control_temperature_schedule_name [data]
low_air_control_temperature_schedule_name [data]
outdoor_air_node_name [data]
airoutlet_node_name [data]
airinlet_node_name [data]
supply_fanoutlet_node_name [data]
outdoor_air_unit_list_name [data]
availability_manager_list_name [data]
ZoneHVAC:OutdoorAirUnit:EquipmentList
Equipment list for components in a ZoneHVAC:OutdoorAirUnit. Components are simulated sequentially in the order given in the equipment list.

Fields

component_1_object_type [data]
component_1_name [data]
component_2_object_type [data]
component_2_name [data]
component_3_object_type [data]
component_3_name [data]
component_4_object_type [data]
component_4_name [data]
component_5_object_type [data]
component_5_name [data]
component_6_object_type [data]
component_6_name [data]
component_7_object_type [data]
component_7_name [data]
component_8_object_type [data]
component_8_name [data]
ZoneHVAC:TerminalUnit:VariableRefrigerantFlow
A terminal unit with variable refrigerant flow (VRF) DX cooling and heating coils (air-to-air heat pump). The VRF terminal units are served by an AirConditioner:VariableRefrigerantFlow or AirConditioner:VariableRefrigerantFlow:FluidTemperatureControl:* system. Terminal units can be configured as zone, air loop or outside air system equipment.

Fields

terminal_unit_availability_schedule [data]
terminal_unit_air_inlet_node_name [data]
terminal_unit_air_outlet_node_name [data]
cooling_supply_air_flow_rate [unknown field type]
no_cooling_supply_air_flow_rate [unknown field type]
heating_supply_air_flow_rate [unknown field type]
no_heating_supply_air_flow_rate [unknown field type]
cooling_outdoor_air_flow_rate [unknown field type]
heating_outdoor_air_flow_rate [unknown field type]
no_load_outdoor_air_flow_rate [unknown field type]
supply_air_fan_operating_mode_schedule_name [data]
supply_air_fan_placement [data] (Default: BlowThrough)
supply_air_fan_object_type [data] (Default: Fan:ConstantVolume)
supply_air_fan_object_name [data]
outside_air_mixer_object_type [data]
outside_air_mixer_object_name [data]
cooling_coil_object_type [data]
cooling_coil_object_name [data]
heating_coil_object_type [data]
heating_coil_object_name [data]
zone_terminal_unit_on_parasitic_electric_energy_use [data] (Default: 0.0)
zone_terminal_unit_off_parasitic_electric_energy_use [data] (Default: 0.0)
rated_heating_capacity_sizing_ratio [data] (Default: 1.0)
availability_manager_list_name [data]
design_specification_zonehvac_sizing_object_name [data]
supplemental_heating_coil_object_type [data]
supplemental_heating_coil_name [data]
maximum_supply_air_temperature_from_supplemental_heater [unknown field type] (Default: Autosize)
maximum_outdoor_dry_bulb_temperature_for_supplemental_heater_operation [data] (Default: 21.0)
controlling_zone_or_thermostat_location [data]
"""