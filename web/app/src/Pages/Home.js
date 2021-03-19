import React, {Fragment} from 'react'
import {Button, Container, Grid, Paper} from "@material-ui/core";
import {Line, LineChart, XAxis, YAxis} from "recharts";

export class Home extends React.Component {
    defaultData = [
        {
            x: 0,
            y: 0
        },
        {
            x: 1,
            y: 1
        },
    ]

    dataToShow = this.defaultData

    state = {
        currencies: [],
        graph_data: []
    }

    reRender(name){
        fetch(`http://localhost/storage/range/${name}`)
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            this.setState(
                {
                    graph_data: data
                }
            )
        })
    };

    componentDidMount() {
        fetch('http://localhost/storage/currencies')
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            this.setState(
                {
                    currencies: data
                }
            )
        })
    }

    render() {
        console.log("Re-render")
        const {currencies, graph_data} = this.state
        const buttons = currencies.map((cur) => 
            <Button variant="contained" className="m-1" color="primary" onClick={() => this.reRender(cur)} key={cur}>
                {cur}
            </Button>)
        return (
            <Fragment>
                <h1>Home page</h1>
                <Container>
                    {buttons}
                </Container>
                <Container>
                    <Grid>
                        <Grid item xs={12} md={8} lg={9}>
                            <Paper>
                                <div className="Chart">
                                    <h2 style={{textAlign: "center"}}>Stonks</h2>
                                    <LineChart width={730} height={250} data={graph_data}
                                               margin={{top: 5, bottom: 5}}>
                                        <XAxis dataKey="time"/>
                                        <YAxis dataKey="value"/>
                                        <Line type="monotone" dataKey="value" stroke="#8884d8"/>
                                    </LineChart>
                                </div>
                            </Paper>
                        </Grid>
                    </Grid>
                </Container>
            </Fragment>
        )
    }
}
