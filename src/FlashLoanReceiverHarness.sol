// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;


import {IFlashLoanReceiver, MinimalToken} from "./MinimalLendingTokenFixed.sol";
import {PowerVoting} from "./PowerVotingFixed.sol";

// A contract that may do anything.
// We use the Provver's over-approximation of storage for enabling any possible action.
contract FlashLoanReceiverHarness is IFlashLoanReceiver {

    MinimalToken public token;
    PowerVoting public voting;

    // Which function to call
    enum Func {
        Deposit,
        FlashLoan,
        Vote,
        DoNothing
    }
    mapping(uint8 => Func) public toCalls;

    // The amounts to use in the function calls
    mapping(uint8 => uint256) public amounts;

    // Boolean values to use
    mapping(uint8 => bool) public booleans;

    // The iteration number
    uint8 public i;

    function doSingleSomething() public {
        i += 1;  // Increase iteration

        if (toCalls[i] == Func.Deposit) {
            token.deposit{value: amounts[i]}(amounts[i]);
        } else if (toCalls[i] == Func.FlashLoan) {
            token.flashLoan(amounts[i]);
        } else if (toCalls[i] == Func.DoNothing) {
            // Do nothing
        } else {
            voting.vote(booleans[i]);
        }
    }

    function doSomethings() public {
        for (uint8 j; j < 2; j++) {
            doSingleSomething();
        }
    }

    function execute() external payable override {
        doSomethings();
    }
}
