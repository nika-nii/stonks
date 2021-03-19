import React, { Component } from "react";
import {TextField} from "@material-ui/core";

class Signin extends Component {
    render() {
        return (
            <form className="sign-in-form">
                <h1>Signin page</h1>
                <TextField id="filled-basic" label="email" variant="filled" />
                <TextField id="filled-basic" label="password" variant="filled" />
                <TextField id="filled-basic" label="login" variant="filled" />
            </form>
        );
    }
}

export default Signin;