# Description : Script to generate the ELOG TB Components
# Author : jyadav

# reading all lines from the elog_tb_gen_configuration

f = open("elog_tb_gen_config", 'r')
elog_config_file_lines = f.readlines()
f.close()

#---------------------------------------------------------------------------------------
# NOTE : The first line of the config file needs to have the project name
projname_line = elog_config_file_lines[0]
# removing all whitespaces if any
proj_name = projname_line.replace(" ", "").rsplit(":")
PROJECT_NAME = proj_name[1]
PROJECT_NAME_CAPS = PROJECT_NAME.upper()

#---------------------------------------------------------------------------------------
# Getting the EVL Instance path
evl_inst_path_line = elog_config_file_lines[1]
evl_inst_path_list = evl_inst_path_line.replace(" ", "").rsplit(":")
evl_inst_path = evl_inst_path_list[1]

#---------------------------------------------------------------------------------------
# Getting the EVL Source 0
evl_num_source0_line = elog_config_file_lines[2]
evl_num_source0_list = evl_num_source0_line.replace(" ", "").rsplit(":")
evl_num_source0 = evl_num_source0_list[1]

#---------------------------------------------------------------------------------------
# Getting the EVL Source 0
evl_num_source1_line = elog_config_file_lines[3]
evl_num_source1_list = evl_num_source1_line.replace(" ", "").rsplit(":")
evl_num_source1 = evl_num_source1_list[1]

# creating name for the defines file
project_defines_filename = str(PROJECT_NAME.replace("\n", "")) + "_elog_test_defines.sv"
# creating name for the single source tests
project_single_source_tests_filename = str(PROJECT_NAME.replace("\n", "")) + "_soc_evl_single_source_evm_tests.sv"
# creating name for the mega random test
project_mega_random_test_filename = str(PROJECT_NAME.replace("\n", "")) + "_elog_mega_random_test.sv"

# creating a different files
f_defines_file = open(project_defines_filename, 'w')
f_mega_random_file = open(project_mega_random_test_filename, 'w')
f_single_source_tests_file = open(project_single_source_tests_filename, 'w')

num_of_lines_of_config_file = len(elog_config_file_lines)
# print(num_of_lines_of_config_file)
tick_define = "`define"
ral_block_name = PROJECT_NAME_CAPS.replace("\n", "") + "_block"
proj_env_config = PROJECT_NAME.replace("\n", "") + "_env_cfg"

evm_config_list = []
evm_instances_start_line = 6

for line_num in range(0, num_of_lines_of_config_file):
    if line_num >= (int(evm_instances_start_line) - 1):
        evm_config_list.append(elog_config_file_lines[line_num].replace("\n", ""))

#-------------------------------------------------------------------------------------------------------------
# Functions related to creating the defines file:
def evm_file_comment(cmnt, file):
    comment_length = len(cmnt)
    cmnt_len_with_pad = comment_length + 30 + 16

    line1 = "//" + "-"*cmnt_len_with_pad
    line2 = "//" + " "*15 + cmnt + " Related Defines" + " "*15
    line3 = "//" + "-"*cmnt_len_with_pad

    file.write(line1 + "\n")
    file.write(line2 + "\n")
    file.write(line3 + "\n")

def evm_define_source_dsize_and_path(inst, sources, dsize, inst_path, file):
    line1 = tick_define + " " + inst + "_EVM_SOURCES " + sources
    line2 = tick_define + " " + inst + "_EVM_SOURCE_DSIZE " + dsize
    line3 = tick_define + " " + inst + "_EVM_PATH " + inst_path

    file.write(line1 + "\n")
    file.write(line2 + "\n")
    file.write(line3 + "\n")
    file.write("\n")

def evm_define_evl_related_end_of_file(inst, sources0, sources1, inst_path, file):
    line1 = tick_define + " " + inst + "_EVL_PATH " + inst_path
    line2 = tick_define + " " + "EVT_LOG_NUM_CHAN0_SOURCES " + sources0
    line3 = tick_define + " " + "EVT_LOG_NUM_CHAN1_SOURCES " + sources1
    evm_file_comment("EVENT LOG ", f_defines_file)
    file.write(line1)
    file.write(line2)
    file.write(line3)

#-------------------------------------------------------------------------------------------------------------
# Functions related to creating the tests file:

def proj_evl_gpio_config_sequence_gen (proj_name, file):
    sequence_name = proj_name.replace("\n", "") + "_elog_gpio_configure_sequence"
    # print(sequence_name)
    file.write("class " + sequence_name + " extends mvm_reg_sequence (.RM_TYPE(" + ral_block_name + "), .CFG_TYPE(" + proj_env_config + "));\n")
    file.write("\n")
    file.write("`uvm_object_utils(" + sequence_name + ")\n")
    file.write("\n")
    file.write("// Class Constructor\n")
    file.write("function new (string name = \"" + sequence_name + "\");\n")
    file.write("  super.new(name);" + "\n")
    file.write("endfunction" + "\n")
    file.write("\n")
    file.write("// Main Sequence Body" + "\n")
    file.write("task body();" + "\n")
    file.write("  `uvm_info(get_name(),\"Starting Sequence Body !!.....\", UVM_LOW)" + "\n")
    file.write("  // NEXUS Configuration code goes here" + "\n")
    file.write("\n")
    file.write("  `uvm_info(get_name(),\"Done Configuring NEXUS !!.....\", UVM_LOW)" + "\n")
    file.write("endtask" + "\n")
    file.write("\n")
    file.write("endclass" + "\n")


proj_evl_gpio_config_sequence_gen(PROJECT_NAME, f_single_source_tests_file)


















for element in evm_config_list:
    evm_configuration = element.replace(" ", "").rsplit(":")
    evm_instance_name = evm_configuration[0]
    evm_dsize = evm_configuration[1]
    evm_sources = evm_configuration[2]
    evm_instance_path = evm_configuration[3]

    # top level defines files
    evm_file_comment(evm_instance_name.upper(), f_defines_file)
    evm_define_source_dsize_and_path(evm_instance_name.upper(), evm_sources, evm_dsize, evm_instance_path, f_defines_file)

evm_define_evl_related_end_of_file(PROJECT_NAME_CAPS.replace("\n", ""), evl_num_source0, evl_num_source1, evl_inst_path, f_defines_file)


#--------------------------------------------------------------------------------
# End of program and closing all created files
f_defines_file.close()
f_mega_random_file.close()
f_single_source_tests_file.close()