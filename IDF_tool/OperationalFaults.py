"""
# Operational Faults
"""
"""
FaultModel:TemperatureSensorOffset:OutdoorAir
This object describes outdoor air temperature sensor offset

Fields

availability_schedule_name [string]
severity_schedule_name [string]
controller_object_type [string]
controller_object_name [string]
temperature_sensor_offset [number] (Default: 0.0)
FaultModel:HumiditySensorOffset:OutdoorAir
This object describes outdoor air humidity sensor offset

Fields

availability_schedule_name [string]
severity_schedule_name [string]
controller_object_type [string]
controller_object_name [string]
humidity_sensor_offset [number] (Default: 0.0)
FaultModel:EnthalpySensorOffset:OutdoorAir
This object describes outdoor air enthalpy sensor offset

Fields

availability_schedule_name [string]
severity_schedule_name [string]
controller_object_type [string]
controller_object_name [string]
enthalpy_sensor_offset [number] (Default: 0.0)
FaultModel:TemperatureSensorOffset:ReturnAir
This object describes return air temperature sensor offset

Fields

availability_schedule_name [string]
severity_schedule_name [string]
controller_object_type [string]
controller_object_name [string]
temperature_sensor_offset [number] (Default: 0.0)
FaultModel:EnthalpySensorOffset:ReturnAir
This object describes return air enthalpy sensor offset

Fields

availability_schedule_name [string]
severity_schedule_name [string]
controller_object_type [string]
controller_object_name [string]
enthalpy_sensor_offset [number] (Default: 0.0)
FaultModel:TemperatureSensorOffset:ChillerSupplyWater
This object describes fault of chiller supply water temperature sensor offset

Fields

availability_schedule_name [string]
severity_schedule_name [string]
chiller_object_type [string]
chiller_object_name [string]
reference_sensor_offset [number] (Default: 0.0)
FaultModel:TemperatureSensorOffset:CoilSupplyAir
This object describes fault of coil supply air temperature sensor offset

Fields

availability_schedule_name [string]
severity_schedule_name [string]
coil_object_type [string]
coil_object_name [string]
water_coil_controller_name [string]
reference_sensor_offset [number] (Default: 0.0)
FaultModel:TemperatureSensorOffset:CondenserSupplyWater
This object describes fault of condenser supply water temperature sensor offset

Fields

availability_schedule_name [string]
severity_schedule_name [string]
cooling_tower_object_type [string]
cooling_tower_object_name [string]
reference_sensor_offset [number] (Default: 0.0)
FaultModel:ThermostatOffset
This object describes fault of thermostat offset

Fields

thermostat_name [string]
availability_schedule_name [string]
severity_schedule_name [string]
reference_thermostat_offset [number] (Default: 2.0)
FaultModel:HumidistatOffset
This object describes fault of humidistat offset

Fields

humidistat_name [string]
humidistat_offset_type [string] (Default: ThermostatOffsetIndependent)
availability_schedule_name [string]
severity_schedule_name [string]
reference_humidistat_offset [number] (Default: 5.0)
related_thermostat_offset_fault_name [string]
FaultModel:Fouling:AirFilter
This object describes fault of dirty air filters

Fields

fan_object_type [string]
fan_name [string]
availability_schedule_name [string]
pressure_fraction_schedule_name [string]
fan_curve_name [string]
FaultModel:Fouling:Boiler
This object describes the fouling fault of boilers with water-based heat exchangers

Fields

availability_schedule_name [string]
severity_schedule_name [string]
boiler_object_type [string]
boiler_object_name [string]
fouling_factor [number] (Default: 1.0)
FaultModel:Fouling:EvaporativeCooler
This object describes the fouling fault of the wetted coil evaporative cooler

Fields

availability_schedule_name [string]
severity_schedule_name [string]
evaporative_cooler_object_type [string]
evaporative_cooler_object_name [string]
fouling_factor [number] (Default: 1.0)
FaultModel:Fouling:Chiller
This object describes the fouling fault of chillers with water-cooled condensers

Fields

availability_schedule_name [string]
severity_schedule_name [string]
chiller_object_type [string]
chiller_object_name [string]
fouling_factor [number] (Default: 1.0)
FaultModel:Fouling:CoolingTower
This object describes the fault of fouling cooling towers

Fields

availability_schedule_name [string]
severity_schedule_name [string]
cooling_tower_object_type [string]
cooling_tower_object_name [string]
reference_ua_reduction_factor [number]
FaultModel:Fouling:Coil
This object describes fouling water heating or cooling coils

Fields

coil_name [string]
availability_schedule_name [string]
severity_schedule_name [string]
fouling_input_method [string] (Default: FouledUARated)
uafouled [number]
water_side_fouling_factor [number] (Default: 0.0)
air_side_fouling_factor [number] (Default: 0.0)
outside_coil_surface_area [number]
inside_to_outside_coil_surface_area_ratio [number] (Default: 0.07)
"""