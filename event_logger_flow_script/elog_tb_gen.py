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

def proj_elog_gpio_config_sequence_gen(proj_name, file):
    sequence_name = proj_name.replace("\n", "") + "_elog_gpio_configure_sequence"
    # print(sequence_name)
    evm_file_comment("Description : To Configure the CHIP Nexus ports for Event Logger NEXUS", file)
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
    file.write("\n")

def proj_elog_sram_nexus_coonfigure_sequence_gen(proj_name, file):
    sequence_name = proj_name.replace("\n", "") + "_elog_sram_nexus_configure_sequence"
    evm_file_comment("Description : To configure the SRAM and NEXUS for the Event Logger", file)
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

    file.write("  if($test$plusargs(\"ELOG_chan0_sram_en\"))" + "\n")
    file.write("    begin" + "\n")
    file.write("      // Code goes here" + "\n")
    file.write("      " + "\n")
    file.write("    end" + "\n")
    file.write("\n")

    file.write("  if($test$plusargs(\"ELOG_chan0_sram_en\"))" + "\n")
    file.write("    begin" + "\n")
    file.write("      // Code goes here" + "\n")
    file.write("      " + "\n")
    file.write("    end" + "\n")
    file.write("\n")

    file.write("  if($test$plusargs(\"elog_spare_rw_read_write_test\"))" + "\n")
    file.write("    begin" + "\n")
    file.write("      // Code goes here" + "\n")
    file.write("      " + "\n")
    file.write("      #100ns;" + "\n")
    file.write("    end" + "\n")
    file.write("\n")

    file.write("  if($test$plusargs(\"elog_ds_toggle_test\"))" + "\n")
    file.write("    begin" + "\n")
    file.write("      // Code goes here" + "\n")
    file.write("      " + "\n")
    file.write("      #100ns;" + "\n")
    file.write("    end" + "\n")
    file.write("\n")

    file.write("  if($test$plusargs(\"elog_sd_toggle_test\"))" + "\n")
    file.write("    begin" + "\n")
    file.write("      // Code goes here" + "\n")
    file.write("      " + "\n")
    file.write("      #100ns;" + "\n")
    file.write("    end" + "\n")
    file.write("\n")

    file.write("  if($test$plusargs(\"elog_dbg_intr_test\"))" + "\n")
    file.write("    begin" + "\n")
    file.write("      // Code goes here" + "\n")
    file.write("      " + "\n")
    file.write("      #100ns;" + "\n")
    file.write("    end" + "\n")
    file.write("\n")

    file.write("endtask" + "\n")
    file.write("" + "\n")
    file.write("endclass" + "\n")
    file.write("\n")

def evm_in_single_tx_gen(file):
    evm_file_comment("Description : Sequence to generate single event on EVM Instance", file)
    sequence_name = "evm_in_single_tx_seq"
    file.write("class " + sequence_name + " #(parameter D_SIZE = 32)" + " extends uvm_sequence #(evm_in_transaction);\n")
    file.write("\n")
    file.write("typedef " + sequence_name + " #(.D_SIZE(D_SIZE) evm_in_single_tx_seq_t;" + "\n")
    file.write("\n")
    file.write("`uvm_object_param_utils(evm_in_single_tx_seq_t)" + "\n")
    file.write("\n")
    file.write("evm_in_transaction           evm_in_tx;" + "\n")
    file.write("\n")
    file.write("rand bit   [6:0]   gid;" + "\n")
    file.write("rand bit   [63:0]  data;" + "\n")
    file.write("rand bit           overflow;" + "\n")
    file.write("\n")
    file.write("bit                dsize; // 0 : 32b" + "\n")
    file.write("                          // 1 : 64b" + "\n")
    file.write("constraint gid_valid { gid > 1; gid != 7'h7e; gid != 7'h7f; }" + "\n")
    file.write("\n")
    file.write("// Class Constructor" + "\n")
    file.write("function new (string name = \"" + sequence_name + "\");\n")
    file.write("  super.new(name);" + "\n")
    file.write("endfunction" + "\n")
    file.write("\n")
    file.write("// Sequence Body" + "\n")
    file.write("virtual task body();" + "\n")
    file.write("  evm_in_tx = evm_in_transaction::type_id::create(\"evm_in_tx\");" + "\n")
    file.write("  `uvm_info(get_name(),\"Starting EVM In Transaction Sequence\", UVM_LOW)" + "\n")
    file.write("\n")
    file.write("  if(D_SIZE == 32)" + "\n")
    file.write("    begin dsize = 1'b0; end" + "\n")
    file.write("  else" + "\n")
    file.write("    begin dsize = 1'b1; end" + "\n")
    file.write("\n")
    file.write("  start_item.(evm_in_tx);" + "\n")
    file.write("\n")
    file.write("  if(!(evm_in_tx.randomize() with {source_valid == 1;" + "\n")
    file.write("                                   source_oflow == 0;" + "\n")
    file.write("                                   source_reset == 0;" + "\n")
    file.write("                                   source_size  == dsize ? 1 : 0;" + "\n")
    file.write("                                   source_gid   == gid;" + "\n")
    file.write("                                   source_data  == dsize ? data : {32'd0,data[31:0]};" + "\n")
    file.write("                                   } ))" + "\n")
    file.write("    `uvm_error(get_name(),\"EVM In Transaction ......... RANDOMIZATION FAILED !!......\")" + "\n")
    file.write("  finish_item(evm_in_tx)" + "\n")
    file.write("endtask" + "\n")
    file.write("" + "\n")
    file.write("endclass" + "\n")
    file.write("\n")


proj_elog_gpio_config_sequence_gen(PROJECT_NAME, f_single_source_tests_file)
proj_elog_sram_nexus_coonfigure_sequence_gen(PROJECT_NAME, f_single_source_tests_file)
evm_in_single_tx_gen(f_single_source_tests_file)

















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