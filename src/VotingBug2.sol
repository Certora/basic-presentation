// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/// @title A simple voting contract
contract Voting {

  // `_hasVoted[user]` is true if the user voted.
  mapping(address => bool) public hasVoted;

  uint256 public votesInFavor;  // How many in favor
  uint256 public votesAgainst;  // How many opposed
  uint256 public totalVotes;  // Total number voted

  function vote(bool isInFavor) external {
    require(!hasVoted[msg.sender]);
    hasVoted[msg.sender] = true;

    totalVotes += 1;
    if (isInFavor) {
      votesInFavor += 1;
    } else {
      votesAgainst = 1;  // NOTE: injected bug
    }
  }
}
