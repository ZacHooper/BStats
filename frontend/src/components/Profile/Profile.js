import React, { useState } from 'react'
import './Profile.css';
import ProfileBrawler from '../ProfileBrawler/ProfileBrawler'
import { Switch, Route, useRouteMatch, useParams } from 'react-router-dom';

const Profile = (props) => {
    const [currentBrawler, setCurrentBrawler] = useState("")
    const [currentBrawlerStats, setCurrentBrawlerStats] = useState("")

    const handleCurrentBrawler = async (brawler) => {
        setCurrentBrawler(brawler)
        const endpoint = `http://127.0.0.1:5000/api/v1/${encodeURIComponent(props.currentUser._id)}/${brawler.id}/stats/`
        try {
            const res = await fetch(endpoint);
            if (res.ok) {
                const json = await res.json();                
                setCurrentBrawlerStats(json);              
            }
            else {
                throw new Error('Unable to fetch brawler stats');
            }
        } catch (error) {
            console.log(error);    
        }
    }

    let match = useRouteMatch();
    
    if (!props.currentUser.name) {
        return "Loading"
    }

    return (
        <div className="profile">
            <div className="profile-name-container">
                <h2>{props.currentUser.name}</h2>
                <h6>{props.currentUser._id}</h6>
            </div>
            <Switch>
                <Route path={`${match.url}/brawler/:id`}>
                    <PlayerBrawlerProfile brawler={currentBrawler} brawlerStats={currentBrawlerStats}/>
                </Route>
                <Route path={`${match.url}/`}>
                    <ProfileHome currentUser={props.currentUser} setCurrentBrawler={handleCurrentBrawler} />
                </Route>
            </Switch>
        </div>
    )
}

const PlayerBrawlerProfile = (props) => {
    let { id } = useParams();

    if (!props.brawler || !props.brawlerStats) {
        return `Loading ${id}`;
    }

    return (
        <div className="PlayerBrawlerProfile">
            <div className="BrawlerProfile">
                {props.brawler.name}
                {props.brawler.trophies}
                Power: {props.brawler.power} / 9
            </div>
            <div className="BrawlerModeStats">
                <table>
                    <tbody>
                        <tr>
                            <td>Gem Grab</td>
                            <td>{!props.brawlerStats.gemGrab ? "NA" : props.brawlerStats.gemGrab.averageResult * 100}%</td>
                        </tr>
                        <tr>
                            <td>Brawl Ball</td>
                            <td>{!props.brawlerStats.brawlBall ? "NA" : props.brawlerStats.brawlBall.averageResult * 100}%</td>
                        </tr>
                        <tr>
                            <td>Bounty</td>
                            <td>{!props.brawlerStats.bounty ? "NA" : props.brawlerStats.bounty.averageResult * 100}%</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    )
}

const ProfileHome = (props) => {
    const renderBrawlers = () => {
        return props.currentUser.brawlers.map(brawler => {
                return <ProfileBrawler key={brawler.id} brawler={brawler} setCurrentBrawler={props.setCurrentBrawler} />
        });
    }

    return (
        <div className="ProfileHome">
            <div className="profile-stats-container">
                <table>
                    <tbody>
                        <tr>
                            <td>Trophies</td>
                            <td>{props.currentUser.trophies}</td>
                        </tr>
                        <tr>
                            <td>Highest Trophies</td>
                            <td>{props.currentUser.highestTrophies}</td>
                        </tr>
                        <tr>
                            <td>Level</td>
                            <td>{props.currentUser.expLevel}</td>
                        </tr>
                        <tr>
                            <td>3 v 3 Victories</td>
                            <td>{props.currentUser['3vs3Victories']}</td>
                        </tr>
                        <tr>
                            <td>Solo Victories</td>
                            <td>{props.currentUser.soloVictories}</td>
                        </tr>
                        <tr>
                            <td>Duo Victories</td>
                            <td>{props.currentUser.duoVictories}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <h2 className="profile-brawlers-heading">Brawlers ({props.currentUser.brawlers.length} / 38) </h2>
            <div className="profile-brawler-container">
                {props.currentUser.brawlers ? renderBrawlers() : "Loading"}
            </div>
        </div>
    )
}

export default Profile