"""
# Performance Tables
"""
"""
Table:IndependentVariable
An independent variable representing a single dimension of a Table:Lookup object.

Fields

interpolation_method [string] (Default: Linear)
extrapolation_method [string] (Default: Constant)
minimum_value [number]
maximum_value [number]
normalization_reference_value [number]
unit_type [string] (Default: Dimensionless)
external_file_name [string]
external_file_column_number [number]
external_file_starting_row_number [number]
values [Array of {value}]
Table:IndependentVariableList
A sorted list of independent variables used by one or more Table:Lookup objects.

Fields

independent_variables [Array of {independent_variable_name}]
Table:Lookup
Lookup tables are used in place of curves and can represent any number of independent variables (defined as Table:IndependentVariable objects in a Table:IndependentVariableList). Output values are interpolated within the bounds defined by each independent variable and extrapolated beyond the bounds according to the interpolation/extrapolation methods defined by each independent variable.

Fields

independent_variable_list_name [string]
normalization_method [string] (Default: None)
normalization_divisor [number] (Default: 1.0)
minimum_output [number]
maximum_output [number]
output_unit_type [string] (Default: Dimensionless)
external_file_name [string]
external_file_column_number [number]
external_file_starting_row_number [number]
values [Array of {output_value}]
"""