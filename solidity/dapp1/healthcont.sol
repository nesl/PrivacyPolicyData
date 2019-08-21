pragma solidity >=0.4.22 <0.6.0;
contract health_contract {

    //Save roles
    uint256[] roles;

    //Save times of access
    uint256[] time_begin;
    uint256[] time_end;

    bool[] effects;

    constructor(uint256[] memory rs, uint256[] memory ts, uint256[] memory te, bool[] memory efs) public {
        roles = rs;
        time_begin = ts;
        time_end = te;
        effects = efs;
    }

    //Evaluate whether or not the request is permitted
    function evaluate(uint256 role, uint256 timebegin, uint256 timeend) view public returns (bool) {

        bool evaluation = false;

        for(uint i = 0; i < effects.length; i++) {

            //If the roles match
            if (roles[i] == role) {

                //If the times of access also are within the policy
                if (timebegin >= time_begin[i] && timeend <= time_end[i]) {
                    evaluation = effects[i];
                }


            }
        }
        return evaluation;
    }


}
