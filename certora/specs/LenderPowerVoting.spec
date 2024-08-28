using MinimalToken as token;
using FlashLoanReceiverHarness as borrower;

methods {
    function totalVotes() external returns (uint256) envfree;
    function hasVoted(address) external returns (bool) envfree;

    function MinimalToken.balanceOf(address) external returns (uint256) envfree;

    // Instructs the `Prover` to use any appropriate contract it finds
    function _.execute() external => DISPATCHER(true);
}


/// @title An exploit example
rule example() {
    // The following requirements are just to make it easier to see the problem
    require totalVotes() == 0;
    require nativeBalances[borrower] == 0;
    require token.balanceOf(borrower) == 0;

    // The total ETH in the system before
    mathint totalBalances = nativeBalances[token] + nativeBalances[borrower];

    env e;
    borrower.doSomethings(e);

    // More votes than total ETH
    satisfy to_mathint(totalVotes()) > totalBalances;
}
