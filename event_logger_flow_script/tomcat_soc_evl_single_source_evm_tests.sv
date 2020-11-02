//----------------------------------------------------------------------------------------------------
//               Description : To Configure the CHIP Nexus ports for Event Logger NEXUS               
//----------------------------------------------------------------------------------------------------
class tomcat_elog_gpio_configure_sequence extends mvm_reg_sequence (.RM_TYPE(TOMCAT_block), .CFG_TYPE(tomcat_env_cfg));

`uvm_object_utils(tomcat_elog_gpio_configure_sequence)

// Class Constructor
function new (string name = "tomcat_elog_gpio_configure_sequence");
  super.new(name);
endfunction

// Main Sequence Body
task body();
  `uvm_info(get_name(),"Starting Sequence Body !!.....", UVM_LOW)
  // NEXUS Configuration code goes here

  `uvm_info(get_name(),"Done Configuring NEXUS !!.....", UVM_LOW)
endtask

endclass

//------------------------------------------------------------------------------------------------
//               Description : To configure the SRAM and NEXUS for the Event Logger               
//------------------------------------------------------------------------------------------------
class tomcat_elog_sram_nexus_configure_sequence extends mvm_reg_sequence (.RM_TYPE(TOMCAT_block), .CFG_TYPE(tomcat_env_cfg));

`uvm_object_utils(tomcat_elog_sram_nexus_configure_sequence)

// Class Constructor
function new (string name = "tomcat_elog_sram_nexus_configure_sequence");
  super.new(name);
endfunction

// Main Sequence Body
task body();
  `uvm_info(get_name(),"Starting Sequence Body !!.....", UVM_LOW)
  if($test$plusargs("ELOG_chan0_sram_en"))
    begin
      // Code goes here
      
    end

  if($test$plusargs("ELOG_chan0_sram_en"))
    begin
      // Code goes here
      
    end

  if($test$plusargs("elog_spare_rw_read_write_test"))
    begin
      // Code goes here
      
      #100ns;
    end

  if($test$plusargs("elog_ds_toggle_test"))
    begin
      // Code goes here
      
      #100ns;
    end

  if($test$plusargs("elog_sd_toggle_test"))
    begin
      // Code goes here
      
      #100ns;
    end

  if($test$plusargs("elog_dbg_intr_test"))
    begin
      // Code goes here
      
      #100ns;
    end

endtask

endclass

//---------------------------------------------------------------------------------------------
//               Description : Sequence to generate single event on EVM Instance               
//---------------------------------------------------------------------------------------------
class evm_in_single_tx_seq #(parameter D_SIZE = 32) extends uvm_sequence #(evm_in_transaction);

typedef evm_in_single_tx_seq #(.D_SIZE(D_SIZE) evm_in_single_tx_seq_t;

`uvm_object_param_utils(evm_in_single_tx_seq_t)

evm_in_transaction           evm_in_tx;

rand bit   [6:0]   gid;
rand bit   [63:0]  data;
rand bit           overflow;

bit                dsize; // 0 : 32b
                          // 1 : 64b
constraint gid_valid { gid > 1; gid != 7'h7e; gid != 7'h7f; }

// Class Constructor
function new (string name = "evm_in_single_tx_seq");
  super.new(name);
endfunction

// Sequence Body
virtual task body();
  evm_in_tx = evm_in_transaction::type_id::create("evm_in_tx");
  `uvm_info(get_name(),"Starting EVM In Transaction Sequence", UVM_LOW)

  if(D_SIZE == 32)
    begin dsize = 1'b0; end
  else
    begin dsize = 1'b1; end

  start_item.(evm_in_tx);

  if(!(evm_in_tx.randomize() with {source_valid == 1;
                                   source_oflow == 0;
                                   source_reset == 0;
                                   source_size  == dsize ? 1 : 0;
                                   source_gid   == gid;
                                   source_data  == dsize ? data : {32'd0,data[31:0]};
                                   } ))
    `uvm_error(get_name(),"EVM In Transaction ......... RANDOMIZATION FAILED !!......")
  finish_item(evm_in_tx)
endtask

endclass

//-------------------------------------------------------------------------------------
//               SOC EVL base test for all necessaryTOMCATInitialization               
//-------------------------------------------------------------------------------------
class tomcat_soc_evl_base_test extends project_evl_base_test;

// Sequences for Configuration
tomcat_elog_gpio_configure_sequence          tomcat_gpio_config_seq
tomcat_elog_sram_nexus_configure_sequence    tomcat_sram_nexus_config_seq

// Sequences for event driving


endtask

endclass

// DMA
evm_in_single_tx_seq #(.D_SIZE(`DMA_EVM_SOURCE_DSIZE))                                              dma_evm_in_tx_seq[`DMA_EVM_SOURCES];

// DDR
evm_in_single_tx_seq #(.D_SIZE(`DDR_EVM_SOURCE_DSIZE))                                              ddr_evm_in_tx_seq[`DDR_EVM_SOURCES];

// SYSM_L2P
evm_in_single_tx_seq #(.D_SIZE(`SYSM_L2P_EVM_SOURCE_DSIZE))                                         sysm_l2p_evm_in_tx_seq[`SYSM_L2P_EVM_SOURCES];

// SYSM_CC
evm_in_single_tx_seq #(.D_SIZE(`SYSM_CC_EVM_SOURCE_DSIZE))                                          sysm_cc_evm_in_tx_seq[`SYSM_CC_EVM_SOURCES];

// GID Values
logic [6:0] DMA_GID                                = 7'd2;
logic [6:0] DDR_GID                                = 7'd3;
logic [6:0] SYSM_L2P_GID                           = 7'd4;
logic [6:0] SYSM_CC_GID                            = 7'd5;

int      event_iterations;
int      active_sources;
string   agent_name;

`ifdef EVL_MEGA_RANDOM_TEST
int max_iter_cnt = 500;
`else
int max_iter_cnt = 50;
`endif 

`uvm_component_utils(tomcat)

// Class Constructor
function new(string name = "tomcat", uvm_component parent = null);
  super.new(name, parent);
endfunction
// Build Phase
function void build_phase(uvm_phase phase);
  super.build_phase(phase)
  // Add any project rellated builds here
  
 tomcat_gpio_config_seq =  tomcat_elog_gpio_configure_sequence::type_id::create("{sequence_name_inst1}");
 tomcat_sram_nexus_config_seq =  tomcat_elog_sram_nexus_configure_sequence::type_id::create(" + sequence_name_inst2 + ");
endfunction

// Configure Phase
task configure_phase(uvm_phase phase);
  phase.raise_objection(this, "configure_phase");
  
  `uvm_info(get_name(),"Entering Configure Phase", UVM_LOW)
  super.configure_phase(phase)
  
  // NEXUS GPIO Configure sequence
  tomcat_gpio_config_seq.set_sequencer(env_h.get_sequencer());
  `randomize_or_fatal(tomcat_gpio_config_seq)
  tomcat_gpio_config_seq.start(null);
  
  // SRAM NEXUS Configure Sequence
  tomcat_sram_nexus_config_seq.set_sequencer(env_h.get_sequencer());
  `randomize_or_fatal(tomcat_sram_nexus_config_seq)
  tomcat_sram_nexus_config_seq.start(null);
  
  `uvm_info(get_name(),"Exiting Configure Phase", UVM_LOW)
  phase.drop_objection(this, "configure_phase");
endtask

// Shutdown Phase
task shutdown_phase(uvm_phase phase)
  phase.raise_objection(this, "shutdown_phase");
  
  `uvm_info(get_name(),"Entering Shutdown Phase", UVM_LOW)
  super.shutdown_phase(phase);
  tomcat_evl_aux_intf.start_clock_forcing = 1'b0;
  
  #1000ns;
  phase.drop_objection(this, "shutdown_phase");
endtask

// Task to write Events on DMA
task dma_event_drive;
  if($test$plusargs("ALL_DMA_EVM_SOURCE_ACTIVE")) // To RUN on all Sources of the EVM Instance
    begin
      foreach(dma_evm_in_tx_seq[i])
        begin
          automatic int var_i = i;
          
          fork
            agent_name = $psprintf("dma_evm_in_tx_seq[%0d]",var_i);
            event_iterations = $urandom_range(10,max_iter_cnt);
            
            `uvm_info(get_name(),$sformatf("Event Iteration for Agent %0d of DMA is :: %0d",var_i,event_iterations),UVM_LOW)
            
            repeat(event_iterations)
              begin
                dma_evm_in_tx_seq[var_i] = evm_in_single_tx_seq#(.D_SIZE(DMA_EVM_SOURCE_DSIZE))::type_id::create(agent_name);
                if($test$plusargs("ENABLE_UNIQUE_GID")) begin dma_evm_in_tx_seq[var_i].randomize() with { gid == DMA_GID}; end else begin dma_evm_in_tx_seq[var_i].randomize(); end
                dma_evm_in_tx_seq[var_i].start(evl_env_tc.dma_evm_env.evm_in_agt[var_i].evm_sqr);
              end
          join_none
        end
      wait fork;
    end
  else // To RUN on any one source of t he EVM Instance
    begin
      event_iterations = $urandom_range(10, max_iter_cnt);
      active_source = $urandom_range(0, (`DMA_EVM_SOURCES - 1));
      agent_name = $psprintf("dma_evm_in_tx_seq[%0d]",active_source);
      
      `uvm_info(get_name(),$sformatf("Event Iteration          :: %0d",event_iterations),UVM_LOW)
      `uvm_info(get_name(),$sformatf("Active Source Selected   :: %0d",active_source),UVM_LOW)
       
       repeat(event_iterations)
         begin
           dma_evm_in_tx_seq[active_source] = evm_in_single_tx_seq#(.D_SIZE(`DMA_EVM_SOURCE_DSIZE))::type_id::create(agent_name);
           dma_evm_in_tx_seq[active_source].randomize();
           dma_evm_in_tx_seq[active_source].start(evl_env_tc.dma_evm_env.evm_in_agt[active_source].evm_sqr);
         end
       #5000ns;
     end
endtask

// Task to write Events on DDR
task ddr_event_drive;
  if($test$plusargs("ALL_DDR_EVM_SOURCE_ACTIVE")) // To RUN on all Sources of the EVM Instance
    begin
      foreach(ddr_evm_in_tx_seq[i])
        begin
          automatic int var_i = i;
          
          fork
            agent_name = $psprintf("ddr_evm_in_tx_seq[%0d]",var_i);
            event_iterations = $urandom_range(10,max_iter_cnt);
            
            `uvm_info(get_name(),$sformatf("Event Iteration for Agent %0d of DDR is :: %0d",var_i,event_iterations),UVM_LOW)
            
            repeat(event_iterations)
              begin
                ddr_evm_in_tx_seq[var_i] = evm_in_single_tx_seq#(.D_SIZE(DDR_EVM_SOURCE_DSIZE))::type_id::create(agent_name);
                if($test$plusargs("ENABLE_UNIQUE_GID")) begin ddr_evm_in_tx_seq[var_i].randomize() with { gid == DDR_GID}; end else begin ddr_evm_in_tx_seq[var_i].randomize(); end
                ddr_evm_in_tx_seq[var_i].start(evl_env_tc.ddr_evm_env.evm_in_agt[var_i].evm_sqr);
              end
          join_none
        end
      wait fork;
    end
  else // To RUN on any one source of t he EVM Instance
    begin
      event_iterations = $urandom_range(10, max_iter_cnt);
      active_source = $urandom_range(0, (`DDR_EVM_SOURCES - 1));
      agent_name = $psprintf("ddr_evm_in_tx_seq[%0d]",active_source);
      
      `uvm_info(get_name(),$sformatf("Event Iteration          :: %0d",event_iterations),UVM_LOW)
      `uvm_info(get_name(),$sformatf("Active Source Selected   :: %0d",active_source),UVM_LOW)
       
       repeat(event_iterations)
         begin
           ddr_evm_in_tx_seq[active_source] = evm_in_single_tx_seq#(.D_SIZE(`DDR_EVM_SOURCE_DSIZE))::type_id::create(agent_name);
           ddr_evm_in_tx_seq[active_source].randomize();
           ddr_evm_in_tx_seq[active_source].start(evl_env_tc.ddr_evm_env.evm_in_agt[active_source].evm_sqr);
         end
       #5000ns;
     end
endtask

// Task to write Events on SYSM_L2P
task sysm_l2p_event_drive;
  if($test$plusargs("ALL_SYSM_L2P_EVM_SOURCE_ACTIVE")) // To RUN on all Sources of the EVM Instance
    begin
      foreach(sysm_l2p_evm_in_tx_seq[i])
        begin
          automatic int var_i = i;
          
          fork
            agent_name = $psprintf("sysm_l2p_evm_in_tx_seq[%0d]",var_i);
            event_iterations = $urandom_range(10,max_iter_cnt);
            
            `uvm_info(get_name(),$sformatf("Event Iteration for Agent %0d of SYSM_L2P is :: %0d",var_i,event_iterations),UVM_LOW)
            
            repeat(event_iterations)
              begin
                sysm_l2p_evm_in_tx_seq[var_i] = evm_in_single_tx_seq#(.D_SIZE(SYSM_L2P_EVM_SOURCE_DSIZE))::type_id::create(agent_name);
                if($test$plusargs("ENABLE_UNIQUE_GID")) begin sysm_l2p_evm_in_tx_seq[var_i].randomize() with { gid == SYSM_L2P_GID}; end else begin sysm_l2p_evm_in_tx_seq[var_i].randomize(); end
                sysm_l2p_evm_in_tx_seq[var_i].start(evl_env_tc.sysm_l2p_evm_env.evm_in_agt[var_i].evm_sqr);
              end
          join_none
        end
      wait fork;
    end
  else // To RUN on any one source of t he EVM Instance
    begin
      event_iterations = $urandom_range(10, max_iter_cnt);
      active_source = $urandom_range(0, (`SYSM_L2P_EVM_SOURCES - 1));
      agent_name = $psprintf("sysm_l2p_evm_in_tx_seq[%0d]",active_source);
      
      `uvm_info(get_name(),$sformatf("Event Iteration          :: %0d",event_iterations),UVM_LOW)
      `uvm_info(get_name(),$sformatf("Active Source Selected   :: %0d",active_source),UVM_LOW)
       
       repeat(event_iterations)
         begin
           sysm_l2p_evm_in_tx_seq[active_source] = evm_in_single_tx_seq#(.D_SIZE(`SYSM_L2P_EVM_SOURCE_DSIZE))::type_id::create(agent_name);
           sysm_l2p_evm_in_tx_seq[active_source].randomize();
           sysm_l2p_evm_in_tx_seq[active_source].start(evl_env_tc.sysm_l2p_evm_env.evm_in_agt[active_source].evm_sqr);
         end
       #5000ns;
     end
endtask

// Task to write Events on SYSM_CC
task sysm_cc_event_drive;
  if($test$plusargs("ALL_SYSM_CC_EVM_SOURCE_ACTIVE")) // To RUN on all Sources of the EVM Instance
    begin
      foreach(sysm_cc_evm_in_tx_seq[i])
        begin
          automatic int var_i = i;
          
          fork
            agent_name = $psprintf("sysm_cc_evm_in_tx_seq[%0d]",var_i);
            event_iterations = $urandom_range(10,max_iter_cnt);
            
            `uvm_info(get_name(),$sformatf("Event Iteration for Agent %0d of SYSM_CC is :: %0d",var_i,event_iterations),UVM_LOW)
            
            repeat(event_iterations)
              begin
                sysm_cc_evm_in_tx_seq[var_i] = evm_in_single_tx_seq#(.D_SIZE(SYSM_CC_EVM_SOURCE_DSIZE))::type_id::create(agent_name);
                if($test$plusargs("ENABLE_UNIQUE_GID")) begin sysm_cc_evm_in_tx_seq[var_i].randomize() with { gid == SYSM_CC_GID}; end else begin sysm_cc_evm_in_tx_seq[var_i].randomize(); end
                sysm_cc_evm_in_tx_seq[var_i].start(evl_env_tc.sysm_cc_evm_env.evm_in_agt[var_i].evm_sqr);
              end
          join_none
        end
      wait fork;
    end
  else // To RUN on any one source of t he EVM Instance
    begin
      event_iterations = $urandom_range(10, max_iter_cnt);
      active_source = $urandom_range(0, (`SYSM_CC_EVM_SOURCES - 1));
      agent_name = $psprintf("sysm_cc_evm_in_tx_seq[%0d]",active_source);
      
      `uvm_info(get_name(),$sformatf("Event Iteration          :: %0d",event_iterations),UVM_LOW)
      `uvm_info(get_name(),$sformatf("Active Source Selected   :: %0d",active_source),UVM_LOW)
       
       repeat(event_iterations)
         begin
           sysm_cc_evm_in_tx_seq[active_source] = evm_in_single_tx_seq#(.D_SIZE(`SYSM_CC_EVM_SOURCE_DSIZE))::type_id::create(agent_name);
           sysm_cc_evm_in_tx_seq[active_source].randomize();
           sysm_cc_evm_in_tx_seq[active_source].start(evl_env_tc.sysm_cc_evm_env.evm_in_agt[active_source].evm_sqr);
         end
       #5000ns;
     end
endtask

endclass
//-------------------------------------------------------------------
//               TESTCASE : To drive events on DMA EVM               
//-------------------------------------------------------------------
class tomcat_elog_dma_event_drive_test extends tomcat_soc_evl_base_test;

`uvm_component_utils(tomcat_elog_dma_event_drive_test)

// Class Constructor
function new(string name = "tomcat_elog_dma_event_drive_test", uvm_component parent = null);
  super.new(name,parent);
endfunction

// Build Phase
function void build_phase(uvm_phase phase);
  super.build_phase(phase);
endfunction

// Main Phase
task main_phase(uvm_phase phase);
  super.main_phase(phase);
  phase.raise_objection(this, "main_phase");

  wait(evl_configuration_done == 1'b1);
    `uvm_info(get_name(),"EVL CONFIGURATION DONE FLAG SET :: Starting TEST",UVM_LOW)
  dma_event_drive();
  #500ns;

  phase.drop_objection(this, "main_phase");
endtask

endclass

//-------------------------------------------------------------------
//               TESTCASE : To drive events on DDR EVM               
//-------------------------------------------------------------------
class tomcat_elog_ddr_event_drive_test extends tomcat_soc_evl_base_test;

`uvm_component_utils(tomcat_elog_ddr_event_drive_test)

// Class Constructor
function new(string name = "tomcat_elog_ddr_event_drive_test", uvm_component parent = null);
  super.new(name,parent);
endfunction

// Build Phase
function void build_phase(uvm_phase phase);
  super.build_phase(phase);
endfunction

// Main Phase
task main_phase(uvm_phase phase);
  super.main_phase(phase);
  phase.raise_objection(this, "main_phase");

  wait(evl_configuration_done == 1'b1);
    `uvm_info(get_name(),"EVL CONFIGURATION DONE FLAG SET :: Starting TEST",UVM_LOW)
  ddr_event_drive();
  #500ns;

  phase.drop_objection(this, "main_phase");
endtask

endclass

//------------------------------------------------------------------------
//               TESTCASE : To drive events on SYSM_L2P EVM               
//------------------------------------------------------------------------
class tomcat_elog_sysm_l2p_event_drive_test extends tomcat_soc_evl_base_test;

`uvm_component_utils(tomcat_elog_sysm_l2p_event_drive_test)

// Class Constructor
function new(string name = "tomcat_elog_sysm_l2p_event_drive_test", uvm_component parent = null);
  super.new(name,parent);
endfunction

// Build Phase
function void build_phase(uvm_phase phase);
  super.build_phase(phase);
endfunction

// Main Phase
task main_phase(uvm_phase phase);
  super.main_phase(phase);
  phase.raise_objection(this, "main_phase");

  wait(evl_configuration_done == 1'b1);
    `uvm_info(get_name(),"EVL CONFIGURATION DONE FLAG SET :: Starting TEST",UVM_LOW)
  sysm_l2p_event_drive();
  #500ns;

  phase.drop_objection(this, "main_phase");
endtask

endclass

//-----------------------------------------------------------------------
//               TESTCASE : To drive events on SYSM_CC EVM               
//-----------------------------------------------------------------------
class tomcat_elog_sysm_cc_event_drive_test extends tomcat_soc_evl_base_test;

`uvm_component_utils(tomcat_elog_sysm_cc_event_drive_test)

// Class Constructor
function new(string name = "tomcat_elog_sysm_cc_event_drive_test", uvm_component parent = null);
  super.new(name,parent);
endfunction

// Build Phase
function void build_phase(uvm_phase phase);
  super.build_phase(phase);
endfunction

// Main Phase
task main_phase(uvm_phase phase);
  super.main_phase(phase);
  phase.raise_objection(this, "main_phase");

  wait(evl_configuration_done == 1'b1);
    `uvm_info(get_name(),"EVL CONFIGURATION DONE FLAG SET :: Starting TEST",UVM_LOW)
  sysm_cc_event_drive();
  #500ns;

  phase.drop_objection(this, "main_phase");
endtask

endclass

//-----------------------------------------------------------------
//               *** tomcat EVL MEGA RANDOM TEST ***               
//-----------------------------------------------------------------
class tomcat_elog_mega_random_test extends tomcat_soc_evl_base_test;

`uvm_component_utils(tomcat_elog_mega_random_test)

// Class Constructor
// Build Phase
function void build_phase(uvm_phase phase);
  super.build_phase(phase)

task main_phase(uvm_phase phase);
  super.main_phase(phase);
  phase.raise_objection(this, "main_phase");

  wait(evl_configuration_done == 1'b1);
    `uvm_info(get_name(),"EVL CONFIGURATION DONE FLAG SET :: Starting TEST",UVM_LOW)

   fork
      //DMA
      begin DMA_event_drive();  end

      //DDR
      begin DDR_event_drive();  end

      //SYSM_L2P
      begin SYSM_L2P_event_drive();  end

      //SYSM_CC
      begin SYSM_CC_event_drive();  end

   join

   #5us;

phase.drop_objection(this,"main_phase");
endtask

endclass
