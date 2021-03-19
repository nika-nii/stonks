import React, { Component } from "react";
import {Button, TextField} from "@material-ui/core";
import './Signin.css'

class Signin extends Component {
    render() {
        return (
            <form className="sign-in-form">
                <h1>Signin page</h1>
                <TextField id="filled-basic" label="email" />
                <TextField id="filled-basic" label="password" />
                <TextField id="filled-basic" label="login" />
                <Button className="button-margin" variant="contained" color="primary">
                    Sign in
                </Button>
            </form>
        );
    }
}

export default Signin;