// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;


/// @title Interface for borrower
interface IFlashLoanReceiver {
    function execute() external payable;
}


/// @title A minimal ERC-20 style token
contract MinimalToken {

    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowances;
    uint256 public totalSupply;

    /// @notice Lends ETH
    function flashLoan(uint256 amount) public {
        uint256 preBalance = address(this).balance;
        require(preBalance >= amount, "Insufficient funds");
        
        IFlashLoanReceiver(msg.sender).execute{value: amount}(); 

        uint256 postBalance = address(this).balance;
        require(postBalance >= preBalance, "Loan has not been repaid");
    }

    function transfer(address recipient, uint256 amount) public returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }
    
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public returns (bool) {
        uint256 currentAllowance = allowances[sender][msg.sender];
        require(currentAllowance >= amount, "Transfer exceeds allowance");

        _approve(sender, msg.sender, currentAllowance - amount);
        _transfer(sender, recipient, amount);

        return true;
    }
    
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal {
        require(recipient != address(0), "Transfer to zero address");

        uint256 senderBalance = balanceOf[sender];
        require(senderBalance >= amount, "Transfer exceeds balance");
        
        balanceOf[sender] = senderBalance - amount;
        balanceOf[recipient] += amount;
    }
    
    function approve(address spender, uint256 amount) public returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }
    
    function _approve(
        address owner,
        address spender,
        uint256 amount
    ) internal {
        allowances[owner][spender] = amount;
    }

    function deposit(uint256 amount) public payable {
        require(msg.value >= amount, "Insufficient eth");
        require(msg.sender != address(0), "Depositing to zero address");
        require(msg.sender != address(this), "Depositing to self");
        balanceOf[msg.sender] += amount;
        totalSupply += amount;
    }
}