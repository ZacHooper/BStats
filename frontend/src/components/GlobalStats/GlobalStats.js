import React from 'react';
import './GlobalStats.css';

const GlobalStats = (props) => {
    return (
        <div>
            Global Stats
            <iframe style={{background: "#FFFFFF"}} 
                    width="640" height="480" src="https://charts.mongodb.com/charts-bstats-ekaam/embed/charts?id=a6d14b59-897f-487a-a6c0-5f74ab595c9c&theme=light"></iframe>
        </div>
    );
}

export default GlobalStats;