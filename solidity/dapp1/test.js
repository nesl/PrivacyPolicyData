Web3 = require('web3')
fs = require("fs")
web3 = new Web3("http://localhost:8545")

// Display the accounts from Ganache
//web3.eth.getAccounts(console.log)


bytecode = fs.readFileSync('healthcont_sol_health_contract.bin').toString()
abi = JSON.parse(fs.readFileSync('healthcont_sol_health_contract.abi').toString())
//bytecode = fs.readFileSync('temp_sol_hc.bin').toString()
//abi = JSON.parse(fs.readFileSync('temp_sol_hc.abi').toString())
//web3.eth.getAccounts(console.log)

var contracts = [];
constructedContract1 = new web3.eth.Contract(abi)
constructedContract2 = new web3.eth.Contract(abi)

// roles: 1 is doctor, 2 is friend

// First user details
user1 = "0x444dbdab390038c9b1780f902a91a0afd301d665"
role1 = [1]
ts1 = [0]
te1 = [24]
effects1 = [true]

//Second user details
user2 = "0x444dbdab390038c9b1780f902a91a0afd301d665"
role2 = [2]
ts2 = [9]
te2 = [12]
effects2 = [true]


constructedContract1.deploy({
  data: bytecode,
  arguments: [role1, ts1, te1, effects1]
}).send({
  from: "0x4939c5dbd70b22c23fce63e27f756e1a42fee3be",
  gas: 1500000,
  gasPrice: web3.utils.toWei('0.00003', 'ether')
}).then((newContractInstance) => {
  constructedContract1.options.address = newContractInstance.options.address
  console.log(constructedContract1.options.address)
  //console.log("HEEEELLLLOOO")
  //console.log(constructedContract1.methods.evaluate(1, 1, 2).call(console.log))
});

//contracts.push(constructedContract1);
/*
constructedContract2.deploy({
  data: bytecode,
  arguments: [role2, ts2, te2, effects2]
}).send({
  from: user2,
  gas: 1500000,
  gasPrice: web3.utils.toWei('0.00003', 'ether')
}).then((newContractInstance) => {
  constructedContract2.options.address = newContractInstance.options.address
  //console.log(newContractInstance.options.address)
  constructedContract2.methods.evaluate(1, 1, 2).call(console.log)
});
*/
//contracts.push(constructedContract2);
