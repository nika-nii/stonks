import React, { Component } from 'react'
import {TextField} from "@material-ui/core";

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
                <div className='sign-up-form__text-links'>
                    <span>Forgot Password</span>
                    <span>Signup here</span>
                </div>
            </form>
            </div>
        );
    }
}

export default Signup;