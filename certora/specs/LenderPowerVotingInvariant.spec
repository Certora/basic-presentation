using MinimalToken as token;
using FlashLoanReceiverHarness as borrower;

methods {
    function totalVotes() external returns (uint256) envfree;
    function hasVoted(address) external returns (bool) envfree;

    function MinimalToken.balanceOf(address) external returns (uint256) envfree;
    function MinimalToken.totalSupply() external returns (uint256) envfree;

    // Instructs the `Prover` to use any appropriate contract it finds
    function _.execute() external => DISPATCHER(true);
}


/// @title Total supply not greater than ETH balance
invariant tokenSolvency()
    nativeBalances[token] >= token.totalSupply();
