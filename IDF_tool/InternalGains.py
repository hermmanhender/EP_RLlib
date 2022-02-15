'''
# Internal Gains

This module contains all the functions for Internal Gains configuration.
'''
class People():
    '''
    Sets internal gains and contaminant rates for occupants in the zone. If a ZoneList, SpaceList, or a Zone comprised of more than one Space is specified then this definition applies to all applicable spaces, and each instance will be named with the Space Name plus this Object Name.
    '''
    def zone_or_zonelist_or_space_or_spacelist_name(epJSON, ObjectName, data=str):
        epJSON["People"][ObjectName]["zone_or_zonelist_or_space_or_spacelist_name"] = data
        return epJSON
    
    def number_of_people_schedule_name(epJSON, ObjectName, data=str):
        epJSON["People"][ObjectName]["number_of_people_schedule_name"] = data
        return epJSON
    
    def number_of_people_calculation_method(epJSON, ObjectName, data="People"):
        epJSON["People"][ObjectName]["number_of_people_calculation_method"] = data
        return epJSON
    
    def number_of_people(epJSON, ObjectName, data=int):
        epJSON["People"][ObjectName]["number_of_people"] = data
        return epJSON
    
    def people_per_floor_area(epJSON, ObjectName, data):
        epJSON["People"][ObjectName]["people_per_floor_area"] = data
        return epJSON
    
    def floor_area_per_person(epJSON, ObjectName, data=str):
        epJSON["People"][ObjectName]["floor_area_per_person"] = data
        return epJSON
    
    def fraction_radiant(epJSON, ObjectName, data=0.3):
        epJSON["People"][ObjectName]["fraction_radiant"] = data
        return epJSON
    
    def sensible_heat_fraction(epJSON, ObjectName, data="Autocalculate"):
        epJSON["People"][ObjectName]["sensible_heat_fraction"] = data
        return epJSON
    
    def activity_level_schedule_name(epJSON, ObjectName, data=str):
        epJSON["People"][ObjectName]["activity_level_schedule_name"] = data
        return epJSON
    
    def carbon_dioxide_generation_rate(epJSON, ObjectName, data=3.82e-08):
        epJSON["People"][ObjectName]["carbon_dioxide_generation_rate"] = data
        return epJSON
    
    def enable_ashrae_55_comfort_warnings(epJSON, ObjectName, data="No"):
        epJSON["People"][ObjectName]["enable_ashrae_55_comfort_warnings"] = data
        return epJSON
    
    def mean_radiant_temperature_calculation_type(epJSON, ObjectName, data="ZoneAveraged"):
        epJSON["People"][ObjectName]["mean_radiant_temperature_calculation_type"] = data
        return epJSON
    
    def surface_name_angle_factor_list_name(epJSON, ObjectName, data=str):
        epJSON["People"][ObjectName]["surface_name_angle_factor_list_name"] = data
        return epJSON
    
    def work_efficiency_schedule_name(epJSON, ObjectName, data=str):
        epJSON["People"][ObjectName]["work_efficiency_schedule_name"] = data
        return epJSON
    
    def clothing_insulation_calculation_method(epJSON, ObjectName, data="ClothingInsulationSchedule"):
        epJSON["People"][ObjectName]["clothing_insulation_calculation_method"] = data
        return epJSON
    
    def clothing_insulation_calculation_method_schedule_name(epJSON, ObjectName, data=str):
        epJSON["People"][ObjectName]["clothing_insulation_calculation_method_schedule_name"] = data
        return epJSON
    
    def clothing_insulation_schedule_name(epJSON, ObjectName, data=str):
        epJSON["People"][ObjectName]["clothing_insulation_schedule_name"] = data
        return epJSON
    
    def air_velocity_schedule_name(epJSON, ObjectName, data=str):
        epJSON["People"][ObjectName]["air_velocity_schedule_name"] = data
        return epJSON
    
    def thermal_comfort_model_1_type(epJSON, ObjectName, data=str):
        epJSON["People"][ObjectName]["thermal_comfort_model_1_type"] = data
        return epJSON
    
    def thermal_comfort_model_2_type(epJSON, ObjectName, data=str):
        epJSON["People"][ObjectName]["thermal_comfort_model_2_type"] = data
        return epJSON
    
    def thermal_comfort_model_3_type(epJSON, ObjectName, data=str):
        epJSON["People"][ObjectName]["thermal_comfort_model_3_type"] = data
        return epJSON
    
    def thermal_comfort_model_4_type(epJSON, ObjectName, data=str):
        epJSON["People"][ObjectName]["thermal_comfort_model_4_type"] = data
        return epJSON
    
    def thermal_comfort_model_5_type(epJSON, ObjectName, data=str):
        epJSON["People"][ObjectName]["thermal_comfort_model_5_type"] = data
        return epJSON
    
    def thermal_comfort_model_6_type(epJSON, ObjectName, data=str):
        epJSON["People"][ObjectName]["thermal_comfort_model_6_type"] = data
        return epJSON
    
    def thermal_comfort_model_7_type(epJSON, ObjectName, data=str):
        epJSON["People"][ObjectName]["thermal_comfort_model_7_type"] = data
        return epJSON
    
    def ankle_level_air_velocity_schedule_name(epJSON, ObjectName, data=str):
        epJSON["People"][ObjectName]["ankle_level_air_velocity_schedule_name"] = data
        return epJSON


class ComfortViewFactorAngles():
    '''
    Used to specify radiant view factors for thermal comfort calculations. Note that the following angle factor fractions must sum up to 1.0 The number of surfaces can be expanded beyond 100, if necessary, by adding more groups to the end of the list.
    '''
    def zone_name(epJSON, ObjectName, data=str):
        epJSON["ComfortViewFactorAngles"][ObjectName]["zone_name"] = data
        return epJSON
    
    def surface_name(epJSON, Objectname, surface_numer=int, data=str):
        '''
        surface_numer must be a int number between 1 and 100.
        '''
        epJSON["ComfortViewFactorAngles"][Objectname]["surface_"+str(surface_numer)+"name"] = data
        return epJSON

    def angle_factor(epJSON, ObjectName, surface_numer=int, data=bool):
        '''
        surface_numer must be a int number between 1 and 100.
        '''
        epJSON["ComfortViewFactorAngles"][ObjectName]["angle_factor_"+str(surface_numer)] = data
        return epJSON
    

class Lights():
    '''
    Sets internal gains for lights in the zone. If a ZoneList, SpaceList, or a Zone comprised of more than one Space is specified then this definition applies to all applicable spaces, and each instance will be named with the Space Name plus this Object Name.
    '''
    def zone_or_zonelist_or_space_or_spacelist_name(epJSON, ObjectName, data=str):
        epJSON["Lights"][ObjectName]["zone_or_zonelist_or_space_or_spacelist_name"] = data
        return epJSON

    def schedule_name(epJSON, ObjectName, data=str):
        epJSON["Lights"][ObjectName]["schedule_name"] = data
        return epJSON

    def design_level_calculation_method(epJSON, ObjectName, data="LightingLevel"):
        epJSON["Lights"][ObjectName]["design_level_calculation_method"] = data
        return epJSON

    def lighting_level(epJSON, ObjectName, data=bool):
        epJSON["Lights"][ObjectName]["lighting_level"] = data
        return epJSON

    def watts_per_zone_floor_area(epJSON, ObjectName, data=bool):
        epJSON["Lights"][ObjectName]["watts_per_zone_floor_area"] = data
        return epJSON

    def watts_per_person(epJSON, ObjectName, data=bool):
        epJSON["Lights"][ObjectName]["watts_per_person"] = data
        return epJSON

    def return_air_fraction(epJSON, ObjectName, data=0.0):
        epJSON["Lights"][ObjectName]["return_air_fraction"] = data
        return epJSON

    def fraction_radiant(epJSON, ObjectName, data=0.0):
        epJSON["Lights"][ObjectName]["fraction_radiant"] = data
        return epJSON

    def fraction_visible(epJSON, ObjectName, data=0.0):
        epJSON["Lights"][ObjectName]["fraction_visible"] = data
        return epJSON

    def fraction_replaceable(epJSON, ObjectName, data=1.0):
        epJSON["Lights"][ObjectName]["fraction_replaceable"] = data
        return epJSON

    def end_use_subcategory(epJSON, ObjectName, data="General"):
        epJSON["Lights"][ObjectName]["end_use_subcategory"] = data
        return epJSON

    def return_air_fraction_calculated_from_plenum_temperature(epJSON, ObjectName, data="No"):
        epJSON["Lights"][ObjectName]["return_air_fraction_calculated_from_plenum_temperature"] = data
        return epJSON

    def return_air_fraction_function_of_plenum_temperature_coefficient_1(epJSON, ObjectName, data=0.0):
        epJSON["Lights"][ObjectName]["return_air_fraction_function_of_plenum_temperature_coefficient_1"] = data
        return epJSON

    def return_air_fraction_function_of_plenum_temperature_coefficient_2(epJSON, ObjectName, data=0.0):
        epJSON["Lights"][ObjectName]["return_air_fraction_function_of_plenum_temperature_coefficient_2"] = data
        return epJSON

    def return_air_heat_gain_node_name(epJSON, ObjectName, data=str):
        epJSON["Lights"][ObjectName]["return_air_heat_gain_node_name"] = data
        return epJSON

    def exhaust_air_heat_gain_node_name(epJSON, ObjectName, data=str):
        epJSON["Lights"][ObjectName]["exhaust_air_heat_gain_node_name"] = data
        return epJSON


class ElectricEquipment():
    '''
    Sets internal gains for electric equipment in the zone. If a ZoneList, SpaceList, or a Zone comprised of more than one Space is specified then this definition applies to all applicable spaces, and each instance will be named with the Space Name plus this Object Name.
    '''
    def zone_or_zonelist_or_space_or_spacelist_name(epJSON, ObjectName, data=str):
        epJSON["ElectricEquipment"][ObjectName]["zone_or_zonelist_or_space_or_spacelist_name"] = data
        return epJSON
    
    def schedule_name(epJSON, ObjectName, data=str):
        epJSON["ElectricEquipment"][ObjectName]["schedule_name"] = data
        return epJSON
    
    def design_level_calculation_method(epJSON, ObjectName, data="EquipmentLevel"):
        epJSON["ElectricEquipment"][ObjectName]["design_level_calculation_method"] = data
        return epJSON
    
    def design_level(epJSON, ObjectName, data=bool):
        epJSON["ElectricEquipment"][ObjectName]["design_level"] = data
        return epJSON
    
    def watts_per_zone_floor_area(epJSON, ObjectName, data=bool):
        epJSON["ElectricEquipment"][ObjectName]["watts_per_zone_floor_area"] = data
        return epJSON
    
    def watts_per_person(epJSON, ObjectName, data=bool):
        epJSON["ElectricEquipment"][ObjectName]["watts_per_person"] = data
        return epJSON
    
    def fraction_latent(epJSON, ObjectName, data=0.0):
        epJSON["ElectricEquipment"][ObjectName]["fraction_latent"] = data
        return epJSON
    
    def fraction_radiant(epJSON, ObjectName, data=0.0):
        epJSON["ElectricEquipment"][ObjectName]["fraction_radiant"] = data
        return epJSON
    
    def fraction_lost(epJSON, ObjectName, data=0.0):
        epJSON["ElectricEquipment"][ObjectName]["fraction_lost"] = data
        return epJSON
    
    def end_use_subcategory(epJSON, ObjectName, data="General"):
        epJSON["ElectricEquipment"][ObjectName]["end_use_subcategory"] = data
        return epJSON
    

class GasEquipment():
    '''
    Sets internal gains and contaminant rates for gas equipment in the zone. If a ZoneList, SpaceList, or a Zone comprised of more than one Space is specified then this definition applies to all applicable spaces, and each instance will be named with the Space Name plus this Object Name.
    '''
    def zone_or_zonelist_or_space_or_spacelist_name(epJSON, ObjectName, data=str):
        epJSON["GasEquipment"][ObjectName]["zone_or_zonelist_or_space_or_spacelist_name"] = data
        return epJSON
    
    def schedule_name(epJSON, ObjectName, data=str):
        epJSON["GasEquipment"][ObjectName]["schedule_name"] = data
        return epJSON
    
    def design_level_calculation_method(epJSON, ObjectName, data="EquipmentLevel"):
        epJSON["GasEquipment"][ObjectName]["design_level_calculation_method"] = data
        return epJSON
    
    def design_level(epJSON, ObjectName, data=bool):
        epJSON["GasEquipment"][ObjectName]["design_level"] = data
        return epJSON
    
    def power_per_zone_floor_area(epJSON, ObjectName, data=bool):
        epJSON["GasEquipment"][ObjectName]["power_per_zone_floor_area"] = data
        return epJSON
    
    def power_per_person(epJSON, ObjectName, data=bool):
        epJSON["GasEquipment"][ObjectName]["power_per_person"] = data
        return epJSON
    
    def fraction_latent(epJSON, ObjectName, data=0.0):
        epJSON["GasEquipment"][ObjectName]["fraction_latent"] = data
        return epJSON
    
    def fraction_radiant(epJSON, ObjectName, data=0.0):
        epJSON["GasEquipment"][ObjectName]["fraction_radiant"] = data
        return epJSON
    
    def fraction_lost(epJSON, ObjectName, data=0.0):
        epJSON["GasEquipment"][ObjectName]["fraction_lost"] = data
        return epJSON
    
    def carbon_dioxide_generation_rate(epJSON, ObjectName, data=0.0):
        epJSON["GasEquipment"][ObjectName]["carbon_dioxide_generation_rate"] = data
        return epJSON
    
    def end_use_subcategory(epJSON, ObjectName, data="General"):
        epJSON["GasEquipment"][ObjectName]["end_use_subcategory"] = data
        return epJSON
    

class HotWaterEquipment():
    '''
    Sets internal gains for hot water equipment in the zone. If a ZoneList, SpaceList, or a Zone comprised of more than one Space is specified then this definition applies to all applicable spaces, and each instance will be named with the Space Name plus this Object Name.
    '''
    def zone_or_zonelist_or_space_or_spacelist_name(epJSON, ObjectName, data=str):
        epJSON["HotWaterEquipment"][ObjectName]["zone_or_zonelist_or_space_or_spacelist_name"] = data
        return epJSON
    
    def schedule_name(epJSON, ObjectName, data=str):
        epJSON["HotWaterEquipment"][ObjectName]["schedule_name"] = data
        return epJSON
    
    def design_level_calculation_method(epJSON, ObjectName, data="EquipmentLevel"):
        epJSON["HotWaterEquipment"][ObjectName]["design_level_calculation_method"] = data
        return epJSON
    
    def design_level(epJSON, ObjectName, data=bool):
        epJSON["HotWaterEquipment"][ObjectName]["design_level"] = data
        return epJSON
    
    def power_per_zone_floor_area(epJSON, ObjectName, data=bool):
        epJSON["HotWaterEquipment"][ObjectName]["power_per_zone_floor_area"] = data
        return epJSON
    
    def power_per_person(epJSON, ObjectName, data=bool):
        epJSON["HotWaterEquipment"][ObjectName]["power_per_person"] = data
        return epJSON
    
    def fraction_latent(epJSON, ObjectName, data=0.0):
        epJSON["HotWaterEquipment"][ObjectName]["fraction_latent"] = data
        return epJSON
    
    def fraction_radiant(epJSON, ObjectName, data=0.0):
        epJSON["HotWaterEquipment"][ObjectName]["fraction_radiant"] = data
        return epJSON
    
    def fraction_lost(epJSON, ObjectName, data=0.0):
        epJSON["HotWaterEquipment"][ObjectName]["fraction_lost"] = data
        return epJSON
    
    def carbon_dioxide_generation_rate(epJSON, ObjectName, data=0.0):
        epJSON["HotWaterEquipment"][ObjectName]["carbon_dioxide_generation_rate"] = data
        return epJSON
    
    def end_use_subcategory(epJSON, ObjectName, data="General"):
        epJSON["HotWaterEquipment"][ObjectName]["end_use_subcategory"] = data
        return epJSON

class SteamEquipment():
    '''
    Sets internal gains for steam equipment in the zone. If a ZoneList, SpaceList, or a Zone comprised of more than one Space is specified then this definition applies to all applicable spaces, and each instance will be named with the Space Name plus this Object Name.
    '''
    def zone_or_zonelist_or_space_or_spacelist_name(epJSON, ObjectName, data=str):
        epJSON["SteamEquipment"][ObjectName]["zone_or_zonelist_or_space_or_spacelist_name"] = data
        return epJSON
    
    def schedule_name(epJSON, ObjectName, data=str):
        epJSON["SteamEquipment"][ObjectName]["schedule_name"] = data
        return epJSON
    
    def design_level_calculation_method(epJSON, ObjectName, data="EquipmentLevel"):
        epJSON["SteamEquipment"][ObjectName]["design_level_calculation_method"] = data
        return epJSON
    
    def design_level(epJSON, ObjectName, data=bool):
        epJSON["SteamEquipment"][ObjectName]["design_level"] = data
        return epJSON
    
    def power_per_zone_floor_area(epJSON, ObjectName, data=bool):
        epJSON["SteamEquipment"][ObjectName]["power_per_zone_floor_area"] = data
        return epJSON
    
    def power_per_person(epJSON, ObjectName, data=bool):
        epJSON["SteamEquipment"][ObjectName]["power_per_person"] = data
        return epJSON
    
    def fraction_latent(epJSON, ObjectName, data=0.0):
        epJSON["SteamEquipment"][ObjectName]["fraction_latent"] = data
        return epJSON
    
    def fraction_radiant(epJSON, ObjectName, data=0.0):
        epJSON["SteamEquipment"][ObjectName]["fraction_radiant"] = data
        return epJSON
    
    def fraction_lost(epJSON, ObjectName, data=0.0):
        epJSON["SteamEquipment"][ObjectName]["fraction_lost"] = data
        return epJSON
    
    def carbon_dioxide_generation_rate(epJSON, ObjectName, data=0.0):
        epJSON["SteamEquipment"][ObjectName]["carbon_dioxide_generation_rate"] = data
        return epJSON
    
    def end_use_subcategory(epJSON, ObjectName, data="General"):
        epJSON["SteamEquipment"][ObjectName]["end_use_subcategory"] = data
        return epJSON

class OtherEquipment():
    '''
    Sets internal gains or losses for “other” equipment in the zone. If a ZoneList, SpaceList, or a Zone comprised of more than one Space is specified then this definition applies to all applicable spaces, and each instance will be named with the Space Name plus this Object Name.
    '''
    def zone_or_zonelist_or_space_or_spacelist_name(epJSON, ObjectName, data=str):
        epJSON["OtherEquipment"][ObjectName]["zone_or_zonelist_or_space_or_spacelist_name"] = data
        return epJSON
    
    def schedule_name(epJSON, ObjectName, data=str):
        epJSON["OtherEquipment"][ObjectName]["schedule_name"] = data
        return epJSON
    
    def design_level_calculation_method(epJSON, ObjectName, data="EquipmentLevel"):
        epJSON["OtherEquipment"][ObjectName]["design_level_calculation_method"] = data
        return epJSON
    
    def design_level(epJSON, ObjectName, data=bool):
        epJSON["OtherEquipment"][ObjectName]["design_level"] = data
        return epJSON
    
    def power_per_zone_floor_area(epJSON, ObjectName, data=bool):
        epJSON["OtherEquipment"][ObjectName]["power_per_zone_floor_area"] = data
        return epJSON
    
    def power_per_person(epJSON, ObjectName, data=bool):
        epJSON["OtherEquipment"][ObjectName]["power_per_person"] = data
        return epJSON
    
    def fraction_latent(epJSON, ObjectName, data=0.0):
        epJSON["OtherEquipment"][ObjectName]["fraction_latent"] = data
        return epJSON
    
    def fraction_radiant(epJSON, ObjectName, data=0.0):
        epJSON["OtherEquipment"][ObjectName]["fraction_radiant"] = data
        return epJSON
    
    def fraction_lost(epJSON, ObjectName, data=0.0):
        epJSON["OtherEquipment"][ObjectName]["fraction_lost"] = data
        return epJSON
    
    def carbon_dioxide_generation_rate(epJSON, ObjectName, data=0.0):
        epJSON["OtherEquipment"][ObjectName]["carbon_dioxide_generation_rate"] = data
        return epJSON
    
    def end_use_subcategory(epJSON, ObjectName, data="General"):
        epJSON["OtherEquipment"][ObjectName]["end_use_subcategory"] = data
        return epJSON

class ElectricEquipment_ITE_AirCooled():
    '''
    This object describes air-cooled electric information technology equipment (ITE) which has variable power consumption as a function of loading and temperature. If a Zone comprised of more than one Space is specified then this definition applies to all applicable spaces, and each instance will be named with the Space Name plus this Object Name.
    '''
    def zone_or_space_name(epJSON, ObjectName, data=str):
        epJSON["ElectricEquipment:ITE:AirCooled"][ObjectName]["zone_or_space_name"] = data
        return epJSON
    
    def air_flow_calculation_method(epJSON, ObjectName, data="FlowFromSystem"):
        epJSON["ElectricEquipment:ITE:AirCooled"][ObjectName]["air_flow_calculation_method"] = data
        return epJSON
    
    def design_power_input_calculation_method(epJSON, ObjectName, data="Watts/Unit"):
        epJSON["ElectricEquipment:ITE:AirCooled"][ObjectName]["design_power_input_calculation_method"] = data
        return epJSON
    
    def watts_per_unit(epJSON, ObjectName, data=bool):
        epJSON["ElectricEquipment:ITE:AirCooled"][ObjectName]["watts_per_unit"] = data
        return epJSON
    
    def number_of_units(epJSON, ObjectName, data=1.0):
        epJSON["ElectricEquipment:ITE:AirCooled"][ObjectName]["number_of_units"] = data
        return epJSON
    
    def watts_per_zone_floor_area(epJSON, ObjectName, data=bool):
        epJSON["ElectricEquipment:ITE:AirCooled"][ObjectName]["watts_per_zone_floor_area"] = data
        return epJSON
    
    def design_power_input_schedule_name(epJSON, ObjectName, data=str):
        epJSON["ElectricEquipment:ITE:AirCooled"][ObjectName]["design_power_input_schedule_name"] = data
        return epJSON
    
    def cpu_loading_schedule_name(epJSON, ObjectName, data=str):
        epJSON["ElectricEquipment:ITE:AirCooled"][ObjectName]["cpu_loading_schedule_name"] = data
        return epJSON
    
    def cpu_power_input_function_of_loading_and_air_temperature_curve_name(epJSON, ObjectName, data=str):
        epJSON["ElectricEquipment:ITE:AirCooled"][ObjectName]["cpu_power_input_function_of_loading_and_air_temperature_curve_name"] = data
        return epJSON
    
    def design_fan_power_input_fraction(epJSON, ObjectName, data=0.0):
        epJSON["ElectricEquipment:ITE:AirCooled"][ObjectName]["design_fan_power_input_fraction"] = data
        return epJSON
    
    def design_fan_air_flow_rate_per_power_input(epJSON, ObjectName, data=bool):
        epJSON["ElectricEquipment:ITE:AirCooled"][ObjectName]["design_fan_air_flow_rate_per_power_input"] = data
        return epJSON
    
    def air_flow_function_of_loading_and_air_temperature_curve_name(epJSON, ObjectName, data=str):
        epJSON["ElectricEquipment:ITE:AirCooled"][ObjectName]["air_flow_function_of_loading_and_air_temperature_curve_name"] = data
        return epJSON
    
    def fan_power_input_function_of_flow_curve_name(epJSON, ObjectName, data=str):
        epJSON["ElectricEquipment:ITE:AirCooled"][ObjectName]["fan_power_input_function_of_flow_curve_name"] = data
        return epJSON
    
    def design_entering_air_temperature(epJSON, ObjectName, data=15.0):
        epJSON["ElectricEquipment:ITE:AirCooled"][ObjectName]["design_entering_air_temperature"] = data
        return epJSON
    
    def environmental_class(epJSON, ObjectName, data="None"):
        epJSON["ElectricEquipment:ITE:AirCooled"][ObjectName]["environmental_class"] = data
        return epJSON
    
    def air_inlet_connection_type(epJSON, ObjectName, data="AdjustedSupply"):
        epJSON["ElectricEquipment:ITE:AirCooled"][ObjectName]["air_inlet_connection_type"] = data
        return epJSON
    
    def air_inlet_room_air_model_node_name(epJSON, ObjectName, data=str):
        epJSON["ElectricEquipment:ITE:AirCooled"][ObjectName]["air_inlet_room_air_model_node_name"] = data
        return epJSON
    
    def air_outlet_room_air_model_node_name(epJSON, ObjectName, data=str):
        epJSON["ElectricEquipment:ITE:AirCooled"][ObjectName]["air_outlet_room_air_model_node_name"] = data
        return epJSON
    
    def supply_air_node_name(epJSON, ObjectName, data=str):
        epJSON["ElectricEquipment:ITE:AirCooled"][ObjectName]["supply_air_node_name"] = data
        return epJSON
    
    def design_recirculation_fraction(epJSON, ObjectName, data=0.0):
        epJSON["ElectricEquipment:ITE:AirCooled"][ObjectName]["design_recirculation_fraction"] = data
        return epJSON
    
    def recirculation_function_of_loading_and_supply_temperature_curve_name(epJSON, ObjectName, data=str):
        epJSON["ElectricEquipment:ITE:AirCooled"][ObjectName]["recirculation_function_of_loading_and_supply_temperature_curve_name"] = data
        return epJSON
    
    def design_electric_power_supply_efficiency(epJSON, ObjectName, data=1.0):
        epJSON["ElectricEquipment:ITE:AirCooled"][ObjectName]["design_electric_power_supply_efficiency"] = data
        return epJSON
    
    def electric_power_supply_efficiency_function_of_part_load_ratio_curve_name(epJSON, ObjectName, data=str):
        epJSON["ElectricEquipment:ITE:AirCooled"][ObjectName]["electric_power_supply_efficiency_function_of_part_load_ratio_curve_name"] = data
        return epJSON
    
    def fraction_of_electric_power_supply_losses_to_zone(epJSON, ObjectName, data=1.0):
        epJSON["ElectricEquipment:ITE:AirCooled"][ObjectName]["fraction_of_electric_power_supply_losses_to_zone"] = data
        return epJSON
    
    def cpu_end_use_subcategory(epJSON, ObjectName, data="ITE-CPU"):
        epJSON["ElectricEquipment:ITE:AirCooled"][ObjectName]["cpu_end_use_subcategory"] = data
        return epJSON
    
    def fan_end_use_subcategory(epJSON, ObjectName, data="ITE-Fans"):
        epJSON["ElectricEquipment:ITE:AirCooled"][ObjectName]["fan_end_use_subcategory"] = data
        return epJSON
    
    def electric_power_supply_end_use_subcategory(epJSON, ObjectName, data="ITE-UPS"):
        epJSON["ElectricEquipment:ITE:AirCooled"][ObjectName]["electric_power_supply_end_use_subcategory"] = data
        return epJSON
    
    def supply_temperature_difference(epJSON, ObjectName, data=bool):
        epJSON["ElectricEquipment:ITE:AirCooled"][ObjectName]["supply_temperature_difference"] = data
        return epJSON
    
    def supply_temperature_difference_schedule(epJSON, ObjectName, data=str):
        epJSON["ElectricEquipment:ITE:AirCooled"][ObjectName]["supply_temperature_difference_schedule"] = data
        return epJSON
    
    def return_temperature_difference(epJSON, ObjectName, data=bool):
        epJSON["ElectricEquipment:ITE:AirCooled"][ObjectName]["return_temperature_difference"] = data
        return epJSON
    
    def return_temperature_difference_schedule(epJSON, ObjectName, data=str):
        epJSON["ElectricEquipment:ITE:AirCooled"][ObjectName]["return_temperature_difference_schedule"] = data
        return epJSON


class ZoneBaseboard_OutdoorTemperatureControlled():
    '''
    Specifies outside temperature-controlled electric baseboard heating. If a ZoneList, SpaceList, or a Zone comprised of more than one Space is specified then this definition applies to all applicable spaces, and each instance will be named with the Space Name plus this Object Name.
    '''
    def zone_or_zonelist_or_space_or_spacelist_name(epJSON, ObjectName, data=str):
        epJSON["ZoneBaseboard:OutdoorTemperatureControlled"][ObjectName]["zone_or_zonelist_or_space_or_spacelist_name"] = data
        return epJSON
    
    def schedule_name(epJSON, ObjectName, data=str):
        epJSON["ZoneBaseboard:OutdoorTemperatureControlled"][ObjectName]["schedule_name"] = data
        return epJSON
    
    def capacity_at_low_temperature(epJSON, ObjectName, data=bool):
        epJSON["ZoneBaseboard:OutdoorTemperatureControlled"][ObjectName]["capacity_at_low_temperature"] = data
        return epJSON
    
    def low_temperature(epJSON, ObjectName, data=bool):
        epJSON["ZoneBaseboard:OutdoorTemperatureControlled"][ObjectName]["low_temperature"] = data
        return epJSON
    
    def capacity_at_high_temperature(epJSON, ObjectName, data=bool):
        epJSON["ZoneBaseboard:OutdoorTemperatureControlled"][ObjectName]["capacity_at_high_temperature"] = data
        return epJSON
    
    def high_temperature(epJSON, ObjectName, data=bool):
        epJSON["ZoneBaseboard:OutdoorTemperatureControlled"][ObjectName]["high_temperature"] = data
        return epJSON
    
    def fraction_radiant(epJSON, ObjectName, data=0.0):
        epJSON["ZoneBaseboard:OutdoorTemperatureControlled"][ObjectName]["fraction_radiant"] = data
        return epJSON
    
    def end_use_subcategory(epJSON, ObjectName, data="General"):
        epJSON["ZoneBaseboard:OutdoorTemperatureControlled"][ObjectName]["end_use_subcategory"] = data
        return epJSON


class SwimmingPool_Indoor():
    '''
    Specifies an indoor swimming pools linked to a floor surface. The pool is assumed to cover the entire floor to which it is linked.
    '''
    def surface_name(epJSON, ObjectName, data=str):
        epJSON["SwimmingPool:Indoor"][ObjectName]["surface_name"] = data
        return epJSON
    
    def average_depth(epJSON, ObjectName, data=bool):
        epJSON["SwimmingPool:Indoor"][ObjectName]["average_depth"] = data
        return epJSON
    
    def activity_factor_schedule_name(epJSON, ObjectName, data=str):
        epJSON["SwimmingPool:Indoor"][ObjectName]["activity_factor_schedule_name"] = data
        return epJSON
    
    def make_up_water_supply_schedule_name(epJSON, ObjectName, data=str):
        epJSON["SwimmingPool:Indoor"][ObjectName]["make_up_water_supply_schedule_name"] = data
        return epJSON
    
    def cover_schedule_name(epJSON, ObjectName, data=str):
        epJSON["SwimmingPool:Indoor"][ObjectName]["cover_schedule_name"] = data
        return epJSON
    
    def cover_evaporation_factor(epJSON, ObjectName, data=0.0):
        epJSON["SwimmingPool:Indoor"][ObjectName]["cover_evaporation_factor"] = data
        return epJSON
    
    def cover_convection_factor(epJSON, ObjectName, data=0.0):
        epJSON["SwimmingPool:Indoor"][ObjectName]["cover_convection_factor"] = data
        return epJSON
    
    def cover_short_wavelength_radiation_factor(epJSON, ObjectName, data=0.0):
        epJSON["SwimmingPool:Indoor"][ObjectName]["cover_short_wavelength_radiation_factor"] = data
        return epJSON
    
    def cover_long_wavelength_radiation_factor(epJSON, ObjectName, data=0.0):
        epJSON["SwimmingPool:Indoor"][ObjectName]["cover_long_wavelength_radiation_factor"] = data
        return epJSON
    
    def pool_water_inlet_node(epJSON, ObjectName, data=str):
        epJSON["SwimmingPool:Indoor"][ObjectName]["pool_water_inlet_node"] = data
        return epJSON
    
    def pool_water_outlet_node(epJSON, ObjectName, data=str):
        epJSON["SwimmingPool:Indoor"][ObjectName]["pool_water_outlet_node"] = data
        return epJSON
    
    def pool_heating_system_maximum_water_flow_rate(epJSON, ObjectName, data=bool):
        epJSON["SwimmingPool:Indoor"][ObjectName]["pool_heating_system_maximum_water_flow_rate"] = data
        return epJSON
    
    def pool_miscellaneous_equipment_power(epJSON, ObjectName, data=bool):
        epJSON["SwimmingPool:Indoor"][ObjectName]["pool_miscellaneous_equipment_power"] = data
        return epJSON
    
    def setpoint_temperature_schedule(epJSON, ObjectName, data=str):
        epJSON["SwimmingPool:Indoor"][ObjectName]["setpoint_temperature_schedule"] = data
        return epJSON
    
    def maximum_number_of_people(epJSON, ObjectName, data=bool):
        epJSON["SwimmingPool:Indoor"][ObjectName]["maximum_number_of_people"] = data
        return epJSON
    
    def people_schedule(epJSON, ObjectName, data=str):
        epJSON["SwimmingPool:Indoor"][ObjectName]["people_schedule"] = data
        return epJSON
    
    def people_heat_gain_schedule(epJSON, ObjectName, data=str):
        epJSON["SwimmingPool:Indoor"][ObjectName]["people_heat_gain_schedule"] = data
        return epJSON
    

class ZoneContaminantSourceAndSink_CarbonDioxide():
    '''
    Represents internal CO2 gains and sinks in the zone.
    '''
    def zone_name(epJSON, ObjectName, data=str):
        epJSON["ZoneContaminantSourceAndSink:CarbonDioxide"][ObjectName]["zone_name"] = data
        return epJSON
    
    def design_generation_rate(epJSON, ObjectName, data=bool):
        epJSON["ZoneContaminantSourceAndSink:CarbonDioxide"][ObjectName]["design_generation_rate"] = data
        return epJSON
    
    def schedule_name(epJSON, ObjectName, data=str):
        epJSON["ZoneContaminantSourceAndSink:CarbonDioxide"][ObjectName]["schedule_name"] = data
        return epJSON


class ZoneContaminantSourceAndSink_Generic_Constant():
    '''
    Sets internal generic contaminant gains and sinks in a zone with constant values.
    '''
    def zone_name(epJSON, ObjectName, data=str):
        epJSON["ZoneContaminantSourceAndSink:Generic:Constant"][ObjectName]["zone_name"] = data
        return epJSON
    
    def design_generation_rate(epJSON, ObjectName, data=bool):
        epJSON["ZoneContaminantSourceAndSink:Generic:Constant"][ObjectName]["design_generation_rate"] = data
        return epJSON
    
    def generation_schedule_name(epJSON, ObjectName, data=str):
        epJSON["ZoneContaminantSourceAndSink:Generic:Constant"][ObjectName]["generation_schedule_name"] = data
        return epJSON
    
    def design_removal_coefficient(epJSON, ObjectName, data=bool):
        epJSON["ZoneContaminantSourceAndSink:Generic:Constant"][ObjectName]["design_removal_coefficient"] = data
        return epJSON
    
    def removal_schedule_name(epJSON, ObjectName, data=str):
        epJSON["ZoneContaminantSourceAndSink:Generic:Constant"][ObjectName]["removal_schedule_name"] = data
        return epJSON
    

class SurfaceContaminantSourceAndSink_Generic_PressureDriven():
    '''
    Simulate generic contaminant source driven by the pressure difference across a surface.
    '''
    def surface_name(epJSON, ObjectName, data=str):
        epJSON["SurfaceContaminantSourceAndSink:Generic:PressureDriven"][ObjectName]["surface_name"] = data
        return epJSON
    
    def design_generation_rate_coefficient(epJSON, ObjectName, data=bool):
        epJSON["SurfaceContaminantSourceAndSink:Generic:PressureDriven"][ObjectName]["design_generation_rate_coefficient"] = data
        return epJSON
    
    def generation_schedule_name(epJSON, ObjectName, data=str):
        epJSON["SurfaceContaminantSourceAndSink:Generic:PressureDriven"][ObjectName]["generation_schedule_name"] = data
        return epJSON
    
    def generation_exponent(epJSON, ObjectName, data=bool):
        epJSON["SurfaceContaminantSourceAndSink:Generic:PressureDriven"][ObjectName]["generation_exponent"] = data
        return epJSON
    

class ZoneContaminantSourceAndSink_Generic_CutoffModel():
    '''
    Simulate generic contaminant source driven by the cutoff concentration model.
    '''
    def zone_name(epJSON, ObjectName, data=str):
        epJSON["ZoneContaminantSourceAndSink:Generic:CutoffModel"][ObjectName]["zone_name"] = data
        return epJSON
    
    def design_generation_rate_coefficient(epJSON, ObjectName, data=bool):
        epJSON["ZoneContaminantSourceAndSink:Generic:CutoffModel"][ObjectName]["design_generation_rate_coefficient"] = data
        return epJSON
    
    def schedule_name(epJSON, ObjectName, data=str):
        epJSON["ZoneContaminantSourceAndSink:Generic:CutoffModel"][ObjectName]["schedule_name"] = data
        return epJSON
    
    def cutoff_generic_contaminant_at_which_emission_ceases(epJSON, ObjectName, data=bool):
        epJSON["ZoneContaminantSourceAndSink:Generic:CutoffModel"][ObjectName]["cutoff_generic_contaminant_at_which_emission_ceases"] = data
        return epJSON
    

class ZoneContaminantSourceAndSink_Generic_DecaySource():
    '''
    Simulate generic contaminant source driven by the cutoff concentration model.
    '''
    def zone_name(epJSON, ObjectName, data=str):
        epJSON["ZoneContaminantSourceAndSink:Generic:DecaySource"][ObjectName]["zone_name"] = data
        return epJSON
    
    def initial_emission_rate(epJSON, ObjectName, data=bool):
        epJSON["ZoneContaminantSourceAndSink:Generic:DecaySource"][ObjectName]["initial_emission_rate"] = data
        return epJSON
    
    def schedule_name(epJSON, ObjectName, data=str):
        epJSON["ZoneContaminantSourceAndSink:Generic:DecaySource"][ObjectName]["schedule_name"] = data
        return epJSON
    
    def delay_time_constant(epJSON, ObjectName, data=bool):
        epJSON["ZoneContaminantSourceAndSink:Generic:DecaySource"][ObjectName]["delay_time_constant"] = data
        return epJSON
    

class SurfaceContaminantSourceAndSink_Generic_BoundaryLayerDiffusion():
    '''
    Simulate generic contaminant source driven by the boundary layer diffusion controlled model.
    '''
    def surface_name(epJSON, ObjectName, data=str):
        epJSON["SurfaceContaminantSourceAndSink:Generic:BoundaryLayerDiffusion"][ObjectName]["surface_name"] = data
        return epJSON
    
    def mass_transfer_coefficient(epJSON, ObjectName, data=bool):
        epJSON["SurfaceContaminantSourceAndSink:Generic:BoundaryLayerDiffusion"][ObjectName]["mass_transfer_coefficient"] = data
        return epJSON
    
    def schedule_name(epJSON, ObjectName, data=str):
        epJSON["SurfaceContaminantSourceAndSink:Generic:BoundaryLayerDiffusion"][ObjectName]["schedule_name"] = data
        return epJSON
    
    def henry_adsorption_constant_or_partition_coefficient(epJSON, ObjectName, data=bool):
        epJSON["SurfaceContaminantSourceAndSink:Generic:BoundaryLayerDiffusion"][ObjectName]["henry_adsorption_constant_or_partition_coefficient"] = data
        return epJSON
    

class SurfaceContaminantSourceAndSink_Generic_DepositionVelocitySink():
    '''
    Simulate generic contaminant source driven by the boundary layer diffusion controlled model.
    '''
    def surface_name(epJSON, ObjectName, data=str):
        epJSON["SurfaceContaminantSourceAndSink:Generic:DepositionVelocitySink"][ObjectName]["surface_name"] = data
        return epJSON
    
    def deposition_velocity(epJSON, ObjectName, data=bool):
        epJSON["SurfaceContaminantSourceAndSink:Generic:DepositionVelocitySink"][ObjectName]["deposition_velocity"] = data
        return epJSON
    
    def schedule_name(epJSON, ObjectName, data=str):
        epJSON["SurfaceContaminantSourceAndSink:Generic:DepositionVelocitySink"][ObjectName]["schedule_name"] = data
        return epJSON
    

class ZoneContaminantSourceAndSink_Generic_DepositionRateSink():
    '''
    Simulate generic contaminant source driven by the boundary layer diffusion controlled model.
    '''
    def zone_name(epJSON, ObjectName, data=str):
        epJSON["ZoneContaminantSourceAndSink:Generic:DepositionRateSink"][ObjectName]["zone_name"] = data
        return epJSON
    
    def deposition_rate(epJSON, ObjectName, data=bool):
        epJSON["ZoneContaminantSourceAndSink:Generic:DepositionRateSink"][ObjectName]["deposition_rate"] = data
        return epJSON
    
    def schedule_name(epJSON, ObjectName, data=str):
        epJSON["ZoneContaminantSourceAndSink:Generic:DepositionRateSink"][ObjectName]["schedule_name"] = data
        return epJSON