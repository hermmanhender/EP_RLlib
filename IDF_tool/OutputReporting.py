"""
# Output Reporting
"""
"""
Output:VariableDictionary
Produces a list summarizing the output variables and meters that are available for reporting for the model being simulated (rdd output file). The list varies depending on the types of objects present in the idf file. For example, variables related to lights will only appear if a Lights object is present. The IDF option generates complete Output:Variable objects to simplify adding the desired output to the idf file.

Fields

key_field [string] (Default: regular)
sort_option [string]
Output:Surfaces:List
Produces a report summarizing the details of surfaces in the eio output file.

Fields

report_type [string]
report_specifications [string]
Output:Surfaces:Drawing
Produces reports/files that are capable of rendering graphically or being imported into other programs. Rendering does not alter the actual inputs/surfaces.

Fields

report_type [string]
report_specifications_1 [string] (Default: Triangulate3DFace)
report_specifications_2 [string]
Output:Schedules
Produces a condensed reporting that illustrates the full range of schedule values in the eio output file. In the style of input: DaySchedule, WeekSchedule, and Annual Schedule.

Fields

key_field [string]
Output:Constructions
Adds a report to the eio output file which shows details for each construction, including overall properties, a list of material layers, and calculated results related to conduction transfer functions.

Fields

details_type_1 [string]
details_type_2 [string]
Output:EnergyManagementSystem
This object is used to control the output produced by the Energy Management System

Fields

actuator_availability_dictionary_reporting [string] (Default: None)
internal_variable_availability_dictionary_reporting [string] (Default: None)
ems_runtime_language_debug_output_level [string] (Default: None)
OutputControl:SurfaceColorScheme
This object is used to set colors for reporting on various building elements particularly for the DXF reports. We know the user can enter 0 to 255 and the color map is available in DXF output. Therefore, we are limiting the colors in that range. You can extend by editing the IDD but you do so on your own. Colors not changed in any scheme will remain as the default scheme uses.

Fields

drawing_element_1_type [string]
color_for_drawing_element_1 [number]
drawing_element_2_type [string]
color_for_drawing_element_2 [number]
drawing_element_3_type [string]
color_for_drawing_element_3 [number]
drawing_element_4_type [string]
color_for_drawing_element_4 [number]
drawing_element_5_type [string]
color_for_drawing_element_5 [number]
drawing_element_6_type [string]
color_for_drawing_element_6 [number]
drawing_element_7_type [string]
color_for_drawing_element_7 [number]
drawing_element_8_type [string]
color_for_drawing_element_8 [number]
drawing_element_9_type [string]
color_for_drawing_element_9 [number]
drawing_element_10_type [string]
color_for_drawing_element_10 [number]
drawing_element_11_type [string]
color_for_drawing_element_11 [number]
drawing_element_12_type [string]
color_for_drawing_element_12 [number]
drawing_element_13_type [string]
color_for_drawing_element_13 [number]
drawing_element_14_type [string]
color_for_drawing_element_14 [number]
drawing_element_15_type [string]
color_for_drawing_element_15 [number]
Output:Table:SummaryReports
This object allows the user to call report types that are predefined and will appear with the other tabular reports. These predefined reports are sensitive to the OutputControl:Table:Style object and appear in the same files as the tabular reports. The entries for this object is a list of the predefined reports that should appear in the tabular report output file.

Fields

reports [Array of {report_name}]
Output:Table:TimeBins
Produces a bin report in the table output file which shows the amount of time in hours that occurs in different bins for a single specific output variable or meter. Two different types of binning are reported: by month and by hour of the day.

Fields

key_value [string] (Default: *)
variable_name [string]
interval_start [number]
interval_size [number]
interval_count [number]
schedule_name [string]
variable_type [string]
Output:Table:Monthly
Provides a generic method of setting up tables of monthly results. The report has multiple columns that are each defined using a repeated group of fields for any number of columns. A single Output:Table:Monthly object often produces multiple tables in the output. A table is produced for every instance of a particular output variable. For example, a table defined with zone variables will be produced once for every zone.

Fields

digits_after_decimal [number] (Default: 2.0)
variable_details [Array of {variable_or_meter_name, aggregation_type_for_variable_or_meter}]
Output:Table:Annual
Provides a generic method of setting up tables of annual results with one row per object. The report has multiple columns that are each defined using a repeated group of fields for any number of columns. A single Output:Table:Annual produces a single table in the output.

Fields

filter [string]
schedule_name [string]
variable_details [Array of {variable_or_meter_or_ems_variable_or_field_name, aggregation_type_for_variable_or_meter, digits_after_decimal}]
OutputControl:Table:Style
default style for the OutputControl:Table:Style is comma – this works well for importing into spreadsheet programs such as Excel(tm) but not so well for word processing programs – there tab may be a better choice. fixed puts spaces between the “columns”. HTML produces tables in HTML. XML produces an XML file. note - if no OutputControl:Table:Style is included, the defaults are comma and None.

Fields

column_separator [string] (Default: Comma)
unit_conversion [string] (Default: None)
OutputControl:ReportingTolerances
Calculations of the time that setpoints are not met use a tolerance of 0.2C. This object allows changing the tolerance used to determine when setpoints are being met.

Fields

tolerance_for_time_heating_setpoint_not_met [number] (Default: 0.2)
tolerance_for_time_cooling_setpoint_not_met [number] (Default: 0.2)
Output:Variable
each Output:Variable command picks variables to be put onto the standard output file (.eso) some variables may not be reported for every simulation. a list of variables that can be reported are available after a run on the report dictionary file (.rdd) if the Output:VariableDictionary has been requested.

Fields

key_value [string] (Default: *)
variable_name [string]
reporting_frequency [string] (Default: Hourly)
schedule_name [string]
Output:Meter
Each Output:Meter command picks meters to be put onto the standard output file (.eso) and meter file (.mtr). Not all meters are reported in every simulation. A list of meters that can be reported are available after a run on the meter dictionary file (.mdd) if the Output:VariableDictionary has been requested.

Fields

key_name [string]
reporting_frequency [string] (Default: Hourly)
Output:Meter:MeterFileOnly
Each Output:Meter:MeterFileOnly command picks meters to be put only onto meter file (.mtr). Not all meters are reported in every simulation. A list of meters that can be reported a list of meters that can be reported are available after a run on the meter dictionary file (.mdd) if the Output:VariableDictionary has been requested.

Fields

key_name [string]
reporting_frequency [string] (Default: Hourly)
Output:Meter:Cumulative
Each Output:Meter:Cumulative command picks meters to be reported cumulatively onto the standard output file (.eso) and meter file (.mtr). Not all meters are reported in every simulation. a list of meters that can be reported are available after a run on the meter dictionary file (.mdd) if the Output:VariableDictionary has been requested.

Fields

key_name [string]
reporting_frequency [string] (Default: Hourly)
Output:Meter:Cumulative:MeterFileOnly
Each Output:Meter:Cumulative:MeterFileOnly command picks meters to be reported cumulatively onto the standard output file (.eso) and meter file (.mtr). Not all meters are reported in every simulation. a list of meters that can be reported are available after a run on the meter dictionary file (.mdd) if the Output:VariableDictionary has been requested.

Fields

key_name [string]
reporting_frequency [string] (Default: Hourly)
Meter:Custom
Used to allow users to combine specific variables and/or meters into “custom” meter configurations. To access these meters by name, one must first run a simulation to generate the RDD/MDD files and names. A Meter:Custom cannot reference another Meter:Custom.

Fields

resource_type [string]
variable_details [Array of {key_name, output_variable_or_meter_name}]
Meter:CustomDecrement
Used to allow users to combine specific variables and/or meters into “custom” meter configurations. To access these meters by name, one must first run a simulation to generate the RDD/MDD files and names.

Fields

resource_type [string]
source_meter_name [string]
variable_details [Array of {key_name, output_variable_or_meter_name}]
OutputControl:Files
Conditionally turn on/off output from EnergyPlus.

Fields

output_csv [string] (Default: No)
output_mtr [string] (Default: Yes)
output_eso [string] (Default: Yes)
output_eio [string] (Default: Yes)
output_tabular [string] (Default: Yes)
output_sqlite [string] (Default: Yes)
output_json [string] (Default: Yes)
output_audit [string] (Default: Yes)
output_zone_sizing [string] (Default: Yes)
output_system_sizing [string] (Default: Yes)
output_dxf [string] (Default: Yes)
output_bnd [string] (Default: Yes)
output_rdd [string] (Default: Yes)
output_mdd [string] (Default: Yes)
output_mtd [string] (Default: Yes)
output_end [string] (Default: Yes)
output_shd [string] (Default: Yes)
output_dfs [string] (Default: Yes)
output_glhe [string] (Default: Yes)
output_delightin [string] (Default: Yes)
output_delighteldmp [string] (Default: Yes)
output_delightdfdmp [string] (Default: Yes)
output_edd [string] (Default: Yes)
output_dbg [string] (Default: Yes)
output_perflog [string] (Default: Yes)
output_sln [string] (Default: Yes)
output_sci [string] (Default: Yes)
output_wrl [string] (Default: Yes)
output_screen [string] (Default: Yes)
output_extshd [string] (Default: Yes)
output_tarcog [string] (Default: Yes)
Output:JSON
Output from EnergyPlus can be written to JSON format files.

Fields

option_type [string]
output_json [string] (Default: Yes)
output_cbor [string] (Default: No)
output_messagepack [string] (Default: No)
Output:SQLite
Output from EnergyPlus can be written to an SQLite format file.

Fields

option_type [string]
unit_conversion_for_tabular_data [string] (Default: UseOutputControlTableStyle)
Output:EnvironmentalImpactFactors
This is used to Automatically report the facility meters and turn on the Environmental Impact Report calculations for all of the Environmental Factors.

Fields

reporting_frequency [string]
EnvironmentalImpactFactors
Used to help convert district and ideal energy use to a fuel type and provide total carbon equivalent with coefficients Also used in Source=>Site conversions.

Fields

district_heating_efficiency [number] (Default: 0.3)
district_cooling_cop [number] (Default: 3.0)
steam_conversion_efficiency [number] (Default: 0.25)
total_carbon_equivalent_emission_factor_from_n2o [number] (Default: 80.7272)
total_carbon_equivalent_emission_factor_from_ch4 [number] (Default: 6.2727)
total_carbon_equivalent_emission_factor_from_co2 [number] (Default: 0.2727)
FuelFactors
Provides Fuel Factors for Emissions as well as Source=>Site conversions. OtherFuel1, OtherFuel2 provide options for users who want to create and use fuels that may not be mainstream (biomass, wood, pellets).

Fields

existing_fuel_resource_name [string]
units_of_measure [string]
energy_per_unit_factor [number]
source_energy_factor [number]
source_energy_schedule_name [string]
co2_emission_factor [number]
co2_emission_factor_schedule_name [string]
co_emission_factor [number]
co_emission_factor_schedule_name [string]
ch4_emission_factor [number]
ch4_emission_factor_schedule_name [string]
nox_emission_factor [number]
nox_emission_factor_schedule_name [string]
n2o_emission_factor [number]
n2o_emission_factor_schedule_name [string]
so2_emission_factor [number]
so2_emission_factor_schedule_name [string]
pm_emission_factor [number]
pm_emission_factor_schedule_name [string]
pm10_emission_factor [number]
pm10_emission_factor_schedule_name [string]
pm2_5_emission_factor [number]
pm2_5_emission_factor_schedule_name [string]
nh3_emission_factor [number]
nh3_emission_factor_schedule_name [string]
nmvoc_emission_factor [number]
nmvoc_emission_factor_schedule_name [string]
hg_emission_factor [number]
hg_emission_factor_schedule_name [string]
pb_emission_factor [number]
pb_emission_factor_schedule_name [string]
water_emission_factor [number]
water_emission_factor_schedule_name [string]
nuclear_high_level_emission_factor [number]
nuclear_high_level_emission_factor_schedule_name [string]
nuclear_low_level_emission_factor [number]
nuclear_low_level_emission_factor_schedule_name [string]
Output:Diagnostics
Special keys to produce certain warning messages or effect certain simulation characteristics.

Fields

diagnostics [Array of {key}]
Output:DebuggingData
switch eplusout.dbg file on or off

Fields

report_debugging_data [string] (Default: No)
report_during_warmup [string] (Default: No)
Output:PreprocessorMessage
This object does not come from a user input. This is generated by a pre-processor so that various conditions can be gracefully passed on by the InputProcessor.

Fields

preprocessor_name [string]
error_severity [string]
message_line_1 [string]
message_line_2 [string]
message_line_3 [string]
message_line_4 [string]
message_line_5 [string]
message_line_6 [string]
message_line_7 [string]
message_line_8 [string]
message_line_9 [string]
message_line_10 [string]
"""