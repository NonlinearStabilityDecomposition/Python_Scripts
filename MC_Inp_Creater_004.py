# Script to modify an Abaqus INP file and create multiple outputs
# Replace *NODE and *ELEMENT sections for each scenario

# Define the original INP file path
original_inp_path = "Dummy_scaled_0_01.inp"  # Change this to your file path

# Define the scenarios with the node and element file replacements
scenarios = [
    {"nodes": "IW1_17_scaled_nodes_1.000.txt", "elements": "IW1_17_scaled_elements_1.000.txt", "output": "IW1_17_scaled.inp"},
    {"nodes": "IW1_18_scaled_nodes_1.000.txt", "elements": "IW1_18_scaled_elements_1.000.txt", "output": "IW1_18_scaled.inp"},
    {"nodes": "IW1_19_scaled_nodes_1.000.txt", "elements": "IW1_19_scaled_elements_1.000.txt", "output": "IW1_19_scaled.inp"},
    {"nodes": "IW1_20_scaled_nodes_1.000.txt", "elements": "IW1_20_scaled_elements_1.000.txt", "output": "IW1_20_scaled.inp"},
    {"nodes": "IW1_21_scaled_nodes_1.000.txt", "elements": "IW1_21_scaled_elements_1.000.txt", "output": "IW1_21_scaled.inp"},
    {"nodes": "IW1_22_scaled_nodes_1.000.txt", "elements": "IW1_22_scaled_elements_1.000.txt", "output": "IW1_22_scaled.inp"},
    {"nodes": "IW1_23_scaled_nodes_1.000.txt", "elements": "IW1_23_scaled_elements_1.000.txt", "output": "IW1_23_scaled.inp"},
    {"nodes": "IW1_24_scaled_nodes_1.000.txt", "elements": "IW1_24_scaled_elements_1.000.txt", "output": "IW1_24_scaled.inp"},
    {"nodes": "IW1_25_scaled_nodes_1.000.txt", "elements": "IW1_25_scaled_elements_1.000.txt", "output": "IW1_25_scaled.inp"},
    {"nodes": "IW1_26_scaled_nodes_1.000.txt", "elements": "IW1_26_scaled_elements_1.000.txt", "output": "IW1_26_scaled.inp"},
    {"nodes": "IW1_27_scaled_nodes_1.000.txt", "elements": "IW1_27_scaled_elements_1.000.txt", "output": "IW1_27_scaled.inp"},
    {"nodes": "IW1_28_scaled_nodes_1.000.txt", "elements": "IW1_28_scaled_elements_1.000.txt", "output": "IW1_28_scaled.inp"},
    {"nodes": "IW1_29_scaled_nodes_1.000.txt", "elements": "IW1_29_scaled_elements_1.000.txt", "output": "IW1_29_scaled.inp"},
    {"nodes": "IW1_30_scaled_nodes_1.000.txt", "elements": "IW1_30_scaled_elements_1.000.txt", "output": "IW1_30_scaled.inp"},
    {"nodes": "IW1_31_scaled_nodes_1.000.txt", "elements": "IW1_31_scaled_elements_1.000.txt", "output": "IW1_31_scaled.inp"},
    {"nodes": "IW1_32_scaled_nodes_1.000.txt", "elements": "IW1_32_scaled_elements_1.000.txt", "output": "IW1_32_scaled.inp"},
    {"nodes": "IW1_33_scaled_nodes_1.000.txt", "elements": "IW1_33_scaled_elements_1.000.txt", "output": "IW1_33_scaled.inp"},
    {"nodes": "IW1_34_scaled_nodes_1.000.txt", "elements": "IW1_34_scaled_elements_1.000.txt", "output": "IW1_34_scaled.inp"},
    {"nodes": "IW1_35_scaled_nodes_1.000.txt", "elements": "IW1_35_scaled_elements_1.000.txt", "output": "IW1_35_scaled.inp"},
    {"nodes": "IW1_36_scaled_nodes_1.000.txt", "elements": "IW1_36_scaled_elements_1.000.txt", "output": "IW1_36_scaled.inp"},
    {"nodes": "IW1_37_scaled_nodes_1.000.txt", "elements": "IW1_37_scaled_elements_1.000.txt", "output": "IW1_37_scaled.inp"},
    {"nodes": "IW1_38_scaled_nodes_1.000.txt", "elements": "IW1_38_scaled_elements_1.000.txt", "output": "IW1_38_scaled.inp"},
    {"nodes": "IW1_39_scaled_nodes_1.000.txt", "elements": "IW1_39_scaled_elements_1.000.txt", "output": "IW1_39_scaled.inp"},
    {"nodes": "IW1_40_scaled_nodes_1.000.txt", "elements": "IW1_40_scaled_elements_1.000.txt", "output": "IW1_40_scaled.inp"},
    {"nodes": "IW1_41_scaled_nodes_1.000.txt", "elements": "IW1_41_scaled_elements_1.000.txt", "output": "IW1_41_scaled.inp"},
    {"nodes": "IW1_42_scaled_nodes_1.000.txt", "elements": "IW1_42_scaled_elements_1.000.txt", "output": "IW1_42_scaled.inp"},
    {"nodes": "IW1_43_scaled_nodes_1.000.txt", "elements": "IW1_43_scaled_elements_1.000.txt", "output": "IW1_43_scaled.inp"},
    {"nodes": "IW1_44_scaled_nodes_1.000.txt", "elements": "IW1_44_scaled_elements_1.000.txt", "output": "IW1_44_scaled.inp"},
    {"nodes": "IW1_45_scaled_nodes_1.000.txt", "elements": "IW1_45_scaled_elements_1.000.txt", "output": "IW1_45_scaled.inp"},
    {"nodes": "IW1_46_scaled_nodes_1.000.txt", "elements": "IW1_46_scaled_elements_1.000.txt", "output": "IW1_46_scaled.inp"},
    {"nodes": "IW1_47_scaled_nodes_1.000.txt", "elements": "IW1_47_scaled_elements_1.000.txt", "output": "IW1_47_scaled.inp"},
    {"nodes": "N_6_scaled_nodes_1.000.txt"   , "elements": "N_6_scaled_elements_1.000.txt"   , "output": "IW1_48_scaled.inp"},
    {"nodes": "N_9_scaled_nodes_1.000.txt"   , "elements": "N_9_scaled_elements_1.000.txt"   , "output": "IW1_49_scaled.inp"},
    {"nodes": "N_11_scaled_nodes_1.000.txt"  , "elements": "N_11_scaled_elements_1.000.txt"  , "output": "IW1_50_scaled.inp"},
    {"nodes": "B_1_scaled_nodes_1.000.txt"   , "elements": "B_1_scaled_elements_1.000.txt"   , "output": "IW1_51_scaled.inp"},
    {"nodes": "B_2_scaled_nodes_1.000.txt"   , "elements": "B_2_scaled_elements_1.000.txt"   , "output": "IW1_52_scaled.inp"},
    {"nodes": "B_3_scaled_nodes_1.000.txt"   , "elements": "B_3_scaled_elements_1.000.txt"   , "output": "IW1_53_scaled.inp"},
    {"nodes": "B_4_scaled_nodes_1.000.txt"   , "elements": "B_4_scaled_elements_1.000.txt"   , "output": "IW1_54_scaled.inp"},
    {"nodes": "ST_1_scaled_nodes_1.000.txt"  , "elements": "ST_1_scaled_elements_1.000.txt"  , "output": "IW1_55_scaled.inp"},
    {"nodes": "ST_2_scaled_nodes_1.000.txt"  , "elements": "ST_2_scaled_elements_1.000.txt"  , "output": "IW1_56_scaled.inp"},
    {"nodes": "ST_3_scaled_nodes_1.000.txt"  , "elements": "ST_3_scaled_elements_1.000.txt"  , "output": "IW1_57_scaled.inp"},
    {"nodes": "ST_4_scaled_nodes_1.000.txt"  , "elements": "ST_4_scaled_elements_1.000.txt"  , "output": "IW1_58_scaled.inp"},
    {"nodes": "ST_5_scaled_nodes_1.000.txt"  , "elements": "ST_5_scaled_elements_1.000.txt"  , "output": "IW1_59_scaled.inp"},
    {"nodes": "ST_6_scaled_nodes_1.000.txt"  , "elements": "ST_6_scaled_elements_1.000.txt"  , "output": "IW1_60_scaled.inp"},

    {"nodes": "S1_89_scaled_nodes_1.000.txt" , "elements": "S1_89_scaled_elements_1.000.txt" , "output": "IW1_61_scaled.inp"},
    {"nodes": "S2_89_scaled_nodes_1.000.txt" , "elements": "S2_89_scaled_elements_1.000.txt" , "output": "IW1_62_scaled.inp"},
    {"nodes": "S3_89_scaled_nodes_1.000.txt" , "elements": "S3_89_scaled_elements_1.000.txt" , "output": "IW1_63_scaled.inp"},
    {"nodes": "S4_89_scaled_nodes_1.000.txt" , "elements": "S4_89_scaled_elements_1.000.txt" , "output": "IW1_64_scaled.inp"},
    {"nodes": "S5_89_scaled_nodes_1.000.txt" , "elements": "S5_89_scaled_elements_1.000.txt" , "output": "IW1_65_scaled.inp"},
    {"nodes": "S1_178_scaled_nodes_1.000.txt", "elements": "S1_178_scaled_elements_1.000.txt", "output": "IW1_66_scaled.inp"},
    {"nodes": "S2_178_scaled_nodes_1.000.txt", "elements": "S2_178_scaled_elements_1.000.txt", "output": "IW1_67_scaled.inp"},
    {"nodes": "S3_178_scaled_nodes_1.000.txt", "elements": "S3_178_scaled_elements_1.000.txt", "output": "IW1_68_scaled.inp"},
    {"nodes": "S4_178_scaled_nodes_1.000.txt", "elements": "S4_178_scaled_elements_1.000.txt", "output": "IW1_69_scaled.inp"},
    {"nodes": "S5_178_scaled_nodes_1.000.txt", "elements": "S5_178_scaled_elements_1.000.txt", "output": "IW1_70_scaled.inp"}
    
    
]

# Read the original INP file
with open(original_inp_path, "r") as inp_file:
    inp_content = inp_file.readlines()

# Process each scenario and generate the corresponding INP file
for scenario in scenarios:
    modified_content = []
    for line in inp_content:
        # Replace *NODE section
        if "*NODE,INPUT=" in line:
            line = f"*NODE,INPUT={scenario['nodes']}\n"
        # Replace *ELEMENT section
        elif "*ELEMENT, TYPE=S4R, ELSET=ESHELL,INPUT=" in line:
            line = f"*ELEMENT, TYPE=S4R, ELSET=ESHELL,INPUT={scenario['elements']}\n"
        modified_content.append(line)
    
    # Write the modified content to the new INP file
    with open(scenario["output"], "w") as output_file:
        output_file.writelines(modified_content)
    print(f"Generated: {scenario['output']}")

print("All INP files have been successfully generated.")
