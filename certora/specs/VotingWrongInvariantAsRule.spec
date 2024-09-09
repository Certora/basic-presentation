/* Wrong invariant as rule */
methods {
    // Declares the getters for the public state variables as `envfree`
    function totalVotes() external returns (uint256) envfree;
    function votesInFavor() external returns (uint256) envfree;
    function votesAgainst() external returns (uint256) envfree;
}

/// @title Total votes is sum of in favor and against - wrong rule
rule totalVotesIsSumWrong(env e) {

    bool isInFavor;
    vote(e, isInFavor);

    assert (
        votesInFavor() + votesAgainst() == totalVotes(),
        "totalVotes is sum of in favor and against"
    );
}
