// Class definition for TOMCAT EVL env for SoC Environment
class tomcat_evl_env#(int SOURCES0 = 2, INT SOURCES1 = 2) extends mvm_reg_env #(TOMCAT_block,tomcat_env_cfg);

typedef tomcat_evl_env#(.SOURCES0(`TOMCAT_EVL_CHAN0_SOURCES), .SOURCES1(`TOMCAT_EVL_CHAN1_SOURCES))      t_evl_env;

`uvm_component_param_utils(t_evl_env)

TOMCAT_block     TOMCAT_block_h;

typedef          eva_env#(.SOURCES(`TOMCAT_EVL_CHAN0_SOURCES),.D_SIZE(64))       t_eva_env0;
typedef          eva_env#(.SOURCES(`TOMCAT_EVL_CHAN1_SOURCES),.D_SIZE(64))       t_eva_env1;

//DMA EVM env
evm_env #(.SOURCES(`DMA_EVM_SOURCES),.D_SIZE(`DMA_EVM_SOURCE_DSIZE))                                                    DMA_evm_env;

//DDR EVM env
evm_env #(.SOURCES(`DDR_EVM_SOURCES),.D_SIZE(`DDR_EVM_SOURCE_DSIZE))                                                    DDR_evm_env;

//SYSM_L2P EVM env
evm_env #(.SOURCES(`SYSM_L2P_EVM_SOURCES),.D_SIZE(`SYSM_L2P_EVM_SOURCE_DSIZE))                                          SYSM_L2P_evm_env;

//SYSM_CC EVM env
evm_env #(.SOURCES(`SYSM_CC_EVM_SOURCES),.D_SIZE(`SYSM_CC_EVM_SOURCE_DSIZE))                                            SYSM_CC_evm_env;

// sub-environment
t_eva_env0            eva_env_h0;
t_eva_env1            eva_env_h1

// NEXUS Environment
typedef nexus_agent #(.D_WIDTH(8),.M_WIDTH(1))      t_nexus_agent;

// nexus agent
t_nexus_agent                      nexus_agent_h;
// evl nexus predictor
tomcat_evl_nexus_pd               evl_nexus_pd_h;
// evl nexus scoreboard
tomcat_evl_nexus_sb_h             evl_nexus_sb_h;

// EVL virtual sequencer
tomcat_evl_virtual_sequencer      virt_seqr;
// EVL Event Checker Block
tomcat_elog_event_checker_block   evl_check_blk

// Class Constructor
function new(string name="tomcat_evl_env", uvm_component parent = null);
  super.new(name,parent);
endfunction

// Build Phase
function void build_phase(uvm_phase phase);
  string agent_name;
  super.build_phase(phase);

  // Creating the register model
  TOMCAT_block_h  =  get_rm();

//---------------------------------------------------------------------------------
//               Creating the EVM Environments for the EVM Instances               
//---------------------------------------------------------------------------------
  //DMA
  dma_evm_env = evm_env #(.SOURCES(`DMA_EVM_SOURCES),.D_SIZE(`DMA_EVM_SOURCE_DSIZE))::type_id::create("dma_evm_env",this);

  //DDR
  ddr_evm_env = evm_env #(.SOURCES(`DDR_EVM_SOURCES),.D_SIZE(`DDR_EVM_SOURCE_DSIZE))::type_id::create("ddr_evm_env",this);

  //SYSM_L2P
  sysm_l2p_evm_env = evm_env #(.SOURCES(`SYSM_L2P_EVM_SOURCES),.D_SIZE(`SYSM_L2P_EVM_SOURCE_DSIZE))::type_id::create("sysm_l2p_evm_env",this);

  //SYSM_CC
  sysm_cc_evm_env = evm_env #(.SOURCES(`SYSM_CC_EVM_SOURCES),.D_SIZE(`SYSM_CC_EVM_SOURCE_DSIZE))::type_id::create("sysm_cc_evm_env",this);

//--------------------------------------------------------------
//               Creating the EVL Subenvironments               
//--------------------------------------------------------------

  // creating the EVL CH0 EVA Sub Environment
  eva_env_h0 = t_eva_env0::type_id::create("eva_env_h0",this);
  agent_name = "eva_env_h0.eva_out_agent";
  `mvm_set_enum(uvm_active_passive_enum, this, agent_name,"is_active",UVM_PASSIVE)
  foreach(eva_env_h0.eva_in_agent[i])
    begin
      agent_name = $psprintf("eva_env_h0.eva_in_agent[%0d]",i);
      `mvm_set_enum(uvm_active_passive_enum, this, agent_name,"is_active",UVM_PASSIVE)
    end

  // creating the EVL CH1 EVA Sub Environment
  eva_env_h1 = t_eva_env1::type_id::create("eva_env_h1",this);
  agent_name = "eva_env_h1.eva_out_agent";
  `mvm_set_enum(uvm_active_passive_enum, this, agent_name,"is_active",UVM_PASSIVE)
  foreach(eva_env_h1.eva_in_agent[i])
    begin
      agent_name = $psprintf("eva_env_h1.eva_in_agent[%0d]",i);
      `mvm_set_enum(uvm_active_passive_enum, this, agent_name,"is_active",UVM_PASSIVE)
    end

//-------------------------------------------------------------
//               Creating the NEXUS Environments               
//-------------------------------------------------------------

  if($test$plusargs("enable_elog_nexus_sb"))
    begin
      // Create the Nexus Predictor and Scoreboard
      nexus_agent_h = t_nexus_agent::type_id::create("nexus_agent_h",this);
      evl_nexus_pd_h = tomcat_evl_nexus_pd::type_id::create("evl_nexus_pd_h", this);
      evl_nexus_sb_h = tomcat_evl_nexus_sb_h::type_id::create("evl_nexus_sb_h", this);
    end

//------------------------------------------------------------
//               Creating the virtual sequencer               
//------------------------------------------------------------
  virt_seqr = tomcat_evl_virtual_sequencertype_id::create::("virt_seqr",this);

  if($test$plusargs("ENABLE_UNIQUE_GID"))
    begin
      // Event Checker Block
      `uvm_info(get_name(),"Creating the EVENT CHECKER Block", UVM_LOW)
      evl_check_blk = tomcat_elog_event_checker_block::type_id::create("evl_check_blk",this);
    end

endfunction

// Connect Phase
function void connect_phase(uvm_phase phase);
  super.connect_phase(phase);

  // Connecting NEXUS Scoreboard components
  if($test$plusargs("enable_elog_nexus_sb"))
    begin
      // connect the nexus agent monitor to the evl_nexus_predictor
      nexus_agent_h.mon_h.actual_ap.connect(evl_nexus_pd_h.evl_nexus_exp);
      // connect the evl nexus predictor to the evl nexus scorebaord
      evl_nexus_pd_h.evl_nexus_ap.connect(evl_nexus_sb_h.ev_actual_exp);
      // connect event channel0 and channel1 to the nexus scorebaord
      eva_env_h0.eva_out_agent.mon_h.actual_ap.connect(evl_nexus_sb_h.ev_expected0_exp);
      eva_env_h1.eva_out_agent.mon_h.actual_ap.connect(evl_nexus_sb_h.ev_expected1_exp);
    end

  if($test$plusargs("ENABLE_UNIQUE_GID"))
    begin
      dma_evm_env.evm_out_agt.evm_mon.evm_mon_ap.connect                                                  (evl_check_blk.dma_event_exp);
      ddr_evm_env.evm_out_agt.evm_mon.evm_mon_ap.connect                                                  (evl_check_blk.ddr_event_exp);
      sysm_l2p_evm_env.evm_out_agt.evm_mon.evm_mon_ap.connect                                             (evl_check_blk.sysm_l2p_event_exp);
      sysm_cc_evm_env.evm_out_agt.evm_mon.evm_mon_ap.connect                                              (evl_check_blk.sysm_cc_event_exp);
    end

  //DMA
  foreach(virt_seqr.dma_evm_sequencer[i]) begin virt_seqr.dma_evm_sequencer[i] = dma_evm_env.evm_in_agt[i].evm_sqr; end

  //DDR
  foreach(virt_seqr.ddr_evm_sequencer[i]) begin virt_seqr.ddr_evm_sequencer[i] = ddr_evm_env.evm_in_agt[i].evm_sqr; end

  //SYSM_L2P
  foreach(virt_seqr.sysm_l2p_evm_sequencer[i]) begin virt_seqr.sysm_l2p_evm_sequencer[i] = sysm_l2p_evm_env.evm_in_agt[i].evm_sqr; end

  //SYSM_CC
  foreach(virt_seqr.sysm_cc_evm_sequencer[i]) begin virt_seqr.sysm_cc_evm_sequencer[i] = sysm_cc_evm_env.evm_in_agt[i].evm_sqr; end

endfunction

endclass
