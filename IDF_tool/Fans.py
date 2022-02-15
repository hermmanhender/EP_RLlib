"""
# Fans
"""

class Fan_SystemModel():
    '''
    Versatile simple fan that can be used in variable air volume, constant volume, on-off cycling, two-speed or multi-speed applications. Performance at different flow rates, or speed levels, is determined using separate performance curve or table or prescribed power fractions at discrete speed levels for two-speed or multi-speed fans.
    '''
    def availability_schedule_name(epJSON, ObjectName, data=str):
        epJSON['Fan:SystemModel'][ObjectName]['availability_schedule_name'] = data
        return epJSON

    def air_inlet_node_name(epJSON, ObjectName, data=str):
        epJSON['Fan:SystemModel'][ObjectName]['air_inlet_node_name'] = data
        return epJSON

    def air_outlet_node_name(epJSON, ObjectName, data=str):
        epJSON['Fan:SystemModel'][ObjectName]['air_outlet_node_name'] = data
        return epJSON

    def design_maximum_air_flow_rate(epJSON, ObjectName, data):
        epJSON['Fan:SystemModel'][ObjectName]['design_maximum_air_flow_rate'] = data
        return epJSON

    def speed_control_method(epJSON, ObjectName, data='Discrete'):
        epJSON['Fan:SystemModel'][ObjectName]['speed_control_method'] = data
        return epJSON

    def electric_power_minimum_flow_rate_fraction(epJSON, ObjectName, data=0.2):
        epJSON['Fan:SystemModel'][ObjectName]['electric_power_minimum_flow_rate_fraction'] = data
        return epJSON

    def design_pressure_rise(epJSON, ObjectName, data=bool):
        epJSON['Fan:SystemModel'][ObjectName]['design_pressure_rise'] = data
        return epJSON

    def motor_efficiency(epJSON, ObjectName, data=0.9):
        epJSON['Fan:SystemModel'][ObjectName]['motor_efficiency'] = data
        return epJSON

    def motor_in_air_stream_fraction(epJSON, ObjectName, data=1.0):
        epJSON['Fan:SystemModel'][ObjectName]['motor_in_air_stream_fraction'] = data
        return epJSON

    def design_electric_power_consumption(epJSON, ObjectName, data='Autosize'):
        epJSON['Fan:SystemModel'][ObjectName]['design_electric_power_consumption'] = data
        return epJSON

    def design_power_sizing_method(epJSON, ObjectName, data='PowerPerFlowPerPressure'):
        epJSON['Fan:SystemModel'][ObjectName]['design_power_sizing_method'] = data
        return epJSON

    def electric_power_per_unit_flow_rate(epJSON, ObjectName, data=bool):
        epJSON['Fan:SystemModel'][ObjectName]['electric_power_per_unit_flow_rate'] = data
        return epJSON

    def electric_power_per_unit_flow_rate_per_unit_pressure(epJSON, ObjectName, data=1.66667):
        epJSON['Fan:SystemModel'][ObjectName]['electric_power_per_unit_flow_rate_per_unit_pressure'] = data
        return epJSON

    def fan_total_efficiency(epJSON, ObjectName, data=0.7):
        epJSON['Fan:SystemModel'][ObjectName]['fan_total_efficiency'] = data
        return epJSON

    def electric_power_function_of_flow_fraction_curve_name(epJSON, ObjectName, data=str):
        epJSON['Fan:SystemModel'][ObjectName]['electric_power_function_of_flow_fraction_curve_name'] = data
        return epJSON

    def night_ventilation_mode_pressure_rise(epJSON, ObjectName, data=bool):
        epJSON['Fan:SystemModel'][ObjectName]['night_ventilation_mode_pressure_rise'] = data
        return epJSON

    def night_ventilation_mode_flow_fraction(epJSON, ObjectName, data=bool):
        epJSON['Fan:SystemModel'][ObjectName]['night_ventilation_mode_flow_fraction'] = data
        return epJSON

    def motor_loss_zone_name(epJSON, ObjectName, data=str):
        epJSON['Fan:SystemModel'][ObjectName]['motor_loss_zone_name'] = data
        return epJSON

    def motor_loss_radiative_fraction(epJSON, ObjectName, data=bool):
        epJSON['Fan:SystemModel'][ObjectName]['motor_loss_radiative_fraction'] = data
        return epJSON

    def end_use_subcategory(epJSON, ObjectName, data='General'):
        epJSON['Fan:SystemModel'][ObjectName]['end_use_subcategory'] = data
        return epJSON

    def number_of_speeds(epJSON, ObjectName, data=1.0):
        epJSON['Fan:SystemModel'][ObjectName]['number_of_speeds'] = data
        return epJSON

    def speed_fractions(epJSON, ObjectName, data):
        '''
        [Array of {speed_flow_fraction, speed_electric_power_fraction}]
        '''
        epJSON['Fan:SystemModel'][ObjectName]['speed_fractions'] = data
        return epJSON

"""
Fan:ConstantVolume
Constant volume fan that is intended to operate continuously based on a time schedule. This fan will not cycle on and off based on cooling/heating load or other control signals.

Fields

availability_schedule_name [string]
fan_total_efficiency [number] (Default: 0.7)
pressure_rise [number]
maximum_flow_rate [unknown field type]
motor_efficiency [number] (Default: 0.9)
motor_in_airstream_fraction [number] (Default: 1.0)
air_inlet_node_name [string]
air_outlet_node_name [string]
end_use_subcategory [string] (Default: General)
Fan:VariableVolume
Variable air volume fan where the electric power input varies according to a performance curve as a function of flow fraction.

Fields

availability_schedule_name [string]
fan_total_efficiency [number] (Default: 0.7)
pressure_rise [number]
maximum_flow_rate [unknown field type]
fan_power_minimum_flow_rate_input_method [string] (Default: Fraction)
fan_power_minimum_flow_fraction [number] (Default: 0.25)
fan_power_minimum_air_flow_rate [number]
motor_efficiency [number] (Default: 0.9)
motor_in_airstream_fraction [number] (Default: 1.0)
fan_power_coefficient_1 [number]
fan_power_coefficient_2 [number]
fan_power_coefficient_3 [number]
fan_power_coefficient_4 [number]
fan_power_coefficient_5 [number]
air_inlet_node_name [string]
air_outlet_node_name [string]
end_use_subcategory [string] (Default: General)
Fan:OnOff
Constant volume fan that is intended to cycle on and off based on cooling/heating load or other control signals. This fan can also operate continuously like Fan:ConstantVolume.

Fields

availability_schedule_name [string]
fan_total_efficiency [number] (Default: 0.6)
pressure_rise [number]
maximum_flow_rate [unknown field type]
motor_efficiency [number] (Default: 0.8)
motor_in_airstream_fraction [number] (Default: 1.0)
air_inlet_node_name [string]
air_outlet_node_name [string]
fan_power_ratio_function_of_speed_ratio_curve_name [string]
fan_efficiency_ratio_function_of_speed_ratio_curve_name [string]
end_use_subcategory [string] (Default: General)
Fan:ZoneExhaust
Models a fan that exhausts air from a zone.

Fields

availability_schedule_name [string]
fan_total_efficiency [number] (Default: 0.6)
pressure_rise [number]
maximum_flow_rate [number]
air_inlet_node_name [string]
air_outlet_node_name [string]
end_use_subcategory [string] (Default: General)
flow_fraction_schedule_name [string]
system_availability_manager_coupling_mode [string] (Default: Coupled)
minimum_zone_temperature_limit_schedule_name [string]
balanced_exhaust_fraction_schedule_name [string]
FanPerformance:NightVentilation
Specifies an alternate set of performance parameters for a fan. These alternate parameters are used when a system manager (such as AvailabilityManager:NightVentilation) sets a specified flow rate. May be used with Fan:ConstantVolume, Fan:VariableVolume and Fan:ComponentModel. If the fan model senses that a fixed flow rate has been set, it will use these alternate performance parameters. It is assumed that the fan will run at a fixed speed in the alternate mode.

Fields

fan_name [string]
fan_total_efficiency [number]
pressure_rise [number]
maximum_flow_rate [unknown field type]
motor_efficiency [number]
motor_in_airstream_fraction [number] (Default: 1.0)
Fan:ComponentModel
A detailed fan type for constant-air-volume (CAV) and variable-air-volume (VAV) systems. It includes inputs that describe the air-distribution system as well as the fan, drive belt (if used), motor, and variable-frequency-drive (if used).

Fields

air_inlet_node_name [string]
air_outlet_node_name [string]
availability_schedule_name [string]
maximum_flow_rate [unknown field type]
minimum_flow_rate [unknown field type]
fan_sizing_factor [number] (Default: 1.0)
fan_wheel_diameter [number]
fan_outlet_area [number]
maximum_fan_static_efficiency [number]
euler_number_at_maximum_fan_static_efficiency [number]
maximum_dimensionless_fan_airflow [number]
motor_fan_pulley_ratio [unknown field type] (Default: 1.0)
belt_maximum_torque [unknown field type]
belt_sizing_factor [number] (Default: 1.0)
belt_fractional_torque_transition [number] (Default: 0.167)
motor_maximum_speed [number]
maximum_motor_output_power [unknown field type]
motor_sizing_factor [number] (Default: 1.0)
motor_in_airstream_fraction [number] (Default: 1.0)
vfd_efficiency_type [string]
maximum_vfd_output_power [unknown field type]
vfd_sizing_factor [number] (Default: 1.0)
fan_pressure_rise_curve_name [string]
duct_static_pressure_reset_curve_name [string]
normalized_fan_static_efficiency_curve_name_non_stall_region [string]
normalized_fan_static_efficiency_curve_name_stall_region [string]
normalized_dimensionless_airflow_curve_name_non_stall_region [string]
normalized_dimensionless_airflow_curve_name_stall_region [string]
maximum_belt_efficiency_curve_name [string]
normalized_belt_efficiency_curve_name_region_1 [string]
normalized_belt_efficiency_curve_name_region_2 [string]
normalized_belt_efficiency_curve_name_region_3 [string]
maximum_motor_efficiency_curve_name [string]
normalized_motor_efficiency_curve_name [string]
vfd_efficiency_curve_name [string]
end_use_subcategory [string] (Default: General)
"""