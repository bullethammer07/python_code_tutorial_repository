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

#---------------------------------------------------------------------------------------
# Getting the project base test name
evl_soc_base_test_line = elog_config_file_lines[4]
evl_soc_base_test_list = evl_soc_base_test_line.replace(" ", "").rsplit(":")
evl_soc_base_test = evl_soc_base_test_list[1]

# creating name for the defines file
project_defines_filename = str(PROJECT_NAME.replace("\n", "")) + "_elog_test_defines.sv"
# creating name for the single source tests
project_single_source_tests_filename = str(PROJECT_NAME.replace("\n", "")) + "_soc_evl_single_source_evm_tests.sv"
# creating name for the proj_evl_env
project_evl_env_filename = str(PROJECT_NAME.replace("\n", "")) + "_evl_env.sv"
# creating name for the interface connections
project_intf_connect_filename = str(PROJECT_NAME.replace("\n", "")) + "_evm_interface_connections.sv"

# creating name for the mega random test
#project_mega_random_test_filename = str(PROJECT_NAME.replace("\n", "")) + "_elog_mega_random_test.sv"

# creating a different files
f_defines_file = open(project_defines_filename, 'w')
#f_mega_random_file = open(project_mega_random_test_filename, 'w')
f_single_source_tests_file = open(project_single_source_tests_filename, 'w')
f_evl_env_file = open(project_evl_env_filename, 'w')
f_evm_intf_connect_file = open(project_intf_connect_filename, 'w')

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
    cmnt_len_with_pad = comment_length + 30

    line1 = "//" + "-"*cmnt_len_with_pad
    line2 = "//" + " "*15 + cmnt + " "*15
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

def evm_instance_event_drive_task_gen(evm_inst_name, file):
    inst_name = evm_inst_name.replace("\n", "")
    inst_name_lower = inst_name.lower()

    task_name = inst_name_lower + "_event_drive"
    all_evl_plusarg = "ALL_" + inst_name + "_EVM_SOURCE_ACTIVE"
    inst_src_dsize = inst_name + "_EVM_SOURCE_DSIZE"
    inst_sources = inst_name + "_EVM_SOURCES"
    gid_name = inst_name + "_GID"
    seq_name = inst_name_lower + "_evm_in_tx_seq"
    agent_path = "evl_env_tc." + inst_name_lower + "_evm_env.evm_in_agt"

    cbo = "{"
    cbc = "}"

    file.write("// Task to write Events on " + inst_name + "\n")
    file.write("task " + task_name + ";" + "\n")
    file.write("  if($test$plusargs(\"" + all_evl_plusarg + "\")) // To RUN on all Sources of the EVM Instance" + "\n")
    file.write("    begin" + "\n")
    file.write("      foreach(" + seq_name + "[i])" + "\n")
    file.write("        begin" + "\n")
    file.write("          automatic int var_i = i;" + "\n")
    file.write("          " + "\n")
    file.write("          fork" + "\n")
    file.write("            agent_name = $psprintf(\"" + seq_name + "[%0d]\",var_i);" + "\n")
    file.write("            event_iterations = $urandom_range(10,max_iter_cnt);" + "\n")
    file.write("            " + "\n")
    file.write("            `uvm_info(get_name(),$sformatf(\"Event Iteration for Agent %0d of " + inst_name + " is :: %0d\",var_i,event_iterations),UVM_LOW)" + "\n")
    file.write("            " + "\n")
    file.write("            repeat(event_iterations)" + "\n")
    file.write("              begin" + "\n")
    file.write("                " + seq_name + "[var_i] = evm_in_single_tx_seq#(.D_SIZE(" + inst_src_dsize + "))::type_id::create(agent_name);" + "\n")
    file.write("                if($test$plusargs(\"ENABLE_UNIQUE_GID\")) begin " + seq_name + "[var_i].randomize() with { gid == " + gid_name + "}; end else begin " + seq_name + "[var_i].randomize(); end" + "\n")
    file.write("                " + seq_name + "[var_i].start(" + agent_path + "[var_i].evm_sqr);" + "\n")
    file.write("              end" + "\n")
    file.write("          join_none" + "\n")
    file.write("        end" + "\n")
    file.write("      wait fork;" + "\n")
    file.write("    end" + "\n")
    file.write("  else // To RUN on any one source of t he EVM Instance" + "\n")
    file.write("    begin" + "\n")
    file.write("      event_iterations = $urandom_range(10, max_iter_cnt);" + "\n")
    file.write("      active_source = $urandom_range(0, (`" + inst_sources + " - 1));" + "\n")
    file.write("      agent_name = $psprintf(\"" + seq_name + "[%0d]\",active_source);" + "\n")
    file.write("      " + "\n")
    file.write("      `uvm_info(get_name(),$sformatf(\"Event Iteration          :: %0d\",event_iterations),UVM_LOW)" + "\n")
    file.write("      `uvm_info(get_name(),$sformatf(\"Active Source Selected   :: %0d\",active_source),UVM_LOW)" + "\n")
    file.write("       " + "\n")
    file.write("       repeat(event_iterations)" + "\n")
    file.write("         begin" + "\n")
    file.write("           " + seq_name + "[active_source] = evm_in_single_tx_seq#(.D_SIZE(`" + inst_src_dsize + "))::type_id::create(agent_name);" + "\n")
    file.write("           " + seq_name + "[active_source].randomize();" + "\n")
    file.write("           " + seq_name + "[active_source].start(" + agent_path + "[active_source].evm_sqr);" + "\n")
    file.write("         end" + "\n")
    file.write("       #5000ns;" + "\n")
    file.write("     end" + "\n")
    file.write("endtask" + "\n")
    file.write("\n")

def single_evm_instance_test_gen(proj_name, evm_inst_name, file):
    project_name = proj_name.replace("\n", "")
    inst_name_caps = evm_inst_name.replace("\n", "")
    inst_name = inst_name_caps.lower()
    base_test_name = project_name + "_soc_evl_base_test"
    test_name = project_name + "_elog_" + inst_name + "_event_drive_test"
    task_name = inst_name + "_event_drive"

    file.write("class " + test_name + " extends " + base_test_name + ";" + "\n")
    file.write("\n")
    file.write("`uvm_component_utils("+test_name+")" + "\n")
    file.write("\n")
    file.write("// Class Constructor" + "\n")
    file.write("function new(string name = \"" + test_name + "\", uvm_component parent = null);" + "\n")
    file.write("  super.new(name,parent);" + "\n")
    file.write("endfunction" + "\n")
    file.write("\n")
    file.write("// Build Phase" + "\n")
    file.write("function void build_phase(uvm_phase phase);" + "\n")
    file.write("  super.build_phase(phase);" + "\n")
    file.write("endfunction" + "\n")
    file.write("\n")
    file.write("// Main Phase" + "\n")
    file.write("task main_phase(uvm_phase phase);" + "\n")
    file.write("  super.main_phase(phase);" + "\n")
    file.write("  phase.raise_objection(this, \"main_phase\");" + "\n")
    file.write("\n")
    file.write("  wait(evl_configuration_done == 1'b1);" + "\n")
    file.write("    `uvm_info(get_name(),\"EVL CONFIGURATION DONE FLAG SET :: Starting TEST\",UVM_LOW)" + "\n")
    file.write("  " + task_name + "();" + "\n")
    file.write("  #500ns;" + "\n")
    file.write("\n")
    file.write("  phase.drop_objection(this, \"main_phase\");" + "\n")
    file.write("endtask" + "\n")
    file.write("\n")
    file.write("endclass" + "\n")
    file.write("\n")

def proj_evl_env_gen(proj_name, file):
    project_name = proj_name.replace("\n", "")
    proj_name_upper = project_name.upper()

    proj_nexus_pd = project_name + "_evl_nexus_pd"
    proj_nexus_sb = project_name + "_evl_nexus_sb_h"
    proj_virt_seqr = project_name + "_evl_virtual_sequencer"
    proj_checker_block = project_name + "_elog_event_checker_block"

    env_name = project_name + "_evl_env"
    reg_block_name = proj_name_upper + "_block"
    proj_env_cfg = project_name + "_env_cfg"

    src0_define = proj_name_upper + "_EVL_CHAN0_SOURCES"
    src1_define = proj_name_upper + "_EVL_CHAN1_SOURCES"

    file.write("// Class definition for " + proj_name_upper + " EVL env for SoC Environment" + "\n")
    file.write("class " + env_name + "#(int SOURCES0 = 2, INT SOURCES1 = 2) extends mvm_reg_env #(" + reg_block_name + "," + proj_env_cfg + ");" + "\n")
    file.write("\n")
    file.write("typedef " + env_name + "#(.SOURCES0(`" + src0_define + "), .SOURCES1(`" + src1_define + "))      t_evl_env;" + "\n")
    file.write("\n")
    file.write("`uvm_component_param_utils(t_evl_env)" + "\n")
    file.write("\n")
    file.write(reg_block_name + "     " + reg_block_name + "_h;" + "\n")
    file.write("\n")
    file.write("typedef " + "         eva_env#(.SOURCES(`" + src0_define + "),.D_SIZE(64))" + "       t_eva_env0;" + "\n")
    file.write("typedef " + "         eva_env#(.SOURCES(`" + src1_define + "),.D_SIZE(64))" + "       t_eva_env1;" + "\n")
    file.write("\n")

    for element in evm_config_list:
        evm_configuration = element.replace(" ", "").rsplit(":")
        instance_name = evm_configuration[0]
        instance_name_lower = instance_name.lower()
        srcs = "`" + instance_name + "_EVM_SOURCES"
        dsize = "`" + instance_name + "_EVM_SOURCE_DSIZE"
        LHS = "evm_env #(.SOURCES(" + srcs + "),.D_SIZE(" + dsize + "))"
        lhs_len = len(LHS)
        inst_evm_env = instance_name + "_evm_env"

        file.write("//" + instance_name + " EVM env" + "\n")
        file.write(LHS + " "*(120 - lhs_len) + inst_evm_env + ";" + "\n")
        file.write("\n")

    file.write("// sub-environment" + "\n")
    file.write("t_eva_env0            eva_env_h0;" + "\n")
    file.write("t_eva_env1            eva_env_h1" + "\n")
    file.write("\n")
    file.write("// NEXUS Environment" + "\n")
    file.write("typedef nexus_agent #(.D_WIDTH(8),.M_WIDTH(1))      t_nexus_agent;" + "\n")
    file.write("\n")
    file.write("// nexus agent" + "\n")
    file.write("t_nexus_agent                      nexus_agent_h;" + "\n")
    file.write("// evl nexus predictor" + "\n")
    file.write(proj_nexus_pd + "               evl_nexus_pd_h;" + "\n")
    file.write("// evl nexus scoreboard" + "\n")
    file.write(proj_nexus_sb + "             evl_nexus_sb_h;" + "\n")
    file.write("\n")
    file.write("// EVL virtual sequencer" + "\n")
    file.write(proj_virt_seqr + "      virt_seqr;" + "\n")
    file.write("// EVL Event Checker Block" + "\n")
    file.write(proj_checker_block + "   evl_check_blk" + "\n")
    file.write("\n")
    file.write("// Class Constructor" + "\n")
    file.write("function new(string name=\"" + env_name + "\", uvm_component parent = null);" + "\n")
    file.write("  super.new(name,parent);" + "\n")
    file.write("endfunction" + "\n")
    file.write("\n")
    file.write("// Build Phase" + "\n")
    file.write("function void build_phase(uvm_phase phase);" + "\n")
    file.write("  string agent_name;" + "\n")
    file.write("  super.build_phase(phase);" + "\n")
    file.write("\n")
    file.write("  // Creating the register model" + "\n")
    file.write("  " + reg_block_name + "_h" + "  =  get_rm();" + "\n")
    file.write("\n")

    evm_file_comment("Creating the EVM Environments for the EVM Instances", file)

    for element in evm_config_list:
        evm_configuration = element.replace(" ", "").rsplit(":")
        instance_name = evm_configuration[0]
        instance_name_lower = instance_name.lower()

        env_name = instance_name_lower + "_evm_env"
        srcs = "`" + instance_name + "_EVM_SOURCES"
        dsize = "`" + instance_name + "_EVM_SOURCE_DSIZE"

        file.write("  //" + instance_name + "\n")
        file.write("  " + env_name + " = evm_env #(.SOURCES(" + srcs + "),.D_SIZE(" + dsize + "))::type_id::create(\"" + env_name + "\",this);" + "\n")
        file.write("\n")

    evm_file_comment("Creating the EVL Subenvironments", file)

    file.write("\n")
    file.write("  // creating the EVL CH0 EVA Sub Environment" + "\n")
    file.write("  eva_env_h0 = t_eva_env0::type_id::create(\"eva_env_h0\",this);" + "\n")
    file.write("  agent_name = \"eva_env_h0.eva_out_agent\";" + "\n")
    file.write("  `mvm_set_enum(uvm_active_passive_enum, this, agent_name,\"is_active\",UVM_PASSIVE)" + "\n")
    file.write("  foreach(eva_env_h0.eva_in_agent[i])" + "\n")
    file.write("    begin" + "\n")
    file.write("      agent_name = $psprintf(\"eva_env_h0.eva_in_agent[%0d]\",i);" + "\n")
    file.write("      `mvm_set_enum(uvm_active_passive_enum, this, agent_name,\"is_active\",UVM_PASSIVE)" + "\n")
    file.write("    end" + "\n")
    file.write("\n")
    file.write("  // creating the EVL CH1 EVA Sub Environment" + "\n")
    file.write("  eva_env_h1 = t_eva_env1::type_id::create(\"eva_env_h1\",this);" + "\n")
    file.write("  agent_name = \"eva_env_h1.eva_out_agent\";" + "\n")
    file.write("  `mvm_set_enum(uvm_active_passive_enum, this, agent_name,\"is_active\",UVM_PASSIVE)" + "\n")
    file.write("  foreach(eva_env_h1.eva_in_agent[i])" + "\n")
    file.write("    begin" + "\n")
    file.write("      agent_name = $psprintf(\"eva_env_h1.eva_in_agent[%0d]\",i);" + "\n")
    file.write("      `mvm_set_enum(uvm_active_passive_enum, this, agent_name,\"is_active\",UVM_PASSIVE)" + "\n")
    file.write("    end" + "\n")
    file.write("\n")

    evm_file_comment("Creating the NEXUS Environments", file)
    file.write("\n")
    file.write("  if($test$plusargs(\"enable_elog_nexus_sb\"))" + "\n")
    file.write("    begin" + "\n")
    file.write("      // Create the Nexus Predictor and Scoreboard" + "\n")
    file.write("      nexus_agent_h = t_nexus_agent::type_id::create(\"nexus_agent_h\",this);" + "\n")
    file.write("      evl_nexus_pd_h = " + proj_nexus_pd + "::type_id::create(\"evl_nexus_pd_h\", this);" + "\n")
    file.write("      evl_nexus_sb_h = " + proj_nexus_sb + "::type_id::create(\"evl_nexus_sb_h\", this);" + "\n")
    file.write("    end" + "\n")
    file.write("\n")

    evm_file_comment("Creating the virtual sequencer", file)
    file.write("  virt_seqr = " + proj_virt_seqr + "type_id::create::(\"virt_seqr\",this);" + "\n")
    file.write("\n")
    file.write("  if($test$plusargs(\"ENABLE_UNIQUE_GID\"))" + "\n")
    file.write("    begin" + "\n")
    file.write("      // Event Checker Block" + "\n")
    file.write("      `uvm_info(get_name(),\"Creating the EVENT CHECKER Block\", UVM_LOW)" + "\n")
    file.write("      evl_check_blk = " + proj_checker_block + "::type_id::create(\"evl_check_blk\",this);" + "\n")
    file.write("    end" + "\n")
    file.write("\n")

    file.write("endfunction" + "\n")
    file.write("\n")

    file.write("// Connect Phase" + "\n")
    file.write("function void connect_phase(uvm_phase phase);" + "\n")
    file.write("  super.connect_phase(phase);" + "\n")
    file.write("\n")
    file.write("  // Connecting NEXUS Scoreboard components" + "\n")
    file.write("  if($test$plusargs(\"enable_elog_nexus_sb\"))" + "\n")
    file.write("    begin" + "\n")
    file.write("      // connect the nexus agent monitor to the evl_nexus_predictor" + "\n")
    file.write("      nexus_agent_h.mon_h.actual_ap.connect(evl_nexus_pd_h.evl_nexus_exp);" + "\n")
    file.write("      // connect the evl nexus predictor to the evl nexus scorebaord" + "\n")
    file.write("      evl_nexus_pd_h.evl_nexus_ap.connect(evl_nexus_sb_h.ev_actual_exp);" + "\n")
    file.write("      // connect event channel0 and channel1 to the nexus scorebaord" + "\n")
    file.write("      eva_env_h0.eva_out_agent.mon_h.actual_ap.connect(evl_nexus_sb_h.ev_expected0_exp);" + "\n")
    file.write("      eva_env_h1.eva_out_agent.mon_h.actual_ap.connect(evl_nexus_sb_h.ev_expected1_exp);" + "\n")
    file.write("    end" + "\n")
    file.write("\n")
    file.write("  if($test$plusargs(\"ENABLE_UNIQUE_GID\"))" + "\n")
    file.write("    begin" + "\n")

    for element in evm_config_list:
        evm_configuration = element.replace(" ", "").rsplit(":")
        instance_name = evm_configuration[0]
        instance_name_lower = instance_name.lower()

        lhs = instance_name_lower + "_evm_env.evm_out_agt.evm_mon.evm_mon_ap.connect"
        rhs = "(evl_check_blk." + instance_name_lower + "_event_exp);"
        lhs_len = len(lhs)

        file.write("      " + lhs + " "*(100 - (lhs_len)) + rhs + "\n")

    file.write("    end" + "\n")
    file.write("\n")

    for element in evm_config_list:
        evm_configuration = element.replace(" ", "").rsplit(":")
        instance_name = evm_configuration[0]
        instance_name_lower = instance_name.lower()

        file.write("  //" + instance_name + "\n")
        file.write("  foreach(virt_seqr." + instance_name_lower + "_evm_sequencer[i]) begin virt_seqr." + instance_name_lower + "_evm_sequencer[i] = " + instance_name_lower + "_evm_env.evm_in_agt[i].evm_sqr; end" + "\n")
        file.write("\n")

    file.write("endfunction" + "\n")
    file.write("\n")
    file.write("endclass" + "\n")

def proj_soc_evl_base_test_gen(proj_name, base_test_name, file):
    project_name = proj_name.replace("\n", "")
    bt_name = base_test_name.replace("\n", "")

    sequence_name1 = proj_name.replace("\n", "") + "_elog_gpio_configure_sequence"
    sequence_name_inst1 = proj_name.replace("\n", "") + "_gpio_config_seq"

    sequence_name2 = proj_name.replace("\n", "") + "_elog_sram_nexus_configure_sequence"
    sequence_name_inst2 = proj_name.replace("\n", "") + "_sram_nexus_config_seq"

    aux_intf_name = proj_name.replace("\n", "") + "_evl_aux_intf"

    evm_file_comment("SOC EVL base test for all necessary" + project_name.upper() + "Initialization", file)
    test_name = proj_name.replace("\n", "")
    file.write("class " + test_name + "_soc_evl_base_test extends " + bt_name + ";" + "\n")
    file.write("\n")
    file.write("// Sequences for Configuration" + "\n")
    file.write(sequence_name1 + "          " + sequence_name_inst1 + "\n")
    file.write(sequence_name2 + "    " + sequence_name_inst2 + "\n")
    file.write("\n")
    file.write("// Sequences for event driving" + "\n")
    file.write("\n")

    file.write("" + "\n")
    file.write("endtask" + "\n")
    file.write("" + "\n")
    file.write("endclass" + "\n")
    file.write("\n")

    for element in evm_config_list:
        evm_configuration = element.replace(" ", "").rsplit(":")
        instance_name = evm_configuration[0]
        instance_name_lower = instance_name.lower()
        file.write("// " + instance_name + "\n")
        seq_decl = "evm_in_single_tx_seq #(.D_SIZE(`" + instance_name + "_EVM_SOURCE_DSIZE))"
        seq_inst = instance_name_lower + "_evm_in_tx_seq[`" + instance_name + "_EVM_SOURCES];"
        sd_len = len(seq_decl)
        file.write(seq_decl + " "*(100 - sd_len) + seq_inst + "\n")
        file.write("\n")

    file.write("// GID Values" + "\n")

    count = 2
    for element in evm_config_list:
        evm_configuration = element.replace(" ", "").rsplit(":")
        instance_name = evm_configuration[0]
        instance_name_upper = instance_name.upper()
        logic_decl = "logic [6:0] " + instance_name_upper + "_GID"
        logic_inst = " = 7'd" + str(count) + ";"
        count += 1
        sd_len = len(logic_decl)
        file.write(logic_decl + " " * (50 - sd_len) + logic_inst + "\n")

    file.write("\n")
    file.write("int      event_iterations;" + "\n")
    file.write("int      active_sources;" + "\n")
    file.write("string   agent_name;" + "\n")
    file.write("\n")
    file.write("`ifdef EVL_MEGA_RANDOM_TEST" + "\n")
    file.write("int max_iter_cnt = 500;" + "\n")
    file.write("`else" + "\n")
    file.write("int max_iter_cnt = 50;" + "\n")
    file.write("`endif " + "\n")
    file.write("\n")
    file.write("`uvm_component_utils(" + test_name + ")" + "\n")
    file.write("\n")
    file.write("// Class Constructor" + "\n")
    file.write("function new(string name = \"" + test_name + "\", uvm_component parent = null);" + "\n")
    file.write("  super.new(name, parent);" + "\n")
    file.write("endfunction" + "\n")
    file.write("// Build Phase" + "\n")
    file.write("function void build_phase(uvm_phase phase);" + "\n")
    file.write("  super.build_phase(phase)" + "\n")
    file.write("  // Add any project rellated builds here" + "\n")
    file.write("  " + "\n")
    file.write(" " + sequence_name_inst1 + " =  " + sequence_name1 + "::type_id::create(\"{sequence_name_inst1}\");" + "\n")
    file.write(" " + sequence_name_inst2 + " =  " + sequence_name2 + "::type_id::create(\" + sequence_name_inst2 + \");" + "\n")
    file.write("endfunction" + "\n")
    file.write("\n")
    file.write("// Configure Phase" + "\n")
    file.write("task configure_phase(uvm_phase phase);" + "\n")
    file.write("  phase.raise_objection(this, \"configure_phase\");" + "\n")
    file.write("  " + "\n")
    file.write("  `uvm_info(get_name(),\"Entering Configure Phase\", UVM_LOW)" + "\n")
    file.write("  super.configure_phase(phase)" + "\n")
    file.write("  " + "\n")
    file.write("  // NEXUS GPIO Configure sequence" + "\n")
    file.write("  " + sequence_name_inst1 + ".set_sequencer(env_h.get_sequencer());" + "\n")
    file.write("  `randomize_or_fatal(" + sequence_name_inst1 + ")" + "\n")
    file.write("  " + sequence_name_inst1 + ".start(null);" + "\n")
    file.write("  " + "\n")
    file.write("  // SRAM NEXUS Configure Sequence" + "\n")
    file.write("  " + sequence_name_inst2 + ".set_sequencer(env_h.get_sequencer());" + "\n")
    file.write("  `randomize_or_fatal(" + sequence_name_inst2 + ")" + "\n")
    file.write("  " + sequence_name_inst2 + ".start(null);" + "\n")
    file.write("  " + "\n")
    file.write("  `uvm_info(get_name(),\"Exiting Configure Phase\", UVM_LOW)" + "\n")
    file.write("  phase.drop_objection(this, \"configure_phase\");" + "\n")
    file.write("endtask" + "\n")
    file.write("\n")
    file.write("// Shutdown Phase" + "\n")
    file.write("task shutdown_phase(uvm_phase phase)" + "\n")
    file.write("  phase.raise_objection(this, \"shutdown_phase\");" + "\n")
    file.write("  " + "\n")
    file.write("  `uvm_info(get_name(),\"Entering Shutdown Phase\", UVM_LOW)" + "\n")
    file.write("  super.shutdown_phase(phase);" + "\n")
    file.write("  " + aux_intf_name + ".start_clock_forcing = 1'b0;" + "\n")
    file.write("  " + "\n")
    file.write("  #1000ns;" + "\n")
    file.write("  phase.drop_objection(this, \"shutdown_phase\");" + "\n")
    file.write("endtask" + "\n")
    file.write("\n")

    for element in evm_config_list:
        evm_configuration = element.replace(" ", "").rsplit(":")
        instance_name = evm_configuration[0]
        instance_name_upper = instance_name.upper()

        evm_instance_event_drive_task_gen(instance_name_upper, file)

    file.write("endclass" + "\n")

    for element in evm_config_list:
        evm_configuration = element.replace(" ", "").rsplit(":")
        instance_name = evm_configuration[0]

        evm_file_comment("TESTCASE : To drive events on " + instance_name + " EVM", file)
        single_evm_instance_test_gen(project_name, instance_name, file)

    mega_random_test_name = project_name + "_elog_mega_random_test"
    base_test = project_name + "_soc_evl_base_test"

    evm_file_comment("*** " + project_name + " EVL MEGA RANDOM TEST ***", file)
    file.write("class " + mega_random_test_name + " extends " + base_test + ";" + "\n")
    file.write("\n")
    file.write("`uvm_component_utils(" + mega_random_test_name + ")" + "\n")
    file.write("\n")
    file.write("// Class Constructor" + "\n")
    file.write("// Build Phase" + "\n")
    file.write("function void build_phase(uvm_phase phase);" + "\n")
    file.write("  super.build_phase(phase)" + "\n")
    file.write("\n")
    file.write("task main_phase(uvm_phase phase);" + "\n")
    file.write("  super.main_phase(phase);" + "\n")
    file.write("  phase.raise_objection(this, \"main_phase\");" + "\n")
    file.write("\n")
    file.write("  wait(evl_configuration_done == 1'b1);" + "\n")
    file.write("    `uvm_info(get_name(),\"EVL CONFIGURATION DONE FLAG SET :: Starting TEST\",UVM_LOW)" + "\n")
    file.write("\n")
    file.write("   fork" + "\n")

    for element in evm_config_list:
        evm_configuration = element.replace(" ", "").rsplit(":")
        instance_name = evm_configuration[0]
        task_name = instance_name + "_event_drive();"

        file.write("      //" + instance_name + "\n")
        file.write("      begin " + task_name + "  end" + "\n")
        file.write("\n")

    file.write("   join" + "\n")
    file.write("\n")
    file.write("   #5us;" + "\n")
    file.write("\n")
    file.write("phase.drop_objection(this,\"main_phase\");" + "\n")
    file.write("endtask" + "\n")
    file.write("\n")
    file.write("endclass" + "\n")

def proj_evm_intf_connect_gen(proj_name, file):
    project_name = proj_name.replace("\n", "")

proj_elog_gpio_config_sequence_gen(PROJECT_NAME, f_single_source_tests_file)
proj_elog_sram_nexus_coonfigure_sequence_gen(PROJECT_NAME, f_single_source_tests_file)
evm_in_single_tx_gen(f_single_source_tests_file)
proj_soc_evl_base_test_gen(PROJECT_NAME, evl_soc_base_test, f_single_source_tests_file)
proj_evl_env_gen(PROJECT_NAME, f_evl_env_file)

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
#f_mega_random_file.close()
f_single_source_tests_file.close()
f_evl_env_file.close()
f_evm_intf_connect_file.close()