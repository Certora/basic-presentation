// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import {MinimalToken} from "./MinimalTokenFixed.sol";

/// @title A simple voting contract
contract PowerVoting {

    MinimalToken public token;

    bool public isVotingEnded;
    
    // How much was transferred when voting
    mapping(address => uint256) amountVoted;

    // `_hasVoted[user]` is true if the user voted.
    mapping(address => bool) public hasVoted;

    uint256 public votesInFavor;  // How many in favor
    uint256 public votesAgainst;  // How many opposed

    function totalVotes() public view returns (uint256) {
        return token.balanceOf(address(this));
    }

    function endVoting() public {
        require(!isVotingEnded, "Already ended");
        isVotingEnded = true;
    }

    function vote(bool isInFavor) public {
        require(!isVotingEnded, "Voting ended");
        require(!hasVoted[msg.sender]);
        hasVoted[msg.sender] = true;

        uint256 power = token.balanceOf(msg.sender);

        // Take the money to prevent voting twice with it
        token.transferFrom(msg.sender, address(this), power);
        amountVoted[msg.sender] += power;
        
        if (isInFavor) {
            votesInFavor += power;
        } else {
            votesAgainst += power;
        }
    }
}
