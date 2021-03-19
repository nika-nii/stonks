import React from 'react';
import { LineChart, Line, XAxis, YAxis} from 'recharts';

const data = [
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
export default function Chart() {
    return (
        <div className="Chart">

            <h2 style={{ textAlign: "center" }}>Stonks</h2>
            <LineChart width={730} height={250} data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
                <XAxis dataKey="x" />
                <YAxis dataKey="y" />
                <Line type="monotone" dataKey="y" stroke="#8884d8" />
            </LineChart>
        </div>
    );
}