import React, { useState, useEffect } from "react";
import PhoneInput from "react-phone-input-2";
import "react-phone-input-2/lib/style.css";
import "./personalDetails.css";

function PersonalDetails() {
  const [code, setCode] = useState();
  return (
    <div>
      <h1>Let's create your profile</h1>
      <div className="formContaier">
        <form>
          <label for="fname">First Name</label> <br></br>
          <input
            type="text"
            id="fname"
            name="First name"
            placeholder="First Name"
          />
          <br></br> <br></br>
          <label for="lname">Last Name</label> <br></br>
          <input
            type="text"
            id="lname"
            name="Last name"
            placeholder="Last Name"
          />
          <br></br> <br></br>
          <label for="Email Address">Email Address</label> <br></br>
          <input
            type="email"
            id="emailAddress"
            name="emailAddress"
            placeholder="Email Address "
          />
          <br></br> <br></br>
          <label for="dob">Date of birth</label>
          <input type="date" id="dob" name="Date of birth" />
          <br></br>
          <br></br>
          <PhoneInput
            placeholder="Enter phone number"
            value={code}
            onChange={setCode}
          />
          <br></br>
          <br></br>
          <label for="country">Country</label>
          <input type="country" id="country" name="country" />
          <br></br>
          <br></br>
          <input
            type="submit"
            id="submit"
            name="submit"
            value="save and continue"
          />
        </form>
      </div>
    </div>
  );
}

export default PersonalDetails;
