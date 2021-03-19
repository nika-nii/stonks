import React, { Component } from "react";
import {Button, TextField} from "@material-ui/core";
import './Signin.css'

var button_style = {
    margin: "5px"
}
class Signin extends Component {
    render() {
        return (
            <form className="sign-in-form">
                <h1>Signin page</h1>
                <TextField id="filled-basic" label="email" />
                <TextField id="filled-basic" label="password" />
                <TextField id="filled-basic" label="login" />
                <Button variant="contained" color="primary" style={button_style}>
                    Sign in
                </Button>
            </form>

        );
    }
}

export default Signin;