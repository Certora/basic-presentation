/* Wrong invariant as rule */
methods {
    // Declares the getters for the public state variables as `envfree`
    function totalVotes() external returns (uint256) envfree;
    function votesInFavor() external returns (uint256) envfree;
    function votesAgainst() external returns (uint256) envfree;
}

/// @title Total votes is sum of in favor and against - wrong rule
rule totalVotesIsSumWrong(bool isInFavor) {

    env e;
    vote(e, isInFavor);

    uint256 totalPost = totalVotes();
    uint256 inFavorPost = votesInFavor();
    uint256 againstPost = votesAgainst();
    assert (
        inFavorPost + againstPost == to_mathint(totalPost),
        "totalVotes is sum of in favor and against"
    );
}
