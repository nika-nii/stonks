import React, { Component } from "react";
import {TextField} from "@material-ui/core";
import './Signin.css'

class Signin extends Component {
    render() {
        return (
            <form className="sign-in-form">
                <h1>Signin page</h1>
                <div className="sign-in-form">
                    <TextField id="filled-basic" label="email" variant="filled" />
                    <TextField id="filled-basic" label="password" variant="filled" />
                    <TextField id="filled-basic" label="login" variant="filled" />
                </div>
            </form>
        );
    }
}

export default Signin;