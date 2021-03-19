import React, { Component } from 'react'
import {TextField} from "@material-ui/core";
import './Signup.css'
class Signup extends Component {
    render() {
        return (
            <div>
            <h1>signup page</h1>
            <form className="sign-up-form">
                <h1>Signup page</h1>
                <TextField id="filled-basic" label="email" variant="filled" />
                <TextField id="filled-basic" label="password" variant="filled" />
                <TextField id="filled-basic" label="login" variant="filled" />

            </form>
            </div>
        );
    }
}

export default Signup;