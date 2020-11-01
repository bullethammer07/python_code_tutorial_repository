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
# creating a file by name of the defines file and opening it
f_defines_file = open(project_defines_filename, 'w')

num_of_lines_of_config_file = len(elog_config_file_lines)
# print(num_of_lines_of_config_file)
tick_define = "`define"

evm_config_list = []
evm_instances_start_line = 5

for line_num in range(0, num_of_lines_of_config_file):
    if line_num >= (int(evm_instances_start_line) - 1):
        evm_config_list.append(elog_config_file_lines[line_num].replace("\n", ""))

def evm_file_comment(cmnt, file):
    comment_length = len(cmnt)
    cmnt_len_with_pad = comment_length + 8 + 30 + 16

    line1 = "//" + "-"*cmnt_len_with_pad
    line2 = "//" + " "*15 + "*** " + cmnt + " Related Defines" + " ***" + " "*15
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