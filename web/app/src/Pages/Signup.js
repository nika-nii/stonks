import React, { Component } from 'react'
import {Button, TextField} from "@material-ui/core";
import './Signup.css'

var button_style = {
    margin: "5px"
}

class Signup extends Component {
    render() {
        return (
            <form className="sign-up-form">
                <h1>Signup page</h1>
                <TextField id="filled-basic" label="email" />
                <TextField id="filled-basic" label="password" />
                <TextField id="filled-basic" label="login" />
                <Button variant="contained" color="primary" style={button_style}>
                    Sign up
                </Button>
            </form>
        );
    }
}

export default Signup;