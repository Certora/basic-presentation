/* Verification of the `PowerVoting` contract */
using MinimalToken as token;

methods {
    // Declares the getters for the public state variables as `envfree`
    function totalVotes() external returns (uint256) envfree;
    function votesInFavor() external returns (uint256) envfree;
    function votesAgainst() external returns (uint256) envfree;

    function MinimalToken.balanceOf(address) external returns (uint256) envfree;
}


/// @title Integrity of vote
rule voteIntegrity(bool isInFavor) {
    uint256 votedBefore = totalVotes();

    env e;
    vote(e, isInFavor);

    assert (
        (token.balanceOf(e.msg.sender) > 0) => totalVotes() > votedBefore,
        "totalVotes increases after voting"
    );
}

/// @title No allowance is given to use `PowerVoting` funds
invariant noAllowance()
    forall address a. token.allowances[currentContract][a] == 0;


/// @title Total votes is sum of in favor and against
invariant totalVotesIsSumInvariant()
    votesInFavor() + votesAgainst() <= to_mathint(totalVotes());
