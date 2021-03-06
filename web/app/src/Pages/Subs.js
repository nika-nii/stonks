import React, {Fragment} from 'react'
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import {Button, Container, TextField} from "@material-ui/core";

var button_style = {
    margin: "5px"
}

var in_column_style = {
    display: "flex",
    flexDirection: "column",
    marginTop: "5px",
    width: "500px"
}
export const Subs = () => {
    const classes = useStyles();
    return (
        <Fragment>
            <h1>Подписки</h1>
            <TableContainer component={Paper}>
                <Table className={classes.table} size="small" aria-label="a dense table">
                    <TableHead>
                        <TableRow>
                            <TableCell>Валюта</TableCell>
                            <TableCell align="right">Событие</TableCell>
                            <TableCell align="right">Порог</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {rows.map((row) => (
                            <TableRow key={row.val}>
                                <TableCell component="th" scope="row">
                                    {row.val}
                                </TableCell>
                                <TableCell align="right">{row.event}</TableCell>
                                <TableCell align="right">{row.watch}</TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </TableContainer>
            <div style={in_column_style}>
                <span>Чтобы добавить подписку заполните поля снизу, если не заполните, то все крашнется к чертям</span>
                <TextField id="filled-basic" label="email" />
                <TextField id="filled-basic" label="password" />
                <TextField id="filled-basic" label="login" />
            </div>
            <Button variant="contained" color="primary" style={button_style}>
                Добавить подиску
            </Button>
        </Fragment>
    )
}

const useStyles = makeStyles({
    table: {
        minWidth: 650,
    },
});

function createData(val, event, watch) {
    return {val, event, watch};
}

const rows = [
    createData('RUB', 'up', 6.0),
    createData('GRI', 'up', 9.0),
    createData('TEN', 'down', 16.0),
];

