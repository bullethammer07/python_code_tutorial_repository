//---------------------------------
//               DMA               
//---------------------------------
`define DMA_EVM_SOURCES 3
`define DMA_EVM_SOURCE_DSIZE 32
`define DMA_EVM_PATH dma_inst_path

//---------------------------------
//               DDR               
//---------------------------------
`define DDR_EVM_SOURCES 9
`define DDR_EVM_SOURCE_DSIZE 64
`define DDR_EVM_PATH ddr_inst_path

//--------------------------------------
//               SYSM_L2P               
//--------------------------------------
`define SYSM_L2P_EVM_SOURCES 3
`define SYSM_L2P_EVM_SOURCE_DSIZE 32
`define SYSM_L2P_EVM_PATH sysm_l2p_inst_path

//-------------------------------------
//               SYSM_CC               
//-------------------------------------
`define SYSM_CC_EVM_SOURCES 8
`define SYSM_CC_EVM_SOURCE_DSIZE 32
`define SYSM_CC_EVM_PATH sysm_cc_inst_path

//----------------------------------------
//               EVENT LOG                
//----------------------------------------
`define TOMCAT_EVL_PATH soc_evl_instance_path
`define EVT_LOG_NUM_CHAN0_SOURCES 9
`define EVT_LOG_NUM_CHAN1_SOURCES 3
