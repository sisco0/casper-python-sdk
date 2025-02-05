# Node RPC endpoints.
RPC_ACCOUNT_PUT_DEPLOY = "account_put_deploy"
RPC_CHAIN_GET_BLOCK = "chain_get_block"
RPC_CHAIN_GET_BLOCK_TRANSFERS = "chain_get_block_transfers"
RPC_CHAIN_GET_ERA_INFO_BY_SWITCH_BLOCK = "chain_get_era_info_by_switch_block"
RPC_CHAIN_GET_STATE_ROOT_HASH = "chain_get_state_root_hash"
RPC_DISCOVER = "rpc.discover"
RPC_INFO_GET_DEPLOY = "info_get_deploy"
RPC_INFO_GET_PEERS = "info_get_peers"
RPC_INFO_GET_STATUS = "info_get_status"
RPC_STATE_GET_ACCOUNT_INFO = "state_get_account_info"
RPC_STATE_GET_AUCTION_INFO = "state_get_auction_info"
RPC_STATE_GET_BALANCE = "state_get_balance"
RPC_STATE_GET_DICTIONARY_ITEM = "state_get_dictionary_item"
RPC_STATE_GET_ITEM = "state_get_item"
RPC_STATE_QUERY_GLOBAL_STATE = "query_global_state"

RPC_ENDPOINTS: set = {
    RPC_ACCOUNT_PUT_DEPLOY,
    RPC_CHAIN_GET_BLOCK,
    RPC_CHAIN_GET_BLOCK_TRANSFERS,
    RPC_CHAIN_GET_ERA_INFO_BY_SWITCH_BLOCK,
    RPC_CHAIN_GET_STATE_ROOT_HASH,
    RPC_INFO_GET_DEPLOY,
    RPC_INFO_GET_PEERS,
    RPC_INFO_GET_STATUS,
    RPC_STATE_GET_ACCOUNT_INFO,
    RPC_STATE_GET_AUCTION_INFO,
    RPC_STATE_GET_BALANCE,
    RPC_STATE_GET_DICTIONARY_ITEM,
    RPC_STATE_GET_ITEM,
    RPC_STATE_QUERY_GLOBAL_STATE,
    }

# Node REST endpoints.
REST_GET_METRICS = "metrics"
REST_GET_STATUS = "status"

REST_ENDPOINTS: set = {
    REST_GET_METRICS,
    REST_GET_STATUS,
    }

# Node SSE endpoints/channels.
SSE_DEPLOYS = "deploys"
SSE_MAIN = "main"
SSE_SIGS = "sigs"

SSE_ENDPOINTS: set = {
    SSE_DEPLOYS,
    SSE_MAIN,
    SSE_SIGS,
}
