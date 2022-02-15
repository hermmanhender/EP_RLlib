"""
# Location and climate
"""
class Site_Location():
    """
    Specifies the building's location. Only one location is allowed. Weather data file location, if it exists, will override this object.
    """
    def latitude(epJSON, ObjectName, data=0.0):
        epJSON["Site:Location"][ObjectName]["latitude"] = data # [data] (Default: 0.0)
        return epJSON

    def longitude(epJSON, ObjectName, data=0.0):
        epJSON["Site:Location"][ObjectName]["longitude"] = data # [data] (Default: 0.0)
        return epJSON
    
    def time_zone(epJSON, ObjectName, data=0.0):
        epJSON["Site:Location"][ObjectName]["time_zone"] = data # [data] (Default: 0.0)
        return epJSON

    def elevation(epJSON, ObjectName, data=0.0):
        epJSON["Site:Location"][ObjectName]["elevation"] = data # [data] (Default: 0.0)
        return epJSON

class Site_VariableLocation():
    """
    Captures the scheduling of a moving/reorienting building, or more likely a vessel.
    """
    def building_location_latitude_schedule(epJSON, data=str):
        epJSON["Site:VariableLocation"]["Site:VariableLocation 1"]["building_location_latitude_schedule"] = data # [data]
        return epJSON
    
    def building_location_longitude_schedule(epJSON, data=str):
        epJSON["Site:VariableLocation"]["Site:VariableLocation 1"]["building_location_longitude_schedule"] = data # [data]
        return epJSON

    def building_location_orientation_schedule(epJSON, data=str):
        epJSON["Site:VariableLocation"]["Site:VariableLocation 1"]["building_location_orientation_schedule"] = data # [data]
        return epJSON


class SizingPeriod_DesignDay():
    """
    The design day object creates the parameters for the program to create the 24 hour weather profile that can be used for sizing as well as running to test the other simulation parameters. Parameters in this include a date (month and day), a day type (which uses the appropriate schedules for either sizing or simple tests), min/max temperatures, wind speeds, and solar radiation values.
    """
    def month(epJSON, data):
        epJSON["SizingPeriod:DesignDay"]["SizingPeriod:DesignDay 1"]["month"] = data # [data]
        return epJSON
    
    def day_of_month(epJSON, data):
        epJSON["SizingPeriod:DesignDay"]["SizingPeriod:DesignDay 1"]["day_of_month"] = data # [data]
        return epJSON
    
    def day_type(epJSON, data):
        epJSON["SizingPeriod:DesignDay"]["SizingPeriod:DesignDay 1"]["day_type"] = data # [data]
        return epJSON
    
    def maximum_dry_bulb_temperature(epJSON, data):
        epJSON["SizingPeriod:DesignDay"]["SizingPeriod:DesignDay 1"]["maximum_dry_bulb_temperature"] = data # [data]
        return epJSON
    
    def daily_dry_bulb_temperature_range(epJSON, data=0.0):
        epJSON["SizingPeriod:DesignDay"]["SizingPeriod:DesignDay 1"]["daily_dry_bulb_temperature_range"] = data # [data] (Default: 0.0)
        return epJSON
    
    def dry_bulb_temperature_range_modifier_type(epJSON, data="DefaultMultipliers"):
        epJSON["SizingPeriod:DesignDay"]["SizingPeriod:DesignDay 1"]["dry_bulb_temperature_range_modifier_type"] = data # [data] (Default: DefaultMultipliers)
        return epJSON
    
    def dry_bulb_temperature_range_modifier_day_schedule_name(epJSON, data):
        epJSON["SizingPeriod:DesignDay"]["SizingPeriod:DesignDay 1"]["dry_bulb_temperature_range_modifier_day_schedule_name"] = data # [data]
        return epJSON

    def humidity_condition_type(epJSON, data="WetBulb"):
        epJSON["SizingPeriod:DesignDay"]["SizingPeriod:DesignDay 1"]["humidity_condition_type"] = data # [data] (Default: WetBulb)
        return epJSON
    
    def wetbulb_or_dewpoint_at_maximum_dry_bulb(epJSON, data):
        epJSON["SizingPeriod:DesignDay"]["SizingPeriod:DesignDay 1"]["wetbulb_or_dewpoint_at_maximum_dry_bulb"] = data # [data]
        return epJSON
    
    def humidity_condition_day_schedule_name(epJSON, data):
        epJSON["SizingPeriod:DesignDay"]["SizingPeriod:DesignDay 1"]["humidity_condition_day_schedule_name"] = data # [data]
        return epJSON
    
    def humidity_ratio_at_maximum_dry_bulb(epJSON, data):
        epJSON["SizingPeriod:DesignDay"]["SizingPeriod:DesignDay 1"]["humidity_ratio_at_maximum_dry_bulb"] = data # [data]
        return epJSON

    def enthalpy_at_maximum_dry_bulb(epJSON, data):
        epJSON["SizingPeriod:DesignDay"]["SizingPeriod:DesignDay 1"]["enthalpy_at_maximum_dry_bulb"] = data # [data]
        return epJSON

    def daily_wet_bulb_temperature_range(epJSON, data):
        epJSON["SizingPeriod:DesignDay"]["SizingPeriod:DesignDay 1"]["daily_wet_bulb_temperature_range"] = data # [data]
        return epJSON

    def barometric_pressure(epJSON, data):
        epJSON["SizingPeriod:DesignDay"]["SizingPeriod:DesignDay 1"]["barometric_pressure"] = data # [data]
        return epJSON

    def wind_speed(epJSON, data):
        epJSON["SizingPeriod:DesignDay"]["SizingPeriod:DesignDay 1"]["wind_speed"] = data # [data]
        return epJSON

    def wind_direction(epJSON, data):
        epJSON["SizingPeriod:DesignDay"]["SizingPeriod:DesignDay 1"]["wind_direction"] = data # [data]
        return epJSON

    def rain_indicator(epJSON, data="No"):
        epJSON["SizingPeriod:DesignDay"]["SizingPeriod:DesignDay 1"]["rain_indicator"] = data # [data] (Default: No)
        return epJSON

    def snow_indicator(epJSON, data="No"):
        epJSON["SizingPeriod:DesignDay"]["SizingPeriod:DesignDay 1"]["snow_indicator"] = data # [data] (Default: No)
        return epJSON

    def daylight_saving_time_indicator(epJSON, data="No"):
        epJSON["SizingPeriod:DesignDay"]["SizingPeriod:DesignDay 1"]["daylight_saving_time_indicator"] = data # [data] (Default: No)
        return epJSON

    def solar_model_indicator(epJSON, data="ASHRAEClearSky"):
        epJSON["SizingPeriod:DesignDay"]["SizingPeriod:DesignDay 1"]["solar_model_indicator"] = data # [data] (Default: ASHRAEClearSky)
        return epJSON

    def beam_solar_day_schedule_name(epJSON, data):
        epJSON["SizingPeriod:DesignDay"]["SizingPeriod:DesignDay 1"]["beam_solar_day_schedule_name"] = data # [data]
        return epJSON

    def diffuse_solar_day_schedule_name(epJSON, data):
        epJSON["SizingPeriod:DesignDay"]["SizingPeriod:DesignDay 1"]["diffuse_solar_day_schedule_name"] = data # [data]
        return epJSON

    def ashrae_clear_sky_optical_depth_for_beam_irradiance_taub_(epJSON, data=0.0):
        epJSON["SizingPeriod:DesignDay"]["SizingPeriod:DesignDay 1"]["ashrae_clear_sky_optical_depth_for_beam_irradiance_taub_"] = data # [data] (Default: 0.0)
        return epJSON

    def ashrae_clear_sky_optical_depth_for_diffuse_irradiance_taud_(epJSON, data=0.0):
        epJSON["SizingPeriod:DesignDay"]["SizingPeriod:DesignDay 1"]["ashrae_clear_sky_optical_depth_for_diffuse_irradiance_taud_"] = data # [data] (Default: 0.0)
        return epJSON

    def sky_clearness(epJSON, data=0.0):
        epJSON["SizingPeriod:DesignDay"]["SizingPeriod:DesignDay 1"]["sky_clearness"] = data # [data] (Default: 0.0)
        return epJSON

    def maximum_data_warmup_days(epJSON, data):
        epJSON["SizingPeriod:DesignDay"]["SizingPeriod:DesignDay 1"]["maximum_data_warmup_days"] = data # [data]
        return epJSON

    def begin_environment_reset_mode(epJSON, data="FullResetAtBeginEnvironment"):
        epJSON["SizingPeriod:DesignDay"]["SizingPeriod:DesignDay 1"]["begin_environment_reset_mode"] = data # [data] (Default: FullResetAtBeginEnvironment)
        return epJSON


class SizingPeriod_WeatherFileDays():
    """
    Use a weather file period for design sizing calculations.
    """
    def begin_month(epJSON, data):
        epJSON["SizingPeriod:WeatherFileDays"]["SizingPeriod:WeatherFileDays 1"]["begin_month"] = data # [data]
        return epJSON

    def begin_day_of_month(epJSON, data):
        epJSON["SizingPeriod:WeatherFileDays"]["SizingPeriod:WeatherFileDays 1"]["begin_day_of_month"] = data # [data]
        return epJSON

    def end_month(epJSON, data):
        epJSON["SizingPeriod:WeatherFileDays"]["SizingPeriod:WeatherFileDays 1"]["end_month"] = data # [data]
        return epJSON
    
    def end_day_of_month(epJSON, data):
        epJSON["SizingPeriod:WeatherFileDays"]["SizingPeriod:WeatherFileDays 1"]["end_day_of_month"] = data # [data]
        return epJSON

    def day_of_week_for_start_day(epJSON, data="Monday"):
        epJSON["SizingPeriod:WeatherFileDays"]["SizingPeriod:WeatherFileDays 1"]["day_of_week_for_start_day"] = data # [data] (Default: Monday)
        return epJSON

    def use_weather_file_daylight_saving_period(epJSON, data="Yes"):
        epJSON["SizingPeriod:WeatherFileDays"]["SizingPeriod:WeatherFileDays 1"]["use_weather_file_daylight_saving_period"] = data # [data] (Default: Yes)
        return epJSON

    def use_weather_file_rain_and_snow_indicators(epJSON, data="Yes"):
        epJSON["SizingPeriod:WeatherFileDays"]["SizingPeriod:WeatherFileDays 1"]["use_weather_file_rain_and_snow_indicators"] = data # [data] (Default: Yes)
        return epJSON


class SizingPeriod_WeatherFileConditionType():
    """
    Use a weather file period for design sizing calculations. EPW weather files are created with typical and extreme periods created heuristically from the weather file data. For more details on these periods, see AuxiliaryPrograms document.
    """
    def period_selection(epJSON, data):
        epJSON["SizingPeriod:WeatherFileConditionType"]["SizingPeriod:WeatherFileConditionType 1"]["period_selection"] = data # [data]
        return epJSON

    def day_of_week_for_start_day(epJSON, data="Monday"):
        epJSON["SizingPeriod:WeatherFileConditionType"]["SizingPeriod:WeatherFileConditionType 1"]["day_of_week_for_start_day"] = data # [data] (Default: Monday)
        return epJSON

    def use_weather_file_daylight_saving_period(epJSON, data="Yes"):
        epJSON["SizingPeriod:WeatherFileConditionType"]["SizingPeriod:WeatherFileConditionType 1"]["use_weather_file_daylight_saving_period"] = data # [data] (Default: Yes)
        return epJSON

    def use_weather_file_rain_and_snow_indicators(epJSON, data="Yes"):
        epJSON["SizingPeriod:WeatherFileConditionType"]["SizingPeriod:WeatherFileConditionType 1"]["use_weather_file_rain_and_snow_indicators"] = data # [data] (Default: Yes)
        return epJSON


class RunPeriod():
    """
    Specify a range of dates and other parameters for a simulation. Multiple run periods may be input, but they may not overlap.
    """

    def begin_month(epJSON, ObjectName, data):
        epJSON["RunPeriod"][ObjectName]["begin_month"] = data
        return epJSON

    def begin_day_of_month(epJSON, ObjectName, data):
        epJSON["RunPeriod"][ObjectName]["begin_day_of_month"] = data
        return epJSON

    def begin_year(epJSON, ObjectName, data):
        epJSON["RunPeriod"][ObjectName]["begin_year"] = data
        return epJSON

    def end_month(epJSON, ObjectName, data):
        epJSON["RunPeriod"][ObjectName]["end_month"] = data
        return epJSON

    def end_day_of_month(epJSON, ObjectName, data):
        epJSON["RunPeriod"][ObjectName]["end_day_of_month"] = data
        return epJSON

    def end_year(epJSON, ObjectName, data):
        epJSON["RunPeriod"][ObjectName]["end_year"] = data
        return epJSON

    def day_of_week_for_start_day(epJSON, ObjectName, data):
        epJSON["RunPeriod"][ObjectName]["day_of_week_for_start_day"] = data
        return epJSON

    def use_weather_file_holidays_and_special_days(epJSON, ObjectName, data):
        epJSON["RunPeriod"][ObjectName]["use_weather_file_holidays_and_special_days"] = data
        return epJSON

    def use_weather_file_daylight_saving_period(epJSON, ObjectName, data):
        epJSON["RunPeriod"][ObjectName]["use_weather_file_daylight_saving_period"] = data
        return epJSON

    def apply_weekend_holiday_rule(epJSON, ObjectName, data):
        epJSON["RunPeriod"][ObjectName]["apply_weekend_holiday_rule"] = data
        return epJSON

    def use_weather_file_rain_indicators(epJSON, ObjectName, data):
        epJSON["RunPeriod"][ObjectName]["use_weather_file_rain_indicators"] = data
        return epJSON

    def use_weather_file_snow_indicators(epJSON, ObjectName, data):
        epJSON["RunPeriod"][ObjectName]["use_weather_file_snow_indicators"] = data
        return epJSON

    def treat_weather_as_actual(epJSON, ObjectName, data):
        epJSON["RunPeriod"][ObjectName]["treat_weather_as_actual"] = data
        return epJSON
    
    def first_hour_interpolation_starting_values(epJSON, ObjectName, data):
        epJSON["RunPeriod"][ObjectName]["first_hour_interpolation_starting_values"] = data
        return epJSON

class RunPeriodControl_SpecialDays():
    """
    This object sets up holidays/special days to be used during weather file run periods. (These are not used with SizingPeriod:* objects.) Depending on the value in the run period, days on the weather file may also be used. However, the weather file specification will take precedence over any specification shown here. (No error message on duplicate days or overlapping days).
    """
    def start_date(epJSON, data, ObjectName="RunPeriodControl:SpecialDays 1"):
        epJSON["RunPeriodControl:SpecialDays"][ObjectName]["start_date"] = data #start_date [data]
        return epJSON
    
    def duration(epJSON, data=1.0, ObjectName="RunPeriodControl:SpecialDays 1"):
        epJSON["RunPeriodControl:SpecialDays"][ObjectName]["duration"] = data #duration [data] (Default: 1.0)
        return epJSON
    
    def special_day_type(epJSON, data="Holiday", ObjectName="RunPeriodControl:SpecialDays 1"):
        epJSON["RunPeriodControl:SpecialDays"][ObjectName]["special_day_type"] = data #special_day_type [data] (Default: Holiday)
        return epJSON
  
"""
class RunPeriodControl:DaylightSavingTime():
    '''
    This object sets up the daylight saving time period for any RunPeriod. Ignores any daylight saving time period on the weather file and uses this definition. These are not used with SizingPeriod:DesignDay objects. Use with SizingPeriod:WeatherFileDays object can be controlled in that object.
    '''
    def (epJSON, data, ObjectName=):
        epJSON[""][ObjectName][""] = data #start_date [data]
        return epJSON
    
    def (epJSON, data, ObjectName=):
        epJSON[""][ObjectName][""] = data #end_date [data]
        return epJSON
    

class WeatherProperty:SkyTemperature():
    '''
    This object is used to override internal sky temperature calculations.
    '''

calculation_type [data] (Default: ClarkAllen)
schedule_name [data]
use_weather_file_horizontal_ir [data] (Default: Yes)

class Site:WeatherStation():
    '''
    This object should only be used for non-standard weather data. Standard weather data such as TMY2, IWEC, and ASHRAE design day data are all measured at the default conditions and do not require this object.
    '''

wind_sensor_height_above_ground [data] (Default: 10.0)
wind_speed_profile_exponent [data] (Default: 0.14)
wind_speed_profile_boundary_layer_thickness [data] (Default: 270.0)
air_temperature_sensor_height_above_ground [data] (Default: 1.5)

class Site:HeightVariation():
    '''
    This object is used if the user requires advanced control over height-dependent variations in wind speed and temperature. When this object is not present, the default model for temperature dependence on height is used, and the wind speed is modeled according to the Terrain field of the BUILDING object.
    '''

wind_speed_profile_exponent [data] (Default: 0.22)
wind_speed_profile_boundary_layer_thickness [data] (Default: 370.0)
air_temperature_gradient_coefficient [data] (Default: 0.0065)

class Site:GroundTemperature:BuildingSurface():
    '''
    These temperatures are specifically for those surfaces that have the outside environment of “Ground”. Documentation about what values these should be is located in the Auxiliary programs document (Ground Heat Transfer) as well as the InputOutput Reference. CAUTION - Do not use the “undisturbed” ground temperatures from the weather data. These values are too extreme for the soil under a conditioned building. For best results, use the Slab or Basement program to calculate custom monthly average ground temperatures (see Auxiliary Programs). For typical commercial buildings in the USA, a reasonable default value is 2C less than the average indoor space temperature.
    '''

january_ground_temperature [data] (Default: 18.0)
february_ground_temperature [data] (Default: 18.0)
march_ground_temperature [data] (Default: 18.0)
april_ground_temperature [data] (Default: 18.0)
may_ground_temperature [data] (Default: 18.0)
june_ground_temperature [data] (Default: 18.0)
july_ground_temperature [data] (Default: 18.0)
august_ground_temperature [data] (Default: 18.0)
september_ground_temperature [data] (Default: 18.0)
october_ground_temperature [data] (Default: 18.0)
november_ground_temperature [data] (Default: 18.0)
december_ground_temperature [data] (Default: 18.0)

class Site:GroundTemperature:FCfactorMethod():
    '''
    These temperatures are specifically for underground walls and ground floors defined with the C-factor and F-factor methods, and should be close to the monthly average outdoor air temperature delayed by 3 months for the location.
    '''

january_ground_temperature [data] (Default: 13.0)
february_ground_temperature [data] (Default: 13.0)
march_ground_temperature [data] (Default: 13.0)
april_ground_temperature [data] (Default: 13.0)
may_ground_temperature [data] (Default: 13.0)
june_ground_temperature [data] (Default: 13.0)
july_ground_temperature [data] (Default: 13.0)
august_ground_temperature [data] (Default: 13.0)
september_ground_temperature [data] (Default: 13.0)
october_ground_temperature [data] (Default: 13.0)
november_ground_temperature [data] (Default: 13.0)
december_ground_temperature [data] (Default: 13.0)

class Site:GroundTemperature:Shallow():
    '''
    These temperatures are specifically for the Surface Ground Heat Exchanger and should probably be close to the average outdoor air temperature for the location. They are not used in other models.
    '''

january_surface_ground_temperature [data] (Default: 13.0)
february_surface_ground_temperature [data] (Default: 13.0)
march_surface_ground_temperature [data] (Default: 13.0)
april_surface_ground_temperature [data] (Default: 13.0)
may_surface_ground_temperature [data] (Default: 13.0)
june_surface_ground_temperature [data] (Default: 13.0)
july_surface_ground_temperature [data] (Default: 13.0)
august_surface_ground_temperature [data] (Default: 13.0)
september_surface_ground_temperature [data] (Default: 13.0)
october_surface_ground_temperature [data] (Default: 13.0)
november_surface_ground_temperature [data] (Default: 13.0)
december_surface_ground_temperature [data] (Default: 13.0)

class Site:GroundTemperature:Deep():
    '''
    These temperatures are specifically for the ground heat exchangers that would use “deep” (3-4 m depth) ground temperatures for their heat source. They are not used in other models.
    '''

january_deep_ground_temperature [data] (Default: 16.0)
february_deep_ground_temperature [data] (Default: 16.0)
march_deep_ground_temperature [data] (Default: 16.0)
april_deep_ground_temperature [data] (Default: 16.0)
may_deep_ground_temperature [data] (Default: 16.0)
june_deep_ground_temperature [data] (Default: 16.0)
july_deep_ground_temperature [data] (Default: 16.0)
august_deep_ground_temperature [data] (Default: 16.0)
september_deep_ground_temperature [data] (Default: 16.0)
october_deep_ground_temperature [data] (Default: 16.0)
november_deep_ground_temperature [data] (Default: 16.0)
december_deep_ground_temperature [data] (Default: 16.0)

class Site:GroundTemperature:Undisturbed:FiniteDifference():
    '''
    Undisturbed ground temperature object using a detailed finite difference 1-D model
    '''

soil_thermal_conductivity [data]
soil_density [data]
soil_specific_heat [data]
soil_moisture_content_volume_fraction [data] (Default: 30.0)
soil_moisture_content_volume_fraction_at_saturation [data] (Default: 50.0)
evapotranspiration_ground_cover_parameter [data] (Default: 0.4)

class Site:GroundTemperature:Undisturbed:KusudaAchenbach():
    '''
    Undisturbed ground temperature object using the Kusuda-Achenbach 1965 correlation.
    '''

soil_thermal_conductivity [data]
soil_density [data]
soil_specific_heat [data]
average_soil_surface_temperature [data]
average_amplitude_of_surface_temperature [data]
phase_shift_of_minimum_surface_temperature [data]

class Site:GroundTemperature:Undisturbed:Xing():
    '''
    Undisturbed ground temperature object using the Xing 2014 2 harmonic parameter model.
    '''

soil_thermal_conductivity [data]
soil_density [data]
soil_specific_heat [data]
average_soil_surface_tempeature [data]
soil_surface_temperature_amplitude_1 [data]
soil_surface_temperature_amplitude_2 [data]
phase_shift_of_temperature_amplitude_1 [data]
phase_shift_of_temperature_amplitude_2 [data]

class Site:GroundDomain:Slab():
    '''
    Ground-coupled slab model for on-grade and in-grade cases with or without insulation.
    '''

ground_domain_depth [data] (Default: 10.0)
aspect_ratio [data] (Default: 1.0)
perimeter_offset [data] (Default: 5.0)
soil_thermal_conductivity [data] (Default: 1.5)
soil_density [data] (Default: 2800.0)
soil_specific_heat [data] (Default: 850.0)
soil_moisture_content_volume_fraction [data] (Default: 30.0)
soil_moisture_content_volume_fraction_at_saturation [data] (Default: 50.0)
undisturbed_ground_temperature_model_type [data]
undisturbed_ground_temperature_model_name [data]
evapotranspiration_ground_cover_parameter [data] (Default: 0.4)
slab_boundary_condition_model_name [data]
slab_location [data]
slab_material_name [data]
horizontal_insulation [data] (Default: No)
horizontal_insulation_material_name [data]
horizontal_insulation_extents [data] (Default: Full)
perimeter_insulation_width [data]
vertical_insulation [data] (Default: No)
vertical_insulation_material_name [data]
vertical_insulation_depth [data]
simulation_timestep [data] (Default: Hourly)
geometric_mesh_coefficient [data] (Default: 1.6)
mesh_density_parameter [data] (Default: 6.0)

class Site:GroundDomain:Basement():
    '''
    Ground-coupled basement model for simulating basements or other underground zones.
    '''

ground_domain_depth [data] (Default: 10.0)
aspect_ratio [data] (Default: 1.0)
perimeter_offset [data] (Default: 5.0)
soil_thermal_conductivity [data] (Default: 1.5)
soil_density [data] (Default: 2800.0)
soil_specific_heat [data] (Default: 850.0)
soil_moisture_content_volume_fraction [data] (Default: 30.0)
soil_moisture_content_volume_fraction_at_saturation [data] (Default: 50.0)
undisturbed_ground_temperature_model_type [data]
undisturbed_ground_temperature_model_name [data]
evapotranspiration_ground_cover_parameter [data] (Default: 0.4)
basement_floor_boundary_condition_model_name [data]
horizontal_insulation [data] (Default: No)
horizontal_insulation_material_name [data]
horizontal_insulation_extents [data] (Default: Full)
perimeter_horizontal_insulation_width [data]
basement_wall_depth [data]
basement_wall_boundary_condition_model_name [data]
vertical_insulation [data] (Default: No)
basement_wall_vertical_insulation_material_name [data]
vertical_insulation_depth [data]
simulation_timestep [data] (Default: Hourly)
mesh_density_parameter [data] (Default: 4.0)

class Site:GroundReflectance():
    '''
    Specifies the ground reflectance values used to calculate ground reflected solar. The ground reflectance can be further modified when snow is on the ground by Site:GroundReflectance:SnowModifier.
    '''

january_ground_reflectance [data] (Default: 0.2)
february_ground_reflectance [data] (Default: 0.2)
march_ground_reflectance [data] (Default: 0.2)
april_ground_reflectance [data] (Default: 0.2)
may_ground_reflectance [data] (Default: 0.2)
june_ground_reflectance [data] (Default: 0.2)
july_ground_reflectance [data] (Default: 0.2)
august_ground_reflectance [data] (Default: 0.2)
september_ground_reflectance [data] (Default: 0.2)
october_ground_reflectance [data] (Default: 0.2)
november_ground_reflectance [data] (Default: 0.2)
december_ground_reflectance [data] (Default: 0.2)

class Site:GroundReflectance:SnowModifier():
    '''
    Specifies ground reflectance multipliers when snow resident on the ground. These multipliers are applied to the “normal” ground reflectances specified in Site:GroundReflectance.
    '''

ground_reflected_solar_modifier [data] (Default: 1.0)
daylighting_ground_reflected_solar_modifier [data] (Default: 1.0)

class Site:WaterMainsTemperature():
    '''
    Used to calculate water mains temperatures delivered by underground water main pipes. Water mains temperatures are a function of outdoor climate conditions and vary with time of year.
    '''

calculation_method [data] (Default: CorrelationFromWeatherFile)
temperature_schedule_name [data]
annual_average_outdoor_air_temperature [data]
maximum_difference_in_monthly_average_outdoor_air_temperatures [data]

class Site:Precipitation():
    '''
    Used to describe the amount of water precipitation at the building site. Precipitation includes both rain and the equivalent water content of snow.
    '''

precipitation_model_type [data]
design_level_for_total_annual_precipitation [data]
precipitation_rates_schedule_name [data]
average_total_annual_precipitation [data]

class RoofIrrigation():
    '''
    Used to describe the amount of irrigation on the ecoroof surface over the course of the simulation runperiod.
    '''

irrigation_model_type [data]
irrigation_rate_schedule_name [data]
irrigation_maximum_saturation_threshold [data] (Default: 40.0)

class Site:SolarAndVisibleSpectrum():
    '''
    If this object is omitted, the default solar and visible spectrum data will be used.
    '''

spectrum_data_method [data] (Default: Default)
solar_spectrum_data_object_name [data]
visible_spectrum_data_object_name [data]

class Site:SpectrumData():
    '''
    Spectrum Data Type is followed by up to 107 sets of normal-incidence measured values of [wavelength, spectrum] for wavelengths covering the solar (0.25 to 2.5 microns) or visible spectrum (0.38 to 0.78 microns)
    '''

spectrum_data_type [data]
wavelength [data]
spectrum [data]
wavelength_1 [data]
spectrum_2 [data]
extensions [Array of {wavelength, spectrum}]
"""