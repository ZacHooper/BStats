import React from 'react';
import './ProfileBrawler.css'
import { useHistory, useRouteMatch } from 'react-router-dom';

const ProfileBrawler = (props) => {
    let history = useHistory();
    let match = useRouteMatch();

    const handleImageSrc = (id) => {
        try {
            return require(`../../assets/brawlers/${id}.png`)
        } catch (error) {
            console.log(error)
        }
    }

    const handleOnClick = () => {
        props.setCurrentBrawler(props.brawler)
        history.push(`${match.url}/brawler/${props.brawler.id}`)
    }
    
    return (
        <div id={`brawler_${props.brawler.id}`} className="ProfileBrawler" onClick={handleOnClick}>
            <img alt={props.brawler.name} src={handleImageSrc(props.brawler.id)} width="180"></img>
            <h6>{props.brawler.name}</h6>
            <p>{props.brawler.trophies}</p>
        </div>
    );
}

export default ProfileBrawler;