import React from 'react'
import './Profile.css';

const Profile = (props) => {
    return (
        <div className="profile">
            <div className="profile-name-container">
                <h2>{props.currentUser.name}</h2>
                <h6>{props.currentUser._id}</h6>
            </div>
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
        </div>  
    )
}

export default Profile