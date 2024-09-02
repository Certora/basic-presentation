/* A simple invariant for the Voting contract */
methods {
    // Declares the getters for the public state variables as `envfree`
    function totalVotes() external returns (uint256) envfree;
    function votesInFavor() external returns (uint256) envfree;
    function votesAgainst() external returns (uint256) envfree;
}


/// @title Total votes is sum of in favor and against
invariant totalVotesIsSumInvariant()
    votesInFavor() + votesAgainst() == to_mathint(totalVotes());
