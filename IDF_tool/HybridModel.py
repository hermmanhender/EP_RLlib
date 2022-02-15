"""
# Hybrid Model
"""
"""
HybridModel:Zone
Zones with measured air temperature data and a range of dates. If the range of temperature measurement dates includes a leap day, the weather data should include a leap day.

Fields

zone_name [string]
calculate_zone_internal_thermal_mass [string] (Default: No)
calculate_zone_air_infiltration_rate [string] (Default: No)
calculate_zone_people_count [string] (Default: No)
zone_measured_air_temperature_schedule_name [string]
zone_measured_air_humidity_ratio_schedule_name [string]
zone_measured_air_co2_concentration_schedule_name [string]
zone_input_people_activity_schedule_name [string]
zone_input_people_sensible_heat_fraction_schedule_name [string]
zone_input_people_radiant_heat_fraction_schedule_name [string]
zone_input_people_co2_generation_rate_schedule_name [string]
zone_input_supply_air_temperature_schedule_name [string]
zone_input_supply_air_mass_flow_rate_schedule_name [string]
zone_input_supply_air_humidity_ratio_schedule_name [string]
zone_input_supply_air_co2_concentration_schedule_name [string]
begin_month [number]
begin_day_of_month [number]
end_month [number]
end_day_of_month [number]
"""