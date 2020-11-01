# Description : Script to generate the ELOG TB Components
# Author : jyadav

# reading all lines from the elog_tb_gen_configuration

f = open("elog_tb_gen_config", 'r')
elog_config_file_lines = f.readlines()
f.close()

# NOTE : The first line of the config file needs to have the project name
projname_line = elog_config_file_lines[0]
# removing all whitespaces if any
proj_name = projname_line.replace(" ", "").rsplit(":")

PROJECT_NAME = proj_name[1]
PROJECT_NAME_CAPS = PROJECT_NAME.upper()

# creating name for the defines file
project_defines_filename = str(PROJECT_NAME.replace("\n", "")) + "_elog_test_defines.sv"
# creating a file by name of the defines file and opening it
f_defines_file = open(project_defines_filename, 'w')

def evm_define_file_comment(cmnt, file):
    comment_length = len(cmnt)
    cmnt_len_with_pad = comment_length + 8 + 30

    line1 = "//" + "-"*cmnt_len_with_pad
    line2 = "//" + " "*15 + "*** " + cmnt + " ***" + " "*15
    line3 = "//" + "-"*cmnt_len_with_pad

    file.write(line1 + "\n")
    file.write(line2 + "\n")
    file.write(line3 + "\n")

evm_define_file_comment(PROJECT_NAME_CAPS.replace("\n", ""), f_defines_file)

#--------------------------------------------------------------------------------
# End of program and closing all created files
f_defines_file.close()