pragma solidity >=0.4.22 <0.6.0;
contract hc {

    //Save roles
    uint roles;

    //Save times of access
    uint time_begin;
    uint time_end;

    bool effects;

    constructor(uint rs, uint ts, uint te, bool efs) public {
        roles = rs;
        time_begin = ts;
        time_end = te;
        effects = efs;
    }

    //Evaluate whether or not the request is permitted
    function evaluate(uint role, uint timebegin, uint timeend) view public returns (bool) {

        bool evaluation = false;

        //If the roles match
        if (roles == role) {

            //If the times of access also are within the policy
            if (timebegin >= time_begin && timeend <= time_end) {
                evaluation = effects;
            }


        }
        return evaluation;
    }


}
