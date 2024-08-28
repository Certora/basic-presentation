/* A simple invariant for the Voting contract */
methods {
    // Declares the getters for the public state variables as `envfree`
    function totalVotes() external returns (uint256) envfree;
    function votesInFavor() external returns (uint256) envfree;
    function votesAgainst() external returns (uint256) envfree;
}

/// @title Total votes is sum of in favor and against
rule totalVotesIsSum(bool isInFavor) {
    uint256 totalPre = totalVotes();
    uint256 inFavorPre = votesInFavor();
    uint256 againstPre = votesAgainst();

    require inFavorPre + againstPre == to_mathint(totalPre);

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


/// @title Total votes is sum of in favor and against
invariant totalVotesIsSumInvariant()
    votesInFavor() + votesAgainst() == to_mathint(totalVotes());
