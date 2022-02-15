"""
# Schedules
"""


"""

class ScheduleTypeLimits():
    '''
    ScheduleTypeLimits specifies the data types and limits for the values contained in schedules
    '''

lower_limit_value [number]
upper_limit_value [number]
numeric_type [string]
unit_type [string] (Default: Dimensionless)

class Schedule:Day:Hourly():
    '''
    A Schedule:Day:Hourly contains 24 values for each hour of the day.
    '''

schedule_type_limits_name [string]
hour_1 [number] (Default: 0.0)
hour_2 [number] (Default: 0.0)
hour_3 [number] (Default: 0.0)
hour_4 [number] (Default: 0.0)
hour_5 [number] (Default: 0.0)
hour_6 [number] (Default: 0.0)
hour_7 [number] (Default: 0.0)
hour_8 [number] (Default: 0.0)
hour_9 [number] (Default: 0.0)
hour_10 [number] (Default: 0.0)
hour_11 [number] (Default: 0.0)
hour_12 [number] (Default: 0.0)
hour_13 [number] (Default: 0.0)
hour_14 [number] (Default: 0.0)
hour_15 [number] (Default: 0.0)
hour_16 [number] (Default: 0.0)
hour_17 [number] (Default: 0.0)
hour_18 [number] (Default: 0.0)
hour_19 [number] (Default: 0.0)
hour_20 [number] (Default: 0.0)
hour_21 [number] (Default: 0.0)
hour_22 [number] (Default: 0.0)
hour_23 [number] (Default: 0.0)
hour_24 [number] (Default: 0.0)

class Schedule:Day:Interval():
    '''
    A Schedule:Day:Interval contains a full day of values with specified end times for each value Currently, is set up to allow for 10 minute intervals for an entire day.
    '''

schedule_type_limits_name [string]
interpolate_to_timestep [string] (Default: No)
data [Array of {time, value_until_time}]

class Schedule:Day:List():
    '''
    Schedule:Day:List will allow the user to list 24 hours worth of values, which can be sub-hourly in nature.
    '''

schedule_type_limits_name [string]
interpolate_to_timestep [string] (Default: No)
minutes_per_item [number]
extensions [Array of {value}]

class Schedule:Week:Daily():
    '''
    A Schedule:Week:Daily contains 12 Schedule:Day:Hourly objects, one for each day type.
    '''

sunday_schedule_day_name [string]
monday_schedule_day_name [string]
tuesday_schedule_day_name [string]
wednesday_schedule_day_name [string]
thursday_schedule_day_name [string]
friday_schedule_day_name [string]
saturday_schedule_day_name [string]
holiday_schedule_day_name [string]
summerdesignday_schedule_day_name [string]
winterdesignday_schedule_day_name [string]
customday1_schedule_day_name [string]
customday2_schedule_day_name [string]

class Schedule:Week:Compact():
    '''
    Compact definition for Schedule:Day:List
    '''

data [Array of {daytype_list, schedule_day_name}]

class Schedule:Year():
    '''
    A Schedule:Year contains from 1 to 52 week schedules
    '''

schedule_type_limits_name [string]
schedule_weeks [Array of {schedule_week_name, start_month, start_day, end_month, end_day}]

class Schedule:Compact():
    '''
    Irregular object. Does not follow the usual definition for fields. Fields A3… are: Through: Date For: Applicable days (ref: Schedule:Week:Compact) Interpolate: Average/Linear/No (ref: Schedule:Day:Interval) – optional, if not used will be “No” Until: <Time> (ref: Schedule:Day:Interval) <numeric value> words “Through”,”For”,”Interpolate”,”Until” must be included.
    '''

schedule_type_limits_name [string]
data [Array of {field}]

class Schedule:Constant():
    '''
    Constant hourly value for entire year.
    '''

schedule_type_limits_name [string]
hourly_value [number] (Default: 0.0)

class Schedule:File:Shading():
    '''
    A Schedule:File:Shading points to a CSV file that has 8760-8784 hours of sunlit fraction data for all or some of the exterior surfaces.
    '''

file_name [string]
"""
class Schedule_File():
    '''
    A Schedule:File points to a text computer file that has 8760-8784 hours of data.
    '''
    def schedule_type_limits_name(epJSON, ObjectName, data):
        """
        data is a string
        """
        epJSON['Schedule:File'][ObjectName]['schedule_type_limits_name'] = data
        return epJSON

    def file_name(epJSON, ObjectName, data):
        """
        data is a string
        """
        epJSON['Schedule:File'][ObjectName]['file_name'] = data
        return epJSON

    def column_number(epJSON, ObjectName, data):
        """
        data is a number
        """
        epJSON['Schedule:File'][ObjectName]['column_number'] = data
        return epJSON

    def rows_to_skip_at_top(epJSON, ObjectName, data):
        """
        data is a number
        """
        epJSON['Schedule:File'][ObjectName]['rows_to_skip_at_top'] = data
        return epJSON

    def number_of_hours_of_data(epJSON, ObjectName, data=8760.0):
        """
        Default: 8760.0
        """
        epJSON['Schedule:File'][ObjectName]['number_of_hours_of_data'] = data
        return epJSON

    def column_separator(epJSON, ObjectName, data):
        """
        Default: Comma
        """
        epJSON['Schedule:File'][ObjectName]['column_separator'] = data
        return epJSON

    def interpolate_to_timestep(epJSON, ObjectName, data):
        """
        Default: No
        """
        epJSON['Schedule:File'][ObjectName]['interpolate_to_timestep'] = data
        return epJSON

    def minutes_per_item(epJSON, ObjectName, data):
        """
        data is a number
        """
        epJSON['Schedule:File'][ObjectName]['minutes_per_item'] = data
        return epJSON
