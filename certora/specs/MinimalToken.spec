/* A simple spec for `MinimalToken` */
methods {
    function balanceOf(address) external returns (uint256) envfree;
    function totalSupply() external returns (uint256) envfree;
}


/// @title Adress zero has no balance
invariant noBalanceAddressZero()
    balanceOf(0) == 0;


/// @title Total supply not greater than ETH balance
invariant totalSupplyLEBalance()
    nativeBalances[currentContract] >= totalSupply();
