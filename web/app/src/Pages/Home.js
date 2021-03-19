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
    data1 = [
        {
            x: 1,
            y: 2
        },
        {
            x: 2,
            y: 4
        },
        {
            x: 3,
            y: 6
        },
        {
            x: 4,
            y: 8
        },
        {
            x: 5,
            y: 10
        },
    ]
    data2 = [
        {
            x: 1,
            y: 1
        },
        {
            x: 2,
            y: 2
        },
        {
            x: 3,
            y: 3
        },
        {
            x: 4,
            y: 4
        },
        {
            x: 5,
            y: 5
        },
    ]
    data3 = [
        {
            x: 1,
            y: 1
        },
        {
            x: 2,
            y: 2
        },
        {
            x: 3,
            y: 3
        },
        {
            x: 4,
            y: 4
        },
        {
            x: 5,
            y: 5
        },
    ]
    dataToShow = this.defaultData

    reRender(name){
        switch(name){
            case "RUB":
                this.dataToShow = this.data1
                break;
            case "GRI":
                this.dataToShow = this.data2
                break;
            case "TEN":
                this.dataToShow = this.data3
                break;
        }
        this.forceUpdate();
    };

    render() {
        return (
            <Fragment>
                <h1>Home page</h1>
                <Container>
                    <Button variant="contained" color="primary" onClick={() => this.reRender("RUB")}>
                        Рубль
                    </Button>
                    <Button variant="contained" color="primary" onClick={() => this.reRender("GRI")}>
                        Гривна
                    </Button>
                    <Button variant="contained" color="primary" onClick={() => this.reRender("TEN")}>
                        Тэньге
                    </Button>
                </Container>
                <Container>
                    <Grid>
                        <Grid item xs={12} md={8} lg={9}>
                            <Paper>
                                <div className="Chart">
                                    <h2 style={{textAlign: "center"}}>Stonks</h2>
                                    <LineChart width={730} height={250} data={this.dataToShow}
                                               margin={{top: 5, bottom: 5}}>
                                        <XAxis dataKey="x"/>
                                        <YAxis dataKey="y"/>
                                        <Line type="monotone" dataKey="y" stroke="#8884d8"/>
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
