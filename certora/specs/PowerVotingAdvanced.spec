/* Verification of the `PowerVoting` contract */

using MinimalToken as token;

methods {
    // Declares the getters for the public state variables as `envfree`
    function totalVotes() external returns (uint256) envfree;
    function votesInFavor() external returns (uint256) envfree;
    function votesAgainst() external returns (uint256) envfree;

    // Declares function so can be called from the spec via, `token.balanceOf(a)`
    function MinimalToken.balanceOf(address) external returns (uint256) envfree;
}


/// @title Integrity of vote
rule voteIntegrity(bool isInFavor) {
    uint256 votedBefore = totalVotes();

    env e;
    uint256 voterBalance = token.balanceOf(e.msg.sender);
    vote(e, isInFavor);

    assert (
        (voterBalance > 0) => totalVotes() > votedBefore,
        "totalVotes increases after voting"
    );
    assert (
        (voterBalance == 0) => totalVotes() == votedBefore,
        "if voter has no funds then totalVotes is unchanged"
    );
}


/// @title Total votes is sum of in favor and against
invariant totalVotesIsSumInvariant()
    votesInFavor() + votesAgainst() == to_mathint(totalVotes())
    {
        preserved with (env e) {
            // assumptions for the prover when "executing" any contract method
            require e.msg.sender != currentContract;
        }
        preserved token.transfer(address to, uint256 amount) with (env e) {
            // assumptions for the prover when "executing" a specific contract method
            require e.msg.sender != currentContract;
            require to != currentContract;
        }
        preserved token.transferFrom(address from, address to, uint256 amount) with (env e) {
            require from != currentContract;
            require to != currentContract;
        }
    }
