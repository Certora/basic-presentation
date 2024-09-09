/* A simple rule for the Voting contract */
methods {
    // Declares the getter for the public state variables as `envfree`
    function totalVotes() external returns (uint256) envfree;
}

/// @title Integrity of vote
rule voteIntegrity(env e) {
    uint256 votedBefore = totalVotes();

    bool isInFavor;
    vote(e, isInFavor);

    assert (
        totalVotes() > votedBefore,
        "totalVotes increases after voting"
    );
}
