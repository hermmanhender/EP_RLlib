"""
# Room Air Models
"""
"""
class RoomAirModelType():
    '''
    Selects the type of room air model to be used in a given zone. If no RoomAirModelType object is specified then the default Mixing model (all zone air at the same temperature) will be used.
    '''

zone_name [string]
room_air_modeling_type [string] (Default: Mixing)
air_temperature_coupling_strategy [string] (Default: Direct)

class RoomAir:TemperaturePattern:UserDefined():
    '''
    Used to explicitly define temperature patterns that are to be applied to the mean air temperature within a thermal zone. Used with RoomAirModelType = UserDefined.
    '''

zone_name [string]
availability_schedule_name [string]
pattern_control_schedule_name [string]

class RoomAir:TemperaturePattern:ConstantGradient():
    '''
    Used to model room air with a fixed temperature gradient in the vertical direction. Used in combination with RoomAir:TemperaturePattern:UserDefined.
    '''

room_air_temperature_pattern_constant_gradient_name [string]
control_integer_for_pattern_control_schedule_name [number]
thermostat_offset [number]
return_air_offset [number]
exhaust_air_offset [number]
temperature_gradient [number]

class RoomAir:TemperaturePattern:TwoGradient():
    '''
    Used to model room air with two temperature gradients in the vertical direction. Used in combination with RoomAir:TemperaturePattern:UserDefined.
    '''

room_air_temperature_pattern_two_gradient_name [string]
control_integer_for_pattern_control_schedule_name [number]
thermostat_height [number]
return_air_height [number]
exhaust_air_height [number]
temperature_gradient_lower_bound [number]
temperature_gradient_upper_bound [number]
gradient_interpolation_mode [string]
upper_temperature_bound [number]
lower_temperature_bound [number]
upper_heat_rate_bound [number]
lower_heat_rate_bound [number]

class RoomAir:TemperaturePattern:NondimensionalHeight():
    '''
    Defines a distribution pattern for air temperatures relative to the current mean air temperature as a function of height. The height, referred to as Zeta, is nondimensional by normalizing with the zone ceiling height. Used in combination with RoomAir:TemperaturePattern:UserDefined.
    '''

control_integer_for_pattern_control_schedule_name [number]
thermostat_offset [number]
return_air_offset [number]
exhaust_air_offset [number]
pairs [Array of {pair_zeta_nondimensional_height, pair_delta_adjacent_air_temperature}]

class RoomAir:TemperaturePattern:SurfaceMapping():
    '''
    Defines a distribution pattern for the air temperatures adjacent to individual surfaces. This allows controlling the adjacent air temperature on a surface-by-surface basis rather than by height. This allows modeling different adjacent air temperatures on the opposite sides of the zone. Used in combination with RoomAir:TemperaturePattern:UserDefined.
    '''

control_integer_for_pattern_control_schedule_name [number]
thermostat_offset [number]
return_air_offset [number]
exhaust_air_offset [number]
surface_deltas [Array of {surface_name_pair, delta_adjacent_air_temperature_pair}]

class RoomAir:Node():
    '''
    Define an air node for some types of nodal room air models
    '''

node_type [string]
zone_name [string]
height_of_nodal_control_volume_center [number]
surface_1_name [string]
surface_2_name [string]
surface_3_name [string]
surface_4_name [string]
surface_5_name [string]
surface_6_name [string]
surface_7_name [string]
surface_8_name [string]
surface_9_name [string]
surface_10_name [string]
surface_11_name [string]
surface_12_name [string]
surface_13_name [string]
surface_14_name [string]
surface_15_name [string]
surface_16_name [string]
surface_17_name [string]
surface_18_name [string]
surface_19_name [string]
surface_20_name [string]
surface_21_name [string]

class RoomAirSettings:OneNodeDisplacementVentilation():
    '''
    The Mundt model for displacement ventilation
    '''

zone_name [string]
fraction_of_convective_internal_loads_added_to_floor_air [number]
fraction_of_infiltration_internal_loads_added_to_floor_air [number]

class RoomAirSettings:ThreeNodeDisplacementVentilation():
    '''
    The UCSD model for Displacement Ventilation
    '''

zone_name [string]
gain_distribution_schedule_name [string]
number_of_plumes_per_occupant [number] (Default: 1.0)
thermostat_height [number] (Default: 1.1)
comfort_height [number] (Default: 1.1)
temperature_difference_threshold_for_reporting [number] (Default: 0.4)

class RoomAirSettings:CrossVentilation():
    '''
    This UCSD Cross Ventilation Room Air Model provides a simple model for heat transfer and vertical temperature profile prediction in cross ventilated rooms. The model distinguishes two regions in the room, the main jet region and the recirculations, and predicts characteristic airflow velocities and average air temperatures. Used with RoomAirModelType = CrossVentilation.
    '''

zone_name [string]
gain_distribution_schedule_name [string]
airflow_region_used_for_thermal_comfort_evaluation [string]

class RoomAirSettings:UnderFloorAirDistributionInterior():
    '''
    This Room Air Model is applicable to interior spaces that are served by an underfloor air distribution system. The dominant sources of heat gain should be from people, equipment, and other localized sources located in the occupied part of the room. The model should be used with caution in zones which have large heat gains or losses through exterior walls or windows or which have considerable direct solar gain. Used with RoomAirModelType = UnderFloorAirDistributionInterior.
    '''

zone_name [string]
number_of_diffusers [unknown field type] (Default: Autocalculate)
power_per_plume [unknown field type] (Default: Autocalculate)
design_effective_area_of_diffuser [unknown field type] (Default: Autocalculate)
diffuser_slot_angle_from_vertical [unknown field type] (Default: Autocalculate)
thermostat_height [number] (Default: 1.2)
comfort_height [number] (Default: 1.1)
temperature_difference_threshold_for_reporting [number] (Default: 0.4)
floor_diffuser_type [string] (Default: Swirl)
transition_height [unknown field type] (Default: 1.7)
coefficient_a [unknown field type] (Default: Autocalculate)
coefficient_b [unknown field type] (Default: Autocalculate)
coefficient_c [unknown field type] (Default: Autocalculate)
coefficient_d [unknown field type] (Default: Autocalculate)
coefficient_e [unknown field type] (Default: Autocalculate)

class RoomAirSettings:UnderFloorAirDistributionExterior():
    '''
    Applicable to exterior spaces that are served by an underfloor air distribution system. The dominant sources of heat gain should be from people, equipment, and other localized sources located in the occupied part of the room, as well as convective gain coming from a warm window. Used with RoomAirModelType = CrossVentilation.
    '''

zone_name [string]
number_of_diffusers_per_zone [unknown field type] (Default: Autocalculate)
power_per_plume [unknown field type] (Default: Autocalculate)
design_effective_area_of_diffuser [unknown field type] (Default: Autocalculate)
diffuser_slot_angle_from_vertical [unknown field type] (Default: Autocalculate)
thermostat_height [number] (Default: 1.2)
comfort_height [number] (Default: 1.1)
temperature_difference_threshold_for_reporting [number] (Default: 0.4)
floor_diffuser_type [string] (Default: Swirl)
transition_height [unknown field type] (Default: 1.7)
coefficient_a_in_formula_kc_a_gamma_b_c_d_gamma_e_gamma_2 [unknown field type] (Default: Autocalculate)
coefficient_b_in_formula_kc_a_gamma_b_c_d_gamma_e_gamma_2 [unknown field type] (Default: Autocalculate)
coefficient_c_in_formula_kc_a_gamma_b_c_d_gamma_e_gamma_2 [unknown field type] (Default: Autocalculate)
coefficient_d_in_formula_kc_a_gamma_b_c_d_gamma_e_gamma_2 [unknown field type] (Default: Autocalculate)
coefficient_e_in_formula_kc_a_gamma_b_c_d_gamma_e_gamma_2 [unknown field type] (Default: Autocalculate)

class RoomAir:Node:AirflowNetwork():
    '''
    define an air node for some types of nodal air models
    '''

zone_name [string]
fraction_of_zone_air_volume [number]
roomair_node_airflownetwork_adjacentsurfacelist_name [string]
roomair_node_airflownetwork_internalgains_name [string]
roomair_node_airflownetwork_hvacequipment_name [string]

class RoomAir:Node:AirflowNetwork:AdjacentSurfaceList():
    '''
    '''

surfaces [Array of {surface_name}]

class RoomAir:Node:AirflowNetwork:InternalGains():
    '''
    define the internal gains that are associated with one particular RoomAir:Node
    '''

gains [Array of {internal_gain_object_type, internal_gain_object_name, fraction_of_gains_to_node}]

class RoomAir:Node:AirflowNetwork:HVACEquipment():
    '''
    define the zone equipment associated with one particular RoomAir:Node
    '''

equipment_fractions [Array of {zonehvac_or_air_terminal_equipment_object_type, zonehvac_or_air_terminal_equipment_object_name, fraction_of_output_or_supply_air_from_hvac_equipment, fraction_of_input_or_return_air_to_hvac_equipment}]

class RoomAirSettings:AirflowNetwork():
    '''
    RoomAir modeling using Airflow pressure network solver
    '''

zone_name [string]
control_point_roomairflownetwork_node_name [string]
nodes [Array of {roomairflownetwork_node_name}]
"""