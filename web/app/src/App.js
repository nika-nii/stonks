import './App.css';
import React from "react";
import {BrowserRouter, Route, Switch} from 'react-router-dom'
import {Home} from './Pages/Home'
import {Subs} from './Pages/Subs'
import {Navbar} from './Components/Navbar'
import Signin from "./Pages/Signin";
import Signup from "./Pages/Signup";
import 'bootstrap/dist/css/bootstrap.min.css';


function App() {
    return (
        <BrowserRouter>
            <Navbar/>
            <div className="container pt-4">
                <Switch>
                    <Route path={'/'} exact component={Home}/>
                    <Route path={'/subs'} component={Subs}/>
                    <Route path={'/login'} component={Signin}/>
                    <Route path={'/registration'} component={Signup}/>
                </Switch>
            </div>
        </BrowserRouter>
  );
}

export default App;
