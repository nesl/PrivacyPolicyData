
pragma solidity >=0.4.0 <0.6.0;
// We have to specify what version of compiler this code will compile with

//We construct a way of requesting data, sending data
// where all data has a desired party or some secret key
// and each contract encapsulates some data

contract health {
  /* mapping field below is equivalent to an associative array or hash.
  The key of the mapping is candidate name stored as type bytes32 and value is
  an unsigned integer to store the vote count
  */

  mapping (bytes32 => uint256) public votesReceived;

  /* Solidity doesn't let you pass in an array of strings in the constructor (yet).
  We will use an array of bytes32 instead to store the list of candidates
  */

  bytes32[] public candidateList;
  bytes32 private disease;
  bytes32 private id;
  bytes32 requested_id;

  /* This is the constructor which will be called once when you
  deploy the contract to the blockchain. When we deploy the contract,
  we will pass an array of candidates who will be contesting in the election
  */
  /*constructor(bytes32[] memory candidateNames) public {
    candidateList = candidateNames;
  }*/
  constructor(bytes32 dis, bytes32 key, bytes32 other) public {
    disease = dis;
    id = key;
    requested_id = other;
  }

  // This function returns the total votes a candidate has received so far
  function totalVotesFor(bytes32 candidate) view public returns (uint256) {
    require(validCandidate(candidate));
    return votesReceived[candidate];
  }

  function requestData(bytes32 other) view public returns(bool) {
    require(validRequest(other));
    return true;
  }

  function allowedData(bytes32 other) view public returns(bytes32) {
    require(validRequest(other));
    return disease;
  }

  // This function increments the vote count for the specified candidate. This
  // is equivalent to casting a vote
  function voteForCandidate(bytes32 candidate) public {
    require(validCandidate(candidate));
    votesReceived[candidate] += 1;
  }

  //Determine is a request is valid
  function validRequest(bytes32 other) view public returns (bool) {
    if (other == requested_id) {
      return true;
    }
    return false;
  }

  function validCandidate(bytes32 candidate) view public returns (bool) {
    for(uint i = 0; i < candidateList.length; i++) {
      if (candidateList[i] == candidate) {
        return true;
      }
    }
    return false;
  }
}
