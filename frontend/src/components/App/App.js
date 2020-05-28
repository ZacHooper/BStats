import React, { useState } from 'react';
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
  } from "react-router-dom";
import './App.css';
import Profile from '../Profile/Profile'
import ProfileSearch from '../ProfileSearch/ProfileSearch'
import GlobalStats from '../GlobalStats/GlobalStats'
import { defaultPlayer } from '../../util/api'

const App = () => {
    const [currentUser, setCurrectUser] = useState(defaultPlayer)

    const searchPlayerTag = async (playerTag) => {        
        const endpoint = `http://127.0.0.1:5000/api/v1/player/info/${playerTag}`
        try {
            const res = await fetch(endpoint);
            if (res.ok) {
                const json = await res.json();                
                setCurrectUser(json);              
            }
            else {
                throw new Error('Unable to fetch user info');
            }
        } catch (error) {
            console.log(error);    
        }
    }

    return (
        <div className="App">
            <div className="logo">
                <h1><span className="highlight">B</span>Stats</h1>
            </div>
            
            <Router>
                <nav>
                    <ul>
                        <li><Link to="/profile">Profile Page</Link></li>
                        <li><Link to="/stats">Global Stats</Link></li>
                        <li><Link to="/">Home</Link></li>
                    </ul>
                </nav>
                <Switch>
                    <Route path="/profile">
                        <Profile currentUser={currentUser}/>
                    </Route>

                    <Route path="/stats">
                        <GlobalStats />
                    </Route>

                    {
                    // This route needs to go last as it acts as a fallback to any routes above 
                    }
                    <Route path="/">
                        <Home onClick={searchPlayerTag}/>
                    </Route>
                </Switch>
            </Router>
            
            
        </div>
    )
}

const Home = (props) => {
    return (
        <div className="app-profileSearch-container">
            <ProfileSearch onClick={props.onClick}/>
        </div>
    )
}

export default App;