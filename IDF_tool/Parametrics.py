"""
# Parametrics
"""
"""
Parametric:SetValueForRun
Parametric objects allow a set of multiple simulations to be defined in a single idf file. The parametric preprocessor scans the idf for Parametric:* objects then creates and runs multiple idf files, one for each defined simulation. The core parametric object is Parametric:SetValueForRun which defines the name of a parameter and sets the parameter to different values depending on which run is being simulated.

Fields

values [Array of {value_for_run}]
Parametric:Logic
This object allows some types of objects to be included for some parametric cases and not for others. For example, you might want an overhang on a window in some parametric runs and not others. A single Parametric:Logic object is allowed per file. Consult the Input Output Reference for available commands and syntax.

Fields

lines [Array of {parametric_logic_line}]
Parametric:RunControl
Controls which parametric runs are simulated. This object is optional. If it is not included, then all parametric runs are performed.

Fields

runs [Array of {perform_run}]
Parametric:FileNameSuffix
Defines the suffixes to be appended to the idf and output file names for each parametric run. If this object is omitted, the suffix will default to the run number.

Fields

suffixes [Array of {suffix_for_file_name_in_run}]
"""